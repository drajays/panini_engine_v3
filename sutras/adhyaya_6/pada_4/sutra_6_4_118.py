"""
6.4.118  लोपो यि  —  VIDHI

Padaccheda: लोपः यि

लोपो यि (6.4.118)
Pāṭha: ashtadhyayi.com data.txt row i=64118 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_118_lopo_118"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.118", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.118"
    return state


from engine.state import State

from sutras.adhyaya_6.pada_4.sutra_6_4_116 import jahati_site


def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        n = state.terms[i + 1]
        if (jahati_site(state, i) and not t.meta.get("6_4_118_done") and "pratyaya" in n.tags and "kngiti" in n.tags
                and n.varnas and n.varnas[0].slp1 == "y"):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    del t.varnas[-1]                        # जहा + यात् → जह् + यात् (जह्यात्)
    t.meta["6_4_118_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lopo yi",
    text_dev              = "लोपो यि",
    samagra_slp1          = "jahAteH aNgasya sArvaDAtuke kNiti yi lopaH",
    samagra_dev           = "जहातेः अङ्गस्य सार्वधातुके क्ङिति यि लोपः",
    padaccheda_dev        = "लोपः यि",
    why_dev               = "जहाति-अङ्गस्य यकारादौ क्ङिति सार्वधातुके आकारलोपः — जह्यात्, जह्युः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
