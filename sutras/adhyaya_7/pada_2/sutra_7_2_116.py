"""
7.2.116  अतो उपधायाः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=702116
- Kāśikā: अत उपधायाः (णिति-परे)
- Cross-validation: tests/unit/test_kathi_kath_nic.py, test_paTayati_paTu_Nic.py

Operational role (v3.8, kṛt Nvul agent nouns like पाचक):
  When a dhātu has upadhā 'a' and the following pratyaya is **ṇit**,
  apply vṛddhi to that upadhā:

  pac + (ṇit-pratyaya) → pAc ...

We implement narrowly:
  - first term is dhātu
  - last term is kṛt pratyaya whose recorded it-markers contain 'N'
  - dhātu ends with a consonant, and the vowel immediately before that
    consonant is 'a' → replace it with 'A'
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk, HAL

_GATE_1_1_57 = "1.1.57_aca_parasmin_purvavidhau"


def _upadha_vrddhi_blocked(state: State, dhatu) -> bool:
    """**6.4.48** *a*-lopa (para-nimitta) destroys upadhā — no **7.2.116**."""
    if state.paribhasha_gates.get(_GATE_1_1_57) is True:
        return True
    if dhatu.meta.get("6_4_48_a_lopa_done"):
        return True
    if dhatu.meta.get("upadha_blocked_para_nimitta"):
        return True
    return False


def _find_upadha_a_nic_p037(state: State):
    """Narrow **P037**: *aṭ* + *ṇic* residue ``i`` (``Ric`` ``Term`` still *para*)."""
    if len(state.terms) < 2:
        return None
    dhatu = next((t for t in state.terms if "dhatu" in t.tags), None)
    if dhatu is None:
        return None
    if _upadha_vrddhi_blocked(state, dhatu):
        return None
    di = state.terms.index(dhatu)
    if di + 1 >= len(state.terms):
        return None
    pr = state.terms[di + 1]
    if "nic" not in pr.tags:
        return None
    if dhatu.meta.get("upadha_vrddhi_done"):
        return None
    if len(dhatu.varnas) < 2:
        return None
    if dhatu.varnas[-1].slp1 not in HAL:
        return None
    if dhatu.varnas[-2].slp1 != "a":
        return None
    return (di, len(dhatu.varnas) - 2)


def _find_upadha_a_liT_strong(state: State):
    """liṭ strong form (3sg/1sg Ral): vṛddhi of root upadhā 'a' → 'ā'.
    Structural: fires when meta["lakara"] == "liT" and abhyāsa is on tape."""
    if (state.meta.get("lakara") or "").strip() != "liT":
        return None
    # Find the NON-abhyāsa dhātu term (root = second copy after dvitva).
    dhatu = None
    for t in state.terms:
        if "dhatu" in t.tags and "abhyasa" not in t.tags:
            dhatu = t
            break
    if dhatu is None:
        return None
    if dhatu.meta.get("upadha_vrddhi_done"):
        return None
    if len(dhatu.varnas) < 2:
        return None
    if dhatu.varnas[-1].slp1 not in HAL:
        return None
    if dhatu.varnas[-2].slp1 != "a":
        return None
    di = state.terms.index(dhatu)
    return (di, len(dhatu.varnas) - 2)


def _find_upadha_a(state: State):
    hit = _find_upadha_a_nic_p037(state)
    if hit is not None:
        return hit
    hit = _find_upadha_a_liT_strong(state)
    if hit is not None:
        return hit
    if len(state.terms) < 2:
        return None
    dhatu = next((t for t in state.terms if "dhatu" in t.tags), None)
    if dhatu is None:
        return None
    if _upadha_vrddhi_blocked(state, dhatu):
        return None
    pr    = state.terms[-1]
    if "krt" not in pr.tags:
        return None
    itm = pr.meta.get("it_markers", set())
    if not isinstance(itm, set) or not ("N" in itm or "R" in itm):
        return None
    if dhatu.meta.get("upadha_vrddhi_done"):
        return None
    if len(dhatu.varnas) < 2:
        return None
    if dhatu.varnas[-1].slp1 not in HAL:
        return None
    # Upadhā = vowel before final consonant in this minimal model.
    if dhatu.varnas[-2].slp1 != "a":
        return None
    di = state.terms.index(dhatu)
    return (di, len(dhatu.varnas) - 2)


def cond(state: State) -> bool:
    return _find_upadha_a(state) is not None


def act(state: State) -> State:
    hit = _find_upadha_a(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("A")
    state.terms[ti].meta["upadha_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.116",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ata upadhAyAH (Nit pare)",
    text_dev       = "अतो उपधायाः",
    padaccheda_dev = "अतः उपधायाः",
    why_dev        = "णित्-प्रत्यये परे धातोः उपधास्थ-अकारस्य वृद्धि (पच् → पाच्)।",
    apavada_of     = ("7.2.115",),   # अपवाद of 7.2.115 — sutra_ref_out resolver.apavada_of
    anuvritti_from = ("1.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

