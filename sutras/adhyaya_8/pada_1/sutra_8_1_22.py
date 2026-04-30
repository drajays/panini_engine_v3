"""
8.1.22  तेमयावेकवचनस्य  —  ANUVADA (narrow ``prakriya_31``)

**Pāṭha (Kāśikā on *Aṣṭ*. 8.1.22):** *tem ayāvekavacasya* — *ādeśa* ``ते`` / ``मे``
for ``युष्मद्`` / ``अस्मद्`` with certain *ṣaṣṭhī*–*caturthī*–*dvitīyā* *ekavacana*
endings (here: ``मे`` after ``अस्मद्`` + ``ङस्``, recipe-narrow).

Narrow v3 (RV **इमं मे …** accent spine):
  • Two-term demo: ``imam`` + ``me``; stamps ``meta['prakriya_31_me_anudAtta_from_8122']``
    on ``terms[1]`` when ``prakriya_31_8_1_22_arm`` is True.

No *svara* columns on ``Varna`` rows.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_31_8_1_22_arm"):
        return False
    if len(state.terms) < 2:
        return False
    t1 = state.terms[1]
    if "prakriya_31_asmad_me_demo" not in t1.tags:
        return False
    if t1.meta.get("upadesha_slp1") != "me":
        return False
    if t1.meta.get("prakriya_31_me_anudAtta_from_8122"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.terms[1].meta["prakriya_31_me_anudAtta_from_8122"] = True
    state.meta.pop("prakriya_31_8_1_22_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.22",
    sutra_type=SutraType.ANUVADA,
    text_slp1="temayAvekavacasya",
    text_dev="तेमयावेकवचनस्य",
    padaccheda_dev="ते / मे / एकवचनस्य",
    why_dev="युष्मदस्मदोः एकवचनान्तयोः ते-मे-आदेशः (*prakriya_31*, मे-श्रुति)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
