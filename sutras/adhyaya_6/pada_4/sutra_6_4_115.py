"""
6.4.115  भियोऽन्यतरस्याम्  —  VIDHI

Padaccheda: भियः अन्यतरस्याम्

भियोऽन्यतरस्याम् (6.4.115)
Pāṭha: ashtadhyayi.com data.txt row i=64115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_115_Biyonyata_115"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.115", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.115"
    return state


from engine.state import State
from phonology import mk

from sutras.adhyaya_3.pada_4.sutra_3_4_113 import is_sarvadhatuka_upadesha_slp1

_VOWELS = frozenset("aAiIuUfFxXeEoO")


def weak_hal_after(state: State, i: int) -> bool:
    """The Term after i is a hal-initial kṅit sārvadhātuka (the weak ending of 6.4.113 – 118: क्ङिति सार्वधातुके हलि)."""
    if i + 1 >= len(state.terms):
        return False
    n = state.terms[i + 1]
    up = (n.meta.get("upadesha_slp1") or "").strip()
    return "pratyaya" in n.tags and "kngiti" in n.tags and bool(n.varnas) and n.varnas[0].slp1 not in _VOWELS and is_sarvadhatuka_upadesha_slp1(up)


def _find(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags and "abhyasa" not in t.tags and "".join(v.slp1 for v in t.varnas) == "BI" and not t.meta.get("6_4_115_done") and weak_hal_after(state, i):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    t.varnas[-1] = mk("i")                  # भी → भि (बिभितः); the vā: the ī of 6.4.113 stays (बिभीतः)
    t.meta["6_4_115_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.115",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'BiyonyatarasyAm',
    text_dev              = 'भियोऽन्यतरस्याम्',
    samagra_slp1          = "BiyaH aNgasya hali sArvaDAtuke kNiti it anyatarasyAm",
    samagra_dev           = "भियः अङ्गस्य हलि सार्वधातुके क्ङिति इत् अन्यतरस्याम्",
    padaccheda_dev        = "भियः अन्यतरस्याम्",
    why_dev               = "भी-धातोः अन्यतरस्याम् इकारादेशः (हलादौ क्ङिति सार्वधातुके) — बिभितः / बिभीतः।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
