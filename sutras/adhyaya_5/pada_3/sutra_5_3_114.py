"""
5.3.114  आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्  —  VIDHI

Padaccheda: आयुध-जीवि-सङ्‍घात् ञ्यट् वाहीकेषु अ-ब्राह्मण-राजन्यात्

आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात् (5.3.114)
Pāṭha: ashtadhyayi.com data.txt row i=53114 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_114_AyuDajIvis_114"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.114", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.114"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    t = taddhita_site(state, None, ok=True, tag="AyuDajIvisaNGa", lacks=("brAhmaRa", "rAjanya"))
    return "Yyaw" if t is not None and "lex:vAhIka" in t.tags else None      # SHORTCUT S55: vāhīkeṣu is a lex: tag of the stem


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.114")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.114", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.114"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AyuDajIvisaMGAYYyaqvAhIkezvabrAhmaRarAjanyAt",
    text_dev              = "आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्",
    samagra_slp1          = "vAhIkezu AyuDajIvisaNGAt abrAhmaRa-rAjanyAt Yyaw",
    samagra_dev           = "वाहीकेषु आयुधजीविसङ्घात् अब्राह्मण-राजन्यात् ञ्यट्",
    padaccheda_dev        = "आयुध-जीवि-सङ्‍घात् ञ्यट् वाहीकेषु अ-ब्राह्मण-राजन्यात्",
    why_dev               = "(सूत्रम् 5.3.114) आयुधजीविसंघाञ्ञ्यड्वाहीकेष्वब्राह्मणराजन्यात्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
