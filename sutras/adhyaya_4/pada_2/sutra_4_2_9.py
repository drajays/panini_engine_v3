"""
4.2.9  वामदेवाड्ड्यड्ड्यौ  —  VIDHI

Padaccheda: वामदेवात् ड्यत्-ड्यौ

वामदेवाड्ड्यड्ड्यौ (4.2.9)
Pāṭha: ashtadhyayi.com data.txt row i=42009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "dfzwa"), stems=frozenset({"vAmadeva"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, 'qyat' if policy_pick(state, "4.2.9", 2) == 0 else 'qya')


SUTRA = SutraRecord(
    sutra_id              = "4.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAmadevAqqyaqqyO",
    text_dev              = "वामदेवाड्ड्यड्ड्यौ",
    samagra_slp1          = "tena dfzwaM sAma iti vAmadevAt qyat-qyO",
    samagra_dev           = "'तेन दृष्टं साम' (इति)  वामदेवात् ड्यत्-ड्यौ",
    padaccheda_dev        = "वामदेवात् ड्यत्-ड्यौ",
    why_dev               = "(सूत्रम् 4.2.9) वामदेवाड्ड्यड्ड्यौ।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.7',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
