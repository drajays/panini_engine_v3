"""
6.4.74  न माङ्योगे  —  VIDHI

Padaccheda: न माङ्-योगे

न माङ्योगे (6.4.74)
Pāṭha: ashtadhyayi.com data.txt row i=64074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_AT_CONTEXT = "aT_agama_context"       # sutras/.../6.4.71: the luṅ / laṅ / lṛṅ aṅga that waits for aṭ / āṭ
_MANG = "mAN_yoga"                     # the upapada mā(ṅ) stands with the verb: a sentence-level fact the caller gives, as 'ashis' is (S28 style)


def _site(state: State):
    """न माङ्योगे — with माङ् (mā bhavān bhūt, mā sma bhavat), the aṭ / āṭ (6.4.71 / 6.4.72) of luṅ / laṅ / lṛṅ is not made."""
    if "6.4.71" in state.blocked_sutras and "6.4.72" in state.blocked_sutras:
        return None
    return next((t for t in state.terms if "dhatu" in t.tags and _AT_CONTEXT in t.tags and _MANG in t.tags), None)


# SHORTCUT S129: see docs/SHORTCUT_LEDGER.md
def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.update({"6.4.71", "6.4.72"})
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.74",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na mANyoge",
    text_dev              = "न माङ्योगे",
    samagra_slp1          = "luN-laN-lfNkzu mAN yoge aNgasya aw Aw na",
    samagra_dev           = "लुङ्-लङ्-लृङ्क्षु माङ् योगे अङ्गस्य अट् आट्  न",
    padaccheda_dev        = "न माङ्-योगे",
    why_dev               = "न माङ्योगे — माङ्योगे लुङ्-लङ्-लृङ्क्षु अङ्गस्य अट्-आडागमौ (६.४.७१, ६.४.७२) न (मा भवान् भूत्)।",
    anuvritti_from        = ('6.1.1',),
    blocks_sutra_ids      = ('6.4.71', '6.4.72'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
