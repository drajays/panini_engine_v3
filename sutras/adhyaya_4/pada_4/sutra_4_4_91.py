"""
4.4.91  नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु  —  VIDHI

Padaccheda: नौ-वयो-धर्म-विष-मूल-मूल-सीता-तुलाभ्यः तार्य-तुल्य-प्राप्य-वध्य-आनाम्य-सम-समित-सम्मितेषु

नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु (4.4.91)
Pāṭha: ashtadhyayi.com data.txt row i=44091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_91_nOvayoDarm_91"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.91", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.91"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape, open_default_frame, default_site, taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _sense(state: State):
    if not stem_ends_tape(state):
        return None
    if vivaksita(state, "taddhitArtha", "tArya") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('tArya', {'stems': ['nO']})
    if vivaksita(state, "taddhitArtha", "tulya") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('tulya', {'stems': ['vayas']})
    if vivaksita(state, "taddhitArtha", "prApya") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('prApya', {'stems': ['Darma']})
    if vivaksita(state, "taddhitArtha", "vaDya") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('vaDya', {'stems': ['viza']})
    if vivaksita(state, "taddhitArtha", "AnAmya") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('AnAmya', {'stems': ['mUla']})
    if vivaksita(state, "taddhitArtha", "sama") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('sama', {'stems': ['mUla']})
    if vivaksita(state, "taddhitArtha", "samita") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('samita', {'stems': ['sItA']})
    if vivaksita(state, "taddhitArtha", "sammita") and not any(e.get("id") == "4.4.91" for e in state.adhikara_stack) and vivaksita(state, "arthaViSeSa", "saMjYA"):
        return ('sammita', {'stems': ['tulA']})
    return None


def _new_cond(state: State) -> bool:
    return _sense(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _sense(state) is not None:
        v, only = _sense(state)
        return open_default_frame(state, "4.4.91", v, "4.4.75", "5.1.4", only)
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.4.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nOvayoDarmavizamUlamUlasItAtulAByastAryatulyaprApyavaDyAnAmyasamasamitasammitezu",
    text_dev              = "नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु",
    samagra_slp1          = "nO-vayo-Darma-viza-mUla-mUla-sItA-tulAByaH tArya-tulya-prApya-vaDya-AnAmya-sama-samita-sammitezu saMjYAyAm yat",
    samagra_dev           = "नौ-वयो-धर्म-विष-मूल-मूल-सीता-तुलाभ्यः  तार्य-तुल्य-प्राप्य-वध्य-आनाम्य-सम-समित-सम्मितेषु संज्ञायाम् यत्",
    padaccheda_dev        = "नौ-वयो-धर्म-विष-मूल-मूल-सीता-तुलाभ्यः तार्य-तुल्य-प्राप्य-वध्य-आनाम्य-सम-समित-सम्मितेषु",
    why_dev               = "(सूत्रम् 4.4.91) नौवयोधर्मविषमूलमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसम्मितेषु।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
