"""
3.4.99  नित्यं ङितः  —  VIDHI

Two operational paths:
  1. Arm ``3_4_99_arm``: legacy gate-setter (krt_kind = 3.4.99).
  2. Lakāra-based ṅit s-lopa: when state.meta["lakara"] is one of the ṅit
     lakāras {laG, liG, AsIrliG, luG, lRG, loT}, drop the final 's' of
     ṅit tiṅ ādeśas 'vas' and 'mas'.

In laṅ, 'vas' and 'mas' are ṅit (mandatorily applied); 3.4.99 deletes their
final 's' so the tiṅ ādeśa ends with the prātipadika consonant alone.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34099 · नित्यं ङितः
              padaccheda: नित्यम् ङितः
              anuvṛtti:   34077: लस्य | 34097: लोपः | 34098: स उत्तमस्य
  Source #2 — Kāśikā 3.4.99 udāharaṇa:
                अपचाव
                अपचाम
                नित्यग्रहणं विकल्पनिवृत्त्यर्थम्
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhavat_lang.py, tests/unit/test_tinanta_abhavisyat_lrg.py, tests/unit/test_tinanta_bhavatu_lot.py
  Reference record: sutra_ref_out/3_4_99.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.nimitta_predicates import acts_as_ngit_lakara

# ṅit tiṅ ādeśas whose final 's' is dropped.
_NGIT_S_FINAL: frozenset[str] = frozenset({"vas", "mas"})



def _find_ngit_s_term(state: State):
    """Find a ṅit tiṅ ādeśa (vas/mas) ending in 's' for ṅit-lakāra s-lopa."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if not acts_as_ngit_lakara(t):      # ṅit lakāra — or loṭ by 3.4.85 लोटो लङ्वत्
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _NGIT_S_FINAL:
            continue
        if t.meta.get("3_4_99_s_lopa_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "s":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_ngit_s_term(state) is not None


def act(state: State) -> State:
    j = _find_ngit_s_term(state)
    if j is None:
        return state
    t = state.terms[j]
    # उत्तमस्य सः — the final s of a ṅit lakāra's uttama ādeśa (vas, mas), dropped by 1.1.52 अलोऽन्त्यस्य.
    del t.varnas[-1]
    t.meta["3_4_99_s_lopa_done"] = True
    state.samjna_registry["3.4.99_ngit_s_lopa"] = state.samjna_registry.get("3.4.99_ngit_s_lopa", 0) + 1
    state.meta["__why_now_dev__"] = (
        "ङित्-लकारस्य (लङ्-लिङ्-लुङ्-लृङ्; लोट् तु लोटो लङ्वत् ३.४.८५ इत्यनेन) उत्तमपुरुष-प्रत्ययस्य "
        "अन्तिम-सकारस्य नित्यं लोपः — वस् → व, मस् → म (भवाव, भवाम)। (३.४.९९)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.99",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "nityaM NitaH",
    text_dev              = "नित्यं ङितः",
    samagra_slp1          = "NitaH lasya uttamasya saH nityaM lopaH",
    samagra_dev           = "ङितः लस्य उत्तमस्य सः नित्यं लोपः",
    padaccheda_dev        = "नित्यम् ङितः",
    why_dev               = "धातोः प्रत्ययः (३.4.99)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
