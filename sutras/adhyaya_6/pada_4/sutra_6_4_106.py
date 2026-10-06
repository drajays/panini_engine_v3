"""
6.4.106  उतश्च प्रत्ययादसंयोगपूर्वात्  —  VIDHI

Padaccheda: उतः च प्रत्ययात् अ-संयोग-पूर्वात्

उतश्च प्रत्ययादसंयोगपूर्वात् (6.4.106)
Pāṭha: ashtadhyayi.com data.txt row i=64106 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_106_utaSca_106"


_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


def _find(state: State) -> int | None:
    """उतश्च प्रत्ययादसंयोगपूर्वात् (हेः, 6.4.105): हि drops after the u that ends a
    pratyaya (the vikaraṇa u / nu), unless a saṃyoga precedes that u —
    सुनु, तनु, कुरु; but आप्नुहि."""
    for i, t in enumerate(state.terms):
        if "tin_adesha_3_4_78" not in t.tags or "".join(v.slp1 for v in t.varnas) != "hi":
            continue
        prev_i = next((k for k in range(i - 1, -1, -1) if state.terms[k].varnas), None)
        if prev_i is None:
            return None
        prev = state.terms[prev_i]
        if "vikarana" not in prev.tags or prev.varnas[-1].slp1 != "u":
            return None
        flat = [v.slp1 for u in state.terms[:prev_i + 1] for v in u.varnas]
        if len(flat) >= 3 and flat[-2] in _HAL and flat[-3] in _HAL:
            return None                               # asaṃyogapūrvāt
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].varnas = []                          # लोपः
    state.terms[i].meta["6_4_106_hi_lopa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.106",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "utaSca pratyayAdasaMyogapUrvAt",
    text_dev              = "उतश्च प्रत्ययादसंयोगपूर्वात्",
    samagra_slp1          = "asaMyogapUrvAt utaH pratyayAt heH luk",
    samagra_dev           = "असंयोगपूर्वात् उतः प्रत्ययात् हेः लुक्",
    padaccheda_dev        = "उतः च प्रत्ययात् अ-संयोग-पूर्वात्",
    why_dev               = "(सूत्रम् 6.4.106) उतश्च प्रत्ययादसंयोगपूर्वात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
