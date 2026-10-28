"""
1.2.53  तदशिष्यं संज्ञाप्रमाणत्वात्  —  VIDHI

*Padaccheda:* **तत्** / **अशिष्यम्** / **संज्ञा-प्रमाणत्वात्**

"That [yuktavadbhāva of 1.2.51] is not to be taught, because a name (saṃjñā) has its usage as authority": the liṅga and vacana of a name whose pratyaya went by
lup (varaṇāḥ, pañcālāḥ …) are what the language gives it, not what 1.2.51 would copy from the prakṛti.

Engine: on the site of 1.2.51 (a stem whose pratyaya lup took away), under the vivakṣā ``arthaViSeSa=saMjYA``, it stands before 1.2.51 as its exception
(``apavada_of``) and leaves the stem the empty ``yuktavad_linga:`` mark: 1.2.51 then finds the stem spoken for and forces no liṅga.
1.2.54 (lupyogāprakhyānāt) is the reason given for this sūtra and does nothing of its own.
Pāṭha: ashtadhyayi.com data.txt row i=12053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_1.pada_2.sutra_1_2_51 import lup_stem, _TAG


def cond(state: State) -> bool:
    return lup_stem(state) is not None and vivaksita(state, "arthaViSeSa", "saMjYA")


def act(state: State) -> State:
    lup_stem(state).tags.add(_TAG)
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.53",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "tadaSizyaM saMjYApramARatvAt",
    text_dev                = "तदशिष्यं संज्ञाप्रमाणत्वात्",
    samagra_slp1            = "tat aSizyam saMjYA-pramARatvAt",
    samagra_dev             = "तत् अ-शिष्यम् संज्ञा-प्रमाणत्वात्",
    padaccheda_dev          = "तत् / अशिष्यम् / संज्ञा-प्रमाणत्वात्",
    why_dev                 = "संज्ञायां लुपि लिङ्गवचनं लोकप्रमाणम्, न युक्तवद्भावशिष्यम्।",
    anuvritti_from          = ("1.2.51",),
    apavada_of              = ("1.2.51",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
