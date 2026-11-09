"""
8.3.79  विभाषेटः  —  VIDHI

Padaccheda: विभाषा इटः

विभाषेटः (8.3.79)
Pāṭha: ashtadhyayi.com data.txt row i=83079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk

_IN = frozenset("iIuUfFxXeEoOhyvrl")


def _site(state: State):
    """The dh of dhvam/dhve right after an iṭ, in luṅ / liṭ (the iṭ that 8.3.78 leaves alone): लुलुविढ्वे / लुलुविध्वे."""
    for ti, t in enumerate(state.terms):
        if t.meta.get("8_3_79_done"):
            continue
        for vi in range(1, len(t.varnas)):
            v, prev = t.varnas[vi], t.varnas[vi - 1]
            if (v.slp1 == "D" and vi + 1 < len(t.varnas) and t.varnas[vi + 1].slp1 == "v" and prev.slp1 in _IN and "it_agama" in prev.tags
                    and ((t.meta.get("source_lakara_upadesha") or "").strip() in ("liT", "luG")
                         or any(f"tin_src_{x}" in v.tags for x in ("liT", "luG")))):
                return ti, vi
    for i in range(len(state.terms) - 1):                    # before the merge: iṭ | dhve as two Terms
        t1, t2 = state.terms[i], state.terms[i + 1]
        if (t1.varnas and t2.varnas and "pratyaya" in t2.tags and t2.varnas[0].slp1 == "D" and not t2.meta.get("8_3_79_done")
                and (t1.meta.get("it_agama_7_2_35") or "it_agama" in t1.tags or t1.meta.get("upadesha_slp1") == "iw")
                and (t2.meta.get("source_lakara_upadesha") or "").strip() in ("liT", "luG")):
            return i + 1, 0
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    ti, vi = _site(state)
    state.terms[ti].varnas[vi] = _mk("Q")
    state.terms[ti].meta["8_3_79_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.79",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "viBAzewaH",
    text_dev              = "विभाषेटः",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH viBAzA iwaH saH iRaH DaH aNgAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः विभाषा इटः सः इणः धः अङ्गात्",
    padaccheda_dev        = "विभाषा इटः",
    why_dev               = "(सूत्रम् 8.3.79) विभाषेटः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
