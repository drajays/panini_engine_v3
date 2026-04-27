"""
pipelines/sarva_subanta.py — **सर्व** (a-stem masculine sarvanāma) subanta: *one* prakriyā for all 24 *sup* cells.

All forms use the same engine path: ``build_initial_state("sarva", v, vac, "pulliṅga")`` →
``run_subanta_pipeline`` (``pipelines.subanta``), i.e. **only** ``apply_rule``-scheduled
*śāstrīya* *kram* (see ``SUBANTA_RULE_IDS_POST_4_1_2`` in ``subanta.py``).

*Śikṣā link (user* ``सर्वे .md`` *— प्रथमा बहु* *सर्वे*):
  **1.1.27** *sarvanāma*; **1.2.45** *prātipadika*; **4.1.2** *sup* (जस् for 1-3); **1.4.13** *aṅga*;
  **7.1.17** *jasaḥ śī*; *it* **1.3.7** / **1.3.9** on the *śī* *ādeśa* residue; **6.1.87** *ā̐d guṇa*
  (*a* + *ī* → *e*), yielding **sarv** + **e** = ``sarve`` (SLP1) / सर्वे.

*Śikṣā link (user* ``सर्वस्मै and other.md`` *— चतु./पञ्./सप्. एक*):
  **4.1.2** *sup* gives *ṅe* / *ṅasi* / *ṅi*; *it* **1.3.2–1.3.9**; **7.1.12** *ṭāṅ…* (*ato* *aṅga*) is the
  general *ādeśa* for *wA*/*Nasi*/*Nas* on non-sarvanāma (e.g. *rāma* *pañcamī* *eka* → *rAmAt*).
  For *adanta* *sarvanāma* (tag **1.1.27**), **7.1.14** *sarvanāmnar smai* (*Ne* → ``smE``) and
  **7.1.15** *ṅasir… smāt-sminau* (*Nasi* → *smAt*, *Ni* → *smin*) *win* (schedule **7.1.15** before
  **7.1.12** in ``SUBANTA_RULE_IDS_POST_4_1_2``; **1.4.2** *vipratiṣedhe paraṃ kāryam* in the
  resolver). *Ādeśa* of full *sup* *upadeśa* to *smai*/*smāt*/*smin* implements the
  **1.1.55** *anekāl-śit* *prayoga* in this slice without a separate **1.1.55** module.
  Parallel *śabda* **viSva** uses the same ``derive(…, "pulliṅga")`` spine.
  Other *vibhakti*/*vacana* cells add **7.1.52/72/103** etc. as the *upadeśa* and *aṅga* demand —
  *no* second *recipe* and *no* *gold* *shortcuts* in the engine.

*Śikṣā link (user* ``सर्वेषाम्.md`` *— षष्ठी बहु* *सर्वेषाम्*):
  *Vivakṣā* (cell **6-3**): *sampradāna* is not the issue in the engine; the form is **4.1.2** *sup* →
  *upadeśa* **Am** (``Am``) for *ṣaṣṭhī* *bahu*; **1.4.13** *aṅga* on the stem.
  **7.1.52** *āmi sarvanāmnas suṭ* → *sut* (``suw``) before **Am**; **1.1.46** *ādyantau ṭakitau* — *sut*
  is *ṭit* → ādi of **Am**; *it* **1.3.2** (``u``), **1.3.3** (``w``) → lopa by **1.3.9**, leaving
  the *śeṣa* *s* before **am**; **1.3.4** *na vibhaktau …* keeps the *m* of *ām* (not *it*), so
  the surface of the *pratyāya* is **sām** (SLP1 ``sAm``).
  **7.3.103** *bahuvacane jhalyet* (here *jhal* at the start of the actual *sām* = *s*) replaces only
  the *antya* *a* of the *aṅga* with *e* → ``sarve`` + ``sAm`` (the *stāne niyamāya* of **1.1.52**
  is implicit in the *ādeśa* target, not a separate *vidhi* line in the trace in this build).
  **8.3.59** (tripādī) *iṇ-koḥ* … → *s* of *sut* to *ṣ* after the new *e* (in *iṇ*), when that *s* is
  the *pratyayāvayava* of an *ādeśa* → **सर्व** + *e* + *ṣ* + *ām* = ``sarveṣāṃ``/``sarvezAm`` in SLP1.
  Non-*sarvanāma* (e.g. *rāma* **6-3**): **7.1.54** *num* (*nuṭ*), *not* **7.1.52**; contrast only,
  one ``derive(…)`` *prakriyā* each.
  Parallel *śabda* **viSva** uses the same *sup* *sūtra* spine: ``viSveṣām`` / ``viSvezAm`` (SLP1).
  Full *paradigma* of **6-3** already checked by ``test_24_cells_match_reference_gold`` against
  ``data/reference/subanta_gold/sarva_pullinga.json``; this *śikṣā* text names the *dṛśya* chain
  the trace exercises for the *aṣmād* *ādi* *sarvanāma* *adanta* slice.

*Śikṣā link* (user ``सर्वकः.md`` *—* *anuṣṅa* *-aka* *prathama* *eka* *सर्वकः*):
  *not* a second *subanta* *recipe* — use ``derive_sarvakaha`` in ``pipelines.sarvaka_subanta`` (arm **5.3.71** after **5.3.70** *kā* *adhikāra*; *akac* infix, **1.2.46** *vyutpanna*, then the usual *4.1.2*+ *P13–P15* *sup* *spine*).

*Śikṣā link* (user ``प्रियविश्वाय.md`` *—* *sarvādi* in *bahuvrīhī*):
  **1.1.29** *na bahuvrīhau* (after **1.1.27** in *P01*) cancels *sarvanāma*; **7.1.14** inert, **7.1.13** + **7.3.102** for *caturthī* *eka* — use ``derive_priyaviSvAya_caturthI_eka`` in ``pipelines.priyaviSva_bahuvrIhi_subanta`` (``build_initial_state`` / ``derive`` with ``bahuvrIhi_samAsa=True``; stem id ``priya-viSva`` from *sarvādi* *gaṇa* *input*).

*Śikṣā link* (user ``तृतीयासमासे निषेध .md`` *—* *tṛtīyā* *tatpuruṣa*):
  **1.1.30** *tṛtīyā-samāse* (after **1.1.29** in *P01*) cancels *sarvanāma* on ``tRtIyA_tatpurusha`` *aṅga*; same *caturthī* *āya* tail as *priya-viśvāya* but for *māsa-pūrv* *śabda* *ids* — ``pipelines.mAsa_pUrva_tRtIyA_subanta`` and ``sarvadi_slp1`` entries ``mAsa-pUrva``, *etc.*
"""
from __future__ import annotations

