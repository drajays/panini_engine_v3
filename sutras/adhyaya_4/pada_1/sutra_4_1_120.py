"""
4.1.120  स्त्रीभ्यो ढक्  —  VIDHI

Padaccheda: स्त्रीभ्यः ढक्

स्त्रीभ्यो ढक् (4.1.120)
Pāṭha: ashtadhyayi.com data.txt row i=41120 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita  # noqa: F401


def _site(state: State):
    return taddhita_site(state, "apatya", final=lambda f: f[-1:] in ("A", "I") and "strIliNga" in state.terms[-1].tags)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Qak")


SUTRA = SutraRecord(
    sutra_id              = "4.1.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "strIByo Qak",
    text_dev              = "स्त्रीभ्यो ढक्",
    samagra_slp1          = "tasya apatyam iti strIByaH Qak",
    samagra_dev           = "'तस्य अपत्यम्' (इति) स्त्रीभ्यः ढक्",
    padaccheda_dev        = "स्त्रीभ्यः ढक्",
    why_dev               = "(सूत्रम् 4.1.120) स्त्रीभ्यो ढक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.1.95'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
