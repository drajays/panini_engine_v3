"""
3.3.162  लोट् च  —  VIDHI (narrow: loṭ lakāra attachment)

Two operational paths:
  1. ``loT_adhikara_recipe``: legacy P031 adhikāra push.
  2. ``loT_recipe``: glass-box loṭ pipeline — fires as a trace marker;
     the loT placeholder Term is appended inline in the calling pipeline
     (following the same pattern as 3.3.13 for lṛṭ).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 33162 · लोट् च
              padaccheda: लोट् च
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 33161: विधिनिमन्‍त्रणामन्‍त्रणाधीष्‍टसंप्रश्‍नप्रार्थनेषु लिङ्
  Source #2 — Kāśikā 3.3.162 udāharaṇa:
                योगविभाग उत्तरार्थः
                विधौ तावत् — कटं तावद् भवान् करोतु
                ग्रामं भवानागच्छतु
  Cross-check — surface pinned by: tests/unit/test_tinanta_bhavatu_lot.py
  Reference record: sutra_ref_out/3_3_162.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _structural_site(state: State) -> bool:
    """लोट् च, on its own: the dhātu has been given the loṭ vivakṣā (``lot_derivation`` — an input, like
    puruṣa and vacana), धातोः (3.1.91) governs, and no lakāra stands after it yet."""
    if not adhikara_in_effect("3.3.162", state, "3.1.91"):
        return False
    if not any("dhatu" in t.tags and "lot_derivation" in t.tags for t in state.terms):
        return False
    return not any(t.kind == "pratyaya" and "lakAra_pratyaya_placeholder" in t.tags for t in state.terms) \
        and not any((t.meta.get("upadesha_slp1") or "") == "loT" for t in state.terms)


def cond(state: State) -> bool:
    if state.meta.get("loT_recipe"):
        return not state.meta.get("3_3_162_loT_done")
    if not state.meta.get("loT_adhikara_recipe"):
        return _structural_site(state)
    return not any(e.get("id") == "3.3.162" for e in state.adhikara_stack)


def act(state: State) -> State:
    if state.meta.get("loT_recipe"):
        state.meta["3_3_162_loT_done"] = True
        state.meta.pop("loT_recipe", None)
        return state
    if not state.meta.get("loT_adhikara_recipe"):
        # structural path: attach the loṭ placeholder (the ṭ is it: 1.3.3 → 1.3.9 take it away)
        state.terms.append(Term(
            kind="pratyaya",
            varnas=parse_slp1_upadesha_sequence("loT"),
            tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
            meta={"upadesha_slp1": "loT"},
        ))
        return state
    state.adhikara_stack.append({
        "id": "3.3.162",
        "scope_end": "3.3.162",
        "text_dev": 'लोट् च',
    })
    state.meta.pop("loT_adhikara_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.162",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='low ca',
    text_dev='लोट् च',
    samagra_slp1="viDi-nimantraRa-AmantraRa-aDIzwa-sampraSna-prArTanezu low ca",
    samagra_dev="विधि-निमन्त्रण-आमन्त्रण-अधीष्ट-सम्प्रश्न-प्रार्थनेषु लोट् च",
    padaccheda_dev="लोट् / च",
    why_dev="आज्ञार्थे धातोः लोट्-लकारः (आज्ञा/अनुज्ञा/प्रार्थना-पक्षे)।",
    anuvritti_from=("3.3.161",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
