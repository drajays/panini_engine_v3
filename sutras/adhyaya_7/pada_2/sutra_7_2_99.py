"""
7.2.99  त्रिचतुरोः स्त्रियां तिसृचतसृ  —  VIDHI

Padaccheda: त्रि-चतुरोः स्त्रियाम् तिसृ-चतसृ (लुप्तप्रथमान्तनिर्देशः)

त्रिचतुरोः स्त्रियां तिसृचतसृ (7.2.99)
Pāṭha: ashtadhyayi.com data.txt row i=72099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem, vowel_initial
from phonology import mk

def _site(state: State):
    """त्रिचतुरोः स्त्रियां तिसृचतसृ — त्रि / चतुर् denoting the feminine, before a vibhakti: तिसृ / चतसृ (तिसृभिः, चतस्रः). Read from the stem's
    own liṅga tag (strīliṅga) and the word (with tadantavidhi: प्रियतिसृ)."""
    hit = anga_and_sup(state, "7.2.99")
    if hit is None:
        return None
    anga, _sup = hit
    if "strīliṅga" not in anga.tags or anga.meta.get("7_2_99_done"):
        return None
    return anga if is_stem(anga, "tri", "catur", tadanta=True) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    word = "tri" if is_stem(anga, "tri", tadanta=True) else "catur"
    rep = ["t", "i", "s", "f"] if word == "tri" else ["c", "a", "t", "a", "s", "f"]
    new = [mk(x) for x in rep]
    for v in new:
        if v.slp1 == "s":
            v.tags.add("mula_prakrti_v")        # the s of the whole तिसृ / चतसृ ādeśa is no sakāra-ādeśa for 8.3.59: तिसृषु, not *तिषृषु
    anga.varnas[-len(word):] = new
    anga.meta["upadesha_slp1"] = "".join(v.slp1 for v in anga.varnas)      # the aṅga is now the ādeśa word (the masculine rules no longer name it)
    anga.meta["7_2_99_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.2.99",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tricaturoH striyAM tisfcatasf",
    text_dev              = "त्रिचतुरोः स्त्रियां तिसृचतसृ",
    samagra_slp1          = "tricaturoH striyAM tisfcatasf viBaktO",
    samagra_dev           = "त्रिचतुरोः स्त्रियां तिसृचतसृ विभक्तौ",
    padaccheda_dev        = "त्रि-चतुरोः स्त्रियाम् तिसृ-चतसृ (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "(सूत्रम् 7.2.99) त्रिचतुरोः स्त्रियां तिसृचतसृ।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ("7.1.98", "7.1.99", "7.1.53", "7.1.55"),     # the feminine ādeśa takes the word away from the masculine rules (catvAraH / traya… are not for the feminine)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
