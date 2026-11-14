"""
8.4.62  झयो होऽन्यतरस्याम्  —  VIBHASHA

Padaccheda: झयः । हः । अन्यतरस्याम्

Sources consulted:
- ashtadhyayi.com data.txt row i=84062 (samagra: झयः हः पूर्वस्य सवर्णः अन्यतरस्याम्; पूर्वस्य ← 8.4.61, सवर्णः ← 8.4.58)
- Kāśikā: "झय उत्तरस्य हकारस्य पूर्वसवर्णादेशो भवत्यन्यतरस्याम्। वाग्घसति, वाग् हसति। … अग्निचिद्धसति …
  त्रिष्टुब्भसति, त्रिष्टुब् हसति।"
  pratyudāharaṇa: "झय इति किम्? प्राङ् हसति। भवान् हसति॥"
- SK: "घोषवतो नादवतो महाप्राणस्य संवृतकण्ठस्य हस्य तादृशो वर्गचतुर्थं एवादेशः । वाग्घरिः । वाग्हरिः ॥"
- Cross-validation: LK cases tests/fixtures/lk_cases/a8.json (8.4.62; brain ruling R-014: both readings are correct).

A ह that stands right after a jhay (a non-nasal stop) on the saṃhitā tape is replaced, optionally, by the savarṇa of that stop
which is, like ह, voiced and aspirated: the fourth of its varga (sthāne'ntaratamaḥ, SK above). The stop has already gone through
8.2.39 jaśtva at the pada end (वाक् → वाग्), so वाग् + हसति gives वाग्घसति, or वाग्हसति when the option is declined.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_FOURTH = {**dict.fromkeys("kKgG", "G"), **dict.fromkeys("cCjJ", "J"), **dict.fromkeys("wWqQ", "Q"),
           **dict.fromkeys("tTdD", "D"), **dict.fromkeys("pPbB", "B")}       # jhay → the varga's ghoṣa mahāprāṇa


def _site(state: State):
    """(term, index, substitute) for the first ह after a jhay on the flat tape."""
    if not state.tripadi_zone:
        return None
    flat = [(t, i, v.slp1) for t in state.terms for i, v in enumerate(t.varnas)]
    for (_, _, a), (t, i, b) in zip(flat, flat[1:]):
        if a in _FOURTH and b == "h":
            return t, i, _FOURTH[a]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, i, sub = _site(state)
    t.varnas[i] = mk(sub)
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.62",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    text_slp1             = 'Jayo honyatarasyAm',
    text_dev              = 'झयो होऽन्यतरस्याम्',
    samagra_slp1          = "JayaH haH pUrvasya savarRaH anyatarasyAm",
    samagra_dev           = "झयः हः पूर्वस्य सवर्णः अन्यतरस्याम्",
    padaccheda_dev        = "झयः । हः । अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.4.62) झयः परस्य हकारस्य पूर्वसवर्णो वा — वाग्घसति, वाग् हसति।",
    anuvritti_from        = ('8.4.58', '8.4.61'),
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
