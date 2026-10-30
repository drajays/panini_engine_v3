"""
6.4.27  घञि च भावकरणयोः  —  VIDHI

Padaccheda: घञि च भाव-करणयोः

घञि च भावकरणयोः (6.4.27)
Pāṭha: ashtadhyayi.com data.txt row i=64027 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from engine.vivaksha import vivaksita

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
        if "dhatu" not in t.tags or t.meta.get("6_4_27_nalopa_done") or _flat(t) != "raYj":
            continue
        h = _head(state, i)
        if h is not None and _name(h) == "GaY":
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None and (vivaksita(state, "artha", "BAva") or vivaksita(state, "artha", "karaRa"))      # भावकरणयोः


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    del t.varnas[-2]        # रञ्ज् + घञ् (भावे, करणे): रागः; in the adhikaraṇa sense रङ्गः keeps the nasal
    t.meta["6_4_27_nalopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GaYi ca BAvakaraRayoH",
    text_dev              = "घञि च भावकरणयोः",
    samagra_slp1          = "raYjeH aNgasya BAvakaraRayoH GaYi nalopaH",
    samagra_dev           = "रञ्जेः अङ्गस्य भावकरणयोः घञि नलोपः",
    padaccheda_dev        = "घञि च भाव-करणयोः",
    why_dev               = "(सूत्रम् 6.4.27) घञि च भावकरणयोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
