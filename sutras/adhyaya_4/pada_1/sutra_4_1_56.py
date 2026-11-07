"""
4.1.56  न क्रोडादिबह्वचः  —  VIDHI

Padaccheda: न क्रोडा-आदि-बहु-अचः

न क्रोडादिबह्वचः (4.1.56)
Pāṭha: ashtadhyayi.com data.txt row i=41056 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, gana
from engine.declension import n_vowels
from engine.gates import adhikara_in_effect
from engine.state import State

_BLOCKS = ("4.1.54", "4.1.55")      # ṅīṣ after a svāṅga (svāṅgāc copasarjanād …, nāsikodara …)


def _wanted(t) -> bool:
    """A member of the krodādi gaṇa, or bahvac: three or more vowels.
    SHORTCUT S139: bahvac is read as 'three or more ac' (the Kāśikā line is not in the repo); the svāṅga / upasarjana test stays with 4.1.54 / 4.1.55."""
    name = t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)
    return gana.in_gana("kroqAdiH", name) or n_vowels(t) >= 3


def _site(state: State):
    if not adhikara_in_effect("4.1.56", state, "4.1.1"):
        return None
    return next((t for t in state.terms
                 if t.kind == "prakriti" and "prātipadika" in t.tags and "strīliṅga" in t.tags and _wanted(t)), None)


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.56",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na kroqAdibahvacaH",
    text_dev              = "न क्रोडादिबह्वचः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt na kroqa-Adi-bahvacaH NIz sva-aNgAt ca upasarjanAt a-saMyoga-upaDAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् न क्रोड-आदि-बह्वचः ङीष् स्व-अङ्गात् च उपसर्जनात् अ-संयोग-उपधात्",
    padaccheda_dev        = "न क्रोडा-आदि-बहु-अचः",
    why_dev               = "न क्रोडादिबह्वचः — क्रोडादेः बह्वचश्च स्वाङ्गात् ङीष् (४.१.५४) न (कल्याणक्रोडा)।",
    anuvritti_from        = ('4.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
