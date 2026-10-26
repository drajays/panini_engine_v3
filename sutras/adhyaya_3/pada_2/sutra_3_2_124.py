"""
3.2.124  लटः शतृशानचावप्रथमासमानाधिकरणे  —  VIDHI

Padaccheda: लटः शतृ-शानचः अ-प्रथमा-समानाधिकरणे

krt-suffix rule: लटः शतृशानचावप्रथमासमानाधिकरणे (124)
Pāṭha: ashtadhyayi.com data.txt row i=32124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible
from engine.krt_attach import dhatu_ends_tape
from engine.state import Term
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "3_2_124_lawaH_124"


def _laT_site(state: State):
    """The dhātu that ends the tape in a participle request (vartamāne laṭ, apraTamāsamānādhikaraṇe): the ādeśa stands in laṭ's place, so there is
    no lakāra on the tape to replace — the pada (1.3.12 … 1.3.78) is read from the dhātu as for a tiṅanta."""
    if state.terms and vivaksita(state, "kala", "vartamAna") and vivaksita(state, "samAnADikaraRa", "apraTamA") and dhatu_ends_tape(state):
        return state.terms[-1]
    return None


def _atmanepada(state: State, ubhaya_pick: bool = False) -> bool:
    """ātmanepada (1.3.12 anudāttaṅita; ubhayapadī by 1.3.72 on the reading's choice) → śānac; else parasmaipada (1.3.78 śeṣāt kartari) → śatṛ."""
    lic = state.terms[-1].meta.get("kartari_atmanepada_licensed")
    if lic == "ubhaya":
        return ubhaya_pick and policy_pick(state, "3.2.124", 2) == 1
    return lic is True


def cond(state: State) -> bool:
    if _laT_site(state) is not None:
        return True
    if not krt_insertion_eligible(state, "3.2.124", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    site = _laT_site(state)
    if site is not None:
        if not any(e.get("id") == "3.1.91" for e in state.adhikara_stack):       # धातोः governs the ādeśa; 3.1.68 śap reads it
            state.adhikara_stack.append({"id": "3.1.91", "scope_end": "3.4.117", "text_dev": "धातोः"})
        up = "SAnac" if _atmanepada(state, ubhaya_pick=True) else "Satf~"
        state.terms.append(Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence(up), tags={"pratyaya", "krt", "upadesha"}, meta={"upadesha_slp1": up}))
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lawaH SatfSAnacAvapraTamAsamAnADikaraRe",
    text_dev              = "लटः शतृशानचावप्रथमासमानाधिकरणे",
    samagra_slp1          = "lawaH apraTamAsamAnADikaraRe vartamAne SatfSAnacO DAtoH paraH",
    samagra_dev           = "लटः अप्रथमासमानाधिकरणे वर्तमाने शतृशानचौ धातोः परः",
    padaccheda_dev        = "लटः शतृ-शानचः अ-प्रथमा-समानाधिकरणे",
    why_dev               = "धातोः कृत्-प्रत्ययः [लटः शतृशानचावप्रथमासमानाधिकरणे] विहितः (३.२.124)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
