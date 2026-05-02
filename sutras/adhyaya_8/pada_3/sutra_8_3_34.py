"""
8.3.34  विसर्जनीयस्य सः  —  VIDHI (narrow for P021)

Classical rule (broad): visarga (ḥ) can be replaced by dental 's' in certain
following contexts.

v3 narrow slice (vakya illustration P021):
  When a visarga ``H`` is immediately followed by dental ``t`` *across a word
  boundary* (i.e. end of one Term and start of the next), replace that ``H``
  with ``s``:

    grAmaH + tava  →  grAmas + tava

Tripāḍī: requires ``state.tripadi_zone`` (8.2.1).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find_visarga_t_boundary(state: State):
    if not state.tripadi_zone:
        return None
    if len(state.terms) < 2:
        return None
    if state.meta.get("8_3_34_visarjanIyasya_saH_done"):
        return None
    for i in range(len(state.terms) - 1):
        left = state.terms[i]
        right = state.terms[i + 1]
        if not left.varnas or not right.varnas:
            continue
        if left.varnas[-1].slp1 != "H":
            continue
        if right.varnas[0].slp1 != "t":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_visarga_t_boundary(state) is not None


def act(state: State) -> State:
    i = _find_visarga_t_boundary(state)
    if i is None:
        return state
    left = state.terms[i]
    left.varnas[-1] = mk("s")
    state.meta["8_3_34_visarjanIyasya_saH_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.34",
    sutra_type=SutraType.VIDHI,
    text_slp1="visarjanIyasya saH",
    text_dev="विसर्जनीयस्य सः",
    padaccheda_dev="विसर्जनीयस्य / सः",
    why_dev="पदान्त-विसर्गः परे 'त्' (त-वर्गारम्भे) सकार-आदेशः (P021 वाक्य-डेमो)।",
    anuvritti_from=("8.2.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

