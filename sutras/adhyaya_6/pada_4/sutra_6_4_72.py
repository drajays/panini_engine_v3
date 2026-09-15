"""
6.4.72  आडजादीनाम्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=60472
- Kāśikā: आड् आदेशः अच्-आदि-धातुषु लृङि
- Cross-validation: tests/unit/test_tinanta_ad_lrg_kartari.py (आत्स्यत् …)

Prepends *āṭ* (tape **A**) to *ad* in *lṛṅ* when ``state.meta['lRG_ad_spine']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _dhatu_term(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def _site(state: State) -> bool:
    if not state.meta.get("lRG_ad_spine"):
        return False
    if (state.meta.get("lakara") or "").strip() != "lRG":
        return False
    dh = _dhatu_term(state)
    if dh is None:
        return False
    if dh.meta.get("Aq_agama_6_4_72_done"):
        return False
    flat = "".join(v.slp1 for v in dh.varnas)
    if flat == "ad":
        return True
    up = (dh.meta.get("upadesha_slp1") or "").strip().replace("~", "")
    return up in {"ada", "ad", "ada~", "ad~"}


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    dh = _dhatu_term(state)
    if dh is None or not _site(state):
        return state
    dh.varnas.insert(0, mk("A"))
    dh.tags.add("aTa_agama")
    dh.meta["Aq_agama_6_4_72_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.72",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="AqajAdInAm",
    text_dev="आडजादीनाम्",
    padaccheda_dev="आट् / अच्-आदीनाम्",
    why_dev="लृङि अद्-धातौ आट्-आगमः — आत्स्यत्।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
