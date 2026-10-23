"""
6.1.6  जक्षित्यादयः षट्  —  VIDHI

Padaccheda: जक्ष् (अविभक्तिकनिर्देशः) इति-आदयः षट्

जक्षित्यादयः षट् (6.1.6)
Pāṭha: ashtadhyayi.com data.txt row i=61006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# जक्षित्यादिः is the dhātupāṭha's antargaṇa (7 roots: jakṣ + the following ṣaṭ, Kāśikā/SK); it is read
# from the dhātu Term (meta["antarganas"], lexical like the gaṇa), as 1.2.1 reads कुटादिः.
_ANTARGANA = "जक्षित्यादिः"


def _site(state: State):
    for t in state.terms:
        if "dhatu" in t.tags and "abhyasta" not in t.tags and _ANTARGANA in (t.meta.get("antarganas") or ()):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).tags.add("abhyasta")      # abhyasta saṃjñā without reduplication; 7.1.4 reads it (jAgrati, not *jAgfanti)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jakzityAdayaH zaw",
    text_dev              = "जक्षित्यादयः षट्",
    samagra_slp1          = "jakzityAdayaH zaw aByastam",
    samagra_dev           = "जक्षित्यादयः षट् अभ्यस्तम्",
    padaccheda_dev        = "जक्ष् (अविभक्तिकनिर्देशः) इति-आदयः षट्",
    why_dev               = "(सूत्रम् 6.1.6) जक्षित्यादयः षट्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
