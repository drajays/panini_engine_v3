"""
1.4.74  साक्षात्प्रभृतीनि च  —  SAMJNA

The words sākṣāt and others like it (sākṣāt-prabhṛti gaṇa) also get the
gati-saṃjñā.  This gaṇa includes: sākṣāt, vyarthā, āvis, āvir-bhāva,
tirobhāva, and similar compound-forming indeclinables.

v3: registers samjna_registry["gati_saksat_prabhrti"] as the frozenset.
Pāṭha: ashtadhyayi.com data.txt row i=14074 (Art. 14).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

_SAKSAT_PRABHRTI: frozenset[str] = frozenset({
    "sAkzAt", "Avis", "tiras",
    "vyarTA", "AvirbAva", "tirobAva",
    "AzIs",
})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_saksat_prabhrti") is None


def act(state: State) -> State:
    state.samjna_registry["gati_saksat_prabhrti"] = _SAKSAT_PRABHRTI
    existing = state.samjna_registry.get("gati_set", frozenset())
    state.samjna_registry["gati_set"] = existing | _SAKSAT_PRABHRTI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.74",
    sutra_type=SutraType.SAMJNA,
    text_slp1='sAkzAtpraBftIni ca',
    text_dev='साक्षात्प्रभृतीनि च',
    samagra_slp1="AkaqArAt ekA saMjYA prAgrISvarAnnipAtAH sAkzAt-praBftIni ca kriyAyoge gatiH viBAzA kfYi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आकडारात् एका संज्ञा प्राग्रीश्वरान्निपाताः साक्षात्-प्रभृतीनि च क्रियायोगे गतिः विभाषा कृञि",
    padaccheda_dev="साक्षात्-प्रभृतीनि / च",
    why_dev="साक्षात्प्रभृतयः गति-संज्ञकाः — साक्षाद्-गण-सूचिः गति-सेटे योज्यते।",
    anuvritti_from=("1.4.60",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
