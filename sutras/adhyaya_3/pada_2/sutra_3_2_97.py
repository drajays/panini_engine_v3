"""
3.2.97  सप्तम्यां जनेर्डः  —  VIDHI (narrow: corrected-v2 **P005-B** *upasarajaḥ*)

*Śāstra (laghu):* after *√jan* when the prior *upapada* bears *saptamī*, the *kṛt*
**ḍa** (*ḍ*) is introduced.

Engine: armed ``corrected_v2_P005_B_3_2_97_arm`` — insert **qa** (ड् + अ) after the
``jan~`` *dhātu* ``Term`` as a ``kṛt`` *pratyaya* (SLP1 ``q`` = ड्).  The affix is
tagged ``dit_pratyaya`` so **6.4.143** (*ṭi*-lopa before *ḍit*) can apply under the
recipe meta arm for this row.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_META_ARM = "corrected_v2_P005_B_3_2_97_arm"


def _jan_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "jan~":
            continue
        return i
    return None


def cond(state: State) -> bool:
    i = _jan_index(state)
    if i is None:
        return False
    if i + 1 < len(state.terms):
        nxt = state.terms[i + 1]
        if "krt" in nxt.tags and (nxt.meta.get("upadesha_slp1") or "").strip() == "qa":
            return False
    return True


def act(state: State) -> State:
    i = _jan_index(state)
    if i is None:
        return state
    qa = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("qa")),
        tags={"pratyaya", "krt", "upadesha", "dit_pratyaya"},
        meta={"upadesha_slp1": "qa"},
    )
    state.terms.insert(i + 1, qa)
    state.samjna_registry["3.2.97_P005_B_qa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.97",
    sutra_type=SutraType.VIDHI,
    text_slp1="saptamyAM janer qaH",
    text_dev="सप्तम्यां जनेर्डः",
    padaccheda_dev="सप्तम्याम् / जनेः / डः",
    why_dev="उपपद-सप्तम्यां जनेः परः डः कृत् (प००५-ब)।",
    anuvritti_from=("3.1.25",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
