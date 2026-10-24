"""
3.1.110  ऋदुपधाच्चाकॢपिचृतेः  —  VIDHI

Padaccheda: ऋत्-उपधात् च अ-कॢपि-चृतेः

Krt suffix rule from dhatu: ऋदुपधाच्चाकॢपिचृतेः (110)
Pāṭha: ashtadhyayi.com data.txt row i=31110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import kftya_attach, kftya_open, kftya_stem

def cond(state: State) -> bool:
    """ṛ-upadha dhātu → kyap (vṛtyam, vṛdhyam), except kḷp and cṛt; mṛj and vṛṣ wait for 3.1.113 / 3.1.120."""
    st = kftya_stem(state)
    return kftya_open(state, "3.1.110") and len(st) >= 2 and st[-2] == "f" and st[-1] not in "aAiIuUfFxXeEoO" and st not in ("kxp", "kfp", "cft", "mfj", "vfz")


def act(state: State) -> State:
    return kftya_attach(state, "3.1.110", "kyap")


SUTRA = SutraRecord(
    sutra_id              = "3.1.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fdupaDAccAkxpicfteH",
    text_dev              = "ऋदुपधाच्चाकॢपिचृतेः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH fdupaDAt ca akxpicfteH kft kyap",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः ऋदुपधात् च अकॢपिचृतेः कृत् क्यप्",
    padaccheda_dev        = "ऋत्-उपधात् च अ-कॢपि-चृतेः",
    why_dev               = "धातोः [ऋदुपधाच्चाकॢपिचृतेः]-प्रत्ययः विहितः (३.१.110)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    apavada_of            = ('3.1.97', '3.1.124'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
