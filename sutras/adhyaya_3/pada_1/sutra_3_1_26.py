"""
3.1.26  हेतुमति च  —  VIDHI

Glass-box demo slice (भीषयते .md):
  When the recipe arms causative formation, append the sanādi pratyaya ṇic.

Engine representation:
  - By default ṇic is a single ``i`` ``Term`` (``upadesha_slp1`` still ``Ric``).
  - When the stem carries tag ``emit_Ric_tape`` (e.g. **P015** before **7.3.37**),
    the tape is the full ``Ric`` letters so **1.3.7** *cuṭū* can target initial ``R``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    # Structural: nic_recipe="nic" coordination key OR legacy arm.
    if not (state.meta.get("nic_recipe") == "nic" or state.meta.get("3_1_26_nic_arm")):
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    if any("nic" in t.tags for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh0 = state.terms[0]
    # Full ``Ric`` tape when the recipe tags the stem (e.g. **P015** *pā* + *ṇic* before
    # **7.3.37** *yuk*): **1.3.7** needs an initial ``R`` for *cuṭū*.  Default remains the
    # minimal ``i`` residue (other *ṇic* demos merge / augment without re-expanding *ṇ*).
    if "emit_Ric_tape" in dh0.tags:
        dh0.tags.discard("emit_Ric_tape")
        nic_varnas = list(parse_slp1_upadesha_sequence("Ric"))
    else:
        nic_varnas = list(parse_slp1_upadesha_sequence("i"))
    nic = Term(
        kind="pratyaya",
        varnas=nic_varnas,
        tags={"pratyaya", "upadesha", "sanadi", "nic"},
        meta={"upadesha_slp1": "Ric"},
    )
    state.terms.append(nic)
    state.meta.pop("nic_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.26",
    sutra_type=SutraType.VIDHI,
    text_slp1="hetumati ca (Ric)",
    text_dev="हेतुमति च",
    padaccheda_dev="हेतुमति च",
    why_dev="हेतु-अर्थे (प्रेरणार्थके) धातोः परे णिच्-प्रत्ययः।",
    anuvritti_from=("3.1.23",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

