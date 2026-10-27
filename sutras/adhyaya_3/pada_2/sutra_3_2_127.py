"""
3.2.127  तौ सत्  —  VIDHI

Padaccheda: तौ सत्

krt-suffix rule: तौ सत् (127)
Pāṭha: ashtadhyayi.com data.txt row i=32127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# tau = the two of 3.2.124 ff: śatṛ and śānac (and the śānan / cānaś that stand beside śānac)
_TAU = frozenset({"Satf~", "Satf", "SAnac", "SAnan", "cAnaS"})


def _sites(state: State):
    return [t for t in state.terms if t.kind == "pratyaya" and "krt" in t.tags and "sat" not in t.tags
            and (t.meta.get("upadesha_slp1") or "") in _TAU]


def cond(state: State) -> bool:
    return bool(_sites(state))


def act(state: State) -> State:
    for t in _sites(state):
        t.tags.add("sat")                 # sat-saṃjñā: 2.2.11 (sat-pradeśa) and the other sat rules read it
    state.samjna_registry["sat"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.127",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "tO sat",
    text_dev              = "तौ सत्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne tO sat kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने तौ सत् कृत्",
    padaccheda_dev        = "तौ सत्",
    why_dev               = "धातोः कृत्-प्रत्ययः [तौ सत्] विहितः (३.२.127)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
