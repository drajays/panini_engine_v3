"""
7.2.1  सिचि वृद्धिः परस्मैपदेषु  —  VIDHI (narrow: i → ai before sic in luṅ)

Engine scope: for glass-box aorist (luṅ) derivations, when a dhātu with an
*ik* vowel is followed by a sic-pratyaya and a parasmaipada tiṅ, apply vṛddhi
to that dhātu vowel. This supports चि → चै in अचैषीत्.
"""
from __future__ import annotations

from typing import Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _vrddhi_vowel(ch: str, state: State) -> Optional[str]:
    st = state.paribhasha_gates.get("sthanantara_vrddhi") or {}
    if ch in st:
        return st[ch]
    if ch == "a":
        return "A"
    if ch in ("i", "I"):
        return "E"
    if ch in ("u", "U"):
        return "O"
    return None


def _find(state: State):
    if len(state.terms) < 3:
        return None
    dh = state.terms[0]
    sic = state.terms[1]
    tin = state.terms[-1]
    if "dhatu" not in dh.tags:
        return None
    if sic.kind != "pratyaya" or tin.kind != "pratyaya":
        return None
    if not state.meta.get("lakara") == "luG":
        return None
    if dh.meta.get("7_2_1_sici_vrddhi_done"):
        return None
    if (sic.meta.get("upadesha_slp1") or "").strip() != "sic":
        return None
    # Parasmaipada signal: either recipe meta or pratyaya tag by 1.4.99.
    if not (state.meta.get("pada") == "parasmaipada" or "parasmaipada_1_4_99" in tin.tags):
        return None
    # Find target vowel in dhātu. If aṭ-āgama was inserted (6.4.71),
    # skip that leading 'a' and target the dhātu's own vowel (ci → cE).
    start = 0
    if dh.meta.get("aT_agama_6_4_71_done") and dh.varnas and dh.varnas[0].slp1 == "a":
        start = 1
    for j in range(start, len(dh.varnas)):
        v = dh.varnas[j]
        ch = v.slp1
        if is_hrasva(ch) or is_dirgha(ch) or ch in ("e", "E", "o", "O"):
            rep = _vrddhi_vowel(ch, state)
            # Special: vocalic ṛ/ḷ use uRaN-rapara machinery (1.1.51) after substitution.
            if rep is None and ch in ("f", "F", "x", "X"):
                rep = "A"  # vṛddhi component; 1.1.51 will append r/l.
                pending = "r" if ch in ("f", "F") else "l"
                return (0, j, rep, pending)
            if rep is None:
                return None
            return (0, j, rep, None)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j, rep, pending = hit
    state.terms[ti].varnas[j] = mk(rep)
    if pending:
        state.terms[ti].meta["urN_rapara_pending"] = pending
    state.terms[ti].meta["7_2_1_sici_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.1",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sici vRddhiH parasmaipadezu",
    text_dev       = "सिचि वृद्धिः परस्मैपदेषु",
    padaccheda_dev = "सिचि / वृद्धिः / परस्मैपदेषु",
    why_dev        = "लुङ्-सिच्-परस्मैपदे धातोः स्वरस्य वृद्धिः (चि→चै) ।",
    anuvritti_from = ("1.1.1", "1.1.3", "1.1.50"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

