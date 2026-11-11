import { PRACTICAL, RULES } from "./generated/data.js";

const IPA_UNIT_RE = /(?:t͡s|d͡z|t͡ʃ|d͡ʒ|t͡?ɕʰ|t͡?ɕ|d͡?ʑ|eɪ|oʊ|aɪ|aʊ|[ktpsdb]ʰ|m̥|n̥|ŋ̊|ɲ̥|l̥|ʍ|ʃ|ʒ|ɴ|ŋ|ɲ|ɹ|ɦ|ʋ|ɯ|ɛ|ɪ|ɔ|ə|ʊ|θ|ð|[a-zɡʔːˑˈˌ]|[\u0300-\u0305\u030c\u0324\u0330\u0331])/gu;
const STATUS_RANK = {
  ESTABLISHED: 0,
  WELL_SUPPORTED: 1,
  PROPOSED: 2,
  ANALYSIS_DEPENDENT: 3,
  NOT_ESTABLISHED: 4,
  UNSUPPORTED: 5,
  UNCERTAIN: 6,
};
const TONE_MARKS = new Set([
  "\u0300", "\u0301", "\u0302", "\u0303", "\u0304", "\u030c",
]);
const OTHER_DIACRITICS = new Set(["\u0324", "\u0330", "\u0331"]);

function aggregateStatus(statuses, emptyStatus = "NOT_ESTABLISHED") {
  if (!statuses.length) return emptyStatus;
  return statuses.reduce(
    (worst, status) =>
      (STATUS_RANK[status] ?? 4) > (STATUS_RANK[worst] ?? 0) ? status : worst,
    "ESTABLISHED",
  );
}

export function candidateFor(segment) {
  const direct = PRACTICAL[segment]
    || PRACTICAL[segment === "θ" ? "θ~ð" : segment]
    || PRACTICAL[segment === "ɴ" ? "ŋ" : segment];
  if (!direct) {
    return {
      text: "",
      status: "NOT_ESTABLISHED",
      reason: "Немає точного правила для цього IPA-сегмента.",
      ruleIds: [],
    };
  }
  const row = direct[0];
  const candidate = segment === "j"
    ? "й"
    : (row.ukrainian_candidate === "∅" ? "" : row.ukrainian_candidate);
  return {
    text: candidate,
    status: (row.status || "UNKNOWN").toUpperCase(),
    reason: row.policy,
    ruleIds: (RULES[segment] || RULES["/" + segment + "/"] || []).map((item) => item.rule_id),
  };
}

export function renderUkrainian(ipaText) {
  if (!ipaText) return { text: "", status: "NOT_ESTABLISHED", parts: [], prosody: [] };

  let source = ipaText.trim();
  if (source.length > 1 && ((source[0] === "/" && source.at(-1) === "/")
    || (source[0] === "[" && source.at(-1) === "]"))) {
    source = source.slice(1, -1);
  }
  const normalized = source.normalize("NFD");
  const units = [];
  let cursor = 0;
  IPA_UNIT_RE.lastIndex = 0;
  while (cursor < normalized.length) {
    const match = IPA_UNIT_RE.exec(normalized);
    if (!match || match.index !== cursor) {
      return {
        text: "",
        status: "NOT_ESTABLISHED",
        parts: [],
        prosody: [],
        unsupported: normalized.slice(cursor),
      };
    }
    units.push(match[0]);
    cursor = IPA_UNIT_RE.lastIndex;
  }

  const parts = [];
  const prosody = [];
  let status = "ESTABLISHED";
  let syllableStart = true;

  for (let index = 0; index < units.length; index += 1) {
    const unit = units[index];

    if (/^\\s+$/u.test(unit)) {
      parts.push({ text: unit, status: "ESTABLISHED", reason: "Word boundary.", ruleIds: [] });
      syllableStart = true;
      continue;
    }
    if (unit === "." || unit === "·") {
      syllableStart = true;
      continue;
    }

    if (unit === "ː" || unit === "ˑ" || unit === "ˈ" || unit === "ˌ" || TONE_MARKS.has(unit) || OTHER_DIACRITICS.has(unit)) {
      prosody.push({
        kind: unit === "ː" || unit === "ˑ" ? "length" : unit === "ˈ" || unit === "ˌ" ? "stress" : TONE_MARKS.has(unit) ? "tone" : "phonation_or_other_diacritic",
        mark: unit,
      });
      continue;
    }

    // At a syllable onset, Ukrainian letters can encode /j/ + the following
    // vowel. This function is called per parsed Burmese syllable in the UI.
    if (syllableStart && unit === "j" && units.length > index + 1) {
      const vowel = units[index + 1];
      const glideVowels = {
        a: "я", e: "є", ɛ: "є", i: "ї",
        u: "ю", ʊ: "ю", o: "йо", ɔ: "йо", oʊ: "йоу", ɯ: "йи",
      };
      if (glideVowels[vowel]) {
        const vowelCandidate = candidateFor(vowel);
        const combined = {
          text: glideVowels[vowel],
          status: vowelCandidate.status,
          reason: "Contextual Ukrainian rendering of syllable-initial /j/ plus vowel.",
          ruleIds: [],
        };
        parts.push(combined);
        if ((STATUS_RANK[combined.status] ?? 4) > (STATUS_RANK[status] ?? 0)) status = combined.status;
        index += 1;
        syllableStart = false;
        continue;
      }
    }

    const candidate = candidateFor(unit);
    parts.push(candidate);
    if ((STATUS_RANK[candidate.status] ?? 4) > (STATUS_RANK[status] ?? 0)) status = candidate.status;
    syllableStart = false;
  }

  return {
    text: parts.map((part) => part.text).join(""),
    status,
    parts,
    prosody,
    unsupported: null,
  };
}
