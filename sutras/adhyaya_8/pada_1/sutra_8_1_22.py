"""
8.1.22  तेमयावेकवचनस्य  —  VIDHI

एकवचने ṣaṣṭhī / caturthī (dvitīyā में 8.1.23 अपवाद) युष्मद्→ते, अस्मद्→मे।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.1.22 
  Source #2 — Kāśikā 8.1.22: ग्रामो वां स्वम् / ग्रामो वः स्वम् / ग्रामस्ते स्वम् / ग्रामस्त्वा पश्यति (as the sūtra)
  Reference — ashtadhyayi.com sūtra-prayoga list (Kirātārjunīya, Bhaṭṭikāvya … attestations)

Engine: ``cond`` reads Term tags only — the pada's saṃjñā-names ``vib_*`` / ``vac_*`` (4.1.2), the
pronoun's lexical identity, and the adhikāras 8.1.17 / 8.1.18 (*padāt* … *apādādau*). The ādeśa
replaces the whole pada (sarvādeśa, 1.1.55) and is anudātta (accent is not modelled).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import STHA_VIBHAKTI, replace, target
from engine.state import State

_ADESHA = {'yuzmad': 'te', 'asmad': 'me'}


def _site(state: State):
    i = target(state, "8.1.22")
    if i is None:
        return None
    t = state.terms[i]
    return i if (t.tags & STHA_VIBHAKTI and "vac_eka" in t.tags) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    return state if i is None else replace(state, i, "8.1.22", _ADESHA)


SUTRA = SutraRecord(
    sutra_id="8.1.22",
    sutra_type=SutraType.VIDHI,
    text_slp1='temayAvekavacanasya',
    text_dev='तेमयावेकवचनस्य',
    padaccheda_dev='ते-मयौ एकवचनस्य',
    why_dev='एकवचनान्त षष्ठी/चतुर्थी युष्मद्-अस्मद् पद → ते/मे (द्वितीया में ८.१.२३ अपवाद)।',
    anuvritti_from=("8.1.17", "8.1.18", "8.1.20"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
