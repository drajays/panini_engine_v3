"""
4.1.55  नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च  —  VIDHI

Padaccheda: नासिका-उदर-ओष्ठ-जङ्‍घा-दन्त-कर्ण-शृङ्गात् च

नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च (4.1.55)
Pāṭha: ashtadhyayi.com data.txt row i=41055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

_VOWELS = frozenset("aAiIuUfFxXeEoO")


def _svanga_upasarjana(t) -> bool:
    """The lexical fact `lex:svANga` (S14: the Lexicon does not yet say which stems are parts of the body) and the saṃjñā upasarjana."""
    return bool(t.varnas) and "lex:svANga" in t.tags and "upasarjana" in t.tags


_WORDS = ("nAsika", "udara", "ozWa", "jaNGa", "danta", "karRa", "SfNga")      # the sūtra's own list; the conjunct and bahvac prohibitions do not apply (Kāśikā: vacanam)


def _wanted(t) -> bool:
    return _svanga_upasarjana(t) and "".join(x.slp1 for x in t.varnas).endswith(_WORDS)


def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return append_stri(state, "NIz") if _site(state) is not None else state

SUTRA = SutraRecord(
    sutra_id              = "4.1.55",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "nAsikodarOzWajaNGAdantakarRaSfNgAcca",
    text_dev              = "नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt nAsika-udara-ozWa-jaNGA-danta-karRa-SfNgAt ca NIz vA sva-aNgAt upasarjanAt a-saMyoga-upaDAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् नासिक-उदर-ओष्ठ-जङ्घा-दन्त-कर्ण-शृङ्गात् च ङीष् वा स्व-अङ्गात् उपसर्जनात् अ-संयोग-उपधात्",
    padaccheda_dev        = "नासिका-उदर-ओष्ठ-जङ्‍घा-दन्त-कर्ण-शृङ्गात् च",
    why_dev               = "(सूत्रम् 4.1.55) नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
