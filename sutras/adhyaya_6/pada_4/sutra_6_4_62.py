"""
6.4.62  स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च  —  VIDHI

In bhāvakarmaṇa context, before tāsi (luṭ vikaraṇa), optionally insert iṭ
"ciṇvat" (treated like ciṇ, which is ñit). The ciṇvat treatment means 7.2.115
(aco ñṇiti) fires giving vṛddhi on the dhātu, instead of 7.3.84 (guṇa).

Engine: recipe arms via state.meta["6_4_62_arm"]. Finds the tāsi vikaraṇa term
(tagged tAsi_vikaraṇa) and inserts iṭ before it, marking it as ciṇvat.
Pāṭha: ashtadhyayi.com data.txt row i=64062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


# उपदेशेऽज्झनग्रहदृशाम् — ponytail: only the ajanta aṅgas (cāyiṣyate, bhāviṣyate); han / grah / dṛś (ghāniṣyate, grāhiṣyate,
# darśiṣyate) need 7.2.116 + 7.3.32 under the same ciṇvat and are not routed yet (docs/SHORTCUT_LEDGER: coordinator to add).
_AC = "aAiIuUfFxXeEoO"


def _find_tasi(state: State):
    # भावकर्मणोः — the sūtra is for the bhāva / karmaṇi prayoga only (the dhātu carries the usage tag).
    d = next((t for t in state.terms if "dhatu" in t.tags and "bhava_karma_usage" in t.tags), None)
    if d is None or not d.varnas or d.varnas[-1].slp1 not in _AC or d.meta.get("cinvat"):
        return None
    for i, t in enumerate(state.terms):
        if t.meta.get("tAsi_vikaraṇa") and not t.meta.get("6_4_62_done"):
            return i
        # sya vikaraṇa in bhāvakarmaṇa (6.4.62 explicitly names sya)
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "sya" and "vikarana" in t.tags and not t.meta.get("6_4_62_done"):
            return i
    return None


def cond(state: State) -> bool:
    return _find_tasi(state) is not None


def act(state: State) -> State:
    i = _find_tasi(state)
    if i is None:
        return state
    state.terms[i].meta["6_4_62_done"] = True
    # चिण्वत् — the dhātu is treated as before ciṇ (ṇit): 7.2.115 reads this tag, no state-wide arm
    next(t for t in state.terms if "dhatu" in t.tags).meta["cinvat"] = True
    pr = state.terms[i]
    if not (pr.varnas and "it_agama" in pr.varnas[0].tags):         # इट् च — unless 7.2.35 has already put it there
        it_v = mk("i")
        it_v.tags.add("it_agama")
        it_v.tags.add("cinvat_it")
        pr.varnas.insert(0, it_v)
        pr.meta["it_agama_7_2_35_done"] = True
    state.samjna_registry["6.4.62_cinvat_it"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.62",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = cond,
    r1_form_identity_exempt = True,
    text_slp1             = 'syasicsIyuwtAsizu BAvakarmaRorupadeSejJanagrahadfSAM vA ciRvadiw ca',
    text_dev              = 'स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च',
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke sya-sic-sIyuw-tAsizu BAvakarmmaRoH upadeSe ac-hana-graha-dfSAm vA ciRvat iw ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके स्य-सिच्-सीयुट्-तासिषु भावकर्म्मणोः उपदेशे अच्-हन-ग्रह-दृशाम् वा चिण्वत् इट् च",
    padaccheda_dev        = "स्य-सिच्-सीयुट्‍-तासिषु भाव-कर्म्मणोः उपदेशे अच्-हन-ग्रह-दृशाम् वा चिण्-वत् इट् च",
    why_dev               = "(सूत्रम् 6.4.62) स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
