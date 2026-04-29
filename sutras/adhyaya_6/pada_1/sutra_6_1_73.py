"""
6.1.73  छेः च  —  VIDHI (narrow: *tuk* before ``C`` (छकार) after terminal ``i``)

Demo for *dadhi* + *Catram* (पदादिवति ``C`` = ``छ``): insert ``t`` (*tuk*-kārya)
immediately after the terminal ``i`` when the following *pāda* begins with ``C``.

Recipe arms ``state.meta['6_1_73_che_ca_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def cond(state: State) -> bool:
    if not state.meta.get("6_1_73_che_ca_arm"):
        return False
    if len(state.terms) != 2:
        return False
    a, b = state.terms[0], state.terms[1]
    if a.meta.get("6_1_73_che_ca_done"):
        return False
    if not a.varnas or not b.varnas:
        return False
    if a.varnas[-1].slp1 != "i":
        return False
    return b.varnas[0].slp1 == "C"


def act(state: State) -> State:
    t0 = state.terms[0]
    if t0.varnas[-1].slp1 != "i":
        return state
    t0.varnas.append(mk("t"))
    t0.meta["6_1_73_che_ca_done"] = True
    state.meta["6_1_73_che_ca_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.73",
    sutra_type=SutraType.VIDHI,
    text_slp1="CeH ca",
    text_dev="छेः च",
    padaccheda_dev="छेः / च",
    why_dev="छ-कारोपस्थितौ पूर्वपदान्तात् सम्प्रगृहणम् (थुम्-आगमः, डेमो)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
