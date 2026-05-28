"""
3.2.177  भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्  —  VIDHI

Padaccheda: भ्राज-भास-धुर्वि-द्युत-ऊर्जि-पॄ-जु-ग्रावस्तुवः क्विँप्

krt-suffix rule: भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप् (177)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_177_BrAjaBAsaD_177"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_177_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.177"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.177",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BrAjaBAsaDurvidyutorjipFjugrAvastuvaH kvip",
    text_dev              = "भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्",
    padaccheda_dev        = "भ्राज-भास-धुर्वि-द्युत-ऊर्जि-पॄ-जु-ग्रावस्तुवः क्विँप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्] विहितः (३.२.177)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
