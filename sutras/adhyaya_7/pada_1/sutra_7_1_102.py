"""
7.1.102  उदोष्ठ्यपूर्वस्य  —  VIDHI

Padaccheda: उत् ओष्ठ्यपूर्वस्य

उदोष्ठ्यपूर्वस्य (7.1.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_102_udozWyapUr_102"
_OSHTHYA = frozenset("pPbBmv")
_DONE = "7_1_102_ur_done"


def _find(state: State):
    """उदोष्ठ्यपूर्वस्य: a dhātu in ṝ after a labial takes ur (not ir, 7.1.100): pF → pur; 8.2.77 then lengthens before a
    consonant (pipUrtAm), 1.1.51 makes the r (pipuratu)."""
    from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or t.meta.get(_DONE) or t.meta.get("anga_guna_7_3_84"):
            continue
        if len(t.varnas) < 2 or t.varnas[-1].slp1 != "F" or t.varnas[-2].slp1 not in _OSHTHYA:
            continue
        j = i + 1
        while j + 1 < len(state.terms) and "agama" in state.terms[j].tags and "yasut_agama" not in state.terms[j].tags:
            j += 1
        nxt = state.terms[j]
        if "kngiti" not in nxt.tags and not nxt.meta.get("is_apit"):
            continue                                   # kṅiti: pipUrtAm — not sic (apArizma has vṛddhi, 7.2.1)
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if (is_sarvadhatuka_upadesha_slp1(up) or "ardhadhatuka" in nxt.tags or "sarvadhatuka" in nxt.tags
                or "sarvadhatuka_3_4_113" in nxt.tags or "tin_adesha_3_4_78" in nxt.tags
                or "yasut_agama" in nxt.tags or "ling_sIyuw" in nxt.tags):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    from phonology import mk
    d0 = state.terms[i]
    d0.varnas[-1] = mk("u")
    d0.meta["urN_rapara_pending"] = "r"
    d0.meta[_DONE] = True
    d0.meta["anga_guna_7_3_84"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.102",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "udozWyapUrvasya",
    text_dev              = "उदोष्ठ्यपूर्वस्य",
    padaccheda_dev        = "उत् ओष्ठ्यपूर्वस्य",
    why_dev               = "(सूत्रम् 7.1.102) उदोष्ठ्यपूर्वस्य।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ("7.1.100",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
