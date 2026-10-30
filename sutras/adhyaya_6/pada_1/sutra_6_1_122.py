"""
6.1.122  सर्वत्र विभाषा गोः  —  VIDHI

Padaccheda: सर्वत्र विभाषा गोः

सर्वत्र विभाषा गोः (6.1.122)
Pāṭha: ashtadhyayi.com data.txt row i=61122 (Art. 14).
Kāśikā 6.1.122: go agram, gogram (bhāṣāyām and chandasi); Laghukaumudī: goagram, go'agram; citragvagram is outside (not eṅanta).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

META = "prakritibhava_6_1_122"


def _find(state: State):
    live = _live(state)
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if "pada" not in left.tags or left.meta.get(META) or PRAGHYA_TERM_TAG in left.tags:
            continue
        flat = "".join(v.slp1 for v in left.varnas)
        if flat.endswith("go") and right.varnas[0].slp1 == "a":      # eṅanta go, then the short a (ati)
            return i
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    left = state.terms[i]
    left.tags.add(PRAGHYA_TERM_TAG)     # prakṛtibhāva, as for pragṛhya: 6.1.109 / 6.1.78 / 6.1.101 skip the boundary
    left.meta[META] = True
    state.meta["__why_now_dev__"] = "पदान्त-एङन्तस्य गोः अति परे प्रकृतिभावः विभाषा (६.१.१२२)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.122",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'sarvatra viBAzA goH',
    text_dev              = 'सर्वत्र विभाषा गोः',
    samagra_slp1          = "padAntAt goH eNaH ati sarvatra prakftyA viBAzA",
    samagra_dev           = "पदान्तात् गोः एङः अति सर्वत्र प्रकृत्या विभाषा",
    padaccheda_dev        = "सर्वत्र विभाषा गोः",
    why_dev               = "काशिका ६.१.१२२ — एङन्तस्य गोः पदान्तस्य अति परे प्रकृतिभावः विभाषा (गो अग्रम्, गोऽग्रम्)।",
    anuvritti_from        = ('6.1.1',),
    vibhasha_default=False,
    vibhasha_scope=_new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
