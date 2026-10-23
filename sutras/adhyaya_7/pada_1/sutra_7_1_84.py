"""
7.1.84  दिव औत्  —  VIDHI (narrow for P022)

Pāṭha (cross-check: ``sutrANi.tsv`` / ashtadhyayi-com ``data.txt`` i=71084):
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
from engine.declension import anga_and_sup
from phonology import mk


def _site(state: State):
    """दिव औत् — the word दिव् (div, niranubandha) before su (sau): the aṅga's final v becomes औ (द्यौः); yaṇ then gives dy."""
    hit = anga_and_sup(state, "7.1.84")
    if hit is None:
        return None
    anga, sup = hit
    if (anga.meta.get("upadesha_slp1") or "").strip() != "div" or anga.meta.get("7_1_84_done"):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() not in {"s~", "su", "su~"} or anga.varnas[-1].slp1 != "v":
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1] = mk("O")
    anga.meta["7_1_84_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.84",
    sutra_type=SutraType.VIDHI,
    text_slp1='diva Ot',
    text_dev='दिव औत्',
    samagra_slp1="divaH aNgasya sO Ot",
    samagra_dev="दिवः अङ्गस्य सौ औत्",
    padaccheda_dev="दिवः / औत्",
    why_dev="दिव्-शब्दस्य सर्वनामस्थान-सुपि औट्-आदेशः (द्यौः, P022)।",
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

