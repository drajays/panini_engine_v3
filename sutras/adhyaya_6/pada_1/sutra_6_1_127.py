"""
6.1.127  इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च  —  VIBHASHA

पदान्त इक् (i u ṛ ḷ + dīrgha) followed by an asavarṇa ac: in Śākalya's view the
ik becomes hrasva *and* stays unsandhied (prakṛtibhāva, anuvṛtti of 6.1.125
``प्रकृत्या``).  The other reading is the ordinary 6.1.77 yaṇ:

    दधि + अत्र  →  दधि अत्र (Śākalya)   |   दध्यत्र
    मधु + अत्र  →  मधु अत्र              |   मध्वत्र

Optional (vibhāṣā): the default reading leaves the rule unapplied so 6.1.77
yields the yaṇ form; ``engine.vikalpa.choose({"6.1.127": True})`` /
``explore`` yields the other.  Padānta = left Term carries the ``pada`` tag.
Prakṛtibhāva is realised exactly as for pragṛhya (``PRAGHYA_TERM_TAG``), so
6.1.77 / 6.1.78 / 6.1.101 already skip the boundary.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.savarna import is_savarna
from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

_HRASVA = {"i": "i", "I": "i", "u": "u", "U": "u", "f": "f", "F": "f", "x": "x", "X": "x"}
_AC = frozenset("aAiIuUfFxXeEoO")
META = "prakritibhava_6_1_127"


def _find(state: State):
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for i, j in zip(live, live[1:]):
        left, right = state.terms[i], state.terms[j]
        if "pada" not in left.tags or left.meta.get(META) or PRAGHYA_TERM_TAG in left.tags:
            continue
        a, b = left.varnas[-1].slp1, right.varnas[0].slp1
        if a in _HRASVA and b in _AC and not is_savarna(a, b):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    left = state.terms[i]
    old = left.varnas[-1].slp1
    left.varnas[-1] = mk(_HRASVA[old])
    left.tags.add(PRAGHYA_TERM_TAG)   # prakṛtibhāva (6.1.125 anuvṛtti)
    left.meta[META] = True
    state.meta["__why_now_dev__"] = (
        f"पदान्त-इकः ({old}) असवर्णे अचि परे शाकल्य-मतेन ह्रस्वः ({_HRASVA[old]}) प्रकृतिभावश्च; "
        "पक्षे ६.१.७७ यण्। (६.१.१२७)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.127",
    sutra_type=SutraType.VIBHASHA,
    text_slp1='ikosavarRe SAkalyasya hrasvaSca',
    text_dev='इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च',
    padaccheda_dev="इकः असवर्णे शाकल्यस्य ह्रस्वः च",
    why_dev="पदान्तस्य इकः असवर्णे अचि परे शाकल्य-मतेन ह्रस्वः प्रकृतिभावश्च (विकल्पेन)।",
    anuvritti_from=("6.1.125",),
    vibhasha_default=False,
    vibhasha_scope=cond,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
