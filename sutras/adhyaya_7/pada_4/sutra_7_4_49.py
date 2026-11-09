"""
7.4.49  सः स्यार्द्धधातुके  —  VIDHI

Padaccheda: सः सि आर्द्धधातुके

सः स्यार्द्धधातुके (7.4.49)
Pāṭha: ashtadhyayi.com data.txt row i=74049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    """A dhātu ending in s before an ārdhadhātuka that begins with s: vas + syati → vatsyati, ghas + sic → aghatsAtAm (Kāśikā)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" in t.tags and "abhyasa" not in t.tags and t.varnas and t.varnas[-1].slp1 == "s":
            nxt = state.terms[i + 1]
            if nxt.varnas and nxt.varnas[0].slp1 == "s" and "ardhadhatuka" in nxt.tags:
                return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    _find(state).varnas[-1] = mk("t")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.49",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "saH syArdDaDAtuke",
    text_dev              = "सः स्यार्द्धधातुके",
    samagra_slp1          = "saH aNgasya ArDaDAtuke si taH",
    samagra_dev           = "सः अङ्गस्य आर्धधातुके सि तः",
    padaccheda_dev        = "सः सि आर्द्धधातुके",
    why_dev               = "(सूत्रम् 7.4.49) सः स्यार्द्धधातुके।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
