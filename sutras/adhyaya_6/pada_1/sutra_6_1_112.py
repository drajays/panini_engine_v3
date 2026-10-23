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
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence
from sutras.adhyaya_6.pada_1.sutra_6_1_77 import IKO_YANACI_ADESHA_TAG


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


def _khyatyat_site(state: State):
    """ख्यत्यात् परस्य ङसिङसोरतः उत् — the a of ṅasi / ṅas after a stem that ended in khi / khī / ti / tī and has taken yaṇ
    (6.1.77): सख्युः, पत्युः. Read from the yaṇ-ādeśa the tape carries, not from the word."""
    if len(state.terms) < 2:
        return None
    anga, pr = state.terms[-2], state.terms[-1]
    if "sup" not in pr.tags or len(anga.varnas) < 2 or not pr.varnas or pr.varnas[0].slp1 != "a":
        return None
    if (pr.meta.get("upadesha_slp1_original") or pr.meta.get("upadesha_slp1") or "").strip() not in {"Nasi~", "Nasi", "Nas~", "Nas"}:
        return None
    y, before = anga.varnas[-1], anga.varnas[-2].slp1
    if y.slp1 == "y" and IKO_YANACI_ADESHA_TAG in y.tags and before in {"K", "t"}:
        return pr
    return None


def cond(state: State) -> bool:
    return _matches(state) or _khyatyat_site(state) is not None


def act(state: State) -> State:
    if _matches(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("vivacs"))      # legacy P030 slice (see above)
        return state
    pr = _khyatyat_site(state)
    if pr is not None:
        pr.varnas[0] = mk("u")
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
