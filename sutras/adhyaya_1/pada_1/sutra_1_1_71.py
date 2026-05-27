"""
1.1.71  आदिरन्त्येन सहेता  (Adir antyena sahetA)  —  PARIBHASHA

Classical role:
  "The first [member of a pratyāhāra-list] together with the last
  [which carries an it-marker] [represents all elements in between]."

  This is the foundational rule for pratyāhāra interpretation in the
  Aṣṭādhyāyī. Every pratyāhāra (e.g., aṇ, ac, hal, eṄ) is understood
  through this paribhāṣā: the first phoneme of the Śiva-sūtra group and
  the last (it-marked) phoneme bracket all the phonemes in between.

  Example: aṇ = a (first in Śiva-sūtra 1) + ṇ (it of sūtra 1) = {a, i, u,
  ṛ, ḷ} — all vowels including short forms; with 1.1.70 (tapara) one may
  restrict to specific lengths.

  The same principle applies to PRATYAYA lists — e.g.:
    sup   = su (first in 4.1.2) + p (it of last entry "sup") = all 21 sups
    tiṅ   = ti (from "tip") + ṅ (it of "mahiṅ") = all 18 tiṅ ādeśas
    taṅ   = ta + ṅ = ātmanepada subset of tiṅ
    ṭāp   = ṭā (from TAp) + p = ṭāp/ḍāp/cāp strī-pratyaya group
  See phonology/pratyaya_pratyahara.py for the engine implementation.

v3 engine role:
  - Installs gate "1_1_71_Adir_antyena_sahetA" in paribhasha_gates once
    per derivation (idempotent guard via cond).
  - Mirrors it in samjna_registry for audit/pipeline inspection.
  - cond() reads ONLY paribhasha_gates (Art. 2 compliant: no vibhakti,
    vacana, lakāra, surface Devanāgarī, data, or reference access).
  - No arm flags.  r1_form_identity_exempt=True (no surface change).
  - Phoneme pratyāhāras: phonology/pratyahara.py (AC, HAL, IK, …)
  - Pratyaya pratyāhāras: phonology/pratyaya_pratyahara.py (SUP, TIN, …)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_71_Adir_antyena_sahetA"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.71",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "Adir antyena sahetA",
    text_dev                = "आदिरन्त्येन सहेता",
    padaccheda_dev          = "आदिः / अन्त्येन / सह / इता",
    why_dev                 = (
        "प्रत्याहारे प्रथमः वर्णः अन्त्येन इत्-संज्ञकेन सह मिलित्वा "
        "मध्यवर्तिनः सर्वान् वर्णान् गृह्णाति — "
        "यथा अण् = {अ…ण्} = शिव-सूत्रेषु अ-तः ण्-पर्यन्ताः सर्वे।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
