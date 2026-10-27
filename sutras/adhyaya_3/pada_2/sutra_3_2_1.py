"""
3.2.1  कर्मण्यण्  —  VIDHI

Padaccheda: कर्मणि अण्

krt-suffix rule: कर्मण्यण् (1)
Pāṭha: ashtadhyayi.com data.txt row i=32001 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible
from engine.krt_attach import attach_krt, upapada_open, kftya_stem

_GATE_KEY: str = "3_2_1_karmaRyaR_1"


def _site(state: State) -> bool:
    """karmaṇy upapade: aṇ after any dhātu but the ā-final (3.2.3 ka) and hve / ve / mā (3.2.2 aṇ)."""
    if not (upapada_open(state) and not kftya_stem(state).endswith("A") and kftya_stem(state) not in ("hve", "ve")):
        return False
    from engine.registry import get_sutra
    # the special aṇ-takers' apavādas (3.2.20 ṭa, 3.2.38 khac, 3.2.78 ṇini, 3.2.83 ṇini / khaś, 3.2.94 kvanip) take the site away
    return not any(get_sutra(s).cond(state) for s in ("3.2.20", "3.2.38", "3.2.78", "3.2.83", "3.2.94"))


def cond(state: State) -> bool:
    if _site(state):
        return True
    return krt_insertion_eligible(state, "3.2.1", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    if _site(state):
        return attach_krt(state, "aR")
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.1"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRyaR",
    text_dev              = "कर्मण्यण्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karmaRi aR kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कर्मणि अण् कृत्",
    padaccheda_dev        = "कर्मणि अण्",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मण्यण्] विहितः (३.२.1)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
