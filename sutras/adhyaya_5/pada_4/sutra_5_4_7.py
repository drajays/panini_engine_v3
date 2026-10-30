"""
5.4.7  अषडक्षाशितङ्ग्वलंकर्मालम्पुरुषाध्युत्तरपदात् खः  —  VIDHI

Padaccheda: अषडक्ष-आशितङ्‍गु-अलंकर्म-अलम्पुरुष-अधि-उत्तरपदात् खः

अषडक्षाशितङ्ग्वलंकर्मालम्पुरुषाध्युत्तरपदात् खः (5.4.7)
Pāṭha: ashtadhyayi.com data.txt row i=54007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_7_azaqakzASi_7"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.7", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.7"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita

# AMENDMENT 27: a svārthika sūtra — 5.4.7 svārthe khaḥ (Kāśikā); the adhyuttarapada compounds are not modelled (S74). No sense frame, no samartha-vibhakti (Kāśikā 5.3.1); the optional vā (4.1.82, Kāśikā 5.4.39 vikalpaḥ sarvatrānuvartate) is the "-" reading.


def _attach(state: State):
    if not vivaksita(state, "taddhitArtha", "svArTa"):
        return None
    return ('Ka', '-') if taddhita_site(state, None, ok=True, stems=frozenset({"azaqakza", "ASitaNgu", "alaMkarman", "alampuruza"})) is not None else None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.4.7")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.4.7", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the plain stem stays
        state.meta["declined:5.4.7"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.4.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "azaqakzASitaNgvalaMkarmAlampuruzADyuttarapadAt KaH",
    text_dev              = "अषडक्षाशितङ्ग्वलंकर्मालम्पुरुषाध्युत्तरपदात् खः",
    samagra_slp1          = "azaqakza-ASitaNgu-alaMkarma-alampuruza-aDyuttarapadAt KaH",
    samagra_dev           = "अषडक्ष-आशितङ्गु-अलंकर्म-अलम्पुरुष-अध्युत्तरपदात् खः",
    padaccheda_dev        = "अषडक्ष-आशितङ्‍गु-अलंकर्म-अलम्पुरुष-अधि-उत्तरपदात् खः",
    why_dev               = "(सूत्रम् 5.4.7) अषडक्षाशितङ्ग्वलंकर्मालम्पुरुषाध्युत्तरपदात् खः।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
