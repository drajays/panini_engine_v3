"""
1.1.30  तृतीयासमासे  —  NIYAMA

*Śruti* (with *anuvṛtti* from **1.1.27**): the *sarvādi*-*sarvānāma*-*saṃjñā* is **not**
conferred in a *tṛtīyā*-*tatpuruṣa* *samāsa* (*tṛtīyā-samāse*).

v3: after **1.1.27** has set ``sarvanama`` on a *sarvādi*-listed *upadeśa* *aṅga*, this
rule *removes* that tag when the aṅga carries the structural tag ``tRtIyA_tatpurusha``
(samāsa memory; do not inject via subanta input booleans; user
``तृतीयासमासे निषेध .md``).

*CONSTITUTION* Art. 2: *cond* reads only *Term* *tags* / *meta* — not ``(vibhakti, vacana)``,
not *gold*.

*Cross-check* *pāṭha* (row *i* = 11030, *ashtadhyayi-com* *sutraani*) or local *sutr*āṇi TSV.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 11030 · तृतीयासमासे
              padaccheda: तृतीया-समासे ७/१
              anuvṛtti:   11027: सर्वादीनि सर्वनामानि | 11029: न
  Source #2 — Kāśikā 1.1.30 udāharaṇa:
                पाण्डुना रङ्गः
                गङ्गया पतिः
                मासपूर्वाय
  Gloss (sa) — तृतीयातत्पुरुषसमासे सर्वादयः सर्वनामसंज्ञां न लभन्ते।
  Cross-check — surface pinned by: tests/unit/test_tRtIyA_samAse_1_1_30.py
  Reference record: sutra_ref_out/1_1_30.json
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
    apavada_of     = ("1.1.27",),   # अपवाद of 1.1.27 — sutra_ref_out resolver.apavada_of
    anuvritti_from = ("1.1.27",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["META_1_1_30_TRTIYA_STRIPPED", "SUTRA"]
