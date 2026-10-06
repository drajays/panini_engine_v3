"""
3.4.116  लिङाशिषि  —  VIDHI

Two operational paths:
  1. Legacy arm ``3_4_116_arm``: gate-setter.
  2. Phonological path: āśīr-liṅ context (``state.meta["ashir_liG"]``) — mark
     the tiṅ ādeśa as ārdhadhātuka so 3.4.113 cannot tag it sārvadhatuka.

cond (āśīr-liṅ path): ``state.meta["ashir_liG"]`` is set AND a tiṅ ādeśa
  (tagged ``tin_adesha_3_4_78``) without ``3_4_116_ardhadhatuka_done`` exists.
Pāṭha: ashtadhyayi.com data.txt row i=34116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

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


def _structural_site(state: State) -> int | None:
    """आशिषि liṅ's tiṅ (the tag travels from the lakāra placeholder 3.3.173 attached)."""
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and "tin_adesha_3_4_78" in t.tags and "ashir_liG" in t.tags \
                and not t.meta.get("3_4_116_ardhadhatuka_done"):
            return i
    return None


def cond(state: State) -> bool:
    if _structural_site(state) is not None:
        return True
    return tin_pratyaya_gate_eligible(state, "3.4.116", gate_key=_GATE_KEY)


def act(state: State) -> State:
    i = _structural_site(state)
    if i is not None:
        t = state.terms[i]
        t.tags.discard("sarvadhatuka")
        t.tags.discard("sarvadhatuka_3_4_113")
        t.tags.add("ardhadhatuka")
        t.meta["3_4_116_ardhadhatuka_done"] = True
        state.samjna_registry["3.4.116_ardhadhatuka"] = True
        state.meta["__why_now_dev__"] = "आशिषि लिङ्-लकारस्य तिङ् आर्धधातुकसंज्ञः (तिङ्शित्सार्वधातुकम् ३.४.११३ इत्यस्य अपवादः) — अतः शप् नास्ति, गुणः ङित्-वत् न। (३.४.११६)"
        return state
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
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "liNASizi",
    text_dev              = "लिङाशिषि",
    samagra_slp1          = "ASizi liN tiN ArDaDAtukam",
    samagra_dev           = "आशिषि लिङ् तिङ् आर्धधातुकम्",
    padaccheda_dev        = "लिङ् आशिषि",
    why_dev               = (
        "आशीर्-लिङि तिङ्-आदेशः आर्धधातुकः (न सार्वधातुकः) — "
        "एवं ७.३.८४ गुणो न भवति (किद्-यासुट्-कारणात्)।"
    ),
    anuvritti_from        = ('3.1.1',),
    apavada_of            = ("3.4.113",),   # आशिषि liṅ's tiṅ is ārdhadhātuka, not sārvadhātuka
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
