"""
6.4.107  लोपश्चास्यान्यतरस्यां म्वोः  —  VIDHI

Padaccheda: लोपः च अस्य अन्यतरस्याम् म्वोः

anuvritti from 6.4.106: उतश्च प्रत्ययादसंयोगपूर्वात्

For tanādi roots (gana 8) with the vikaraṇa u (3.1.79) inserted after a
non-saṃyoga-final root, **optionally (anyatarasyām)** drop that vikaraṇa u
before a suffix starting with m or v.

  van + u + vaḥ →  van + vaḥ  = vanvaḥ    (1du; anyatarasyā optional)
  van + u + maḥ →  van + maḥ  = vanmaḥ    (1pl; anyatarasyā optional)

For kṛ, 6.4.108 is nityam (obligatory) — 6.4.107 does not overlap with it.

anyatarasyām: both forms vanuvaḥ (no-lopa) and vanvaḥ (lopa) are valid.
The engine fires this rule to produce the lopa form; the no-lopa form is
derived without applying this sūtra.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_MV = frozenset("mv")


def _find(state: State) -> int | None:
    """Return index of vikaraṇa u to drop, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        # 6.4.108 covers kṛ as nityam; 6.4.107 handles the rest
        if "kf" in up:
            continue
        if not t.meta.get("6_4_110_at_ut_done") and not t.meta.get("3_1_79_u_done"):
            # vikaraṇa hasn't been inserted yet
            pass
        # Next term must be the vikaraṇa u
        if i + 1 >= len(state.terms):
            continue
        vik = state.terms[i + 1]
        if "vikarana" not in vik.tags:
            continue
        if not vik.varnas or vik.varnas[0].slp1 != "u":
            continue
        if vik.meta.get("6_4_107_u_lopa_done"):
            continue
        # Term after vikaraṇa must exist and start with m or v
        if i + 2 >= len(state.terms):
            continue
        suf = state.terms[i + 2]
        if not suf.varnas:
            continue
        if suf.varnas[0].slp1 in _MV:
            return i + 1  # index of vikaraṇa to drop
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    idx = _find(state)
    if idx is None:
        return state
    state.terms[idx].meta["6_4_107_u_lopa_done"] = True
    del state.terms[idx]
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lopaScAsyAnyatarasyAM mvoH",
    text_dev              = "लोपश्चास्यान्यतरस्यां म्वोः",
    padaccheda_dev        = "लोपः च अस्य अन्यतरस्याम् म्वोः",
    why_dev               = (
        "तनाद्यादि-धातोः उ-विकरणस्य लोपः अन्यतरस्याम् — म्-व्-आदौ सार्वधातुके परे "
        "(वनुवः / वन्वः, वनुमः / वन्मः)।"
    ),
    anuvritti_from        = ("6.4.106",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
