"""
7.2.66  इडत्त्यर्तिव्ययतीनाम्  —  VIDHI

Padaccheda: इट् अत्ति-अर्ति-व्ययतीनाम्

इडत्त्यर्तिव्ययतीनाम् (7.2.66)
Pāṭha: ashtadhyayi.com data.txt row i=72066 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_BLOCKS = ("7.2.61", "7.2.62", "7.2.63")      # the iṭ-less readings of thal, which these three roots do not allow
_ROOTS  = ("ada", "f", "vyaya")               # atti, arti, vyayati (upadeśa, without the anubandha ~)


def _site(state: State):
    """ad, ṛ (arti) and vyay before thal in liṭ: the iṭ stays (āditha, āriṭha, vivyayitha; Kāśikā 7.2.66)."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "Tal" for t in state.terms) \
            or not any((t.meta.get("source_lakara_upadesha") or "").strip() == "liT" for t in state.terms):
        return None
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dh is not None and (dh.meta.get("upadesha_slp1") or "").replace("~", "").strip() in _ROOTS:
        return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iqattyartivyayatInAm",
    text_dev              = "इडत्त्यर्तिव्ययतीनाम्",
    samagra_slp1          = "aNgasya iw attyartivyayatInAm valAdeH ArDaDAtukasya Tali aniwaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य इट् अत्त्यर्तिव्ययतीनाम् वलादेः आर्धधातुकस्य थलि अनिटः",
    padaccheda_dev        = "इट् अत्ति-अर्ति-व्ययतीनाम्",
    why_dev               = "(सूत्रम् 7.2.66) इडत्त्यर्तिव्ययतीनाम्।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
