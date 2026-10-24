"""
7.1.89  पुंसोऽसुङ्  —  VIDHI

Padaccheda: पुंसः असुङ्

पुंसोऽसुङ् (7.1.89)
Pāṭha: ashtadhyayi.com data.txt row i=71089 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem
from phonology import mk
from engine.state import State

def _site(state: State):
    """पुंसोऽसुङ् — the word पुंस् (with tadantavidhi: सुपुंस्) before a sarvanāmasthāna sup: असुङ् (a-s-u-ṅ, ṅit: it takes the place of the
    last letter s); the u is its it, which makes the aṅga ugit for 7.1.70 (पुमान्, पुमांसौ). The anusvāra of पुंस् is the m of पुम्स्."""
    hit = anga_and_sup(state, "7.1.89")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "puMs", "pums", tadanta=True) or "sarvanamasthana" not in sup.tags or anga.meta.get("7_1_89_done"):
        return None
    return anga if anga.varnas[-1].slp1 == "s" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1:] = [mk("a"), mk("s")]
    for k, v in enumerate(anga.varnas):
        if v.slp1 == "M":
            anga.varnas[k] = mk("m")
    anga.tags.add("origin_it:u")           # asuṅ's u: the aṅga is now ugit (engine/origin reads this record)
    anga.meta["7_1_89_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.89",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'puMsosuN',
    text_dev              = 'पुंसोऽसुङ्',
    samagra_slp1          = "sarvanAmasTAne puMsaH asuN",
    samagra_dev           = "सर्वनामस्थाने पुंसः असुङ्",
    padaccheda_dev        = "पुंसः असुङ्",
    why_dev               = "(सूत्रम् 7.1.89) पुंसोऽसुङ्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
