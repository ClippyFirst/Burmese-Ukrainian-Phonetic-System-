from .ipa import to_ipa
from .ukrainian import ipa_to_ukrainian
def explain(text:str)->dict:
    r=to_ipa(text); r["ukrainian_candidates"]=ipa_to_ukrainian(r.get("ipa",""))
    r["pipeline"]=["Unicode normalization","grapheme/syllable segmentation","onset/conjunct/kinzi/medial/vowel analysis","inherent-vowel interpretation","prosodic annotation","conservative IPA","Ukrainian candidate generation"]
    return r
