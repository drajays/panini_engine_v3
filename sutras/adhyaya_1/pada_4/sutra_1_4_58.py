"""
1.4.58  प्रादयः  (prādayaḥ)  —  SAMJNA

The pra-ādi words (upasargas starting with pra) are nipātas.
This sūtra registers the canonical upasarga list in the saṃjñā registry.

The twenty upasargas (in SLP1): pra, parA, apa, sam, anu, ava, nis, nir,
dus, dur, vi, A, ni, aDi, api, ati, su, ut, ud — these also become nipātas
under the adhikāra of 1.4.56 (prāg rīśvarān nipātāḥ).

v3: registers samjna_registry["upasarga_list"] as a frozenset of SLP1 forms.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

# Canonical twenty upasargas (SLP1)
_PRA_ADI: frozenset[str] = frozenset({
    "pra", "parA", "apa", "sam", "anu", "ava",
    "nis", "nir", "dus", "dur", "vi", "A",
    "ni", "aDi", "api", "ati", "su", "ut", "ud",
})


def cond(state: State) -> bool:
    return state.samjna_registry.get("upasarga_list") is None


def act(state: State) -> State:
    state.samjna_registry["upasarga_list"] = _PRA_ADI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.58",
    sutra_type=SutraType.SAMJNA,
    text_slp1="prAdayaH",
    text_dev="प्रादयः",
    padaccheda_dev="प्र-आदयः",
    why_dev="प्रादयः (प्र, परा, अप, सम्, अनु, अव, निस्, निर्, दुस्, दुर्, वि, आ, नि, अधि, अपि, अति, सु, उत्, उद्) "
            "इत्येते निपात-संज्ञाः सन्ति — उपसर्ग-सूचिः संज्ञारजिस्ट्रीयां स्थाप्यते।",
    anuvritti_from=("1.4.56",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
