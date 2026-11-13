"""
4.1.49  इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणामानुक्  —  VIDHI

Padaccheda: इन्द्र-वरुण-भव-शर्व-रुद्र-मृड-हिम-अरण्य-यव-यवन-मातुल-आचार्याणाम् आनुक्

इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणामानुक् (4.1.49)
Pāṭha: ashtadhyayi.com data.txt row i=41049 (Art. 14).
Kāśikā: इन्द्रादिभ्यः प्रातिपदिकेभ्यः स्त्रियां ङीष् प्रत्ययो भवति, आनुक् चागमः।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_4.pada_1.sutra_4_1_6 import strI_site, append_stri

# the sūtra's own list; a stem that needs a sense carries that lexical fact (Kāśikā: himāraṇyayor mahattve, yavād doṣe, yavanāl lipyām)
_PLAIN = ("indra", "varuRa", "Bava", "Sarva", "rudra", "mfqa", "mAtula", "AcArya")
_SENSE = {"hima": "lex:mahattva", "araRya": "lex:mahattva", "yava": "lex:doza", "yavana": "lex:lipi"}


def _wanted(t) -> bool:
    """anupasarjana member of the list, the woman by her union with the man (puṃyogāt): lex:puMyoga."""
    f = "".join(v.slp1 for v in t.varnas)
    return "upasarjana" not in t.tags and "lex:puMyoga" in t.tags and (f in _PLAIN or _SENSE.get(f) in t.tags)


def _site(state: State):
    return strI_site(state, _wanted)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    t.varnas += [mk("A"), mk("n")]            # Ānuk: the k and u are it (1.3.3, 1.3.9); a kit āgama stands at the end (1.1.46)
    t.meta["Anuk_agama"] = True
    return append_stri(state, "NIz")


SUTRA = SutraRecord(
    sutra_id              = "4.1.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "indravaruRaBavaSarvarudramfqahimAraRyayavayavanamAtulAcAryARAmAnuk",
    text_dev              = "इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणामानुक्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt indra-varuRa-Bava-Sarva-rudra-mfqa-hima-araRya-yava-yavana-mAtula-AcAryARAm Anuk NIz pum-yogAt",
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् इन्द्र-वरुण-भव-शर्व-रुद्र-मृड-हिम-अरण्य-यव-यवन-मातुल-आचार्याणाम् आनुक् ङीष् पुम्-योगात्",
    padaccheda_dev        = "इन्द्र-वरुण-भव-शर्व-रुद्र-मृड-हिम-अरण्य-यव-यवन-मातुल-आचार्याणाम् आनुक्",
    why_dev               = "(सूत्रम् 4.1.49) इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणामानुक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ("4.1.4",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
