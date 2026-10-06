"""
1.4.76  मध्ये पदे निवचने च  (madhye pade nivacane ca)  —  SAMJNA

The words "madhye" (in the middle), "pade" (at the step/place), and forms
used in the sense of nivacana (respectful address) also get the gati-saṃjñā.

v3: registers samjna_registry["gati_madhye_pade"] = frozenset({"maDye","pade"}).
Pāṭha: ashtadhyayi.com data.txt row i=14076 (Art. 14).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_MADHYE_PADE: frozenset[str] = frozenset({"maDye", "pade"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_madhye_pade") is None


def act(state: State) -> State:
    state.samjna_registry["gati_madhye_pade"] = _MADHYE_PADE
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _MADHYE_PADE
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.76",
    sutra_type=SutraType.SAMJNA,
    text_slp1="maDye pade nivacane ca",
    text_dev="मध्ये पदे निवचने च",
    samagra_slp1="AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH maDye pade nivacane ca kriyAyoge gatiH viBAzA kfYi anatyADAne",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः मध्ये पदे निवचने च क्रियायोगे गतिः विभाषा कृञि अनत्याधाने",
    padaccheda_dev="मध्ये / पदे / निवचने / च",
    why_dev="निवचने 'मध्ये' 'पदे' गति-संज्ञकौ — गति-सेटे योज्येते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
