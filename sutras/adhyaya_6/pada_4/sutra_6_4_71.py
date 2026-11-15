"""
6.4.71  लुङ्लङ्लृङ्क्ष्वडुदात्तः  —  VIDHI (narrow: aṭ augment)

Engine: in luṅ/laṅ/lṛṅ contexts, utter **अट्** as taught (``engine.agama.utter_at``) as the ādyavayava of the
aṅga (ṭit, 1.1.46). 1.3.3 names ट् and 1.3.9 deletes it, leaving अ tagged ``aT_agama_v``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64071 · लुङ्लङ्लृङ्क्ष्वडुदात्तः
              padaccheda: लुङ्-लङ्-ल्रुक्षु अट् उदात्तः
              anuvṛtti:   64001: अङ्गस्य
  Source #2 — Kāśikā 6.4.71 udāharaṇa:
                लुङ् — अकार्षीत्
                अहार्षीत्
                लङ् — अकरोत्
  Cross-check — surface pinned by: tests/unit/test_AwIwat_luN_aT_Nic_caN_tip.py, tests/unit/test_aBavatAm_split_prakriyas.py, tests/unit/test_adita_luN_dAda_ghu.py
  Reference record: sutra_ref_out/6_4_71.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.agama import utter_at
from engine.state import State
from phonology import mk

AT_AGAMA_CONTEXT_TAG = "aT_agama_context"


def _find_dhatu_term(state: State):
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def _find_at_agama_site(state: State):
    dh = _find_dhatu_term(state)
    if dh is None:
        return None
    if dh.meta.get("aT_agama_6_4_71_done"):
        return None
    if AT_AGAMA_CONTEXT_TAG not in dh.tags:
        return None
    # 6.4.72 आडजादीनाम् is the apavāda: an ajādi dhātu takes āṭ, not aṭ.
    if dh.varnas and dh.varnas[0].slp1 in "aAiIuUfFxXeEoO":
        return None
    return dh


def cond(state: State) -> bool:
    return _find_at_agama_site(state) is not None


def act(state: State) -> State:
    dh = _find_at_agama_site(state)
    if dh is None:
        return state
    # the aṭ precedes the whole aṅga — an abhyāsa too (अचूचुरत्)
    i = state.terms.index(dh)
    first = state.terms[i - 1] if i and "abhyasa" in state.terms[i - 1].tags else dh
    utter_at(state, first, 0)
    dh.meta["aT_agama_6_4_71_done"] = True
    dh.tags.discard(AT_AGAMA_CONTEXT_TAG)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.71",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'luNlaNlfNkzvaqudAttaH',
    text_dev       = 'लुङ्लङ्लृङ्क्ष्वडुदात्तः',
    samagra_slp1   = "luN-laN-lfNkzu aNgasya aw udAttaH",
    samagra_dev    = "लुङ्-लङ्-लृङ्क्षु अङ्गस्य अट् उदात्तः",
    padaccheda_dev = "लुङ्-लङ्-लृङ्-क्षु / अट् / उदात्तः",
    why_dev        = (
        "लुङ्/लङ्/लृङ्-लकारे अट्-आगमः — अट् उपदिश्यते, टकारः इत् (१.३.३) लुप्यते (१.३.९), "
        "टित्त्वाद् आद्यवयवः (१.१.४६)।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

