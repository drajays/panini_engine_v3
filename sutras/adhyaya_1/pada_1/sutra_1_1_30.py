"""
1.1.30  तृतीयासमासे  —  NIYAMA

*Śruti* (with *anuvṛtti* from **1.1.27**): the *sarvādi*-*sarvānāma*-*saṃjñā* is **not**
conferred in a *tṛtīyā*-*tatpuruṣa* *samāsa* (*tṛtīyā-samāse*).

v3: after **1.1.27** has set ``sarvanama`` on a *sarvādi*-listed *upadeśa* *aṅga*, this
rule *removes* that tag when the aṅga carries the structural tag ``tRtIyA_tatpurusha``
(see ``build_initial_state(..., tRtIyA_tatpurusha_samAsa=True)``; user
``तृतीयासमासे निषेध .md``).

*CONSTITUTION* Art. 2: *cond* reads only *Term* *tags* / *meta* — not ``(vibhakti, vacana)``,
not *gold*.

*Cross-check* *pāṭha* (row *i* = 11030, *ashtadhyayi-com* *sutraani*) or local *sutr*āṇi TSV.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_1_1_30_TRTIYA_STRIPPED: str = "1_1_30_tRtIyA_samAse_sarvanama_stripped"
"""Set on aṅga when **1.1.30** removes *sarvanāma* in *tṛtīyā*-*tatpuruṣa* *samāsa*."""


def _eligible_angas(state: State):
    for t in state.terms:
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "tRtIyA_tatpurusha" not in t.tags:
            continue
        if "sarvanama" not in t.tags:
            continue
        if t.meta.get(META_1_1_30_TRTIYA_STRIPPED):
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible_angas(state), None) is not None


def act(state: State) -> State:
    for t in _eligible_angas(state):
        t.tags.discard("sarvanama")
        t.meta[META_1_1_30_TRTIYA_STRIPPED] = True
    state.samjna_registry["1_1_30_tRtIyA_samAse"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.30",
    sutra_type     = SutraType.NIYAMA,
    r1_form_identity_exempt=True,
    text_slp1      = "tftIyA samAse",
    text_dev       = "तृतीयासमासे",
    padaccheda_dev = "तृतीया-समासे (न सर्वनाम) — १.१.२७ अनुवृत्ति",
    why_dev        = "तृतीया-तत्पुरुष-समासे *सर्वनाम*-*सञ्ज्ञा* न, अतः ७.१.१४ *स्मै* *प्रसङ्गो* *न* — ७.१.१३ *य* *पथः*।",
    anuvritti_from = ("1.1.27",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["META_1_1_30_TRTIYA_STRIPPED", "SUTRA"]
