"""
8.2.26  झलो झलि  —  VIDHI (narrow: P033 *ghas*+*ta* span)

Teaching JSON **P033** step 8: in a *jhal*+*jhal* contact, the first *jhal* is *lopa*
when the second is *jhal* — here **s** (first) between **G** and **t** drops,
yielding **Gta**.

Arms: ``state.meta['jhalo_jhali_recipe']``; Tripāḍī zone; single *pada*
with flat ``Gsta``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _flat_pada(state: State) -> str:
    if len(state.terms) != 1 or "pada" not in state.terms[0].tags:
        return ""
    return "".join(v.slp1 for v in state.terms[0].varnas)


_JHAL = frozenset("kKgGcCjJwWqQtTdDpPbBSzsh")


def _sic_s_between_jhal(state: State) -> int | None:
    """झलो झलि (सिचः / सुटः सकारलोपः): the s of sic or of suṭ (3.4.107) between two jhal — अपाक्ताम्, अपक्त.

    Excludes a preceding ष्/ढ् (z/Q): that pair is 8.2.41's षढोः कः सि
    (ष्/ढ् + स् → क् + स्, e.g. शिष्+स्+त् → शिक्ष्त्, अशिक्षत्) — a more
    specific rule for the same site, not a स्-lopa.
    """
    if len(state.terms) != 1:
        return None
    vs = state.terms[0].varnas
    for i in range(1, len(vs) - 1):
        if (({"sic_s", "suw_s"} & vs[i].tags) and vs[i - 1].slp1 in _JHAL and vs[i + 1].slp1 in _JHAL
                and vs[i - 1].slp1 not in ("z", "Q")):
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    if _sic_s_between_jhal(state) is not None:
        return True
    if not state.meta.get("jhalo_jhali_recipe"):
        return False
    if state.terms[0].meta.get("P033_8_2_26_done"):
        return False
    return _flat_pada(state) == "Gsta"


def act(state: State) -> State:
    if not cond(state):
        return state
    i = _sic_s_between_jhal(state)
    if i is not None:
        del state.terms[0].varnas[i]
        return state
    t = state.terms[0]
    vs = t.varnas
    if (
        len(vs) >= 4
        and vs[0].slp1 == "G"
        and vs[1].slp1 == "s"
        and vs[2].slp1 == "t"
        and vs[3].slp1 == "a"
    ):
        del t.varnas[1]
    t.meta["P033_8_2_26_done"] = True
    state.meta.pop("jhalo_jhali_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.2.26",
    sutra_type=SutraType.VIDHI,
    text_slp1='Jalo Jali',
    text_dev='झलो झलि',
    padaccheda_dev="झलः / झलि",
    why_dev="झलो झलि परे लोपः — प०३३ (घ्स्-त-)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
