"""
3.2.83  आत्ममाने खश्च  —  VIDHI

Padaccheda: आत्ममाने खः च

krt-suffix rule: आत्ममाने खश्च (83)
Pāṭha: ashtadhyayi.com data.txt row i=32083 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import attach_participle
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return upapada_site(state, "karman", dhatus=frozenset({"mana~"})) if vivaksita(state, "AtmamAna", "AtmamAna") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    if policy_pick(state, "3.2.83", 2) == 0:
        return attach_participle(state, "KaS")      # khaś is śit: dhātoḥ (3.1.91) governs it as it does śatṛ, so Syan / śap come between
    return attach_krt(state, "Rin")      # SHORTCUT S12: ṇini held as ṇin; and by the ca ṇini beside khaś


SUTRA = SutraRecord(
    sutra_id              = "3.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmamAne KaSca",
    text_dev              = "आत्ममाने खश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH AtmamAne KaH ca kft supi RiniH manaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आत्ममाने खः च कृत् सुपि णिनिः मनः",
    padaccheda_dev        = "आत्ममाने खः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [आत्ममाने खश्च] विहितः (३.२.83)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
