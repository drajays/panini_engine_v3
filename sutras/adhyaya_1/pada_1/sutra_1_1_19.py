"""
1.1.19  (IdU tau ca saptamyarthe)  —  SAMJNA; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11019 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11019):** *ī* and *ū* in the *dvivacana* (*tau*), with *ca*
(in addition to the **1.1.11** block), in the *saptamī* / locative *artha* *prayoga*, receive the
*pragṛhya* *saṃjñā* by *anuvṛtti* of *pragṛhyam* from **1.1.11** (``an`` in the index).  v3 sets a
boolean in ``samjna_registry`` so *vidhi* *later* can query this extension without *cond* reading
*vibhakti* here (CONSTITUTION Art. 2).

**Cross-check pāṭha:** *sutrANi.tsv* index ``1.1.19`` should match the ``s`` line in ``data.txt``.

See also **1.1.11** (``sutra_1_1_11``) for the base *pragṛhya* vowel set; **1.1.14** *nipāta*; **1.1.100**
(*Kāśikā* *mātrā*-*samāsa*); **1.1.15**–**1.1.16** *saṃjñā*; **1.1.17**–**1.1.18** *paribhāṣā* *gates* in v3.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_1 import sutra_1_1_11 as s1111

# *IdU* + *tau* *saptamī*-*artha* reading extends **1.1.11**; *vidhi* consults this *registry* key.
PRAGHYA_SAPTAMI_EE_UU_KEY: str = "pragrahya_eeUu_tau_saptamIartha"

# Pāṭha bytes match ashtadhyayi ``data.txt`` *s* (i=11019); not ``सप्तम्यार्थे`` with a separate *ā*.
_TEXT_DEV: str = (
    "\u0908\u0926\u0942\u0924\u094c \u091a \u0938\u092a\u094d\u0924\u092e\u094d\u092f\u0930\u094d\u0925\u0947"
)


def cond(state: State) -> bool:
    if not s1111.pragrahya_samjna_is_registered(state):
        return False
    return state.samjna_registry.get(PRAGHYA_SAPTAMI_EE_UU_KEY) is not True


def act(state: State) -> State:
    state.samjna_registry[PRAGHYA_SAPTAMI_EE_UU_KEY] = True
    return state


def eeUu_tau_saptamIartha_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(PRAGHYA_SAPTAMI_EE_UU_KEY) is True


_WHY = (
    "द्विवचन-ईदू-काले सप्तमी-तात्पर्ये, प्रगृह्य-संज्ञा-विस्तारः, इति।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.19",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "IdU tau ca saptamyarthe",
    text_dev       = _TEXT_DEV,
    padaccheda_dev = " / ".join(_TEXT_DEV.split()),  # three *padas* as in index ``pc``
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
