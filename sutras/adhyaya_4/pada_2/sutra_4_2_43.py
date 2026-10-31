"""
4.2.43  ग्रामजनबन्धुसहायेभ्यः तल्  —  VIDHI

Padaccheda: ग्राम-जन-बन्धु-सहायेभ्यः तल्

ग्रामजनबन्धुसहायेभ्यः तल् (4.2.43)
Pāṭha: ashtadhyayi.com data.txt row i=42043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita
from engine.vartika import Vartika


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "samUha"), stems=frozenset({"grAma","jana","banDu","sahAya"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "tal")


# Art. 25 / AMENDMENT 29: the vārttikas of 4.2.43 live here. Bhāṣya 4.2.43 (5368) पर्श्वाः सण् … एवं तर्हि णस् वक्तव्यः: पर्शूनां समूहः पार्श्वम्.
def _parsu_cond(state: State) -> bool:
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "samUha"), stems=frozenset({"parSu"})) is not None


def _parsu_act(state: State) -> State:
    return attach_taddhita(state, "Ras")


VARTIKAS = (
    Vartika(id="4.2.43.v4", source="Kātyāyana vā. 4 on 4.2.43 (Bhāṣya 5368, with the ṇas ruling)", tier="T1", relation="extension",
            text_dev="पर्श्वा णस् वक्तव्यः", cond=_parsu_cond, act=_parsu_act),
)

SUTRA = SutraRecord(
    sutra_id              = "4.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmajanabanDusahAyeByaH tal",
    text_dev              = "ग्रामजनबन्धुसहायेभ्यः तल्",
    samagra_slp1          = "tasya samUhaH iti grAma-jana-banDu-sahAyeByaH tal",
    samagra_dev           = "तस्य समूहः (इति) ग्राम-जन-बन्धु-सहायेभ्यः तल्",
    padaccheda_dev        = "ग्राम-जन-बन्धु-सहायेभ्यः तल्",
    why_dev               = "(सूत्रम् 4.2.43) ग्रामजनबन्धुसहायेभ्यः तल्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.37',),
    vartikas              = VARTIKAS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
