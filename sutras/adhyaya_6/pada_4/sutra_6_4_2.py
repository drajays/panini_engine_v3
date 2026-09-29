"""
6.4.2  हलः  —  VIDHI

Padaccheda: हलः

हलः (6.4.2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_DIRGHA = {"i": "I", "u": "U", "f": "F", "x": "X"}
_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


def _find(state: State):
    """हलः (अङ्गस्य, सम्प्रसारणस्य, दीर्घः 6.3.139): an aṅga-final samprasāraṇa
    after a hal of the same aṅga is lengthened — हु → हू (हूयते), जि → जी (जीयते)."""
    for t in state.terms:
        at = t.meta.get("samprasarana_at")
        if at is None or t.meta.get("6_4_2_done"):
            continue
        if at == len(t.varnas) - 1 and at > 0 and t.varnas[at - 1].slp1 in _HAL \
                and t.varnas[at].slp1 in _DIRGHA:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    t.varnas[-1] = mk(_DIRGHA[t.varnas[-1].slp1])
    t.meta["6_4_2_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.2",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "halaH",
    text_dev              = "हलः",
    padaccheda_dev        = "हलः",
    why_dev               = "हलः परस्य अङ्गान्त-सम्प्रसारणस्य दीर्घः (हूयते, जीयते)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
