"""
3.4.116  लिङाशिषि  —  VIDHI

Two operational paths:
  1. Legacy arm ``3_4_116_arm``: gate-setter.
  2. Phonological path: āśīr-liṅ context (``state.meta["ashir_liG"]``) — mark
     the tiṅ ādeśa as ārdhadhātuka so 3.4.113 cannot tag it sārvadhatuka.

cond (āśīr-liṅ path): ``state.meta["ashir_liG"]`` is set AND a tiṅ ādeśa
  (tagged ``tin_adesha_3_4_78``) without ``3_4_116_ardhadhatuka_done`` exists.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_116_liNASizi_116"


def _find_tin(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_116_ardhadhatuka_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    # Phonological path: in āśīr-liṅ, mark the tiṅ ādeśa ārdhadhātuka.
    # (The legacy gate-setter arm path is dead — no caller sets ``3_4_116_arm``
    # and the gate it produced is read by no other sūtra.  Art.7: no arm read.)
    if state.meta.get("ashir_liG"):
        return _find_tin(state) is not None
    return False


def act(state: State) -> State:
    if state.meta.get("ashir_liG"):
        idx = _find_tin(state)
        if idx is not None:
            t = state.terms[idx]
            t.tags.discard("sarvadhatuka")
            t.tags.add("ardhadhatuka")
            t.meta["3_4_116_ardhadhatuka_done"] = True
        state.samjna_registry["3.4.116_ardhadhatuka"] = True
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liNASizi",
    text_dev              = "लिङाशिषि",
    padaccheda_dev        = "लिङ् आशिषि",
    why_dev               = (
        "आशीर्-लिङि तिङ्-आदेशः आर्धधातुकः (न सार्वधातुकः) — "
        "एवं ७.३.८४ गुणो न भवति (किद्-यासुट्-कारणात्)।"
    ),
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
