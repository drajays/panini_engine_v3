"""
3.2.149  अनुदात्तेतश्च हलादेः  —  VIDHI

Padaccheda: अनुदात्त-इतः च हल्-आदेः

krt-suffix rule: अनुदात्तेतश्च हलादेः (149)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_149_anudAtteta_149"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_149_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.149"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.149",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttetaSca halAdeH",
    text_dev              = "अनुदात्तेतश्च हलादेः",
    padaccheda_dev        = "अनुदात्त-इतः च हल्-आदेः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अनुदात्तेतश्च हलादेः] विहितः (३.२.149)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
