"""
1.1.67  तस्मादित्युत्तरस्य  —  PARIBHASHA (narrow **P044**)

*Sūtra:* when a rule uses **pañcamī** (*tasmāt* “from that”), the operation is
understood on the **following** (*uttara*) element.

Engine (``split_prakriyas_11/P044.json``):
  - Base gate ``1.1.67_tasmAd_iti_uttarasya`` on first application.
  - With ``state.meta['P044_1_1_67_atina_arm']``: gate
    ``1.1.67_atiNa_panchami_targets_uttara`` (*atiṅaḥ* in **8.1.28** position).
  - With ``state.meta['P044_1_1_67_siddhi_arm']``: summary gate
    ``1.1.67_panchami_saptami_positional_semantics`` (paired with **1.1.66**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_MAIN = "1.1.67_tasmAd_iti_uttarasya"
_GATE_ATINA = "1.1.67_atiNa_panchami_targets_uttara"
_GATE_SEM = "1.1.67_panchami_saptami_positional_semantics"


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_P044_paribhasha_note"):
        return False
    if state.meta.get("P044_1_1_67_siddhi_arm"):
        return _GATE_SEM not in state.paribhasha_gates
    if state.meta.get("P044_1_1_67_atina_arm"):
        return _GATE_ATINA not in state.paribhasha_gates
    return _GATE_MAIN not in state.paribhasha_gates


def act(state: State) -> State:
    if not state.meta.get("prakriya_P044_paribhasha_note"):
        return state
    if state.meta.get("P044_1_1_67_siddhi_arm"):
        state.paribhasha_gates[_GATE_SEM] = {
            "mode": "panchami_uttara_saptami_purva",
            "why_dev": "पञ्चम्य-उत्तर- vs सप्तम्य-पूर्व-स्थानिकम् (१.१.६७–६६) — P044।",
        }
        state.meta.pop("P044_1_1_67_siddhi_arm", None)
        return state
    if state.meta.get("P044_1_1_67_atina_arm"):
        state.paribhasha_gates[_GATE_ATINA] = {
            "mode": "atiNa_panchami_para_tin",
            "why_dev": "‘अतिङः’ इति पञ्चम्यर्थः पर-तिङन्ते कार्यम् — १.१.६७ + ८.१.२८ (P044)।",
        }
        state.meta.pop("P044_1_1_67_atina_arm", None)
        return state
    state.paribhasha_gates[_GATE_MAIN] = {
        "mode": "panchami_uttara",
        "why_dev": "पञ्चम्यर्थे निर्देशे पर-ग्रहणम् — १.१.६७ (P044)।",
    }
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.67",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="tasmAd iti uttarasya",
    text_dev="तस्मादित्युत्तरस्य",
    padaccheda_dev="तस्मात् / इति / उत्तरस्य",
    why_dev="परिभाषा-गेट: पञ्चम्यर्थे पर-ग्रहणम् (१.१.६७) — P044।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
