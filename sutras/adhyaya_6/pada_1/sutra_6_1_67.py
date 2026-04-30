"""
6.1.67  वेरपृक्तस्य  —  VIDHI (narrow *glass-box*)

Śāstra: *apṛkta* *v* is elided in specific *saṃhitā* contexts.

Engine (*prakriya_22* / *kvip* residue):
  After **1.3.3**/**1.3.8**/**1.3.9** on ``kvip``, the engine may leave a ``vi`` / ``v``
  residue on the *kṛt* ``Term``.  When ``state.meta['prakriya_22_kvip_residue_arm']``
  is True, delete all Varṇas of the trailing ``kvip`` ``Term`` whose surface is
  exactly ``vi`` or ``v`` (zero *kṛt* affix — *dhātu* alone is the *aṅga*, per
  ``krit_pratyaya.json`` *kvip* note).

``cond`` does not read *vibhakti* / gold forms.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _target_index(state: State) -> int | None:
    if not state.meta.get("prakriya_22_kvip_residue_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "krt" not in t.tags:
            continue
        if t.meta.get("upadesha_slp1") != "kvip":
            continue
        surf = "".join(v.slp1 for v in t.varnas)
        if surf in ("vi", "v"):
            return i
    return None


def cond(state: State) -> bool:
    return _target_index(state) is not None


def act(state: State) -> State:
    j = _target_index(state)
    if j is None:
        return state
    state.terms[j].varnas.clear()
    state.meta.pop("prakriya_22_kvip_residue_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.67",
    sutra_type=SutraType.VIDHI,
    text_slp1="ver apRktasya",
    text_dev="वेरपृक्तस्य",
    padaccheda_dev="वेः / अपृक्तस्य",
    why_dev="क्विप्-शेष-वि-लोपः (*prakriya_22*, ग्लास-बॉक्स्)।",
    anuvritti_from=("6.1.66",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
