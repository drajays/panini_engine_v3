"""
1.4.72  विभाषा कृञि  —  VIBHASHA

The word "tiras" optionally (vibhāṣā) gets the gati-saṃjñā when used with
the root kṛ (kṛñ, do/make).  Thus "tiras-kṛ" may or may not be treated
as a gati + kṛ compound; both derivations are acceptable.

This is an optional rule (vibhāṣā): the gate defaults to the preferred
reading (tiras is treated as a gati with kṛ), but recipes may fork
the derivation.

v3: registers samjna_registry["gati_tiras_kRni_vibhasha"] = True.
    vibhasha_default = True means the gati reading is the preferred option.
Pāṭha: ashtadhyayi.com data.txt row i=14072 (Art. 14).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_tiras_kRni_vibhasha") is None


def act(state: State) -> State:
    state.samjna_registry["gati_tiras_kRni_vibhasha"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.72",
    sutra_type=SutraType.VIBHASHA,
    text_slp1='viBAzA kfYi',
    text_dev='विभाषा कृञि',
    samagra_slp1="AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH viBAzA kfYi kriyAyoge gatiH tiraH antarDO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः विभाषा कृञि क्रियायोगे गतिः तिरः अन्तर्धौ",
    padaccheda_dev="विभाषा / कृञि",
    why_dev="कृञि 'तिरस्' विभाषया गति-संज्ञकः — ऐच्छिकः पक्षः।",
    anuvritti_from=("1.4.60", "1.4.71"),
    r1_form_identity_exempt=True,
    vibhasha_default=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
