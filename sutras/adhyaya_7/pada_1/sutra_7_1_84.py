"""
7.1.84  दिव औत्  —  VIDHI (narrow for P022)

Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=70184):
  *diva aut* — the stem **div** takes the substitute **auT** before a
*sarvanāmasthāna* sup.

v3 narrow slice (P022: द्यौः):
  - recipe arms: ``state.meta["P022_7_1_84_div_aut_arm"] == True``
  - witness: a Term with ``meta["upadesha_slp1"] == "div"`` (or varṇas ``d i v``)
  - following sup Term is tagged ``sarvanamasthana`` (from **1.1.43**)
  - action: rewrite the stem to ``dyOv`` (glass-box: div → dyau + v).

Note: The subsequent *saṃyogānta-lopa* step is handled by **8.2.23** (armed
branch) to drop the final ``v`` before ``su``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    if not state.meta.get("P022_7_1_84_div_aut_arm"):
        return None
    if len(state.terms) < 2:
        return None
    if state.meta.get("P022_7_1_84_div_aut_done"):
        return None
    ang = state.terms[0]
    sup = state.terms[1]
    if (ang.meta.get("upadesha_slp1") or "").strip() not in {"div", "dyOv"}:
        # Fallback: accept bare varṇa identity "div".
        if [v.slp1 for v in ang.varnas] != ["d", "i", "v"]:
            return None
    if sup.kind != "pratyaya" or "sup" not in sup.tags:
        return None
    if "sarvanamasthana" not in sup.tags:
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    ang = state.terms[i]
    ang.varnas = list(parse_slp1_upadesha_sequence("dyOv"))
    ang.meta["upadesha_slp1"] = "dyOv"
    state.meta["P022_7_1_84_div_aut_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.84",
    sutra_type=SutraType.VIDHI,
    text_slp1="diva Out",
    text_dev="दिव औत्",
    padaccheda_dev="दिवः / औत्",
    why_dev="दिव्-शब्दस्य सर्वनामस्थान-सुपि औट्-आदेशः (द्यौः, P022)।",
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

