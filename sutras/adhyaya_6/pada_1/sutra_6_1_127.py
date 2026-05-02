"""
6.1.127  इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च  —  VIDHI (narrow for P023)

This sūtra is cited in P023.json as a commentary-flavoured bridge from
``div`` to an intermediate ``diu`` before the next member of a compound.

v3 narrow slice (P023: दिव् + काम → दिउ + काम):
  - recipe arms: ``state.meta["P023_6_1_127_div_v_to_u_arm"] == True``
  - witness: first Term has ``meta['upadesha_slp1'] == 'div'`` (or varṇas d-i-v)
  - action:
      • rewrite that Term to ``di`` (drop the final ``v``)
      • insert a following Term with single vowel ``u`` (as a residue from the ādeśa)

This structure allows **6.1.77** (*iko yaṇ aci*) to apply across Terms when
recipe-arrested via ``6_1_77_ik_yan_aci_general_arm``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import mk


def _site(state: State):
    if not state.meta.get("P023_6_1_127_div_v_to_u_arm"):
        return None
    if len(state.terms) < 2:
        return None
    if state.meta.get("P023_6_1_127_done"):
        return None
    left = state.terms[0]
    right = state.terms[1]
    if (left.meta.get("upadesha_slp1") or "").strip() not in {"div"}:
        if [v.slp1 for v in left.varnas] != ["d", "i", "v"]:
            return None
    if not right.varnas:
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    left = state.terms[i]
    # div → di + u (residue as a separate Term)
    left.varnas = [mk("d"), mk("i")]
    left.meta["upadesha_slp1"] = "di"
    u = Term(
        kind="prakriti",
        varnas=[mk("u")],
        tags=set(),
        meta={"upadesha_slp1": "u", "P023_residue_from_div": True},
    )
    state.terms.insert(i + 1, u)
    state.meta["P023_6_1_127_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.127",
    sutra_type=SutraType.VIDHI,
    text_slp1="iko'savarRe zAkalyasya hrasvaz ca",
    text_dev="इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च",
    padaccheda_dev="इकः-असवर्णे / शाकल्यस्य / ह्रस्वः / च",
    why_dev="P023: दिव्-शब्दस्य 'v' स्थाने 'u' (दिउ) — ६.१.७७ हेतु-रचना।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

