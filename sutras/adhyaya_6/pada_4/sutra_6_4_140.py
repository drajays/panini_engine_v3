"""
6.4.140  आतो धातोः  —  VIDHI

Padaccheda: आतः धातोः

आतो धातोः (6.4.140)
Pāṭha: ashtadhyayi.com data.txt row i=64140 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_140_Ato_140"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.140", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.140"
    return state


from engine.state import State

def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if ({"anga", "bha"} <= t.tags and len(t.varnas) > 1 and t.varnas[-1].slp1 == "A"
                and any(x.startswith("origin_dhatu:") for x in t.tags) and not t.meta.get("6_4_140_done")):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    del t.varnas[-1]                        # कीलालपा → कीलालप् (कीलालपः); a dhātu-final ā only (खट्वा keeps it)
    t.meta["6_4_140_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ato DAtoH",
    text_dev              = "आतो धातोः",
    samagra_slp1          = "AtaH DAtoH Basya lopaH",
    samagra_dev           = "आतः धातोः भस्य लोपः",
    padaccheda_dev        = "आतः धातोः",
    why_dev               = "आकारान्तस्य धातोः (धात्वन्तस्य) भस्य आकारलोपः — कीलालपः, शुभंयः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
