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

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34093 · एत ऐ
              padaccheda: एतः ऐ (लुप्तप्रथमान्तनिर्देशः)
              anuvṛtti:   34085: लोटः | 34092: उत्तमस्य
  Source #2 — Kāśikā 3.4.93 udāharaṇa:
                लोडुत्तमसंबन्धिन एकारस्य ऐकारादेशो भवति
                आमोऽपवादः
                करवै
  Cross-check — surface pinned by: tests/unit/test_c0_regressions_2026_09.py
  Reference record: sutra_ref_out/3_4_93.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _lot_sthani(state: State) -> bool:
    """लोटः — an ending whose sthānī is loṭ (1.1.56)."""
    return any((t.meta.get("source_lakara_upadesha") or "").strip() == "loT" for t in state.terms)


def _find_target(state: State):
    # एत ऐ (लोटः, उत्तमस्य): kartari (एधै, एधावहै) as well as yak paths
    if not (_lot_sthani(state) or any("yak" in t.tags for t in state.terms)):
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
        # एत ऐ is for the uttama only (3.4.92 उत्तमस्य): e, vahe, mahe — not se, Dve, te, ete, ante
        if not (len(vs) == 1 or vs[0].slp1 in ("v", "m")):
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
