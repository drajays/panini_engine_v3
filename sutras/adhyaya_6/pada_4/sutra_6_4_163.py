"""
6.4.163  प्रकृत्यैकाच्  —  VIDHI

Padaccheda: प्रकृत्या एक-अच्

प्रकृत्यैकाच् (6.4.163)
Pāṭha: ashtadhyayi.com data.txt row i=64163 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_163_prakftyEkA_163"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.163", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.163"
    return state


from engine.state import State

from sutras.adhyaya_6.pada_4.sutra_6_4_156 import _DONE


def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        n = state.terms[i + 1]
        up = (n.meta.get("upadesha_slp1") or "").strip()
        flat = [v.slp1 for v in t.varnas]
        if ("anga" in t.tags and sum(1 for x in flat if x in "aAiIuUfFxXeEoO") == 1 and not t.meta.get("6_4_155_family_done")
                and any(x.startswith("origin_pratyaya:") and ("vin" in x or "mat" in x) for x in t.tags)
                and n.kind == "pratyaya" and up.startswith(("izW", "iman", "Iyas"))):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    state.terms[hit].meta.update(_DONE)     # प्रकृत्या: the ekāc aṅga stays as it is (स्रजिष्ठः, स्रजीयान्): the ṭi family of 6.4.155 – 159 skips it
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.163",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakftyEkAc",
    text_dev              = "प्रकृत्यैकाच्",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya prakftyA ekAc izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य प्रकृत्या एकाच् इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev        = "प्रकृत्या एक-अच्",
    why_dev               = "इष्ठ-इमन्-ईयस्सु परतः एकाच् भसंज्ञकम् प्रकृत्या भवति — स्रजिष्ठः, स्रजीयान्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
