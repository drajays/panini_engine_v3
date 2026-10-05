"""
7.2.72  स्तुसुधूञ्भ्यः परस्मैपदेषु  —  VIDHI

Padaccheda: स्तु-सु-धूञ्भ्यः परस्मैपदेषु

स्तुसुधूञ्भ्यः परस्मैपदेषु (7.2.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_ROOTS = frozenset({"zuY", "zwuY", "DUY"})        # सु (svādi सुञ्, SK's sāhacarya view), स्तु, धू — KV 7.2.72


def _site(state: State):
    """स्तुसुधूञ्भ्यः परस्मैपदेषु: iṭ for sic after these roots in parasmaipada luṅ — अस्तावीत्, असावीत्, अधावीत्; ātmane अस्तोष्ट."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "sic" for t in state.terms):
        return None
    tins = [t for t in state.terms if "tin_adesha_3_4_78" in t.tags]
    if not tins or not any("parasmaipada" in t.tags for t in tins):
        return None
    for dh in state.terms:
        if "dhatu" in dh.tags and (dh.meta.get("upadesha_slp1") or "").strip() in _ROOTS and not dh.meta.get("7_2_72_done"):
            return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    dh = _site(state)
    if dh is not None:
        dh.meta.update({"7_2_72_done": True, "set_dhatu": True, "anit_dhatu": False})
        sic = next(t for t in state.terms if (t.meta.get("upadesha_slp1") or "").strip() == "sic")
        if sic.varnas and "it_agama" not in sic.varnas[0].tags:
            from phonology import mk
            v = mk("i")
            v.tags.add("it_agama")
            sic.varnas.insert(0, v)
            sic.meta["it_agama_7_2_35_done"] = True        # one iṭ per affix
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "stusuDUYByaH parasmEpadezu",
    text_dev              = "स्तुसुधूञ्भ्यः परस्मैपदेषु",
    padaccheda_dev        = "स्तु-सु-धूञ्भ्यः परस्मैपदेषु",
    why_dev               = "(सूत्रम् 7.2.72) स्तुसुधूञ्भ्यः परस्मैपदेषु।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
