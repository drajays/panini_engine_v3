"""
1.4.103  सुपः  (supaḥ)  —  PARIBHASHA

*Padaccheda:* *supaḥ* (ṣaṣṭhī).

*Anuvṛtti:* **1.4.101** *tiṅaḥ trīṇi trīṇi*; **1.4.1** *ekasañjñā*.

*Śāstra:* The 21 *sup* endings (seven triplets: nominative through locative,
plus vocative) listed in **4.1.2** receive the name *sup*.  This *paribhāṣā*
is fundamental: it enables downstream rules (notably **1.4.104**) to use
the *sup-saṃjñā*.

*Engine:* gives each sup its vacana saṃjñā (the triplet order of 4.1.2).
``cond`` never reads vibhakti/vacana/lakāra/surface or any gold corpus.
``r1_form_identity_exempt = True`` (saṃjñā, no surface change).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 14103 · सुपः
              padaccheda: सुपः ६/१
              anuvṛtti:   14101:  त्रीणि त्रीणि | 14102: एकवचनद्विवचनबहुवचनानि एकशः
              adhikāra:   4.1.2
  Source #2 — Kāśikā 1.4.103 udāharaṇa:
                सु इत्येकवचनम्
                औ इति द्विवचनम्
                जसिति बहुवचनम्
  Gloss (sa) — सुपः प्रत्ययाः तिङवत् त्रैष्टुभेन एकवचनादिभिश्च संज्ञकाः भवन्ति।
  Cross-check — surface pinned by: tests/unit/test_sutra_1_4_104_vibhakti.py
  Reference record: sutra_ref_out/1_4_103.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_1.pada_4.sutra_1_4_102 import (
    _SUP_102_DONE_TAG,
    _apply_sup_vacana_102,
    _terms_needing_sup_102_vacana,
)

_GATE_KEY = "1_4_103_supaH"


def cond(state: State) -> bool:
    """सुपः (1.4.101–102 anuvṛtti): each sup triplet's members are ekavacana,
    dvivacana, bahuvacana in order — सु एकवचनम्, औ द्विवचनम्, जस् बहुवचनम्."""
    return bool(_terms_needing_sup_102_vacana(state))


def act(state: State) -> State:
    state.samjna_registry[_GATE_KEY] = True
    for t in _terms_needing_sup_102_vacana(state):
        _apply_sup_vacana_102(t)
    return state


SUTRA = SutraRecord(
    sutra_id             = "1.4.103",
    sutra_type           = SutraType.SAMJNA,
    text_slp1            = "supaH",
    text_dev             = "सुपः",
    samagra_slp1         = "trIRi trIRi supaH ekaSaH ekavacana-dvivacana-bahuvacanAni",
    samagra_dev          = "त्रीणि त्रीणि सुपः एकशः एकवचन-द्विवचन-बहुवचनानि",
    padaccheda_dev       = "सुपः",
    why_dev              = "सुपां त्रिकेषु क्रमेण एकवचन-द्विवचन-बहुवचन-संज्ञाः (सु एकवचनम्, औ द्विवचनम्, जस् बहुवचनम्)।",
    anuvritti_from       = ("1.4.1", "1.4.101"),
    cond                 = cond,
    act                  = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
