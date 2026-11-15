"""
4.1.54  स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्  —  VIDHI

Padaccheda: स्वाङ्गात् च उपसर्जनात् अ-संयोग-उपधात्

स्वाङ्गाच्चोपसर्जनादसंयोगोपधात् (4.1.54)
Pāṭha: ashtadhyayi.com data.txt row i=41054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

_VOWELS = frozenset("aAiIuUfFxXeEoO")


def _svanga_upasarjana(t) -> bool:
    """The lexical fact `lex:svANga` (S14: the Lexicon does not yet say which stems are parts of the body) and the saṃjñā upasarjana."""
    return bool(t.varnas) and "lex:svANga" in t.tags and "upasarjana" in t.tags


def _wanted(t) -> bool:
    """svāṅga + upasarjana + asaṃyogopadha: the upadhā (the varṇa before the last) is not part of a conjunct (Kāśikā: bahuyavā, aśikhā, sugulphā, supārśvā stay with ṭāp)."""
    v = [x.slp1 for x in t.varnas]
    if not _svanga_upasarjana(t) or len(v) < 3 or v[-1] not in _VOWELS:
        return False
    return not (v[-2] not in _VOWELS and v[-3] not in _VOWELS)


def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIz") if _site(state) is not None else state

SUTRA = SutraRecord(
    sutra_id              = "4.1.54",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "svANgAccopasarjanAdasaMyogopaDAt",
    text_dev              = "स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt sva-aNgAt ca upasarjanAt a-saMyoga-upaDAt NIz vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् स्व-अङ्गात् च उपसर्जनात् अ-संयोग-उपधात् ङीष् वा",
    padaccheda_dev        = "स्वाङ्गात् च उपसर्जनात् अ-संयोग-उपधात्",
    why_dev               = "(सूत्रम् 4.1.54) स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
