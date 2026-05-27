"""
6.1.73  छे च  —  VIDHI

Full rule (with anuvṛtti from 6.1.71 hrasvaḥ):
  hrasvaḥ [tuk] che ca — a hrasva vowel gets tuk (= 't') before 'C' (cha).

Two contexts:
  A. Within a single aṅga term: hrasva vowel at position j, C at j+1.
     Example: pracC → insert t after 'a': pratC → by 8.4.40 ścutva: pracC
     Used in: pracchhanīya (pracC + anīya), etc.

  B. Cross-term (arm-gated, existing demo): term[0][-1] = 'i', term[1][0] = 'C'.
     Example: dadhi + Catram → dadhit + Catram → by 8.4.40: dadhic + Catram
     Arm: state.meta['6_1_73_che_ca_arm'] = True

By 1.1.46 (āntaṭakitau): tuk is kit, so it is placed after the preceding element
(the hrasva vowel).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_hrasva


def _find_within_hrasva_C(state: State):
    """Return (term_idx, vowel_idx) for within-term hrasva + C pair."""
    for ti, t in enumerate(state.terms):
        if t.meta.get("6_1_73_within_done"):
            continue
        for j in range(len(t.varnas) - 1):
            if is_hrasva(t.varnas[j].slp1) and t.varnas[j + 1].slp1 == "C":
                return (ti, j)
    return None


def _cross_term_match(state: State) -> bool:
    """Arm-gated cross-term check: term[0] ends in 'i', term[1] starts with 'C'."""
    if not state.meta.get("6_1_73_che_ca_arm"):
        return False
    if len(state.terms) < 2:
        return False
    a, b = state.terms[0], state.terms[1]
    if a.meta.get("6_1_73_che_ca_done"):
        return False
    if not a.varnas or not b.varnas:
        return False
    return a.varnas[-1].slp1 == "i" and b.varnas[0].slp1 == "C"


def cond(state: State) -> bool:
    return _find_within_hrasva_C(state) is not None or _cross_term_match(state)


def act(state: State) -> State:
    # Within-term path
    hit = _find_within_hrasva_C(state)
    if hit is not None:
        ti, j = hit
        state.terms[ti].varnas.insert(j + 1, mk("t"))
        state.terms[ti].meta["6_1_73_within_done"] = True
        return state
    # Cross-term (arm) path
    if _cross_term_match(state):
        t0 = state.terms[0]
        t0.varnas.append(mk("t"))
        t0.meta["6_1_73_che_ca_done"] = True
        state.meta["6_1_73_che_ca_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.73",
    sutra_type=SutraType.VIDHI,
    text_slp1="CeH ca",
    text_dev="छे च",
    padaccheda_dev="छे / च",
    why_dev=(
        "ह्रस्वस्वरात् परः अव्यवहितः छकारः विद्यते चेत् तस्य ह्रस्वस्य 'तुक्' आगमः।"
        " आद्यन्तौ टकितौ १.१.४६ इत्यनेन स्वरात् अनन्तरम्।"
    ),
    anuvritti_from=("6.1.71",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
