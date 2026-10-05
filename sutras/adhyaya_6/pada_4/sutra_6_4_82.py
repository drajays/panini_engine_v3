"""
6.4.82  एरनेकाचोऽसंयोगपूर्वस्य  —  VIDHI

Padaccheda: एः अन्-एक-अचः अ-संयोग-पूर्वस्य

एरनेकाचोऽसंयोगपूर्वस्य (6.4.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_82_eranekAco_82"
_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """एरनेकाचोऽसंयोगपूर्वस्य: an abhyasta (anekāc) aṅga ending in i/ī, not after a conjunct, takes yaṇ before a vowel-initial
    affix — jiGyiva, biByiva, ninyuH (not the savarṇa-dīrgha *jiGIva, nor iyaṅ)."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags or dh.meta.get("6_4_82_yaN_done") or i == 0:
            continue
        if "abhyasa" not in state.terms[i - 1].tags or not dh.varnas or dh.varnas[-1].slp1 not in "iI":
            continue
        if len(dh.varnas) >= 3 and dh.varnas[-2].slp1 not in _AC and dh.varnas[-3].slp1 not in _AC:
            continue                                   # saṃyogapūrva: iyaṅ (6.4.77), not yaṇ
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and nxt.varnas[0].slp1 in _AC:
            return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    from phonology import mk
    dh = state.terms[i]
    dh.varnas[-1] = mk("y")
    dh.meta["6_4_82_yaN_done"] = True
    dh.tags.discard("upadesha")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.82",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'eranekAcosaMyogapUrvasya',
    text_dev              = 'एरनेकाचोऽसंयोगपूर्वस्य',
    padaccheda_dev        = "एः अन्-एक-अचः अ-संयोग-पूर्वस्य",
    why_dev               = "(सूत्रम् 6.4.82) एरनेकाचोऽसंयोगपूर्वस्य।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.1.101", "6.1.77"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
