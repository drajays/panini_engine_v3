"""
6.4.108  नित्यं करोतेः  —  VIDHI

Padaccheda: नित्यम् / करोतेः

For the root kṛ (karoti), the u-vikaraṇa (inserted by 3.1.79) is dropped
(*nityam* = always, i.e., obligatorily) before a consonant-initial sārvadhatuka
suffix that is NOT val (non-stop: semi-vowels y/r/l/v, nasals m/n, etc.).

This accounts for the alternation:
  • kur + u + vaḥ  →  kur + vaḥ  = kurvaḥ   (1du; 'v' is semi-vowel, not val)
  • kur + u + maḥ  →  kur + maḥ  = kurmaḥ   (1pl; 'm' is nasal, not val)
  • kur + u + taḥ  →  kur + u + taḥ (no drop) = kurutaḥ  (3du; 't' is val)
  • kur + u + anti  →  kur + v + anti (6.1.77) = kurvanti (AC-initial, not this rule)

Fires after 6.4.110 (a→u: kar→kur) in the bhuvādi spine.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# Non-val consonants: semi-vowels (y,r,l,v) + nasals (N,n,Y,M,m = ñ,ṇ,n,ṅ,m)
_NON_VAL = frozenset("yrlvNnYMm")


def _find(state: State):
    """Return index of u-vikaraṇa to drop, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if "kf" not in up:
            continue
        if not t.meta.get("6_4_110_at_ut_done"):
            continue
        # Next term must be the u-vikaraṇa
        if i + 1 >= len(state.terms):
            continue
        vik = state.terms[i + 1]
        if "vikarana" not in vik.tags:
            continue
        if not vik.varnas or vik.varnas[0].slp1 != "u":
            continue
        if vik.meta.get("6_4_108_u_lopa_done"):
            continue
        # Term after vikaraṇa must exist and start with a non-val consonant
        if i + 2 >= len(state.terms):
            continue
        suf = state.terms[i + 2]
        if not suf.varnas:
            continue
        first = suf.varnas[0].slp1
        if first in _NON_VAL:
            return i + 1  # index of vikaraṇa to drop
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    idx = _find(state)
    if idx is None:
        return state
    state.terms[idx].meta["6_4_108_u_lopa_done"] = True
    del state.terms[idx]
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM karoteH",
    text_dev              = "नित्यं करोतेः",
    padaccheda_dev        = "नित्यम् / करोतेः",
    why_dev               = (
        "करोति-धातोः उ-विकरणस्य लोपः नित्यम् — अवल्-आदि-सार्वधातुके परे "
        "(कुर्वः, कुर्मः)।"
    ),
    anuvritti_from        = ("6.4.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
