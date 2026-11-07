"""
7.2.39  न लिङि  —  VIDHI

Padaccheda: न लिङि

न लिङि (7.2.39)
Pāṭha: ashtadhyayi.com data.txt row i=72039 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import HAL

_VAL = HAL - {"y", "h"}      # val: every consonant after ha, ya
_BLOCKS = ("7.2.38",)                  # vṛto vā (the iṭ and its dīrgha)


def _site(state: State):
    """A ṛ-final dhātu followed by a val-initial ārdhadhātuka tiṅ of liṅ (the sīyuṭ of āśīrliṅ is part of it, 1.1.46)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        if t.varnas[-1].slp1 != "F" and (t.meta.get("upadesha_slp1") or "").strip() not in ("vfY", "vfN"):      # the dhātus 7.2.38 names: vṛ, ṝ-final
            continue
        rest = state.terms[i + 1:]
        if any((u.meta.get("source_lakara_upadesha") or "").strip() == "liG" for u in rest) \
                and rest and rest[0].varnas and (rest[0].varnas[0].slp1 in _VAL or "it_agama" in rest[0].varnas[0].tags):      # val-initial, or already carrying its iṭ (a recipe applies it after 7.2.35)
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.39",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na liNi",
    text_dev              = "न लिङि",
    samagra_slp1          = "aNgasya na liNi valAdeH iw ArDaDAtukasya dIrGaH vFtaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न लिङि वलादेः इट् आर्धधातुकस्य दीर्घः वॄतः",
    padaccheda_dev        = "न लिङि",
    why_dev               = "न लिङि — वृतः इटः लिङि दीर्घः न (स्तरिषीष्ट)।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
