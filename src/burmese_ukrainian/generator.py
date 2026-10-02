from itertools import product
from .unicode import MEDIALS,VOWEL_SIGNS
from .parser import BASE_CONSONANTS

def generate_structural_syllables(onsets=None,medials=None,vowels=None):
    """Generate structural candidates only; this is not an attested lexical inventory."""
    onsets=list(onsets or sorted(BASE_CONSONANTS))
    medials=list(medials or [()])
    vowels=list(vowels or [()])
    for o,m,v in product(onsets,medials,vowels):
        yield {"onset":o,"medials":[MEDIALS[x] for x in m],"vowels":[VOWEL_SIGNS[x] for x in v],"status":"generated_structural_candidate"}
