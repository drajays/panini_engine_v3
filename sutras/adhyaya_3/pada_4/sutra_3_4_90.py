"""
3.4.90  आमेतः  —  VIDHI

In loṭ (imperative), after 3.4.79 replaces the ṭi of ātmanepada tiṅ with 'e',
this rule replaces that terminal 'e' with 'ām' for prathama and madhyama dvivacana
cells (te, Ate, Je, ATe).

Excluded:
  • thās/TAs (2sg): handled by 3.4.80+3.4.91, skipped here
  • se (2sg after 3.4.80): starts with 's'
  • Dve (2pl): starts with 'D', handled by 3.4.91
  • single 'e' (uttama 1sg): excluded
  • vahe (uttama 1du): starts with 'v', handled by 3.4.93
  • mahe (uttama 1pl): starts with 'm', handled by 3.4.93

Arm: state.meta["3_4_90_loT_karmani_arm"] must be True.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk

# Starts with these consonants → not a candidate for āmeta
_EXCLUDED_STARTS = frozenset({"v", "m", "D", "s"})


def _find_target(state: State):
    if not state.meta.get("3_4_90_loT_karmani_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_90_done"):
            continue
        vs = t.varnas
        if not vs or vs[-1].slp1 != "e":
            continue
        # Skip single 'e' (uttama 1sg)
        if len(vs) == 1:
            continue
        # Skip terms starting with excluded consonants (uttama 1du/1pl, 2sg, 2pl)
        if vs[0].slp1 in _EXCLUDED_STARTS:
            continue
        return ti
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    ti = _find_target(state)
    if ti is None:
        return state
    t = state.terms[ti]
    # Replace terminal 'e' with 'A' (ā) + 'm'
    t.varnas = list(t.varnas[:-1]) + [_mk("A"), _mk("m")]
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["3_4_90_done"] = True
    state.meta.pop("3_4_90_loT_karmani_arm", None)
    state.samjna_registry["3.4.90_ameta_loT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "AmetaH",
    text_dev              = "आमेतः",
    padaccheda_dev        = "आम् एतः",
    why_dev               = (
        "लोट्-आत्मनेपद-प्रथम/मध्यम-प्रत्ययेषु (ते, आते, जे, आथे) "
        "टि-स्थाने 'ए' के बाद 'आम्'-आदेशः — ताम्, आताम्, झाम्, आथाम्।"
    ),
    anuvritti_from        = ('3.4.79',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
