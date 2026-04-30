"""
8.1.6  प्रसमुपोदः पादपूरणे  —  SAMJNA (narrow *Phit* 4.81 anchor, ``prakriya_27``)

**Pāṭha (Kāśikā on *Aṣṭ*. 8.1.6, *anuvṛtti* *pareḥ* from 8.1.5):** *prasamupodaḥ
pādapūraṇe*.

**Śikṣā / Phit (user ``prakriya_27``):** *upasargāś cābhivarjam* (**Phiṭ** **4.81**) —
the vowel of an **upasarga** (here **ā** of **āṅ**) is **udātta** before the
verb base (*triṣṭūpam*, pedagogical **आगच्छ** spine).

This module **does not** realize full **8.1.6** *pāda-pūraṇa* morphology; it only
registers the accent-chain prerequisite ``samjna_registry['prakriya_27_phit481_upasarga_A_udAtta']``
when ``state.meta['prakriya_27_8_1_6_arm']`` is True and ``terms[0]`` is the
``AgacCa`` *tinanta* *śruti* demo (CONSTITUTION Art. 2: no *lakāra* / *puruṣa*
reads in ``cond``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_27_8_1_6_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "tinanta_accent_demo" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "AgacCa":
        return False
    if "prakriya_27_phit481_upasarga_A_udAtta" in state.samjna_registry:
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["prakriya_27_phit481_upasarga_A_udAtta"] = True
    state.meta.pop("prakriya_27_8_1_6_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.6",
    sutra_type=SutraType.SAMJNA,
    text_slp1="prasamupodaH pAdapUraRe",
    text_dev="प्रसमुपोदः पादपूरणे",
    padaccheda_dev="प्रसमुपोदः / पादपूरणे",
    why_dev="फिट् ४.८१ (*उपसर्गाश्चाभिवर्जम्*): उपसर्ग-स्वराङ्कनम् — पूर्णं ८.१.६-विधिं नास्ति (*prakriya_27*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
