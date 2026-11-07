"""
6.4.126  न शसददवादिगुणानाम्  —  VIDHI

Padaccheda: न शस-दद-व-आदि-गुणानाम्

न शसददवादिगुणानाम् (6.4.126)
Pāṭha: ashtadhyayi.com data.txt row i=64126 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_NAMED = frozenset({"Sas", "dad"})     # शस्, दद् — the dhātus the sūtra names (the vakārādi dhātus with a guṇa-a are S130)


def _lit(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == "liT" or (t.meta.get("source_lakara_upadesha") or "").strip() == "liT"
               for t in state.terms)


def _site(state: State):
    """न शसददवादिगुणानाम् — in liṭ, the a of शस् / दद् (ददे, ददाते, ददिरे) takes neither the e (etva, 6.4.120) nor the loss of the abhyāsa (abhyāsalopa)
    nor the thal-iṭ form of 6.4.121."""
    if {"6.4.120", "6.4.121"} <= state.blocked_sutras or not _lit(state):
        return None
    return next((t for t in state.terms if "dhatu" in t.tags and "".join(v.slp1 for v in t.varnas) in _NAMED), None)


# SHORTCUT S130: see docs/SHORTCUT_LEDGER.md
def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.update({"6.4.120", "6.4.121"})
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.126",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na SasadadavAdiguRAnAm",
    text_dev              = "न शसददवादिगुणानाम्",
    samagra_slp1          = "aNgasya asidDavadatrABAt na Sa-sadada-vAdi-guRAnAm kNiti aByAsalopaH ataH Tali sewi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् न श-सदद-वादि-गुणानाम् क्ङिति अभ्यासलोपः अतः थलि सेटि",
    padaccheda_dev        = "न शस-दद-व-आदि-गुणानाम्",
    why_dev               = "न शसददवादिगुणानाम् — शस्-दद्-वकारादीनां गुणशब्देन विहितस्य अकारस्य एत्त्वाभ्यासलोपौ (६.४.१२०, ६.४.१२१) न (ददे)।",
    anuvritti_from        = ('6.1.1',),
    blocks_sutra_ids      = ('6.4.120', '6.4.121'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
