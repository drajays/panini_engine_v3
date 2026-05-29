"""
7.1.92  सख्युरसम्बुद्धौ  —  VIDHI

Padaccheda: सख्युः अ-सम्बुद्धौ

In sarvananāmasthāna contexts OTHER than sambodhana, the pratyaya after
sakhi is treated as ṇit (ṇidvat). This causes vṛddhi on the final 'i' of
sakhi (via 7.2.115 acoñṇiti): i → ai (vṛddhi). Then 6.1.78 eco'yavāyāvaḥ:
ai → āy. Result: sakhi → sakhāy + pratyaya.

Engine: arm ``sakhyu_recipe`` + finds the pratyaya term tagged "sarvanamasthana"
(and not sambodhana/sambuddhi). Applies vṛddhi to the stem's final 'i'.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology     import mk

_GATE_KEY: str = "7_1_92_saKyurasam_92"


def _find_sakhi_pratyaya_boundary(state: State) -> int | None:
    """Return index of sakhi-type stem to apply vṛddhi, or None."""
    for i, t in enumerate(state.terms):
        if "sakhi_ikarant" not in t.tags:
            continue
        if t.meta.get("7_1_92_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 not in {"i", "I"}:
            continue
        # Check that the next term is sarvananāmasthāna and not sambodhana
        if i + 1 >= len(state.terms):
            continue
        pr = state.terms[i + 1]
        if "samboddhi" in pr.tags or "sambuddhi" in pr.tags:
            continue
        if "sarvanamasthana" not in pr.tags and "sup_sarvanamasthana_eligible" not in pr.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not state.meta.get("sakhyu_recipe"):
        return False
    return _find_sakhi_pratyaya_boundary(state) is not None


def act(state: State) -> State:
    idx = _find_sakhi_pratyaya_boundary(state)
    if idx is None:
        return state
    t = state.terms[idx]
    # vṛddhi of final 'i'/'I' → 'ai' (E in SLP1)
    t.varnas[-1] = mk("E")
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["7_1_92_done"] = True
    # vṛddhi changes the stem — no longer pragṛhya (6.1.78 must fire on E)
    t.tags.discard("pragrahya")
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta.pop("sakhyu_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saKyurasambudDO",
    text_dev              = "सख्युरसम्बुद्धौ",
    padaccheda_dev        = "सख्युः अ-सम्बुद्धौ",
    why_dev               = (
        "सखि-शब्दात् सर्वनामस्थान-प्रत्यये (सम्बोधनेतर) ṇिद्वद्भावः → "
        "अचो ञ्णिति (७.२.११५) वृद्धिः: अन्त्य-इकारस्य ऐकारः → "
        "एचोऽयवायावः (६.१.७८): ऐ → आय् → सखाय् + प्रत्ययः।"
    ),
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
