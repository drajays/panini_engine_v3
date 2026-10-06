"""
6.4.55  अयामन्ताल्वाय्येत्न्विष्णुषु  —  VIDHI

Padaccheda: अय् आम्-अन्त-आलु-आय्य-इत्नु-इष्णुषु

अयामन्ताल्वाय्येत्न्विष्णुषु (6.4.55)
Pāṭha: ashtadhyayi.com data.txt row i=64055 (Art. 14).
"""
from __future__ import annotations
from phonology import mk

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_55_ayAmantAlv_55"


def _site(state: State) -> int | None:
    """अयामन्ताल्वाय्येत्न्विष्णुषु (णेः, 6.4.51): the ṇi of a ṇijanta aṅga → ay
    before ām (and ānta, ālu, āyya, itnu, iṣṇu): चोरि + आम् → चोरयाम्."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or not t.meta.get("nijanta") or t.meta.get("6_4_55_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "i":
            continue
        if (state.terms[i + 1].meta.get("upadesha_slp1") or "").strip() in {"Am", "Anta", "Alu", "Ayya", "itnu", "izRu"}:
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas = list(t.varnas[:-1]) + [mk("a"), mk("y")]
    t.meta["6_4_55_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "6.4.55",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ayAmantAlvAyyetnvizRuzu",
    text_dev              = "अयामन्ताल्वाय्येत्न्विष्णुषु",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke ay Am-anta-Alu-Ayya-itnu-izRuzu nalopaH ReH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके अय् आम्-अन्त-आलु-आय्य-इत्नु-इष्णुषु नलोपः णेः",
    padaccheda_dev        = "अय् आम्-अन्त-आलु-आय्य-इत्नु-इष्णुषु",
    why_dev               = "(सूत्रम् 6.4.55) अयामन्ताल्वाय्येत्न्विष्णुषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
