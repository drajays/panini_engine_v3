"""
5.4.87  अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः  —  VIDHI

Padaccheda: अहः-सर्व-एकदेश-संख्यात-पुण्यात् च रात्रेः

अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः (5.4.87)
Pāṭha: ashtadhyayi.com data.txt row i=54087 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_87_ahassarvEk_87"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.87", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.87"
    return state


import re
from engine.gates import adhikara_in_effect
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick

_RX = re.compile(r"(sarva|pUrva|apara|aDara|uttara|saMKyAta|puRya|[a-zA-Z]+)rAtri$")      # SHORTCUT S62: the compound is one Term (S30 / S36); its kind and its last member are read off the lex: tags and the letters


def _attach(state: State):
    if not adhikara_in_effect("5.4.87", state, "5.4.68") or False:
        return None
    t = taddhita_site(state, None, ok=True, final=lambda f: _RX.search(f) is not None)
    if t is None:
        return None
    if not all(f"lex:{x}" in t.tags for x in ('tatpuruza',)):
        return None
    return 'ac'


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.87")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.87", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.4.87"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].tags.add("samasanta")
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahassarvEkadeSasaMKyAtapuRyAcca rAtreH",
    text_dev              = "अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः",
    samagra_slp1          = "tatpuruzasya ahaH-sarva-ekadeSa-saNKyAta-puRyAt saNKyA-avyayAdeH ca rAtreH ac",
    samagra_dev           = "तत्पुरुषस्य अहः-सर्व-एकदेश-सङ्ख्यात-पुण्यात् सङ्ख्या-अव्ययादेः च रात्रेः अच्",
    padaccheda_dev        = "अहः-सर्व-एकदेश-संख्यात-पुण्यात् च रात्रेः",
    why_dev               = "(सूत्रम् 5.4.87) अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
