"""
7.1.22  षड्भ्यो लुक्  —  VIDHI

Padaccheda: षड्‍भ्यः लुक्

षड्भ्यो लुक् (7.1.22)
Pāṭha: ashtadhyayi.com data.txt row i=71022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from engine.state import State


def _site(state: State):
    """A ṣaṭ-saṃjñaka aṅga (the tag 1.1.24 puts on ṣaṣ, pañcan, saptan, aṣṭan, navan, daśan) before jas / śas."""
    hit = anga_and_sup(state)      # no 6.4.1 gate: 6.4.8 is not gated either, and the luk / ādeśa must meet it as a rival (vipratiṣedha, para)
    if hit is None:
        return None
    anga, sup = hit
    if "zat_samjna" not in anga.tags or (sup.meta.get("upadesha_slp1") or "").strip() not in ("jas", "Sas") or LUK_LOPA_GHOST_TAG in sup.tags:
        return None
    return sup


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    sup = _site(state)
    sup.varnas.clear()                 # luk (1.1.61): the sup is gone and nothing it conditioned follows (1.1.62 does not apply to a lumata luk)
    sup.tags.add(LUK_LOPA_GHOST_TAG)
    state.meta["7_1_22_luk"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zaqByo luk",
    text_dev              = "षड्भ्यो लुक्",
    samagra_slp1          = "zaqByaH aNgAt jaS-SasoH luk",
    samagra_dev           = "षड्भ्यः अङ्गात् जश्-शसोः लुक्",
    padaccheda_dev        = "षड्‍भ्यः लुक्",
    why_dev               = "(सूत्रम् 7.1.22) षड्भ्यो लुक्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
