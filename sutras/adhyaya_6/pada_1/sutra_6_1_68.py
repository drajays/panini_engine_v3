"""
6.1.68  हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्  —  VIDHI

Narrow v3: when ``state.meta["6_1_68_arm"]``, the *aṅga* ``Term`` ends in a
*hal*, the following *sup* is a single *s* tagged *apṛkta* (**1.2.41**), drop
that *s* ``Varna`` (and remove an emptied *sup* ``Term``).

  • ``prakriya_35`` — ``vAc`` + ``su``→``s`` apṛkta *śruti* slice (JSON ``ordered_sutra_sequence``
    lists **6.1.66** for this prayoga; śāstrīya anchor here is **6.1.68** — ``prakriya_35_vAc_sup_lopa_arm``).
  • ``prakriya_36`` — ``ardhaBAj`` + ``su``→``s`` apṛkta (``…/separated_prakriyas/prakriya_36_*.json``
    lists **6.1.66** only; commentary uses **6.1.68** — ``prakriya_36_ardhaBAj_sup_lopa_arm``).
  • ``prakriya_37`` — ``ṭāp``/long-vowel-final stem ``pAcakavndArikA`` + apṛkta ``s`` (*śruti* slice for
    **पाचकवृन्दारिका** — ``prakriya_37_6_1_68_tApanta_arm``; distinct from the ``hal``-final branch above).

  • P023 — ``dyukAmA`` (ṭāp-anta) + apṛkta ``s`` → lopa (``P023_6_1_68_tApanta_arm``).
  • P039 — ``viSAKA`` (strī *ṭāp*-anta stem) + apṛkta ``s`` → lopa
    (``P039_6_1_68_tApanta_arm``).
  • P041 — ``agnicit`` (hal-anta) + apṛkta ``s`` → lopa (``P041_6_1_68_arm``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import HAL

from sutras.adhyaya_1.pada_2.sutra_1_2_41 import TAG_APRKTA


def _hal_sup_s_pattern(state: State, meta_arm: str | None) -> bool:
    if len(state.terms) < 2:
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags or len(pr.varnas) != 1:
        return False
    if TAG_APRKTA not in pr.tags:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 not in HAL:
        return False
    if meta_arm == "prakriya_35":
        if not state.meta.get("prakriya_35_vAc_sup_lopa_arm"):
            return False
        if "prakriya_35_vAc_sup_demo" not in anga.tags:
            return False
        if anga.meta.get("upadesha_slp1") != "vAc":
            return False
        return True
    if meta_arm == "prakriya_36":
        if not state.meta.get("prakriya_36_ardhaBAj_sup_lopa_arm"):
            return False
        if "prakriya_36_ardhaBAj_demo" not in anga.tags:
            return False
        if anga.meta.get("upadesha_slp1") != "ardhaBAj":
            return False
        return True
    if not state.meta.get("6_1_68_arm"):
        return False
    return True


def _eligible(state: State) -> bool:
    return _hal_sup_s_pattern(state, None)


def _eligible_prakriya_35_vAc(state: State) -> bool:
    return _hal_sup_s_pattern(state, "prakriya_35")


def _eligible_prakriya_36_ardhaBAj(state: State) -> bool:
    return _hal_sup_s_pattern(state, "prakriya_36")


def _eligible_prakriya_37_tApanta(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if not state.meta.get("prakriya_37_6_1_68_tApanta_arm"):
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags or len(pr.varnas) != 1:
        return False
    if TAG_APRKTA not in pr.tags:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if "prakriya_37_pAcakavndArikA_Atap_demo" not in anga.tags:
        return False
    if anga.meta.get("upadesha_slp1") != "pAcakavndArikA":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 != "A":
        return False
    return True


def _eligible_P023_tApanta(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if not state.meta.get("P023_6_1_68_tApanta_arm"):
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pr.tags or len(pr.varnas) != 1:
        return False
    if TAG_APRKTA not in pr.tags:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 != "A":
        return False
    if not (anga.meta.get("stri_TAp_4_1_4") or "TAp_anta" in anga.tags):
        return False
    return True


def _eligible_P041_agnicit_hal(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if not state.meta.get("P041_6_1_68_arm"):
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "P041_agnicit_demo" not in anga.tags:
        return False
    if "sup" not in pr.tags or len(pr.varnas) != 1:
        return False
    if TAG_APRKTA not in pr.tags:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 not in HAL:
        return False
    return True


def _eligible_P039_tApanta(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if not state.meta.get("P039_6_1_68_tApanta_arm"):
        return False
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "P039_viSAKA_demo" not in anga.tags:
        return False
    if "sup" not in pr.tags or len(pr.varnas) != 1:
        return False
    if TAG_APRKTA not in pr.tags:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if not anga.varnas or anga.varnas[-1].slp1 != "A":
        return False
    if not (anga.meta.get("stri_TAp_4_1_4") or "TAp_anta" in anga.tags):
        return False
    return True


def cond(state: State) -> bool:
    return (
        _eligible_P041_agnicit_hal(state)
        or _eligible_P039_tApanta(state)
        or _eligible_P023_tApanta(state)
        or _eligible_prakriya_37_tApanta(state)
        or _eligible_prakriya_36_ardhaBAj(state)
        or _eligible_prakriya_35_vAc(state)
        or _eligible(state)
    )


def act(state: State) -> State:
    if _eligible_P041_agnicit_hal(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_hal_sup_lopa_P041"] = True
        state.meta.pop("P041_6_1_68_arm", None)
        return state
    if _eligible_P039_tApanta(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_tApanta_sup_lopa_P039"] = True
        state.meta.pop("P039_6_1_68_tApanta_arm", None)
        return state
    if _eligible_P023_tApanta(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_tApanta_sup_lopa_P023"] = True
        state.meta.pop("P023_6_1_68_tApanta_arm", None)
        return state
    if _eligible_prakriya_37_tApanta(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_tApanta_sup_lopa_prakriya_37"] = True
        state.meta.pop("prakriya_37_6_1_68_tApanta_arm", None)
        return state
    if _eligible_prakriya_36_ardhaBAj(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_ardhaBAj_sup_lopa_prakriya_36"] = True
        state.meta.pop("prakriya_36_ardhaBAj_sup_lopa_arm", None)
        return state
    if _eligible_prakriya_35_vAc(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_vAc_sup_lopa_prakriya_35"] = True
        state.meta.pop("prakriya_35_vAc_sup_lopa_arm", None)
        return state
    if _eligible(state):
        pr = state.terms[-1]
        pr.varnas.clear()
        state.terms.pop()
        state.samjna_registry["6.1.68_sut_aprkta_hal_lopa"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.68",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hal~yAbbhyo dIrghAt sutisyapfktaM hal",
    text_dev       = "हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल्",
    padaccheda_dev = "हल्-ङि-आभ्यः / दीर्घात् / सु-तिसि-अपृक्तम् / हल्",
    why_dev        = "हल्-अन्ताद् अङ्गात् परस्य अपृक्त-सु-हल्-लोपः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
