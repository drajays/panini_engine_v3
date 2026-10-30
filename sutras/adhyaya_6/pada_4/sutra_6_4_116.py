"""
6.4.116  जहातेश्च  —  VIDHI

Padaccheda: जहातेः च

जहातेश्च (6.4.116)
Pāṭha: ashtadhyayi.com data.txt row i=64116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_116_jahAteSca_116"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.116", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.116"
    return state


from engine.state import State
from phonology import mk

from sutras.adhyaya_6.pada_4.sutra_6_4_115 import weak_hal_after


def jahati_site(state: State, i: int) -> bool:
    """hā of the juhotyādi (an abhyasta aṅga: जहाति), not hīyate."""
    t = state.terms[i]
    return ("dhatu" in t.tags and "abhyasa" not in t.tags and "".join(v.slp1 for v in t.varnas) == "hA"
            and i > 0 and "abhyasa" in state.terms[i - 1].tags)


def _find(state: State):
    for i, t in enumerate(state.terms):
        if jahati_site(state, i) and not t.meta.get("6_4_116_done") and weak_hal_after(state, i):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    t.varnas[-1] = mk("i")                  # जहा → जहि (जहितः); the vā: the ī of 6.4.113 (जहीतः)
    t.meta["6_4_116_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.116",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "jahAteSca",
    text_dev              = "जहातेश्च",
    samagra_slp1          = "jahAteH aNgasya hali sArvaDAtuke kNiti it anyatarasyAm",
    samagra_dev           = "जहातेः अङ्गस्य हलि सार्वधातुके क्ङिति इत् अन्यतरस्याम्",
    padaccheda_dev        = "जहातेः च",
    why_dev               = "जहाति-अङ्गस्य अन्यतरस्याम् इकारादेशः (हलादौ क्ङिति सार्वधातुके) — जहितः / जहीतः।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
