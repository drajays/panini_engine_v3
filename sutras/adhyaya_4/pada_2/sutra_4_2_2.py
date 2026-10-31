"""
4.2.2  लाक्षारोचनाशकलकर्दमाट्ठक्  —  VIDHI

Padaccheda: लाक्षा-रोचनात् (शकलकर्दमात् ) ठक्

लाक्षारोचना(शकलकर्दमा)ट्ठक् (4.2.2)
Pāṭha: ashtadhyayi.com data.txt row i=42002 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita
from engine.vartika import Vartika


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "rakta"), stems=frozenset({"lAkzA","rocanA","Sakala","kardama"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Wak")


# Art. 25 / AMENDMENT 29: the vārttikas of 4.2.2 live here (Bhāṣya 4.2.2, 5329 - 5331; the rāga words are the caller's lex:rAga facts, as in 4.2.1).
def _rakta(state: State, stems):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "rakta"), stems=frozenset(stems), tag="rAga")


def _v1_cond(state: State) -> bool:
    return _rakta(state, {"Sakala", "kardama"}) is not None


def _v1_act(state: State) -> State:       # ṭhak-prakaraṇe śakalakardamābhyām upasaṃkhyānam: the aṇ of 4.2.1 is also kept (Kāśikā 'aṇ apīṣyate')
    return attach_taddhita(state, ("Wak", "aR")[policy_pick(state, "4.2.2.v1", 2)])


def _v2_cond(state: State) -> bool:
    return _rakta(state, {"nIlI"}) is not None


def _v2_act(state: State) -> State:
    return attach_taddhita(state, "an")


def _v3_cond(state: State) -> bool:
    return _rakta(state, {"pIta"}) is not None


def _v3_act(state: State) -> State:
    return attach_taddhita(state, "kan")


VARTIKAS = (
    Vartika(id="4.2.2.v1", source="Kātyāyana vā. 1 on 4.2.2 (Bhāṣya 5329)", tier="T1", relation="apavada",
            text_dev="शकलकर्दमाभ्यामुपसंख्यानम्", cond=_v1_cond, act=_v1_act),
    Vartika(id="4.2.2.v2", source="Kātyāyana vā. 2 on 4.2.2 (Bhāṣya 5330: nīlyā raktaṃ nīlam)", tier="T1", relation="extension",
            text_dev="नील्या अन् वक्तव्यः", cond=_v2_cond, act=_v2_act),
    Vartika(id="4.2.2.v3", source="Kātyāyana vā. 3 on 4.2.2 (Bhāṣya 5331: pītena raktaṃ pītakam)", tier="T1", relation="extension",
            text_dev="पीतात्कन् वक्तव्यः", cond=_v3_cond, act=_v3_act),
)

SUTRA = SutraRecord(
    sutra_id              = "4.2.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'lAkzArocanASakalakardamAwWak',
    text_dev              = 'लाक्षारोचनाशकलकर्दमाट्ठक्',
    samagra_slp1          = "tena raktaM rAgAt iti lAkzA-rocanA-Sakala-kardamAt Wak pratyayaH",
    samagra_dev           = "'तेन रक्तं रागात्' (इति) लाक्षा-रोचना-शकल-कर्दमात् ठक् प्रत्ययः",
    padaccheda_dev        = "लाक्षा-रोचनात् (शकलकर्दमात् ) ठक्",
    why_dev               = "(सूत्रम् 4.2.2) लाक्षारोचना(शकलकर्दमा)ट्ठक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.1',),
    vartikas              = VARTIKAS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
