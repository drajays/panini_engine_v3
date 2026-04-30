"""
8.1.28  तिङ्ङतिङः  —  ANUVADA (narrow ``prakriya_27`` *āgaccha*)

**Pāṭha (Kāśikā; *pada* *anupūrvī* from *sūtrāṇi*):** *tiṅantaṃ padam
atiṅantāt padāt param anudāttam* — a **tiṅanta** *pada* after a non-**tiṅanta**
*pada* is **anudātta** (here: **gaccha** portion of **āgaccha** is *sarvānudātta*
in the JSON narrative when no other **tiṅ** *pada* precedes; *śruti* stamp only).

**Engine:** when **8.1.6** has already registered
``prakriya_27_phit481_upasarga_A_udAtta`` and ``prakriya_27_8_1_28_arm`` is set,
stamp ``meta['prakriya_27_gaccha_base_anudAtta_note']`` on ``terms[0]``.

No *udātta* / *anudātta* columns on ``Varna`` rows (same policy as **6.1.158** demos).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_27_8_1_28_arm"):
        return False
    if not state.samjna_registry.get("prakriya_27_phit481_upasarga_A_udAtta"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "tinanta_accent_demo" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "AgacCa":
        return False
    if t0.meta.get("prakriya_27_gaccha_base_anudAtta_note"):
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    state.terms[0].meta["prakriya_27_gaccha_base_anudAtta_note"] = True
    state.meta.pop("prakriya_27_8_1_28_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.28",
    sutra_type=SutraType.ANUVADA,
    text_slp1="tiNgatiNg",
    text_dev="तिङ्ङतिङः",
    padaccheda_dev="तिङन्तं पदम् / अतिङन्तात् / पदात् / परम् / अनुदात्तम्",
    why_dev="तिङन्त-पदे अनुदात्त-अनुवादः — *gaccha* भागः (*prakriya_27* मध्ये)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
