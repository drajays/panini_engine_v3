"""
7.3.106  सम्बुद्धौ च  —  VIDHI

Padaccheda: सम्बुद्धौ च

Operational slice (strī · *ā*-banta *prātipadika* + सम्बुद्धि-एकवचन *su*):

  After **4.1.2** tags ``sambuddhi`` on the *sup* and *it*-lopa leaves apṛkta
  ``s``, the *aṅga*'s final long ``A`` becomes ``e`` (SLP1 ``e``) so **6.1.69**
  can then drop ``s`` on an ``e``-final *aṅga* — surface *rādhā* + सम्बुद्धि
  → **राधे** (cf. clip chain **7.3.106** → **6.1.69**).

Blindness: ``strīliṅga`` / ``sambuddhi`` / ``sup`` tags + final ``A`` + ``s``
residue only — no ``vibhakti`` / ``vacana`` / gold reads.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73106 · सम्बुद्धौ च
              padaccheda: सम्बुद्धौ च
              anuvṛtti:   64001: अङ्गस्य | 73103: एत् | 73105: आपः
  Source #2 — Kāśikā 7.3.106 udāharaṇa:
                संबुद्धौ च परत आबन्तस्याङ्गस्य एत्वं भवति
                हे खट्वे
                हे बहुराजे
  Cross-check — surface pinned by: tests/regression/test_rADA_strilinga_gold.py
  Reference record: sutra_ref_out/7_3_106.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk


def _matches(state: State) -> bool:
    if not adhikara_in_effect("7.3.106", state, "6.4.1"):
        return False
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr = state.terms[-1]
    if "anga" not in anga.tags or "strīliṅga" not in anga.tags:
        return False
    if "sup" not in pr.tags or "sambuddhi" not in pr.tags:
        return False
    if not anga.varnas or anga.varnas[-1].slp1 != "A":
        return False
    if anga.meta.get("7_3_106_sambuddhi_A_to_e_done"):
        return False
    # *su* residue: apṛkta ``s`` still present (before **6.1.69**).
    if not pr.varnas or pr.varnas[0].slp1 != "s":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    anga.varnas[-1] = mk("e")
    anga.meta["7_3_106_sambuddhi_A_to_e_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "sambudDO ca",
    text_dev              = "सम्बुद्धौ च",
    padaccheda_dev        = "सम्बुद्धौ च",
    why_dev               = "(सूत्रम् ७.३.१०६) सम्बुद्धौ च — आबन्त-स्त्रीलिङ्ग-अङ्गस्यान्त्य-आ-कारस्य 'ए'-आदेशः।",
    anuvritti_from        = ("7.1.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
