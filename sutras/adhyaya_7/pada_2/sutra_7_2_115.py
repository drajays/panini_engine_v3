"""
7.2.115  अचो ञ्णिति  —  VIDHI

When a following pratyaya is **ñit** or **ṇit**, the **final vowel** (*ac*)
of the *aṅga* receives *vṛddhi* (operational mapping to ``A`` / ``E`` / ``O``
in SLP1).

Narrow use: kṛt ``Nvul`` path where upadhā-vṛddhi (**7.2.116**) does not
apply (e.g. ``nI`` + ``ak`` → ``nE`` + ``ak`` for नायक).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 72115 · अचो ञ्णिति
              padaccheda: अन्त्य&अचः ञ्णिति
              anuvṛtti:   64001: अङ्गस्य | 72114: वृद्धिः
  Source #2 — Kāśikā 7.2.115 udāharaṇa:
                ञिति — एकस्तण्डुलनिश्चायः
                द्वौ शूर्पनिष्पावौ
                कारः
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_nayaka.py, tests/forward/test_forward_krdanta_pacaka.py, tests/unit/test_sthanivat_it_samjna.py
  Reference record: sutra_ref_out/7_2_115.json
"""
from __future__ import annotations

from typing import Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_dirgha, is_hrasva
from sutras.adhyaya_1.pada_1.sutra_1_1_6 import dhatu_blocked_by_1_1_6


def _vrddhi_vowel(ch: str, state: State) -> Optional[str]:
    """Map final ``ac`` to vṛddhi letter (SLP1), using optional sthānāntara gate."""
    st = state.paribhasha_gates.get("sthanantara_vrddhi") or {}
    if ch in st:
        return st[ch]
    if ch in ("a",):
        return "A"
    if ch in ("i", "I"):
        return "E"
    if ch in ("u", "U"):
        return "O"
    if ch in ("f", "F", "x", "X"):
        return "A"                            # + 1.1.51 rapara: कृ → कार् (अकारि, कारक)
    if ch in ("e", "E", "o", "O"):
        return ch
    return None


def _find(state: State):
    # Karmani luṭ arm: direct vṛddhi on dhātu (ciṇvat iṭ from 6.4.62)
    if state.meta.get("7_2_115_karmani_lut_arm"):
        dhatu = next((t for t in state.terms if "dhatu" in t.tags), None)
        if dhatu is None or dhatu.meta.get("aco_nniti_vrddhi_done"):
            return None
        if not dhatu.varnas:
            return None
        last = dhatu.varnas[-1].slp1
        rep = _vrddhi_vowel(last, state)
        if rep is None or rep == last:          # already vṛddhi (ऐ, औ, आ)
            return None
        di = state.terms.index(dhatu)
        return (di, len(dhatu.varnas) - 1, rep)

    # General path: ñit/ṇit pratyaya (kṛt, tiṅ, ...) after the dhātu — the mūla
    # sūtra names no pada-class, only the it-marker, so any pratyaya qualifies.
    if len(state.terms) < 2:
        return None
    dhatu = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dhatu is None:
        return None
    pr = state.terms[-1]
    if "pratyaya" not in pr.tags:
        return None
    if dhatu.meta.get("aco_nniti_vrddhi_done"):
        return None
    if dhatu_blocked_by_1_1_6(dhatu.meta.get("upadesha_slp1")):
        return None
    itm = pr.meta.get("it_markers", set())
    if not isinstance(itm, set):
        return None
    if not (("Y" in itm) or ("R" in itm)):                  # ñit, ṇit — not ṅit (SLP1 N = ṅ)
        return None
    if not dhatu.varnas:
        return None
    # A kit āgama stands at the *end* of the aṅga it belongs to (1.1.46 आद्यन्तौ टकितौ: भू + वुक् → भूव्): the
    # aṅga's final is then that hal, not the root's vowel, and there is no ac to take vṛddhi.
    di0 = state.terms.index(dhatu)
    if any("agama" in u.tags and u.varnas and "it:kit" in u.tags for u in state.terms[di0 + 1:-1]):
        return None
    last = dhatu.varnas[-1].slp1
    # Paninian ``ac`` (अच्) — hrasva + dīrgha; ``AC`` pratyāhāra here is short-only.
    if not (is_hrasva(last) or is_dirgha(last)):
        return None
    rep = _vrddhi_vowel(last, state)
    if rep is None and last in ("f", "F", "x", "X"):
        rep = "A"          # vṛddhi of ṛ/ḷ is ā + r/l (1.1.51): पॄ → पार् (पारयति)
    if rep is None:
        return None
    di = state.terms.index(dhatu)
    return (di, len(dhatu.varnas) - 1, rep)


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi, rep = hit
    old = state.terms[ti].varnas[vi].slp1
    state.terms[ti].varnas[vi] = mk(rep)
    state.terms[ti].meta["aco_nniti_vrddhi_done"] = True
    if old in ("f", "F", "x", "X"):          # hand the r/l to 1.1.51 उरण् रपरः
        state.terms[ti].meta["urN_rapara_pending"] = "r" if old in ("f", "F") else "l"
        state.terms[ti].meta["urN_rapara_after_index"] = vi
    state.meta.pop("7_2_115_karmani_lut_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.115",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'aco YRiti',
    text_dev       = 'अचो ञ्णिति',
    padaccheda_dev = "अचः ञ्-णिति",
    why_dev        = "ञित्/णिति-परे अङ्गान्त्यचः वृद्धिः (णीञ्+ण्वुल् → नै/नायक)।",
    anuvritti_from = ("7.2.114",),
    # vṛddhi before ñit/ṇit is the exception to the guṇa of 7.3.84 (ji + ṇal → jijāya, not *jijaya).
    apavada_of     = ("7.3.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
