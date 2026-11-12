"""
7.1.60  मस्जिनशोर्झलि  —  VIDHI

Padaccheda: मस्जि-नशोः झलि

Kāśikā 7.1.60: masj, naś take num before a jhal-initial pratyaya — maṅktā, maṅktum, naṃṣṭā, naṃṣṭum, naṃṣṭavyam (not majjanam,
nāśanam: the next letter must be jhal). Place: masj — before the last letter (vārttika to 1.1.47 'masjer antyāt pūrvam num': so the
anusvāra-lopa of anuṣaṅga is served, magnaḥ); naś — after the last vowel (the ordinary mid-aco'ntyāt-paraḥ, which here is also
before the last letter).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk, HAL

_JHAL = HAL - frozenset("yrlvhNYRnmM")          # jhal: every consonant but the semivowels, h and the nasals
_ROOTS = frozenset({"masj", "naS"})


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("7_1_60_num_done"):
            continue
        if "".join(v.slp1 for v in t.varnas) not in _ROOTS:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and nxt.varnas[0].slp1 in _JHAL:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.varnas.insert(len(t.varnas) - 1, mk("n", "num_agama"))       # before the last letter: mas-n-j, na-n-ś
    t.meta["7_1_60_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.60",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "masjinaSorJali",
    text_dev              = "मस्जिनशोर्झलि",
    samagra_slp1          = "masji-naSoH num Jali",
    samagra_dev           = "मस्जि-नशोः नुम् झलि",
    padaccheda_dev        = "मस्जि-नशोः झलि",
    why_dev               = "मस्जेः नशेश्च झलादौ प्रत्यये नुम् (मङ्क्ता, नंष्टा)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
