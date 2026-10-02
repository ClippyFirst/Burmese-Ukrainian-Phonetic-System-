from .parser import parse_burmese
ONSET_IPA={"က":"k","ခ":"kʰ","ဂ":"ɡ","ဃ":"ɡ","င":"ŋ","စ":"s","ဆ":"sʰ","ဇ":"z","ဈ":"z","ည":"ɲ","တ":"t","ထ":"tʰ","ဒ":"d","ဓ":"dʰ","န":"n","ပ":"p","ဖ":"pʰ","ဗ":"b","ဘ":"bʰ","မ":"m","ယ":"j","ရ":"ɹ","လ":"l","ဝ":"w","သ":"θ","ဟ":"h","ဠ":"l","အ":"ʔ"}
VOWEL_IPA={"e":"e","i":"i","ii":"iː","ai":"ɛ","u":"u","uu":"uː","tall_aa":"a","aa":"a","anusvara":""}
def _ipa(s):
    o=ONSET_IPA.get(s.get("onset",{}).get("character"))
    if o is None:return None
    v=s.get("vowel")
    if not v:return o+"?"
    vals=[VOWEL_IPA.get(x["id"]) for x in v["signs"]]
    if any(x is None for x in vals):return None
    return o+"".join(x for x in vals if x)
def to_ipa(text:str)->dict:
    r=parse_burmese(text)
    for s in r["syllables"]: s["ipa"]=_ipa(s); s["phonetic_status"]="conservative_partial" if s["ipa"] else "analysis_dependent"
    r["ipa"]=" ".join(s["ipa"] or "?" for s in r["syllables"]); return r
