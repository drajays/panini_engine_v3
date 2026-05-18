"""
3.4.101  तस्थस्थमिपां तांतंतामः  —  VIDHI (laṅ: four tiṅ substitutions)

**Padaccheda:** tas/thas/tha/mip → tām/tam/ta/am in laṅ.

Engine: after **3.4.78** replaces the lac placeholder and the recipe sets
``state.meta['lakara'] == 'laG'``, apply the appropriate substitution:
  tas  (3du)  → tAm  (ताम्)
  Tas  (2du)  → tam  (तम्)
  Ta   (2pl)  → ta   (त)
  mi   (1sg, from mip after p-lopa)  → am  (अम्)

The last case (mi→am) is apavāda to 3.4.100 (which would drop 'i').
Call 3.4.101 BEFORE 3.4.100 in the pipeline to respect this priority.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

# (upadesha_slp1 of tiṅ ādeśa, current varnas as string) → new SLP1 form
_TASTHA_MAP: dict[tuple[str, str], str] = {
    ("tas", "tas"): "tAm",  # 3du: tas → tām
    ("Tas", "Tas"): "tam",  # 2du: Tas → tam
    ("Ta",  "Ta" ): "ta",   # 2pl: Ta  → ta
    ("mip", "mi" ): "am",   # 1sg: mi (from mip after p-lopa) → am
}


def _find_target(state: State) -> tuple[int, str] | None:
    """Return (index, new_slp1) for the first matching tiṅ ādeśa in laṅ."""
    if (state.meta.get("lakara") or "").strip() not in {"laG", "liG", "AsIrliG", "luG", "lRG"}:
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_101_tastha_done"):
            continue
        up  = (t.meta.get("upadesha_slp1") or "").strip()
        cur = "".join(v.slp1 for v in t.varnas)
        key = (up, cur)
        if key in _TASTHA_MAP:
            return i, _TASTHA_MAP[key]
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    result = _find_target(state)
    if result is None:
        return state
    idx, new_slp1 = result
    t = state.terms[idx]
    t.varnas = list(parse_slp1_upadesha_sequence(new_slp1))
    t.meta["upadesha_slp1"] = new_slp1
    t.meta["3_4_101_tastha_done"] = True
    # Discard upadesha tag so 1.3.3 does not misidentify the new final consonant
    # (e.g. 'm' of 'am'/'tam') as halantyam-it in subsequent pipeline calls.
    t.tags.discard("upadesha")
    state.samjna_registry[f"3.4.101_{new_slp1}"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.101",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tasthasthamipAM tAMtaMtAmaH",
    text_dev       = "तस्थस्थमिपां तांतंतामः",
    padaccheda_dev = "तस्थस्थमिपाम् / तांतंतामः",
    why_dev        = (
        "लङि: तस्→ताम् (प्रथम-द्विवचन), थस्→तम् (मध्यम-द्वि), "
        "थ→त (मध्यम-बहु), मि→अम् (उत्तम-एक)।"
    ),
    anuvritti_from = ("3.4.78",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
