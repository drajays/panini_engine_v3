"""
4.3.168  कंसीयपरशव्ययोर्यञञौ लुक् च  —  VIDHI

Padaccheda: कंसीय-परशव्ययोः यञ्-अञौ लुक् च

Sense: see the Kāśikā on this sūtra (`make brain S=4.3.168`); examples — kāṃsyaḥ, pārśavaḥ.
yañ after kaṃsīya (a cha-ending stem, 5.1.1), añ after paraśavya (a yat-ending stem, 5.1.2); the pratyaya that ended the stem (cha, yat) goes by luk in the same breath.
SHORTCUT S25: the stem is given whole (one Term), so the luk of its own pratyaya is done by taking from its end the letters that pratyaya made (cha → īya, yat → ya).
Pāṭha: ashtadhyayi.com data.txt row i=43168 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import attach_taddhita, taddhita_site
from engine.vivaksha import vivaksita

_PAIR = {"kaMsIya": ("yaY", "Ca", 3), "parSavya": ("aY", "yat", 2)}      # stem: (pratyaya, the pratyaya it ends in, its letters)


def _site(state: State):
    t = taddhita_site(state, "vikAra", stems=frozenset(_PAIR))
    if t is None or f"origin_pratyaya:{_PAIR[t.meta.get('upadesha_slp1')][1]}" not in t.tags:
        return None
    return t


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    up, old, n = _PAIR[t.meta["upadesha_slp1"]]
    del t.varnas[-n:]                                  # luk of the earlier pratyaya (S25)
    t.tags.discard(f"origin_pratyaya:{old}")
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "4.3.168",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaMsIyaparaSavyayoryaYaYO luk ca",
    text_dev              = "कंसीयपरशव्ययोर्यञञौ लुक् च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA kaMsIya-paraSavyayoH yaY-aYO luk ca tasya vikAraH avayave",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा कंसीय-परशव्ययोः यञ्-अञौ लुक् च तस्य विकारः अवयवे",
    padaccheda_dev        = "कंसीय-परशव्ययोः यञ्-अञौ लुक् च",
    why_dev               = "(सूत्रम् 4.3.168) कंसीयपरशव्ययोर्यञञौ लुक् च।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
