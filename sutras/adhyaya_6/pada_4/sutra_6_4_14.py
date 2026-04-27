"""
6.4.14  अत्वसन्तस्य चाधातोः  —  VIDHI

Narrow v3: under **6.4.1**, when ``state.meta["6_4_14_arm"]`` and the *aṅga*
ends in ``…vant`` or ``…mant`` (after **7.1.70** *nuṃ*) before a
*sarvanāmasthāna* *sup*, lengthen the short ``a`` sandwiched between ``v``/``m``
and ``n`` (the *upadhā* *a* of the *atvasanta* / *matup* shape) to ``A`` (``ā``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk


def _hit(state: State):
    if not state.meta.get("6_4_14_arm"):
        return None
    if not adhikara_in_effect("6.4.14", state, "6.4.1"):
        return None
    if len(state.terms) < 2:
        return None
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags:
        return None
    if "dhatu" in anga.tags:
        return None
    if "sup" not in pr.tags or "sarvanamasthana" not in pr.tags:
        return None
    vs = anga.varnas
    if len(vs) < 4:
        return None
    # … v a n t  or  … m a n t  at end (7.1.70 nuṃ already inserted)
    if vs[-1].slp1 != "t" or vs[-2].slp1 != "n":
        return None
    if vs[-3].slp1 != "a" or vs[-4].slp1 not in ("v", "m"):
        return None
    return len(vs) - 3


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    ji = _hit(state)
    if ji is None:
        return state
    anga = state.terms[-2]
    anga.varnas[ji] = mk("A")
    anga.meta["6_4_14_atvasanta_dirgha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.14",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "atvasantasya cAdhAtoH",
    text_dev       = "अत्वसन्तस्य चाधातोः",
    padaccheda_dev = "अत्वसन्तस्य / च / अधातोः",
    why_dev        = "अत्वन्त-अङ्गस्य उपधा-अचः दीर्घः सर्वनामस्थाने परि।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
