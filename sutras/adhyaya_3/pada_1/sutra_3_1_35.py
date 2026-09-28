"""
3.1.35  कास्प्रत्ययादाममन्त्रे लिटि  —  VIDHI

Padaccheda: कास्-प्रत्ययात् आम् अमन्त्रे लिटि

Krt suffix rule from dhatu: कास्प्रत्ययादाममन्त्रे लिटि (35)
"""
from __future__ import annotations
from phonology.varna import parse_slp1_upadesha_sequence
from engine.state import Term

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_35_kAspratyayAd_35"


def _site(state: State) -> int | None:
    """कास्प्रत्ययादाममन्त्रे लिटि: after कास् or a pratyayānta dhātu (ṇic, san, …,
    3.1.32), liṭ takes ām — returns the index of the liṭ term."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        pratyayanta = t.meta.get("sanadi_pratyayanta") or \
            (t.meta.get("upadesha_slp1") or "").strip() in {"kAsf~", "kAs"}
        nxt = state.terms[i + 1]
        if pratyayanta and (nxt.meta.get("upadesha_slp1") or "").strip() == "liT":
            return i + 1
        return None
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    li = _site(state)
    if li is None:
        return state
    state.terms.insert(li, Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("Am")),
                                tags={"pratyaya", "upadesha"}, meta={"upadesha_slp1": "Am"}))
    return state

SUTRA = SutraRecord(
    sutra_id              = "3.1.35",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "kAspratyayAdAmamantre liwi",
    text_dev              = "कास्प्रत्ययादाममन्त्रे लिटि",
    padaccheda_dev        = "कास्-प्रत्ययात् आम् अमन्त्रे लिटि",
    why_dev               = "धातोः [कास्प्रत्ययादाममन्त्रे लिटि]-प्रत्ययः विहितः (३.१.35)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
