"""
8.1.23  त्वामौ द्वितीयायाः  —  VIDHI

द्वितीया-एकवचन युष्मद्→त्वा, अस्मद्→मा; ८.१.२२ का अपवाद (declared ``apavada_of``)।

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 8.1.23 
  Source #2 — Kāśikā 8.1.23: ग्रामो वां स्वम् / ग्रामो वः स्वम् / ग्रामस्ते स्वम् / ग्रामस्त्वा पश्यति (as the sūtra)
  Reference — ashtadhyayi.com sūtra-prayoga list (Kirātārjunīya, Bhaṭṭikāvya … attestations)

Engine: ``cond`` reads Term tags only — the pada's saṃjñā-names ``vib_*`` / ``vac_*`` (4.1.2), the
pronoun's lexical identity, and the adhikāras 8.1.17 / 8.1.18 (*padāt* … *apādādau*). The ādeśa
replaces the whole pada (sarvādeśa, 1.1.55) and is anudātta (accent is not modelled).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from sutras.adhyaya_8.pada_1.enclitic_common import STHA_VIBHAKTI, replace, target
from engine.state import State

_ADESHA = {'yuzmad': 'tvA', 'asmad': 'mA'}


def _site(state: State):
    i = target(state, "8.1.23")
    if i is None:
        return None
    t = state.terms[i]
    return i if ("vib_dvitiya" in t.tags and "vac_eka" in t.tags) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    return state if i is None else replace(state, i, "8.1.23", _ADESHA)


SUTRA = SutraRecord(
    sutra_id="8.1.23",
    sutra_type=SutraType.VIDHI,
    text_slp1='tvAmO dvitIyAyAH',
    text_dev='त्वामौ द्वितीयायाः',
    padaccheda_dev='त्व-मौ द्वितीयायाः',
    why_dev='द्वितीयान्त एकवचन युष्मद्-अस्मद् पद → त्वा/मा (पदात् परम्, अपादादौ)।',
    anuvritti_from=("8.1.17", "8.1.18", "8.1.20"),
    apavada_of=("8.1.22",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
