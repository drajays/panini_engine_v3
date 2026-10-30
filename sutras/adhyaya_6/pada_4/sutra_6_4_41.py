"""
6.4.41  विड्वनोरनुनासिकस्यात्  —  VIDHI

Padaccheda: विट्-वनोः अनुनासिकस्य आत्

विड्वनोरनुनासिकस्यात् (6.4.41)
Pāṭha: ashtadhyayi.com data.txt row i=64041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk

_NASAL = frozenset("mnNRY")                      # anunāsika-final: m n ṅ ṇ ñ
_JHAL = frozenset("JBGQDjbgqdKPCWTcwtkpSzsh")


def _head(state: State, i: int):
    """The pratyaya that stands right after the aṅga at ``i`` (an āgama belongs to the affix it precedes; a lopa ghost still counts)."""
    return next((u for u in state.terms[i + 1:] if "agama" not in u.tags), None)


def _name(t) -> str:
    return (t.meta.get("upadesha_slp1") or "").strip()


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _kvi_or_jhal_kngit(h) -> bool:
    """क्विझलोः क्ङिति: a kvip, or a kṅit pratyaya that begins with a jhal."""
    return h is not None and (_name(h) == "kvip" or ("kngiti" in h.tags and bool(h.varnas) and h.varnas[0].slp1 in _JHAL))


# SHORTCUT S82: the pratyaya is read by its upadeśa name and the root by its flat spelling (no kṛt-family / root-class tag yet) — Lexicon tables (S14)
def _site(state: State):
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "anga" not in t.tags or t.meta.get("6_4_41_at_done") or not t.varnas or t.varnas[-1].slp1 not in _NASAL:
            continue
        h = _head(state, i)
        if h is not None and _name(h) in ("viw", "vanip", "vani~p"):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    t.varnas[-1] = mk("A")  # जन् + विट्: जा (गोजाः), वनिप्: विजावा — the final anunāsika is replaced by आ
    t.meta["6_4_41_at_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viqvanoranunAsikasyAt",
    text_dev              = "विड्वनोरनुनासिकस्यात्",
    samagra_slp1          = "aNgasya asidDavadatrABAt viw-vanoH anunAsikasya At nalopaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् विट्-वनोः अनुनासिकस्य आत् नलोपः",
    padaccheda_dev        = "विट्-वनोः अनुनासिकस्य आत्",
    why_dev               = "(सूत्रम् 6.4.41) विड्वनोरनुनासिकस्यात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
