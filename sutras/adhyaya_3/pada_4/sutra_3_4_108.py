"""
3.4.108  झेर्जुस्  —  VIDHI

Two operational paths:
  1. Legacy arm ``3_4_108_arm``: gate-setter (krt_kind = 3.4.108).
  2. Phonological path: liṅ/āśīr-liṅ, or seṭ-luṅ 3pl — substitute the jhi
     tiṅ ādeśa with jus residue [u,s].  jus upadeśa = j+u+s; j is cuṭu-it
     (1.3.7) and drops, leaving [u,s].  Discriminated by lakāra key on state.

cond (phonological path): state.meta["lakara"] ∈ {"liG","AsIrliG"} OR
  (lakāra=="luG" AND dhātu is seṭ, i.e. not anit_dhatu) — AND jhi ādeśa
  tagged tin_adesha_3_4_78 is on the tape.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_GATE_KEY: str = "3_4_108_Jerjus_108"

_JUS_LAKARA: frozenset[str] = frozenset({"liG", "AsIrliG"})


def _dhatu_is_anit(state: State) -> bool:
    for t in state.terms:
        if "dhatu" in t.tags and "abhyasa" not in t.tags:
            return bool(t.meta.get("anit_dhatu"))
    return False


def _find_jhi_tin(state: State) -> int | None:
    """Find jhi tiṅ ādeśa — fires from lakāra context, no arm needed."""
    lakara = state.meta.get("lakara", "")
    is_lug_set = lakara == "luG" and not _dhatu_is_anit(state)
    if lakara not in _JUS_LAKARA and not is_lug_set:
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
        t.varnas = [mk("u"), mk("s")]
        t.meta["upadesha_slp1"] = "jus"
        t.meta["3_4_108_liG_done"] = True
        t.tags.discard("upadesha")
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
