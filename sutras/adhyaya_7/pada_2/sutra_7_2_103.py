"""
7.2.103  किमः कः  —  VIDHI (narrow for P028)

P028: in ``kim`` + nominative dual sup ``O`` (au), replace the prātipadika
``kim`` with ``ka`` so sandhi yields **kO**.

v3 narrow slice:
  • recipe arms ``state.meta['P028_7_2_103_kim_kah_arm']``
  • expects term[0] prātipadika with upadeśa snapshot ``kim``
  • expects a following sup pratyaya (from **4.1.2**) whose tape begins with ``O``
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> bool:
    if not state.meta.get("P028_7_2_103_kim_kah_arm"):
        return False
    if len(state.terms) < 2:
        return False
    a, b = state.terms[0], state.terms[1]
    if "prātipadika" not in a.tags:
        return False
    if (a.meta.get("upadesha_slp1") or "").strip() != "kim":
        return False
    if b.kind != "pratyaya" or "sup" not in b.tags:
        return False
    if not b.varnas or b.varnas[0].slp1 != "O":
        return False
    if a.meta.get("7_2_103_kim_kah_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    a = state.terms[0]
    a.varnas = list(parse_slp1_upadesha_sequence("ka"))
    a.meta["upadesha_slp1"] = "ka"
    a.meta["7_2_103_kim_kah_done"] = True
    state.meta.pop("P028_7_2_103_kim_kah_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.103",
    sutra_type=SutraType.VIDHI,
    text_slp1="kimaH kaH",
    text_dev="किमः कः",
    padaccheda_dev="किमः / कः",
    why_dev="किम्-शब्दस्य क-आदेशः (P028 — किम्+औ → कौ)।",
    anuvritti_from=("7.2.102",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

