"""
4.1.10  न षट्स्वस्रादिभ्यः  —  VIDHI

Padaccheda: न षट्-स्वस्रादिभ्यः

न षट्स्वस्रादिभ्यः (4.1.10)
Pāṭha: ashtadhyayi.com data.txt row i=41010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, gana
from engine.gates import adhikara_in_effect
from engine.state import State

_BLOCKS = tuple(f"4.1.{i}" for i in range(4, 76) if i != 10)      # every strī pratyaya the pāda teaches (ṭāp, ṅīp, ṅīṣ, ūṅ, ṅīn …)


def _wanted(t) -> bool:
    """A word the saṃjñā ṣaṭ (1.1.24: the tag ``zat_samjna``) names, or a member of the svasrādi gaṇa."""
    name = t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)
    return "zat_samjna" in t.tags or gana.in_gana("svasrAdiH", name)


def _site(state: State):
    if not adhikara_in_effect("4.1.10", state, "4.1.1"):
        return None
    return next((t for t in state.terms
                 if t.kind == "prakriti" and "prātipadika" in t.tags and "strīliṅga" in t.tags and _wanted(t)), None)


def cond(state: State) -> bool:
    return _site(state) is not None and not set(_BLOCKS) <= state.blocked_sutras


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.10",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na zawsvasrAdiByaH",
    text_dev              = "न षट्स्वस्रादिभ्यः",
    samagra_slp1          = "zaw-svasrAdiByaH NyApprAtipadikAt striyAm NIp pratyayaH na",
    samagra_dev           = "षट्-स्वस्रादिभ्यः ङ्याप्प्रातिपदिकात् स्त्रियाम् ङीप् प्रत्ययः न",
    padaccheda_dev        = "न षट्-स्वस्रादिभ्यः",
    why_dev               = "न षट्स्वस्रादिभ्यः — षट्-स्वस्रादिभ्यः (स्वसा, तिस्रः, चतस्रः, ननान्दा, दुहिता, याता, माता) ङीप्टापौ न।",
    anuvritti_from        = ('4.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
