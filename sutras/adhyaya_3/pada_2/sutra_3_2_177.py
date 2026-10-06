"""
3.2.177  भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्  —  VIDHI

Padaccheda: भ्राज-भास-धुर्वि-द्युत-ऊर्जि-पॄ-जु-ग्रावस्तुवः क्विँप्

krt-suffix rule: भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप् (177)
Pāṭha: ashtadhyayi.com data.txt row i=32177 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_177_BrAjaBAsaD_177"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.177", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


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
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu BrAja-BAsa-Dur-vidyuta-Urji-pF-ju-grAva-stuvaH kvip kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु भ्राज-भास-धुर्-विद्युत-ऊर्जि-पॄ-जु-ग्राव-स्तुवः क्विप् कृत्",
    padaccheda_dev        = "भ्राज-भास-धुर्वि-द्युत-ऊर्जि-पॄ-जु-ग्रावस्तुवः क्विँप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्] विहितः (३.२.177)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
