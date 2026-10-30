"""
6.4.52  निष्ठायां सेटि  —  VIDHI

Padaccheda: निष्ठायाम् सेटि

निष्ठायां सेटि (6.4.52)
Pāṭha: ashtadhyayi.com data.txt row i=64052 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


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
    for i, t in enumerate(state.terms[:-1]):
        if t.kind != "pratyaya" or not ({"nic"} & t.tags) or t.meta.get("6_4_52_nilopa_done"):
            continue
        h = next((u for u in state.terms[i + 1:] if u.varnas and "agama" not in u.tags), None)
        if h is None or "nistha" not in h.tags:
            continue
        if any("it_agama" in v.tags for u in state.terms[i + 1:] for v in u.varnas[:1]):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    t.varnas[:] = []        # णिच् + इट् + क्त: कारितम् (the ṇi goes before a seṭ niṣṭhā)
    t.meta["6_4_52_nilopa_done"] = True
    t.meta["lopa_6_4_52"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWAyAM sewi",
    text_dev              = "निष्ठायां सेटि",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke nizWAyAm sewi nalopaH lopaH ReH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके निष्ठायाम् सेटि नलोपः लोपः णेः",
    padaccheda_dev        = "निष्ठायाम् सेटि",
    why_dev               = "(सूत्रम् 6.4.52) निष्ठायां सेटि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
