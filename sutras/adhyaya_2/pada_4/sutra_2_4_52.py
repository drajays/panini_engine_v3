"""
2.4.52  अस्तेर्भूः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=20452
- Kāśikā: अस् → भू (आर्धधातुक-प्रत्यय-विवक्षायाम्)
- Cross-validation: pipelines/sthanivat_anal_ashrita_lesson.py — ``derive_aster_bhU``

*As* is replaced by *bhū*; **1.1.56** extends *dhātutva* to the *ādeśa* so **3.1.91** *adhikāra*
and *kṛt* rules treat *bhū* as the *sthānin* *dhātu*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas

_AS_UPADESHA = frozenset({"as", "Asa", "Asa~"})
_BHU_ADESHA = "BU~"


def _find_as_dhatu(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _AS_UPADESHA and not t.meta.get("2_4_52_as_to_bhu_done"):
            return i
    return None


def cond(state: State) -> bool:
    if state.meta.get("2_4_52_as_to_bhu_done"):
        return False
    if not adhikara_in_effect("2.4.52", state, "2.4.35"):
        return False
    return _find_as_dhatu(state) is not None


def act(state: State) -> State:
    i = _find_as_dhatu(state)
    if i is None:
        return state
    t = state.terms[i]
    adesha_substitute_varnas(
        t,
        _BHU_ADESHA,
        state,
        sutra_id="2.4.52",
        gunadharmas=frozenset({DHATUTVA}),
    )
    t.meta["2_4_52_as_to_bhu_done"] = True
    state.meta["2_4_52_as_to_bhu_done"] = True
    state.meta["adesha_kind"] = "2.4.52"
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.52",
    sutra_type=SutraType.VIDHI,
    text_slp1="asterBUH",
    text_dev="अस्तेर्भूः",
    padaccheda_dev="अस्तेः भूः",
    why_dev="अस्-धातोः भू-आदेशः; स्थानिवद्भावेन धातुत्वम् अतिदिश्यते (१.१.५६)।",
    anuvritti_from=("2.4.40",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
