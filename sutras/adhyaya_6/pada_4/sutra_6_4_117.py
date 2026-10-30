"""
6.4.117  आ च हौ  —  VIDHI

Padaccheda: आ (लुप्तप्रथमान्तनिर्देशः) च हौ

आ च हौ (6.4.117)
Pāṭha: ashtadhyayi.com data.txt row i=64117 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_117_A_117"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.117", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.117"
    return state


from engine.state import State
from phonology import mk

from sutras.adhyaya_6.pada_4.sutra_6_4_116 import jahati_site


def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        n = state.terms[i + 1]
        if jahati_site(state, i) and not t.meta.get("6_4_117_done") and (n.meta.get("upadesha_slp1") or "").strip() == "hi":
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    t.varnas[-1] = mk("I")                  # जहा + हि: the ā stays (जहाहि, the first part of the sūtra) or the vā ī (जहीहि)
    t.meta["6_4_117_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.117",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "A ca hO",
    text_dev              = "आ च हौ",
    samagra_slp1          = "jahAteH aNgasya A it anyatarasyAm hO",
    samagra_dev           = "जहातेः अङ्गस्य आ, इत् अन्यतरस्याम् हौ",
    padaccheda_dev        = "आ (लुप्तप्रथमान्तनिर्देशः) च हौ",
    why_dev               = "जहाति-अङ्गस्य हौ परे आकारः (जहाहि) अन्यतरस्याम् ईकारश्च (जहीहि)।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
