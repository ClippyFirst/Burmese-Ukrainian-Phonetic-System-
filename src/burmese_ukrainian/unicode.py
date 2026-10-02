import unicodedata as ud
KINZI="\u1004\u103a\u1039"
MEDIALS={"\u103b":{"id":"medial_ya","character":"ျ","base":"ya"},"\u103c":{"id":"medial_ra","character":"ြ","base":"ra"},"\u103d":{"id":"medial_wa","character":"ွ","base":"wa"},"\u103e":{"id":"medial_ha","character":"ှ","base":"ha"}}
VOWEL_SIGNS={"\u1031":{"id":"e","character":"ေ"},"\u102d":{"id":"i","character":"ိ"},"\u102e":{"id":"ii","character":"ီ"},"\u1032":{"id":"ai","character":"ဲ"},"\u102f":{"id":"u","character":"ု"},"\u1030":{"id":"uu","character":"ူ"},"\u102b":{"id":"tall_aa","character":"ါ"},"\u102c":{"id":"aa","character":"ာ"},"\u1036":{"id":"anusvara","character":"ံ"}}
SPECIAL={"\u103a":"asat","\u1039":"virama","\u1037":"dot_below","\u1038":"visarga"}
def normalize_burmese(text:str,form:str="NFC")->str:
    if form not in {"NFC","NFD","NFKC","NFKD"}: raise ValueError("Unsupported normalization form")
    return ud.normalize(form,text)
def codepoint_name(ch:str)->str: return ud.name(ch,"UNKNOWN")
def is_myanmar(ch:str)->bool:
    cp=ord(ch); return 0x1000<=cp<=0x109F or 0xAA60<=cp<=0xAA7F or 0xA9E0<=cp<=0xA9FF
BASE_CONSONANTS=set(chr(cp) for cp in range(0x1000,0x1022))|{"\u1023","\u1024","\u1025","\u1026","\u1027","\u1029","\u102a","\u103f","\u104e"}
