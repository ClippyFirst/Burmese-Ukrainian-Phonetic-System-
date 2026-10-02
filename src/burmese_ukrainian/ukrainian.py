"""Adapter for ClippyFirst/Ukrainian-Phonetic-Inventory; no Ukrainian inventory is duplicated here."""
def ipa_to_ukrainian(ipa:str)->dict:
    if not ipa or ipa=="?": return {"candidates":[],"status":"insufficient_input"}
    seeds={"p":"п","b":"б","t":"т","d":"д","k":"к","ɡ":"ґ","m":"м","n":"н","ŋ":"нґ","s":"с","z":"з","h":"г","j":"й","w":"в","l":"л","ɹ":"р","i":"і","u":"у","e":"е","a":"а"}
    out=[]; i=0
    while i<len(ipa):
        pair=ipa[i:i+2]
        if pair in seeds: out.append(seeds[pair]); i+=2
        elif ipa[i] in seeds: out.append(seeds[ipa[i]]); i+=1
        elif ipa[i].isspace(): out.append(" "); i+=1
        else: out.append("?"); i+=1
    return {"candidates":[{"orthography":"".join(out),"score":0.0,"reason":"provisional seed candidate; canonical Ukrainian inventory validation required"}],"status":"candidate_only","method":"external_inventory_adapter"}
