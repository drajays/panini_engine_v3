"""
6.4.98  गमहनजनखनघसां लोपः क्ङित्यनङि  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=60498
- Kāśikā: «गमहनजनखनघसां लोपः क्ङित्यनङि» (घस् → घ्स् in *liṭ* reduplication)
- Cross-validation: tests/unit/test_tinanta_ad_lit_kartari.py (जक्षतुः …)

*Liṭ* + *kṅit* (1.2.5 *kit* on the tiṅ ādeśa): non-*abhyāsa* *ghas* (**G-a-s**) loses
penultimate *a* → **G-s** (घ्स्).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_98_gamahanaja_98"


def _has_kngiti_pratyaya(state: State) -> bool:
    return any("kngiti" in t.tags for t in state.terms)


def _find_gas_upadha_lopa(state: State) -> int | None:
    if not state.meta.get("lakara_liT"):
        return None
    if not _has_kngiti_pratyaya(state):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if t.meta.get("6_4_98_gas_upadha_done"):
            continue
        vs = t.varnas
        if len(vs) == 3 and vs[0].slp1 == "G" and vs[1].slp1 == "a" and vs[2].slp1 == "s":
            return i
    return None


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.98", gate_key=_GATE_KEY)


def act(state: State) -> State:
    i = _find_gas_upadha_lopa(state)
    if i is not None:
        t = state.terms[i]
        del t.varnas[1]
        t.meta["6_4_98_gas_upadha_done"] = True
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["anga_kind"] = "6.4.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gamahanajanaKanaGasAM lopaH kNityanaNi",
    text_dev              = "गमहनजनखनघसां लोपः क्ङित्यनङि",
    padaccheda_dev        = "गम-हन-जन-खन-घसाम् लोपः क्ङिति अन्-अङि",
    why_dev               = "(सूत्रम् 6.4.98) गमहनजनखनघसां लोपः क्ङित्यनङि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
