"""
8.1.21  बहुवचनस्य वस्नसौ  —  VIDHI

बहुवचने ṣaṣṭhī / caturthī / dvitīyā में युष्मद्→वस्, अस्मद्→नस्।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.1.21 
  Source #2 — Kāśikā 8.1.21: ग्रामो वां स्वम् / ग्रामो वः स्वम् / ग्रामस्ते स्वम् / ग्रामस्त्वा पश्यति (as the sūtra)
  Reference — ashtadhyayi.com sūtra-prayoga list (Kirātārjunīya, Bhaṭṭikāvya … attestations)

Engine: ``cond`` reads Term tags only — the pada's saṃjñā-names ``vib_*`` / ``vac_*`` (4.1.2), the
pronoun's lexical identity, and the adhikāras 8.1.17 / 8.1.18 (*padāt* … *apādādau*). The ādeśa
replaces the whole pada (sarvādeśa, 1.1.55) and is anudātta (accent is not modelled).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import STHA_VIBHAKTI, replace, target
from engine.state import State

_ADESHA = {'yuzmad': 'vas', 'asmad': 'nas'}


def _site(state: State):
    i = target(state, "8.1.21")
    if i is None:
        return None
    t = state.terms[i]
    return i if (t.tags & STHA_VIBHAKTI and "vac_bahu" in t.tags) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    return state if i is None else replace(state, i, "8.1.21", _ADESHA)


SUTRA = SutraRecord(
    sutra_id="8.1.21",
    sutra_type=SutraType.VIDHI,
    text_slp1='bahuvacanasya vasnasO',
    text_dev='बहुवचनस्य वस्नसौ',
    padaccheda_dev='बहुवचनस्य वस्-नसौ',
    why_dev='बहुवचनान्त षष्ठी/चतुर्थी/द्वितीया युष्मद्-अस्मद् पद → वस्/नस् (रुत्व-विसर्ग से वः/नः)।',
    anuvritti_from=("8.1.17", "8.1.18", "8.1.20"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
