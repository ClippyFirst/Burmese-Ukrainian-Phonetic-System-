def annotate_prosody(syllable:dict, analysis_id:str="four_way_tone")->dict:
    """Attach an analytical slot without inventing a tone from orthography alone."""
    p=syllable.setdefault("prosody",{})
    p.update({"analysis_id":analysis_id,"tone_category":None,"pitch_contour":None,"phonation":None,"duration":None,"checkedness":None,"status":"analysis_dependent"})
    return syllable
