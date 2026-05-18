"""
2.4.85  लुटः प्रथमस्य डारौरसः  —  VIDHI

When ``2_4_85_lut_prathama_arm`` is set and the *tiṅ* residue is the *prathama*
*parasmaipada* shape (after *halantyam*-lopa on *tip*/*tas*/*jhi*), replace it
with the adesha given by ``state.meta['2_4_85_adesha_slp1']``:
  - ``ti``  (from *tip*)  → ``qA``  (ḍā)
  - ``tas`` (from *tas*)  → ``rO``  (rau)
  - ``jhi`` (from *jhi*)  → ``ras`` (ras)

The *recipe* commits the target adesha in ``state.meta['2_4_85_adesha_slp1']``
so ``cond`` remains blind to *puruṣa* / *vacana* coordinates (CONSTITUTION Art. 2).

For backward-compat, when ``2_4_85_adesha_slp1`` is absent, defaults to *ti* → *qA*
(the legacy single-cell path).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk
from phonology.varna import parse_slp1_upadesha_sequence

# Map: (expected current varnas of tiṅ residue, upadesha) → adesha SLP1
_PRATHAMA_MAP: dict[str, tuple[str, ...]] = {
    "qA" : ("ti",),          # tip → qA (ḍā)
    "rO" : ("tas",),         # tas → rO (rau)
    "ras": ("jhi",),         # jhi → ras (ras)
}


def _find_tin_residue(state: State, expected_varnas: tuple[str, ...]) -> int | None:
    """Find the rightmost pratyaya term whose varnas match expected_varnas (SLP1 sequence)."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if "pratyaya" not in t.tags:
            continue
        vs = tuple(v.slp1 for v in t.varnas)
        if vs == expected_varnas:
            return i
        # Also accept tuple prefix for jhi (may still have h if 1.3.9 not yet fired)
        # but in our pipeline 1.3.3/1.3.9 fired before 2.4.85 for jhi
    return None


def cond(state: State) -> bool:
    if not state.meta.get("2_4_85_lut_prathama_arm"):
        return False
    if state.meta.get("2_4_85_lut_prathama_done"):
        return False
    adesha = (state.meta.get("2_4_85_adesha_slp1") or "qA").strip()
    expected_list = _PRATHAMA_MAP.get(adesha)
    if expected_list is None:
        return False
    for exp in expected_list:
        if _find_tin_residue(state, tuple(exp)) is not None:
            return True
    return False


def act(state: State) -> State:
    adesha = (state.meta.get("2_4_85_adesha_slp1") or "qA").strip()
    expected_list = _PRATHAMA_MAP.get(adesha)
    if not expected_list:
        return state
    j = None
    for exp in expected_list:
        j = _find_tin_residue(state, tuple(exp))
        if j is not None:
            break
    if j is None:
        return state
    t = state.terms[j]
    t.varnas = list(parse_slp1_upadesha_sequence(adesha))
    t.meta["upadesha_slp1"] = adesha
    t.tags.add("tin_adesha_2_4_85")
    state.meta["2_4_85_lut_prathama_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.85",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "luTaH prathamasya dArAurasaH",
    text_dev       = "लुटः प्रथमस्य डारौरसः",
    padaccheda_dev = "लुटः प्रथमस्य डा-रौ-रसः",
    why_dev        = "लुट्-लकारे प्रथम-पुरुष-परस्मैपदानां डा-रौ-रस्-आदेशः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
