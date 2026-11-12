// Generated from data/burmese/romanization_ukrainian.csv and
// data/burmese/romanization_rimes_inventory.csv. Keep the CSV registries canonical.
// The rime source inventory is vendor-derived (Mya2Rom 0.4.4), not MLC-primary verified.
const ONSETS = {
  "k": "к",
  "hk": "к'",
  "g": "ґ",
  "gh": "ґ'",
  "ng": "нг",
  "c": "ц",
  "hc": "ц'",
  "j": "дж",
  "jh": "дж'",
  "ny": "нь",
  "t": "т",
  "ht": "т'",
  "d": "д",
  "dh": "д'",
  "n": "н",
  "p": "п",
  "hp": "п'",
  "b": "б",
  "bh": "б'",
  "m": "м",
  "y": "й",
  "r": "р",
  "l": "л",
  "w": "в",
  "s": "с",
  "h": "г",
  "": "∅"
};
const RIMES = {
  "uing:": "уйнгː",
  "uing.": "уйнг·",
  "aung:": "аунгː",
  "aung.": "аунг·",
  "uik": "уйк",
  "wam:": "вамː",
  "wam.": "вам·",
  "wan:": "ванː",
  "wan.": "ван·",
  "auk": "аук",
  "uing": "уйнг",
  "aung": "аунг",
  "um:": "умː",
  "um.": "ум·",
  "un:": "унː",
  "un.": "ун·",
  "im:": "імː",
  "im.": "ім·",
  "in:": "інː",
  "in.": "ін·",
  "un": "ун",
  "wam": "вам",
  "wap": "вап",
  "wan": "ван",
  "wat": "ват",
  "ui:": "уйː",
  "ui.": "уй·",
  "ui": "уй",
  "au.": "ау·",
  "au": "ау",
  "um": "ум",
  "up": "уп",
  "ut": "ут",
  "im": "ім",
  "ip'": "іпʼ",
  "in": "ін",
  "it": "іт",
  "am:": "амː",
  "am.": "ам·",
  "an:": "анː",
  "an.": "ан·",
  "any:": "аньː",
  "any.": "ань·",
  "ang:": "ангː",
  "ang.": "анг·",
  "au:": "ауː",
  "ai.": "ай·",
  "e:": "еː",
  "e.": "е·",
  "u:": "уː",
  "i:": "іː",
  "ai": "ай",
  "am": "ам",
  "ap": "ап",
  "an": "ан",
  "at": "ат",
  "any": "ань",
  "ac": "ац",
  "ang": "анг",
  "a:": "аː",
  "a.": "а·",
  "ai:": "айː",
  "e": "е",
  "u.": "у·",
  "u": "у",
  "i": "і",
  "i.": "і·",
  "ak": "ак",
  "a": "а"
};
const MEDIALS = Object.freeze({ y: "й", r: "р", w: "в" });
const ONSET_KEYS = Object.keys(ONSETS).filter(Boolean).sort((a,b)=>b.length-a.length);
const RIME_KEYS = Object.keys(RIMES).sort((a,b)=>b.length-a.length);

export function renderMlctsSyllable(input) {
  const mlcts = String(input ?? "").trim();
  if (!mlcts) return { text: "", status: "EMPTY", mlcts };
  if (Object.hasOwn(RIMES, mlcts)) {
    return { text: RIMES[mlcts], status: "PROPOSED", evidence: "EVIDENCE_LIMITED", mlcts };
  }
  const onset = ONSET_KEYS.find(key => mlcts.startsWith(key));
  if (!onset) return { text: null, status: "UNSUPPORTED", evidence: "EVIDENCE_LIMITED", mlcts };
  const onsetUa = ONSETS[onset];
  const rest = mlcts.slice(onset.length);
  if (!rest) return { text: onsetUa === "∅" ? "" : onsetUa, status: "PROPOSED", evidence: "EVIDENCE_LIMITED", mlcts };
  for (let length = Math.min(3, rest.length); length >= 0; length -= 1) {
    const medial = rest.slice(0, length);
    if (![...medial].every(char => Object.hasOwn(MEDIALS, char))) continue;
    const rime = rest.slice(length);
    if (!Object.hasOwn(RIMES, rime)) continue;
    return {
      text: (onsetUa === "∅" ? "" : onsetUa) + [...medial].map(char => MEDIALS[char]).join("") + RIMES[rime],
      status: "PROPOSED", evidence: "EVIDENCE_LIMITED", mlcts,
    };
  }
  return { text: null, status: "UNSUPPORTED", evidence: "EVIDENCE_LIMITED", mlcts };
}

export function renderMlctsText(text, romanizer, segmenter, isSupported = () => true) {
  let output = "", unsupported = 0, mapped = 0;
  const normalized = String(text ?? "").normalize("NFC");
  let buffer = "", isMyanmar = null;
  const flush = () => {
    if (!buffer) return;
    if (!isMyanmar) output += buffer;
    else {
      for (const unit of segmenter(buffer)) {
        if (unit.nonMyanmar) { output += unit.raw; continue; }
        if (![...unit.raw].every(isSupported)) { output += "⟦" + unit.raw + "⟧"; unsupported += 1; continue; }
        const mlcts = romanizer(unit.raw, "mlcts", false, true);
        const result = renderMlctsSyllable(mlcts);
        if (result.text === null) { output += "⟦" + (mlcts || unit.raw) + "⟧"; unsupported += 1; }
        else { output += result.text; mapped += 1; }
      }
    }
    buffer = ""; isMyanmar = null;
  };
  for (const char of normalized) {
    const cp = char.codePointAt(0);
    const current = ((cp >= 0x1000 && cp <= 0x109f) || (cp >= 0xa9e0 && cp <= 0xa9ff) || (cp >= 0xaa60 && cp <= 0xaa7f) || (cp >= 0x116d0 && cp <= 0x116ff)) && !(cp >= 0x1040 && cp <= 0x104b);
    if (buffer && current !== isMyanmar) flush();
    buffer += char; isMyanmar = current;
  }
  flush();
  return { text: output, status: unsupported ? (mapped ? "PARTIAL" : "UNSUPPORTED") : (mapped ? "PROPOSED" : "PASSTHROUGH"), mapped, unsupported };
}
