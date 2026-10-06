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

_AS_UPADESHA = frozenset({"as", "asa~"})        # adādi as (bhuvi) — not āsa~ (to sit), whose capital A the old set confused with it
_BHU_ADESHA = "BU"


def _find_as_dhatu(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _AS_UPADESHA and t.meta.get("gana") in (2, None) and not t.meta.get("2_4_52_as_to_bhu_done"):   # adādi as, not bhvādi asa~
            return i
    return None


_ARDHA = frozenset({"liT", "luT", "lRT", "luG", "lRG", "liw", "luw", "lfw", "luN", "lfN"})


def _ardhadhatuka_lakara(state: State) -> bool:
    """आर्धधातुके (anuvṛtti 2.4.35): the lakāra on the tape — liṭ, luṭ, lṛṭ, luṅ, lṛṅ, or āśīr-liṅ — is ārdhadhātuka."""
    return any("ashir_liG" in u.tags or "ardhadhatuka" in u.tags
               or (u.meta.get("source_lakara_upadesha") or u.meta.get("upadesha_slp1") or "").strip() in _ARDHA
               for u in state.terms if "dhatu" not in u.tags)


def cond(state: State) -> bool:
    if state.meta.get("2_4_52_as_to_bhu_done"):
        return False
    if not (adhikara_in_effect("2.4.52", state, "2.4.35") or _ardhadhatuka_lakara(state)):
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
    t.meta["upadesha_slp1"] = "BU~"          # the dhātu bhū as the dhātupāṭha names it (the tape letters are BU)
    t.meta.update({"2_4_52_as_to_bhu_done": True, "set_dhatu": True, "anit_dhatu": False, "ekac_dhatu": True, "gana": 1})   # bhū is seṭ (भविता)
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
