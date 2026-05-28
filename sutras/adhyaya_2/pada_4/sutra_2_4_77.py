"""
2.4.77  गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु  —  VIDHI

Two operational paths:
  1. Arm ``2_4_77_arm``: legacy gate-setter.
  2. Arm ``2_4_77_luG_sic_lopa_arm``: luṅ — luk (total deletion) of the siC
     pratyaya term for bhū in parasmaipada.  After 3.1.44 cli→sic, this arm
     removes the sic term entirely so only dhātu + tiṅ remain.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_77_gati_stha_sica"


def _find_sic_index(state: State) -> int | None:
    if not state.meta.get("2_4_77_luG_sic_lopa_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sic":
            continue
        return i
    return None


def cond(state: State) -> bool:
    # Structural path: luṅ siC-luk for the matched siC pratyaya term.
    # (The legacy gate-setter arm path is dead — no caller sets ``2_4_77_arm``
    # and the gate it produced is read by no other sūtra.  Art.7: no arm read.)
    return _find_sic_index(state) is not None


def act(state: State) -> State:
    j = _find_sic_index(state)
    if j is not None:
        state.terms.pop(j)
        state.meta.pop("2_4_77_luG_sic_lopa_arm", None)
        state.samjna_registry["2.4.77_sic_luk"] = True
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"] = "2.4.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gAtisTAGupABUByaH sicaH parasmEpadezu",
    text_dev              = "गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु",
    padaccheda_dev        = "गाति-स्था-घु-पा-भूभ्यः सिचः परस्मैपदेषु",
    why_dev               = (
        "लुङि भू-आदिभ्यः परस्मैपदे सिच्-विकरणस्य लुक् — "
        "सिच् सम्पूर्णतः लुप्यते; पश्चात् ६.४.८८ वुक्-आगमः।"
    ),
    anuvritti_from        = ('2.4.72',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
