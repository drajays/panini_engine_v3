"""
3.4.93  एत ऐ  —  VIDHI

In loṭ (imperative) uttama (1st person) cells, after 3.4.79 has replaced
the ṭi of ātmanepada tiṅ ādeśas with 'e', this rule replaces that terminal
'e' with 'ai' (E in SLP1).

Applies to:
  • 1sg: e → E      (iṭ → i → e → E = ai)
  • 1du: vahe → vahE
  • 1pl: mahe → mahE  (mahiṅ → mahi → mahe → mahE)

Excluded: all prathama/madhyama forms (already handled by 3.4.90/3.4.91).

Arm: state.meta["3_4_93_loT_karmani_arm"] must be True.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _find_target(state: State):
    if not state.meta.get("3_4_93_loT_karmani_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_93_done"):
            continue
        if t.meta.get("3_4_90_done"):
            continue
        vs = t.varnas
        if not vs or vs[-1].slp1 != "e":
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
    # Replace terminal 'e' with 'E' (ai in SLP1)
    t.varnas = list(t.varnas[:-1]) + [_mk("E")]
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["3_4_93_done"] = True
    state.meta.pop("3_4_93_loT_karmani_arm", None)
    state.samjna_registry["3.4.93_eta_ai"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "eta E",
    text_dev              = "एत ऐ",
    padaccheda_dev        = "एतः ऐ (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = (
        "लोट् उत्तम-आत्मनेपद-प्रत्ययेषु (ए, वहे, महे) "
        "टि-स्थाने 'ए'-स्य 'ऐ'-आदेशः।"
    ),
    anuvritti_from        = ('3.4.79',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
