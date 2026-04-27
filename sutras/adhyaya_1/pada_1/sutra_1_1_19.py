"""
1.1.19  (IdU tau ca saptamyarthe)  —  SAMJNA; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11019 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11019):** *ī* and *ū* in the *dvivacana* (*tau*), with *ca*
(in addition to the **1.1.11** block), in the *saptamī* / locative *artha* *prayoga*, receive the
*pragṛhya* *saṃjñā* by *anuvṛtti* of *pragṛhyam* from **1.1.11** (``an`` in the index).  v3 sets a
boolean in ``samjna_registry`` so *vidhi* *later* can query this extension without *cond* reading
*vibhakti* here (CONSTITUTION Art. 2).

When a recipe arms ``SAPTAMYARTHA_PRAGHYA_TAG_ARM_META`` (Vedic *ṅi*-*luk* *pada* in *saptamī*-*artha*,
e.g. *gau*…*ī* + *adhiśritaḥ*; *padapāṭha* *…* + *iti*), ``act`` also adds ``pragrahya`` to
*prātipadika*/*aṅga* **Term**s whose *anta* is *ī* / *ū* (**``I``** / **``U``** SLP1) so **6.1.77** /
**6.1.125** can block *yaṇ* across the boundary.

**Cross-check pāṭha:** *sutrANi.tsv* index ``1.1.19`` should match the ``s`` line in ``data.txt``.

See also **1.1.11** (``sutra_1_1_11``) for the base *pragṛhya* vowel set; **1.1.14** *nipāta*; **1.1.100**
(*Kāśikā* *mātrā*-*samāsa*); **1.1.15**–**1.1.16** *saṃjñā*; **1.1.17** *paribhāṣā* *gate*; **1.1.18**
*ūṃ* *vidhi* + *gate* (``sutra_1_1_18``).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_1 import sutra_1_1_11 as s1111

PRAGHYA_TERM_TAG: str = s1111.PRAGHYA_TERM_TAG

# *IdU* + *tau* *saptamī*-*artha* reading extends **1.1.11**; *vidhi* consults this *registry* key.
PRAGHYA_SAPTAMI_EE_UU_KEY: str = "pragrahya_eeUu_tau_saptamIartha"

# Recipe arms **1.1.19** *prayoga* that stamps ``pragrahya`` on *ī*/*ū*-final *pada*s in *saptamī*-*artha*.
SAPTAMYARTHA_PRAGHYA_TAG_ARM_META: str = "1_1_19_saptamyartha_pragrahya_tag_arm"

_REGISTRY_REASSERT: str = "1.1.19_pragrahya_prayoga_reassert"

# Pāṭha bytes match ashtadhyayi ``data.txt`` *s* (i=11019); not ``सप्तम्यार्थे`` with a separate *ā*.
_TEXT_DEV: str = (
    "\u0908\u0926\u0942\u0924\u094c \u091a \u0938\u092a\u094d\u0924\u092e\u094d\u092f\u0930\u094d\u0925\u0947"
)


def _tag_I_U_saptamyartha_pragrahya(state: State) -> None:
    for t in state.terms:
        if not ({"prātipadika", "anga"} & t.tags):
            continue
        fin = t.final_varna
        if fin is not None and fin.slp1 in {"I", "U"}:
            t.tags.add(PRAGHYA_TERM_TAG)


def cond(state: State) -> bool:
    if not s1111.pragrahya_samjna_is_registered(state):
        return False
    if bool(state.meta.get(SAPTAMYARTHA_PRAGHYA_TAG_ARM_META)):
        return True
    return state.samjna_registry.get(PRAGHYA_SAPTAMI_EE_UU_KEY) is not True


def act(state: State) -> State:
    arm = state.meta.pop(SAPTAMYARTHA_PRAGHYA_TAG_ARM_META, None)
    if arm:
        _tag_I_U_saptamyartha_pragrahya(state)
    key_missing = state.samjna_registry.get(PRAGHYA_SAPTAMI_EE_UU_KEY) is not True
    if key_missing:
        state.samjna_registry[PRAGHYA_SAPTAMI_EE_UU_KEY] = True
    elif arm:
        state.samjna_registry[_REGISTRY_REASSERT] = (
            state.samjna_registry.get(_REGISTRY_REASSERT, 0) + 1
        )
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
