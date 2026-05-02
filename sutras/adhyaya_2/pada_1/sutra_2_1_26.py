"""
2.1.26  स्वयं क्तेन  —  VIDHI (narrow P025 *vārttika* frame)

The JSON cites **2.1.26** together with the *vārttika* *tat-karoti tad-ācaṣṭe*
as the locus for replacing an internal *sup* with the causative *ṇic* in the
*paṭu* + *am* → *paṭu* + *ṇic* illustration.

v3 narrow slice (P025 only):
  • ``state.meta["P025_2_1_26_Nic_arm"] == True``
  • witness: ``[prātipadika paTu, sup am]`` as two ``Term`` objects
  • *act*: remove the *sup* ``Term`` and append *ṇic* as ``upadesha_slp1 = "Nic"``
    (parsed with *it* markers; **1.3.7** / **1.3.9** elide ``N`` / ``c``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    if not state.meta.get("P025_2_1_26_Nic_arm"):
        return None
    if len(state.terms) != 2:
        return None
    a, b = state.terms[0], state.terms[1]
    if a.kind != "prakriti" or "prātipadika" not in a.tags:
        return None
    if (a.meta.get("upadesha_slp1") or "").strip() != "paTu":
        return None
    if b.kind != "pratyaya" or "sup" not in b.tags:
        return None
    if (b.meta.get("upadesha_slp1") or "").strip() not in {"am", "am~"}:
        return None
    return True


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    state.terms.pop()
    # Engine SLP1: *ṇ* is ``R`` (see **3.1.26** *Ric* modelling); **1.3.7** *cuṭū*
    # applies to the initial ``R`` of ``Ric``.
    nic = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ric")),
        tags={"pratyaya", "upadesha", "sanadi"},
        meta={"upadesha_slp1": "Nic", "P025_Nic_pratyaya": True},
    )
    state.terms.append(nic)
    state.meta["P025_2_1_26_Nic_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="2.1.26",
    sutra_type=SutraType.VIDHI,
    text_slp1="svayaM ktena",
    text_dev="स्वयं क्तेन",
    padaccheda_dev="स्वयम् / क्तेन",
    why_dev="पटु-प्रातिपदिकात् परे णिच्-प्रत्ययः (P025 *tat-karoti tad-ācaṣṭe* डेमो)।",
    anuvritti_from=("2.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
