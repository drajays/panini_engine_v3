"""
1.2.11  लिङ्सिचावात्मनेपदेषु  —  VIDHI (kit-vat)

After a hal-final dhātu with ik beside it, jhal-ādi liṅ/sic in ātmanepada are kit: भित्सीष्ट.
Pāṭha: ashtadhyayi.com data.txt row i=12011 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_1.pada_2._ling_sic_kit import hal_ik, ling_sic_after


def cond(state: State) -> bool:
    return ling_sic_after(state, hal_ik) is not None


def act(state: State) -> State:
    i = ling_sic_after(state, hal_ik)
    if i is not None:
        state.terms[i].tags.update({"kngiti", "kngiti_by_jhal_1_2_9_12"})   # kit only while jhal-initial: an iṭ (7.2.35) undoes it
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.11",
    sutra_type=SutraType.ATIDESHA,
    r1_form_identity_exempt=True,
    text_slp1="liNsicAvAtmanepadezu",
    text_dev="लिङ्सिचावात्मनेपदेषु",
    samagra_slp1="liN-sicO Atmanepadezu kit ikaH Jal halantAt ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="लिङ्-सिचौ आत्मनेपदेषु कित् इकः झल् हलन्तात् च",
    padaccheda_dev="लिङ्-सिचौ / आत्मनेपदेषु",
    why_dev="इक्समीपाद्धलन्तात् परौ झलादी लिङ्सिचौ आत्मनेपदेषु किद्वत् — गुणो न (१.१.५)।",
    anuvritti_from=("1.2.9", "1.2.10"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
