"""
6.1.85  अन्तादिवच्च  —  PARIBHASHA

Padaccheda: अन्त-आदि-वत् च

अन्तादिवच्च (6.1.85)
Pāṭha: ashtadhyayi.com data.txt row i=61085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_85_gate"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.85", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    return state


_EKADESA = frozenset(range(87, 112))        # 6.1.87 - 6.1.111: the ekādeśa sūtras under 6.1.84
_MARK = "ekAdeSa_antAdi"


def _is_ekadesa_varna(v) -> bool:
    for g in v.tags:
        if g.startswith("origin:6.1."):
            tail = g.rsplit(".", 1)[1]
            if tail.isdigit() and int(tail) in _EKADESA:
                return True
    return False


def _site(state: State):
    """The varṇa an ekādeśa sūtra (6.1.87 - 111) put in the place of the pūrva's last and the para's first sound."""
    for t in state.terms:
        for v in t.varnas:
            if _MARK not in v.tags and _is_ekadesa_varna(v):
                return v
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    v = _site(state)
    if v is None:
        return _legacy_act(state)
    # one ekādeśa, sthānin of both: it counts as the anta of the pūrva (for what reads the pūrva's final) and the ādi of the para
    v.tags |= {_MARK, "ekAdeSa_pUrvAnta", "ekAdeSa_parAdi"}
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.85",
    sutra_type            = SutraType.ATIDESHA,
    text_slp1             = "antAdivacca",
    text_dev              = "अन्तादिवच्च",
    samagra_slp1          = "pUrvaparayoH ekAdeSaH anta-Adivat ",
    samagra_dev           = "पूर्वपरयोः एकादेशः अन्त-आदिवत् ।",
    padaccheda_dev        = "अन्त-आदि-वत् च",
    why_dev               = "पूर्वपरयोः स्थाने जात एकादेशः पूर्वस्यान्तवत्, परस्यादिवत् — शिव + इहि → शिवेहि (एकादेशः 'ए' पूर्वान्तः परादिश्च)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
