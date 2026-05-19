"""
6.4.62  स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च  —  VIDHI

In bhāvakarmaṇa context, before tāsi (luṭ vikaraṇa), optionally insert iṭ
"ciṇvat" (treated like ciṇ, which is ñit). The ciṇvat treatment means 7.2.115
(aco ñṇiti) fires giving vṛddhi on the dhātu, instead of 7.3.84 (guṇa).

Engine: recipe arms via state.meta["6_4_62_arm"]. Finds the tāsi vikaraṇa term
(tagged tAsi_vikaraṇa) and inserts iṭ before it, marking it as ciṇvat.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_tasi(state: State):
    if not state.meta.get("6_4_62_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.meta.get("tAsi_vikaraṇa") and not t.meta.get("6_4_62_done"):
            return i
    return None


def cond(state: State) -> bool:
    return _find_tasi(state) is not None


def act(state: State) -> State:
    i = _find_tasi(state)
    if i is None:
        return state
    it_v = Term(
        kind="agama",
        varnas=parse_slp1_upadesha_sequence("iw"),
        tags={"agama", "upadesha", "it_agama", "cinvat_it"},
        meta={"upadesha_slp1": "iw", "cinvat_it": True},
    )
    state.terms.insert(i, it_v)
    state.terms[i + 1].meta["6_4_62_done"] = True
    state.meta.pop("6_4_62_arm", None)
    state.meta["7_2_115_karmani_lut_arm"] = True  # signal vṛddhi via ciṇvat
    state.samjna_registry["6.4.62_cinvat_it"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "syasicsIyuwtAsizu BAvakarmaRorupadeSe'jJanagrahadfSAM vA ciRvadiw ca",
    text_dev              = "स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च",
    padaccheda_dev        = "स्य-सिच्-सीयुट्‍-तासिषु भाव-कर्म्मणोः उपदेशे अच्-हन-ग्रह-दृशाम् वा चिण्-वत् इट् च",
    why_dev               = "(सूत्रम् 6.4.62) स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
