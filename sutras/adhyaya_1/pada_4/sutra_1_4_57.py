"""
1.4.57  चादयोऽसत्त्वे  —  SAMJNA

The ca-ādi particles (ca, vā, ha, aha, eva, evam, nūnam, śaśvat, yugapat,
bhūyas, kila, khalu, bata, nanu, u, ut, tū, pātam, hanta, aho, aṭo, are,
are, hā, hi) are nipātas when used in a non-substantival sense (asattve).

v3: registers the ca-ādi set in samjna_registry["nipata_ca_adi"] and sets
    the gate "1_4_57_ca_adi_nipata" so that the same set is not registered
    twice.
Pāṭha: ashtadhyayi.com data.txt row i=14057 (Art. 14).
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

# SLP1 ca-ādi list (canonical Ashtadhyayi ca-ādi gaṇa members)
_CA_ADI: frozenset[str] = frozenset({
    "ca", "vA", "ha", "aha", "eva", "evam", "nUnam", "SaSvat",
    "yugapat", "BUyas", "kila", "Kalu", "bata", "nanu", "u", "ut",
    "tU", "pAtam", "hanta", "Aho", "aho", "are", "hA", "hi",
})


def cond(state: State) -> bool:
    return state.samjna_registry.get("nipata_ca_adi") is None


def act(state: State) -> State:
    state.samjna_registry["nipata_ca_adi"] = _CA_ADI
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.57",
    sutra_type=SutraType.SAMJNA,
    text_slp1='cAdayosattve',
    text_dev='चादयोऽसत्त्वे',
    samagra_slp1="ca-AdayaH asatve nipAtAH",
    samagra_dev="च-आदयः असत्वे निपाताः",
    padaccheda_dev="च-आदयः / असत्त्वे",
    why_dev="असत्त्वे (अद्रव्यवृत्तौ) चकारादयो निपात-संज्ञाः प्राप्नुवन्ति।",
    anuvritti_from=("1.4.56",),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
