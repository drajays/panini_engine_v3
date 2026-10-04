"""
6.4.24  अनिदितां हल उपधायाः क्ङिति  —  VIDHI (narrow demo)

Demo slice (ईधे):
  For dhātu `inD` (इन्ध्), delete the upadhā consonant `n` when a following
  pratyaya is in the kṅit locus (tagged ``kngiti`` by 1.2.6/1.2.5 etc.).

Engine:
  - narrowly searches for the first dhātu term and removes `n` if it is the
    penultimate varṇa.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64024 · अनिदितां हल उपधायाः क्ङिति
              padaccheda: अन्-इद्-इताम् हलः उपधायाः क्ङिति
              anuvṛtti:   64001: अङ्गस्य | 64023: नलोपः
  Source #2 — Kāśikā 6.4.24 udāharaṇa:
                स्रस्तः
                ध्वस्तः
                स्रस्यते
  Cross-check — surface pinned by: tests/unit/test_IDe_lit_indh.py, tests/unit/test_corrected_prakriyas_v2_bundle.py
  Reference record: sutra_ref_out/6_4_24.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _kngiti_present(state: State) -> bool:
    # *kṅiti* locus: *kṛt* *pratyaya* rows use ``kind="pratyaya"`` with *kngiti* tag
    # (``"pratyaya"`` string tag is not always present on the same ``Term``).
    # The affix must follow the aṅga immediately ("pare"): a pit vikaraṇa (śap) between
    # dhātu and a ṅit tiṅ blocks it (maTAvaH is wrong; manTAvaH).
    nxt = next((t for t in state.terms[1:] if t.varnas), None)
    return nxt is not None and "kngiti" in nxt.tags and (nxt.kind == "pratyaya" or "pratyaya" in nxt.tags)


_NASAL = frozenset("NYRnmM")
_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


def cond(state: State) -> bool:
    if not _kngiti_present(state):
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    dh = state.terms[0]
    # अनिदितां हल उपधायाः क्ङिति: a hal-final root that is not idit, with a
    # nasal upadhā, loses it before a kṅit affix (स्कुन्भ् → स्कुभ्नाति, इन्ध् → इद्ध)
    if "idit" in dh.tags or dh.meta.get("7_1_58_num_done"):
        return False
    if len(dh.varnas) < 2 or dh.varnas[-1].slp1 not in _HAL:
        return False
    if dh.varnas[-2].slp1 not in _NASAL or "num_agama" in dh.varnas[-2].tags:
        return False
    if "snam" in dh.varnas[-2].tags:      # śnam's n is an infix, not the root's upadhā-nasal (rundhaH)
        return False
    if dh.meta.get("6_4_24_n_lopa_done"):
        return False
    if len(dh.varnas) < 2:
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    dh = state.terms[0]
    del dh.varnas[-2]
    dh.meta["6_4_24_n_lopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.24",
    sutra_type=SutraType.VIDHI,
    text_slp1='aniditAM hala upaDAyAH kNiti',
    text_dev='अनिदितां हल उपधायाः क्ङिति',
    padaccheda_dev="अनिदिताम् / हल् / उपधायाः / क्‍ङिति",
    why_dev="क्ङिति परे अनिदित्-धातोः उपधा-हल्-लोपः (इन्ध्→इध्; ईधे)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

