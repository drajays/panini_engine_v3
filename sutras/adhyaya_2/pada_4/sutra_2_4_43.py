"""
2.4.43  हन् लुङि च  —  VIDHI (narrow demo)

*Han* is replaced by *vadh* in *luṅ* (glass-box **avaDIt** spine).

Pipelines must arm ``state.meta['2_4_43_han_vadh_luG_arm']`` and keep
``state.meta['lakara'] == 'luG'``.  The primary *dhātu* ``Term`` must carry
``upadesha_slp1 == 'han'`` (per input recipe, not inferred from surface).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("2_4_43_han_vadh_luG_arm"):
        return False
    if (state.meta.get("lakara") or "").strip() != "luG":
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "han":
        return False
    if dh.meta.get("2_4_43_han_vadh_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh = state.terms[0]
    dh.varnas = list(parse_slp1_upadesha_sequence("vadh"))
    dh.meta["upadesha_slp1"] = "vadh"
    dh.meta["2_4_43_han_vadh_done"] = True
    state.meta["2_4_43_han_vadh_luG_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.43",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="han luGi ca",
    text_dev="हन् लुङि च",
    padaccheda_dev="हन् / लुङि / च",
    why_dev="लुङ्-लकारे हन्-धातोः स्थाने वध्-आदेशः (अवधीत्-प्रक्रिया)।",
    anuvritti_from=("2.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
