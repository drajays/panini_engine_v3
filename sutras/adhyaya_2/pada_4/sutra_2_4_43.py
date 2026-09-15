"""
2.4.43  हन् लुङि च  —  VIDHI (narrow)

Sources consulted:
- ashtadhyayi.com data.txt row i=204043
- Kāśikā: हन् लुङि च (वध-आदेशः)
- Cross-validation: tests/unit/test_avaDIt_luN_han.py,
  tests/unit/test_avadhIt_han_lun_ekavacana.py

*Han* is replaced by *vadh* (अकारान्त आदेश) in *luṅ*. Recipe arms
``2_4_43_han_vadh_luG_arm`` with ``lakara == luG`` and *dhātu*
``upadesha_slp1 == han``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas


def _matches(state: State) -> bool:
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
    adesha_substitute_varnas(
        dh, "vadha", state,
        sutra_id="2.4.43",
        gunadharmas=frozenset({DHATUTVA}),
    )
    dh.meta["2_4_43_han_vadh_done"] = True
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
