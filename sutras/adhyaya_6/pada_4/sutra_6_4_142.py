"""
6.4.142  ति विंशतेर्डिति  —  VIDHI

Padaccheda: ति (लुप्तषष्ठ्यन्तनिर्देशः) विंशतेः डिति

ति विंशतेर्डिति (6.4.142)
Pāṭha: ashtadhyayi.com data.txt row i=64142 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_142_ti_142"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.142", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.142"
    return state


def _site(state: State):
    """ति विंशतेर्डिति: the ti of a bha viṃśati goes before a ḍit pratyaya (viṃśakaḥ, ḍvun 5.1.24); apavāda of 6.4.143 ṭeḥ, which would take only the i."""
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if "anga" not in t.tags or t.meta.get("6_4_142_done") or not ({"taddhita", "pratyaya"} <= pr.tags and {"it:qit", "origin_it:q"} & pr.tags):
            continue
        if "".join(v.slp1 for v in t.varnas).endswith("viMSati"):
            return t
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    del t.varnas[-2:]
    t.meta["6_4_142_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ti viMSaterqiti",
    text_dev              = "ति विंशतेर्डिति",
    samagra_slp1          = "viMSateH Basya teH qiti lopaH",
    samagra_dev           = "विंशतेः भस्य तेः डिति लोपः",
    padaccheda_dev        = "ति (लुप्तषष्ठ्यन्तनिर्देशः) विंशतेः डिति",
    why_dev               = "(सूत्रम् 6.4.142) ति विंशतेर्डिति।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.143',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
