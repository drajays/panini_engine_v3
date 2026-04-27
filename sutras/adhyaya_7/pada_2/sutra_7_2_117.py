"""
7.2.117  तद्धितेषु अचामादेः  —  VIDHI

**Padaccheda:** तद्धितेषु / अचाम् / आदेः

**Anuvṛtti (baked into text fields; CONSTITUTION Art. 4):**
6.4.1 *aṅgasya* (adhikāra), 7.2.114 *vṛddhiḥ*, 7.2.115 *acaḥ ñṇiti*.

**Full teaching form:** *aṅgasya acām ādeḥ acaḥ ṇiti ñiti taddhiteṣu vṛddhiḥ*.

**Meaning (operational):**
When a following **taddhita** pratyaya is **ṇit** or **ñit**, the **first vowel**
(*ādi-ac*) of the aṅga undergoes **vṛddhi**.

**Engine scope:**
- Requires **6.4.1** *aṅgasya* adhikāra to be in effect (via `adhikara_in_effect`).
- Detects **ñit/ṇit** via `pratyaya.meta['it_markers']` containing one of:
  `'Y'` (ñ), `'N'` or `'R'` (ṇ/ṇi-like markers as carried by it-lopa 1.3.9).
- Applies to an `anga` term followed by a `taddhita` pratyaya term.
"""
from __future__ import annotations

from typing import Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _vrddhi_vowel(ch: str, state: State) -> Optional[str]:
    """
    Map a vowel (SLP1) to its vṛddhi substitute.
    Consults `sthanantara_vrddhi` gate (1.1.50) when present, then falls back.
    """
    st = state.paribhasha_gates.get("sthanantara_vrddhi") or {}
    if ch in st:
        return st[ch]
    if ch == "a":
        return "A"
    if ch in ("i", "I"):
        return "E"  # ai
    if ch in ("u", "U"):
        return "O"  # au
    if ch in ("e", "E"):
        return "E"
    if ch in ("o", "O"):
        return "O"
    # Vocalic r/l are intentionally not handled in this v3 slice.
    return None


def _is_ac(v_slp1: str) -> bool:
    return bool(is_hrasva(v_slp1) or is_dirgha(v_slp1) or v_slp1 in ("e", "E", "o", "O"))


def _find(state: State):
    if not adhikara_in_effect("7.2.117", state, "6.4.1"):
        return None
    if len(state.terms) < 2:
        return None
    anga = state.terms[0]
    pr   = state.terms[1]
    if "anga" not in anga.tags:
        return None
    if "taddhita" not in pr.tags:
        return None
    itm = pr.meta.get("it_markers", set())
    if not isinstance(itm, set):
        return None
    if not (("Y" in itm) or ("N" in itm) or ("R" in itm)):
        return None
    if anga.meta.get("7_2_117_adi_vrddhi_done"):
        return None
    for j, v in enumerate(anga.varnas):
        if _is_ac(v.slp1):
            rep = _vrddhi_vowel(v.slp1, state)
            if rep is None or rep == v.slp1:
                return None
            return (0, j, rep)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, j, rep = hit
    state.terms[ti].varnas[j] = mk(rep)
    state.terms[ti].meta["7_2_117_adi_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.117",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "aNgasya acAm AdeH acaH Riti Yiti taddhitezu vRddhiH",
    text_dev       = "अङ्गस्य अचामादेः अचः णिति ञिति तद्धितेषु वृद्धिः",
    padaccheda_dev = "तद्धितेषु / अचाम् / आदेः",
    why_dev        = (
        "णित्/ञित्-तद्धित-प्रत्यये परे अङ्गस्य आद्य-अचः वृद्धिः "
        "(दक्ष+इञ्→दाक्ष, शीत+ष्यञ्→शैत, सोम+ट्यण्→सौम)।"
    ),
    anuvritti_from = ("6.4.1", "7.2.114", "7.2.115"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