from engine.state import State

from pipelines.subanta import derive

SARVA_STEM_SLP1: str = "sarva"
SARVA_LIṄGA: str = "pulliṅga"

# Eight *vibhakti* × three *vacana* (tyadādi *sambodhana* gap does not apply to *sarva*).
SARVA_PUM_24_CELLS: tuple[tuple[int, int], ...] = tuple(
    (v, vac) for v in range(1, 9) for vac in range(1, 4)
)


def derive_sarva_pulliṅga(vibhakti: int, vacana: int) -> State:
    """
    *Subanta* for *sarva* (puṃ, a-anta) at ``(vibhakti, vacana)``.

    This is the **sole** supported entry for *सर्व* *rūpa* in the engine *corpus*;
    it delegates to ``derive("sarva", …, "pulliṅga")`` (same *prakriyā* as
    ``derive_akarant_pullinga("sarva", …)``).
    """
    return derive(
        SARVA_STEM_SLP1,
        vibhakti,
        vacana,
        linga=SARVA_LIṄGA,
    )


def sarva_cell_key(vibhakti: int, vacana: int) -> str:
    return f"{vibhakti}-{vacana}"


def iter_sarva_paradigm() -> tuple[tuple[str, State], ...]:
    """All 24 cells, each as ``(cell_key, final_state)`` (for tools / UI batch)."""
    out: list[tuple[str, State]] = []
    for v, vac in SARVA_PUM_24_CELLS:
        s = derive_sarva_pulliṅga(v, vac)
        out.append((sarva_cell_key(v, vac), s))
    return tuple(out)


__all__ = [
    "SARVA_LIṄGA",
    "SARVA_PUM_24_CELLS",
    "SARVA_STEM_SLP1",
    "derive_sarva_pulliṅga",
    "iter_sarva_paradigm",
    "sarva_cell_key",
]
