"""
3.1.97  अचो यत्  —  ADHIKARA (pāṭha: कृत्यसंज्ञाधिकारः) that is also the yat vidhi (Kāśikā: अजन्ताद् धातोर्यत् प्रत्ययो भवति)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=31097):** *kṛtya-saṃjñādhikāra* — scope
for naming / *kṛtya* readings with **yat** after a vowel-final base, through
**3.1.132** (type: कृत्यसंज्ञाधिकारः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open


def _yat_site(state: State) -> bool:
    """अचो यत् — an ac-final dhātu takes yat in the kṛtya sense (geyam, peyam, ceyam, jeyam)."""
    return kftya_open(state, "3.1.97") and bool(state.terms[-1].varnas) and state.terms[-1].varnas[-1].slp1 in "aAiIuUfFxXeEoO"   # ac, long vowels included


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.1.97" for e in state.adhikara_stack) or _yat_site(state)


def act(state: State) -> State:
    # the pāṭha marks the kṛtyasaṃjñādhikāra (through 3.1.132); the Kāśikā reads the words as the yat vidhi — both (also_vidhi)
    if not any(e.get("id") == "3.1.97" for e in state.adhikara_stack):
        state.adhikara_stack.append({
            "id"        : "3.1.97",
            "scope_end" : "3.1.132",
            "text_dev"  : "अचो यत्",
        })
    if _yat_site(state):
        return kftya_attach(state, "3.1.97", "yat")
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.97",
    sutra_type     = SutraType.ADHIKARA,
    also_vidhi     = True,
    text_slp1      = "aco yat",
    text_dev       = "अचो यत्",
    samagra_slp1   = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH acaH yat kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः अचः यत् कृत्",
    padaccheda_dev = "अचः यत्",
    why_dev        = "कृत्य-संज्ञाधिकारः — ३.१.९७ तः ३.१.१३२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.97", "3.1.132"),
)

register_sutra(SUTRA)
