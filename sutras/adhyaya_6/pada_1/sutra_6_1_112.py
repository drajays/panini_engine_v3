"""
6.1.112  ख्यत्यात् परस्य — *vac*+*san* stem shaping → *vivakṣ*-)

Teaching JSON **P030** collapses several śāstrīya replacements into “*vivakṣa-*”.
Here the engine tape after **6.1.77** + *pada*-merge is ``v`` + ``U`` + ``c`` + ``s``
(SLP1 ``vUcs``), which still lacks the reduplicate shape **vi-** before **vakṣ-**.

Glass-box *prayoga* slice (recipe-armed only): rewrite ``vUcs`` → ``vivacs`` so the
later Tripāḍī spine (**8.2.30** / **8.3.46**) yields ``vivakS`` (*vivakṣ-*).
Pāṭha: ashtadhyayi.com data.txt row i=61112 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if len(state.terms) != 1:
        return False
    vs = state.terms[0].varnas
    if len(vs) != 4:
        return False
    if vs[0].slp1 != "v":
        return False
    if vs[1].slp1 != "U":
        return False
    if vs[2].slp1 != "c":
        return False
    if vs[3].slp1 != "s":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    state.terms[0].varnas = list(parse_slp1_upadesha_sequence("vivacs"))
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.112",
    sutra_type=SutraType.VIDHI,
    text_slp1='KyatyAt parasya',
    text_dev='ख्यत्यात् परस्य',
    samagra_slp1="Kya-tyAt parasya Nasi-NasoH ataH ut ",
    samagra_dev="ख्य-त्यात् परस्य ङसि-ङसोः अतः उत् ।",
    padaccheda_dev="—",
    why_dev="वच्+सन्-मध्यावस्था → विवक्ष्-प्रत्यया-pूर्व आकारः (प०३०)।",
    anuvritti_from=("6.1.72",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
