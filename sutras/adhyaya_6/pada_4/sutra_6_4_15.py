"""
6.4.15  अनुनासिकस्य क्विझलोः क्ङिति  —  VIDHI

Padaccheda: अनुनासिकस्य क्वि-झलोः क्ङिति

अनुनासिकस्य क्विझलोः क्ङिति (6.4.15)
Pāṭha: ashtadhyayi.com data.txt row i=64015 (Art. 14).
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
        if "dhatu" not in t.tags or "anga" not in t.tags or t.meta.get("6_4_15_dirgha_done") or len(t.varnas) < 3:
            continue
        if t.varnas[-1].slp1 not in _NASAL or t.varnas[-2].slp1 not in "aiuf" or t.varnas[-3].slp1 in "aAiIuUfFxXeEoO":
            continue
        if _flat(t) == "han":      # SHORTCUT S143: the stems vṛtrahan, śatruhan keep a short a; the reason (han's own n) is not written
            continue
        h = _head(state, i)
        if not _kvi_or_jhal_kngit(h):
            continue
        if _name(h) != "kvip" and not t.meta.get("udatta_dhatu", True):
            continue        # 6.4.37 (para) drops the nasal of an anudāttopadeśa root before a jhalādi kṅit
        return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    t.varnas[-2] = mk({"a": "A", "i": "I", "u": "U", "f": "F"}[t.varnas[-2].slp1])      # शम् + क्त: शान्त; प्र-शम् + क्विप्: प्रशान्
    t.meta["6_4_15_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anunAsikasya kviJaloH kNiti",
    text_dev              = "अनुनासिकस्य क्विझलोः क्ङिति",
    samagra_slp1          = "anunAsikasya aNgasya upaDAyAH kvi-JaloH kNiti dIrGaH",
    samagra_dev           = "अनुनासिकस्य अङ्गस्य उपधायाः क्वि-झलोः क्ङिति दीर्घः",
    padaccheda_dev        = "अनुनासिकस्य क्वि-झलोः क्ङिति",
    why_dev               = "(सूत्रम् 6.4.15) अनुनासिकस्य क्विझलोः क्ङिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
