"""
6.3.94  तिरसस्तिर्यलोपे  —  VIDHI

Padaccheda: तिरसः तिरि (लुप्तप्रथमान्तनिर्देशः) अलोपे

तिरसस्तिर्यलोपे (6.3.94)
Pāṭha: ashtadhyayi.com data.txt row i=63094 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_94_tirasastir_94"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.94", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.94"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)

def _anc_site(state: State, pu: str):
    """The pūrvapada Term ``pu`` right before the añcu dhātu that a kvin / kvip ends (vapratyayānta añcati)."""
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for i, j in zip(live, live[1:]):
        t, d = state.terms[i], state.terms[j]
        if _flat(t) != pu or t.meta.get("6_3_93_95_done") or not ({"samasa_purvapada", "upasarga", "gati"} & t.tags):
            continue
        if "dhatu" in d.tags and (d.meta.get("upadesha_slp1") or "").startswith("aYc") and any(
                (u.meta.get("upadesha_slp1") or "") in ("kvin", "kvip") for u in state.terms[j + 1:]):
            return t
    return None


def _site(state: State):
    """तिरसस्तिर्यलोपे (the a of tiras is still there): ``tiras`` becomes ``tiri`` (the whole, 1.1.55) before the añcu of a kvin-anta (3.2.59)."""
    return _anc_site(state, "tiras")


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    t.varnas[:] = [mk(c) for c in "tiri"]
    t.meta["6_3_93_95_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tirasastiryalope",
    text_dev              = "तिरसस्तिर्यलोपे",
    samagra_slp1          = "apratyaye alope aYcatO uttarapade tirasaH tiri",
    samagra_dev           = "अप्रत्यये अलोपे अञ्चतौ उत्तरपदे तिरसः तिरि",
    padaccheda_dev        = "तिरसः तिरि (लुप्तप्रथमान्तनिर्देशः) अलोपे",
    why_dev               = 'अलुप्ताकारे वप्रत्ययान्ते अञ्चतौ तिरसः तिरि-आदेशः — तिर्यङ्, तिर्यञ्चौ; तिरश्चः नहि।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
