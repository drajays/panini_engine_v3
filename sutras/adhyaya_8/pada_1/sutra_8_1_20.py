"""
8.1.20  युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ  —  VIDHI

द्विवचने ṣaṣṭhī / caturthī / dvitīyā में युष्मद्→वाम्, अस्मद्→नौ (पदात् परस्य, अपादादौ)।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.1.20 
  Source #2 — Kāśikā 8.1.20: ग्रामो वां स्वम् / ग्रामो वः स्वम् / ग्रामस्ते स्वम् / ग्रामस्त्वा पश्यति (as the sūtra)
  Reference — ashtadhyayi.com sūtra-prayoga list (Kirātārjunīya, Bhaṭṭikāvya … attestations)

Engine: ``cond`` reads Term tags only — the pada's saṃjñā-names ``vib_*`` / ``vac_*`` (4.1.2), the
pronoun's lexical identity, and the adhikāras 8.1.17 / 8.1.18 (*padāt* … *apādādau*). The ādeśa
replaces the whole pada (sarvādeśa, 1.1.55) and is anudātta (accent is not modelled).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import STHA_VIBHAKTI, replace, target
from engine.state import State

_ADESHA = {'yuzmad': 'vAm', 'asmad': 'nO'}


def _site(state: State):
    i = target(state, "8.1.20")
    if i is None:
        return None
    t = state.terms[i]
    return i if (t.tags & STHA_VIBHAKTI and "vac_dvi" in t.tags) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    return state if i is None else replace(state, i, "8.1.20", _ADESHA)


SUTRA = SutraRecord(
    sutra_id="8.1.20",
    sutra_type=SutraType.VIDHI,
    text_slp1='yuzmadasmadoH zazWIcaturWIdvitIyAsWayorvAnnAvO',
    text_dev='युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ',
    padaccheda_dev='युष्मद्-अस्मदोः षष्ठी-चतुर्थी-द्वितीया-स्थयोः वाम्-नौ',
    why_dev='द्विवचनान्त षष्ठी/चतुर्थी/द्वितीया युष्मद्-अस्मद् पद → वाम्/नौ (अपादादौ, पदात् परम्)।',
    anuvritti_from=("8.1.17", "8.1.18"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
