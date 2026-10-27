"""
3.2.126  लक्षणहेत्वोः क्रियायाः  —  VIDHI

Padaccheda: लक्षण-हेत्वोः क्रियायाः

krt-suffix rule: लक्षणहेत्वोः क्रियायाः (126)
Pāṭha: ashtadhyayi.com data.txt row i=32126 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import participle_site, attach_participle, _atmanepada, SAnan_DHATUS  # noqa: F401


def _site(state: State):
    return participle_site(state, vivaksita(state, "kala", "vartamAna"), vivaksita(state, "lakzaRahetu", "lakzaRa") or vivaksita(state, "lakzaRahetu", "hetu"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_participle(state, "SAnac" if _atmanepada(state, ubhaya_pick=True, sid="3.2.126") else "Satf~")


SUTRA = SutraRecord(
    sutra_id              = "3.2.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lakzaRahetvoH kriyAyAH",
    text_dev              = "लक्षणहेत्वोः क्रियायाः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne lakzaRahetvoH kriyAyAH kft lawaH SatfSAnacO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने लक्षणहेत्वोः क्रियायाः कृत् लटः शतृशानचौ",
    padaccheda_dev        = "लक्षण-हेत्वोः क्रियायाः",
    why_dev               = "धातोः कृत्-प्रत्ययः [लक्षणहेत्वोः क्रियायाः] विहितः (३.२.126)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
