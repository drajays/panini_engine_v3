"""
2.4.17  स नपुंसकम्  —  VIDHI

Padaccheda: सः नपुंसकम्

The dvandva compound is neuter.
Pāṭha: ashtadhyayi.com data.txt row i=24017 (Art. 14).
Kāśikā: यस्यायमेकवद्भावो विहितः स नपुंसकलिङ्गो भवति द्विगुर्द्वन्द्वश्च।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_17_sa_napumsaka"


def _old_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def _old_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.17"
    return state


def _site(state: State):
    """The uttarapada of a dvigu (ekavadbhāva by 2.4.1): the compound is neuter, not the liṅga of the last member."""
    last = next((t for t in reversed(state.terms) if "samasa_uttarapada" in t.tags), None)
    if last is None or "dvigu" not in last.tags or any(x.startswith("samasa_linga:") for x in last.tags):
        return None
    return last


def cond(state: State) -> bool:
    return _site(state) is not None or _old_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _old_act(state)
    t.tags.add("samasa_linga:napuṃsaka")
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sa napuMsakam",
    text_dev              = "स नपुंसकम्",
    samagra_slp1          = "saH napuMsakam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "सः नपुंसकम्",
    padaccheda_dev        = "सः नपुंसकम्",
    why_dev               = "सः नपुंसकम् (२.४.१७)।",
    anuvritti_from        = ('2.4.1',),
    apavada_of            = ("2.4.26",),      # paravalliṅgatāpavādo yogaḥ (Kāśikā 2.4.17)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
