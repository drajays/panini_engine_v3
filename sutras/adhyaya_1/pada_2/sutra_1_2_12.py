"""
1.2.12  उश्च  —  VIDHI (kit-vat)

After an ṛ-final dhātu, jhal-ādi liṅ/sic in ātmanepada are kit: कृषीष्ट, अकृत.
Pāṭha: ashtadhyayi.com data.txt row i=12012 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_1.pada_2._ling_sic_kit import r_final, ling_sic_after


def cond(state: State) -> bool:
    return ling_sic_after(state, r_final) is not None


def act(state: State) -> State:
    i = ling_sic_after(state, r_final)
    if i is not None:
        state.terms[i].tags.update({"kngiti", "kngiti_by_jhal_1_2_9_12"})
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.12",
    sutra_type=SutraType.ATIDESHA,
    r1_form_identity_exempt=True,
    text_slp1='uSca',
    text_dev='उश्च',
    samagra_slp1="uH ca kit Jal liN-sicO Atmanepadezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="उः च कित् झल् लिङ्-सिचौ आत्मनेपदेषु",
    padaccheda_dev="उः / च",
    why_dev="ऋवर्णान्ताद्धातोः परौ झलादी लिङ्सिचौ आत्मनेपदेषु किद्वत् — कृषीष्ट, अकृत।",
    anuvritti_from=("1.2.9", "1.2.10"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
