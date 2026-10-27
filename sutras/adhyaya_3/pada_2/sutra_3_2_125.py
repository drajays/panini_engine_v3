"""
3.2.125  सम्बोधने च  —  VIDHI

Padaccheda: सम्बोधने च

krt-suffix rule: सम्बोधने च (125)
Pāṭha: ashtadhyayi.com data.txt row i=32125 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.vivaksha import vivaksita
from sutras.adhyaya_3.pada_2.sutra_3_2_124 import participle_site, attach_participle, _atmanepada, SAnan_DHATUS  # noqa: F401


def _site(state: State):
    return participle_site(state, vivaksita(state, "kala", "vartamAna"), vivaksita(state, "sambodhana", "sambodhana"))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_participle(state, "SAnac" if _atmanepada(state, ubhaya_pick=True, sid="3.2.125") else "Satf~")


SUTRA = SutraRecord(
    sutra_id              = "3.2.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samboDane ca",
    text_dev              = "सम्बोधने च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne samboDane ca kft lawaH SatfSAnacO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने सम्बोधने च कृत् लटः शतृशानचौ",
    padaccheda_dev        = "सम्बोधने च",
    why_dev               = "धातोः कृत्-प्रत्ययः [सम्बोधने च] विहितः (३.२.125)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
