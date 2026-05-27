"""
2.2.1  पूर्वापराधरोत्तरमेकदेशिनैकाधिकरणे  —  VIDHI

पदच्छेदः  पूर्व-अपर-अधर-उत्तरम् / एकदेशिना / एकाधिकरणे

अनुवृत्तिः  (प्राक्कडारात् समासः 2.1.3)

Kāśikā summary: the four words *pūrva*, *apara*, *adhara*, *uttara* — when
denoting a part (*ekadeśin*) within a shared locus (*ekādhikaraṇa*) — form a
tatpuruṣa compound.  Examples: *pūrvakāyaḥ* (pūrva + kāya), *aparakāyaḥ*,
*adharakāyaḥ*, *uttarakāyaḥ*.

Engine (narrow, mechanically blind):
  Gate key ``2_2_1_purva_apara_gate`` on ``paribhasha_gates``.  Recipe sets
  ``state.meta['2_2_1_arm']`` and provides two *prātipadika* Terms where the
  first carries tag ``pUrva_apara`` and the second carries tag ``ekadesha``.
  After merge the gate is raised and a registry stamp is recorded.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_PUURVA_APARA = frozenset({"pUrva", "apara", "aDara", "uttara"})


def _pair_ok(state: State) -> bool:
    terms = state.terms
    if len(terms) < 2:
        return False
    for i in range(len(terms) - 1):
        t1, t2 = terms[i], terms[i + 1]
        if "prātipadika" not in t1.tags or "prātipadika" not in t2.tags:
            continue
        if "pUrva_apara" in t1.tags and "ekadesha" in t2.tags:
            return True
    return False


def cond(state: State) -> bool:
    if state.paribhasha_gates.get("2_2_1_purva_apara_gate") is True:
        return False
    return _pair_ok(state)


def act(state: State) -> State:
    state.paribhasha_gates["2_2_1_purva_apara_gate"] = True
    state.samjna_registry["2_2_1_purva_apara_ekadesha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.2.1",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="pUrva-apara-aDara-uttaram ekadeSinA ekADikaraRe",
    text_dev="पूर्वापराधरोत्तरमेकदेशिनैकाधिकरणे",
    padaccheda_dev="पूर्व-अपर-अधर-उत्तरम् / एकदेशिना / एकाधिकरणे",
    why_dev=(
        "पूर्वादयः एकदेशिनैकाधिकरणे वर्तमानाः समस्यन्ते — "
        "पूर्वकायः इत्यादि तत्पुरुषः।"
    ),
    anuvritti_from=("2.1.3",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
