from dataclasses import dataclass, field
from typing import Any
@dataclass
class Analysis:
    status:str="established"
    confidence:float=0.0
    sources:list[str]=field(default_factory=list)
    alternatives:list[dict[str,Any]]=field(default_factory=list)
@dataclass
class Syllable:
    raw:str
    codepoints:list[str]
    onset:dict[str,Any]=field(default_factory=dict)
    kinzi:dict[str,Any]|None=None
    conjunct:list[dict[str,Any]]=field(default_factory=list)
    medials:list[dict[str,Any]]=field(default_factory=list)
    vowel:dict[str,Any]|None=None
    inherent_vowel:dict[str,Any]|None=None
    coda:dict[str,Any]|None=None
    tone_mark:dict[str,Any]|None=None
    prosody:dict[str,Any]=field(default_factory=dict)
    phonology:dict[str,Any]=field(default_factory=dict)
    ipa:str|None=None
    analysis:Analysis=field(default_factory=Analysis)
