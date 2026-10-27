"""
4.1.95  अत इञ्  —  VIDHI

Padaccheda: अतः इञ्

In the apatya adhikāra (4.1.92), an a-final prātipadika takes the taddhita
suffix iñ (SLP1: iY).  The ñ (Y) is the it-marker (1.3.3 hal-antyam);
1.3.9 will lope it, leaving 'i' and recording 'Y' in `it_markers`.
7.2.117 then applies vṛddhi to the first vowel of the aṅga (ñit context).
6.4.148 then lopos the final 'a' before the 'i' onset.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 41095 · अत इञ्
              padaccheda: अतः इञ्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 41001: ङ्याप्प्रातिपदिकात् | 41076: तद्धिताः | 41092: तस्यापत्यम्
  Source #2 — Kāśikā 4.1.95 udāharaṇa:
                अकारान्तात् प्रातिपदिकादिञ् प्रत्ययो भवति
                अणोऽपवादः
                दक्षस्यापत्यं दाक्षिः
  Cross-check — surface pinned by: tests/unit/test_dASaraThi_apatya_iY.py
  Reference record: sutra_ref_out/4_1_95.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, final=lambda f: f.endswith("a"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "iY")


SUTRA = SutraRecord(
    sutra_id              = "4.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ata iY",
    text_dev              = "अत इञ्",
    samagra_slp1          = "tasya apatyam iti ataH iY pratyayaH",
    samagra_dev           = "'तस्य अपत्यम्' (इति) अतः इञ् प्रत्ययः",
    padaccheda_dev        = "अतः इञ्",
    why_dev               = "(सूत्रम् 4.1.95) अत इञ्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
