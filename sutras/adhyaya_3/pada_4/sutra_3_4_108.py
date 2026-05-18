"""
3.4.108  झेर्जुस्  —  VIDHI

Two operational paths:
  1. Arm ``3_4_108_arm``: legacy gate-setter (krt_kind = 3.4.108).
  2. Arm ``3_4_108_liG_jus_arm``: vidhi-liṅ — substitute the jhi tiṅ ādeśa
     with jus residue [u,s].  jus upadeśa = j+u+s; j is cuṭu-it (1.3.7)
     and drops via 1.3.9, leaving [u,s].  Substituted directly here.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_GATE_KEY: str = "3_4_108_Jerjus_108"


def _find_jhi_tin(state: State) -> int | None:
    """Find the jhi tiṅ ādeśa for vidhi-liṅ jus-substitution."""
    if not state.meta.get("3_4_108_liG_jus_arm"):
        return None
    if state.meta.get("3_4_108_liG_done"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        up  = (t.meta.get("upadesha_slp1") or "").strip()
        cur = "".join(v.slp1 for v in t.varnas)
        if up == "jhi" and cur in {"jhi", "jh", "j"}:
            return i
    return None


def cond(state: State) -> bool:
    if _find_jhi_tin(state) is not None:
        return True
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_108_arm") is True


def act(state: State) -> State:
    j = _find_jhi_tin(state)
    if j is not None:
        t = state.terms[j]
        # jus = j+u+s; j is cuṭu-it, pre-dropped here (like yāsuṭ's u~/T).
        t.varnas = [mk("u"), mk("s")]
        t.meta["upadesha_slp1"] = "jus"
        t.meta["3_4_108_liG_done"] = True
        t.tags.discard("upadesha")  # prevent 1.3.3 from re-marking 's' as halantyam-it
        state.meta.pop("3_4_108_liG_jus_arm", None)
        state.samjna_registry["3.4.108_jhi_jus"] = True
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Jerjus",
    text_dev              = "झेर्जुस्",
    padaccheda_dev        = "झेः जुस्",
    why_dev               = (
        "विधि-लिङि झि-आदेशस्य स्थाने जुस् (j-cuṭु-it → लोपः → [u,s])।"
    ),
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
