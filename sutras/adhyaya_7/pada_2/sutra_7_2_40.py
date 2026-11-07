"""
7.2.40  सिचि च परस्मैपदेषु  —  VIDHI

Padaccheda: सिचि च परस्मैपदेषु

सिचि च परस्मैपदेषु (7.2.40)
Pāṭha: ashtadhyayi.com data.txt row i=72040 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_BLOCKS = ("7.2.38",)      # vṛto vā


def _site(state: State):
    """vṛ / a ṝ-final dhātu, then a sic that begins with its iṭ, then a parasmaipada tiṅ: no dīrgha (atāriṣṭām, avāriṣṭām; Kāśikā 7.2.40)."""
    if not any("parasmaipada" in t.tags for t in state.terms):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        if t.varnas[-1].slp1 != "F" and (t.meta.get("upadesha_slp1") or "").strip() not in ("vfY", "vfN"):
            continue
        nxt = state.terms[i + 1]
        if (nxt.meta.get("upadesha_slp1") or "").strip() == "sic" and nxt.varnas and "it_agama" in nxt.varnas[0].tags:
            return nxt
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sici ca parasmEpadezu",
    text_dev              = "सिचि च परस्मैपदेषु",
    samagra_slp1          = "aNgasya sici ca parasmEpadezu valAdeH iw ArDaDAtukasya dIrGaH vFtaH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य सिचि च परस्मैपदेषु वलादेः इट् आर्धधातुकस्य दीर्घः वॄतः न",
    padaccheda_dev        = "सिचि च परस्मैपदेषु",
    why_dev               = "(सूत्रम् 7.2.40) सिचि च परस्मैपदेषु।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
