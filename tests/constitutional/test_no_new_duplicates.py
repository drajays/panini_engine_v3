"""
CONSTITUTIONAL TEST: No New Duplicate Scheduling Blocks
=======================================================

This repo is mid-migration to canonical scheduling wrappers.
Until we reach zero duplicates, this test enforces **no regression**:

- the number of duplicate scheduling-block groups must not increase
  beyond a pinned baseline.

When we complete the collapse campaign, set the baseline to 0.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from audit.scheduling_block_auditor import SchedulingBlockAuditor


# Pinned after adding 31 corrected-prakriya pipeline files (all untracked, sharing
# apply_rule sequences with krdanta.py and each other).
# Long-term goal: drive to 0 by extracting shared sequences into canonical_pipelines.
# Update only when blocks are intentionally collapsed (should decrease) or new
# pipeline files are deliberately added.
# Updated: +2 from _derive_lit() in pipelines/tinanta.py (liṭ pipeline).
# Updated: +1 from _derive_lRG() in pipelines/tinanta.py (lṛṅ conditional pipeline).
# Updated: +16 from cursor's bhāve/karmaṇi/dhātu-browser tiṅanta work (2026-05-22 session).
# Updated: +50 from additional bhāve/karmani lakāra pipelines restored from stash (2026-05-27).
# Updated: +1 from dASaraThi_apatya_iY_demo.py (2026-05-28).
# Updated: +19 from vandanIya, pracChanIya, mlecChanIya pipelines (2026-05-28).
# Updated: +29 from T3 merge — _derive_laT_jYA_apa/_krI_sna/_kf_u_atmane spines
#          added to tinanta.py for P009/P011/P012 corrected demo integration (2026-05-28).
# Lowered: -353 from T3/T4 cleanup — deleted 31 corrected files, renamed 120 demo
#          pipelines. Remaining 225 groups targeted for canonical extraction.
# Lowered: -1 from 2026-05-29 tinanta.py restructuring — extracted 22 parasmaipada
#          tiṅ-spine blocks into P00_parasmai_tin_adesha (via P00_tin_adesha_base),
#          14 ātmanepada blocks into P00_tin_adesha_base across 5 files.
# Lowered: -13 from 2026-05-29 — canonicalized remaining 3.4.77/78 in canonical_pipelines
#          + vande; extracted P00_lac_lat_attach (3.1.91→3.2.123→laT) into canonical,
#          replacing 9 occurrences across canonical_pipelines, BIzayate, paTayati, tinanta.
# Lowered: -9 from 2026-05-29 — extracted P00_tanadi_u_guna (3.1.79→7.3.84→1.1.51),
#          refactored P00_tanadi_u_kit to call it; updated akurvAtAm, kurutaH, tinanta.
# Lowered: -13 from 2026-05-29 — added P00_hal_anit_it_lopa, P00_hal_it_lopa,
#          P00_lit_lakara_scope, P00_avyayibhava_pratipadika_luk; replaced callers in
#          canonical_pipelines, BIzayate, vande, tinanta, yAyAvaraH, pratyagni, yUpadAru,
#          agda/ninAya/papatuH/vibhidatuH liṭ demos.
# Lowered: -7 from 2026-05-29 — make dADikam/dASaraThi/taddhita use P00_taddhita_it_lopa_to_6_4.
# Lowered: -8 from 2026-05-29 — eliminate remaining direct 3.4.77/78 in demo pipelines
#          (adhyagIzwa, adita_luN, agda, BitzIzwa, paceran, saGgasIzwa, viSiNQi, BIzayate+);
#          add P00_snam_infix_8_2_1 + P00_lac_lat_attach to Binatti/ruNaddhi/muYcati/kirati/viSinanti.
# Lowered: -4 from 2026-05-29 — P00_tripadi_8_4_55_visarga, P00_luk_samjna_60_62,
#          P00_stri_4_1_wap added; callers in tinanta, jakzatuH, agnicit, gArgyAH,
#          dyukAmA, viSAKaH updated.
# Lowered: -12 from 2026-05-30 — P00_san_dvitva + P00_taddhita_1_1_scope scripts;
#          san dvitva in cicIzati, rurudizati, vivakSakaH, tinanta, jiGfkSati;
#          taddhita_1_1_scope in taddhita + taddhita_itika_etikAyana.
# Lowered: -36 from 2026-05-30 — batch extraction: P00_jas_si_num_napumsaka,
#          P00_lit_dvitva_abhyasa_hrasva, P00_samprasarana_dirgha, P00_aniyar_it_lopa_3_1_91,
#          P00_bha_vidhi_6_4_148_1_1_60, P00_mahat_An_samasa_sandhi, P00_jas_7_1_17_it_lopa_6_1_87,
#          P00_hal_anit_guna, P00_lit_ta_esh_it_lopa; + P00_tripadi_rutva_visarga replacements
#          in tinanta; restored sutra_6_1_77 (pre-existing modified sutra).
# Raised: +14 from 2026-05-30 — cursor untracked lesson pipelines
#          (agaty_gam_lyap_acah, avadhIt_han_lun_ekavacana, dIdhye_dIdhi_lat_parasmin,
#           sthanivat_anal_ashrita, sthanivat_it_samjna) sharing sequences with existing files;
#          Round-2 batch extractions: P00_amantrana_2_3_48_accent, P00_tanadi_kit_6_4_110,
#          P00_tuk_tripadi_6_1_73, P00_bha_avakasha_6_4_148, P00_mRj_abhyasa_hrasva,
#          P00_attach_sup_from_pratipadika (krdanta), P00_anga_guna_audit (tinanta).
MAX_DUPLICATE_GROUPS = 41


@pytest.fixture(scope="module")
def audit_result():
    auditor = SchedulingBlockAuditor(project_root=".")
    auditor.scan()
    return {
        "auditor": auditor,
        "duplicates": auditor.find_duplicates(),
    }


class TestNoNewDuplicates:
    def test_duplicate_groups_do_not_increase(self, audit_result) -> None:
        duplicates = audit_result["duplicates"]
        n = len(duplicates)
        assert n <= MAX_DUPLICATE_GROUPS, (
            f"duplicate scheduling-block groups increased: got {n}, "
            f"baseline {MAX_DUPLICATE_GROUPS}. "
            "Collapse more blocks (move scheduling into core.canonical_pipelines) "
            "or update baseline only after an intentional migration."
        )

    def test_all_blocks_in_scan_dirs(self, audit_result) -> None:
        auditor = audit_result["auditor"]
        assert not auditor.errors, "scan errors:\n" + "\n".join(auditor.errors)

    def test_scan_covers_pipelines_dir(self, audit_result) -> None:
        auditor = audit_result["auditor"]
        scanned = set(auditor.files_scanned)
        pipeline_files = list(Path("pipelines").glob("*.py"))
        if not pipeline_files:
            pytest.skip("no pipeline files found")
        assert any(p.as_posix() in scanned for p in pipeline_files), (
            "expected at least one pipelines/*.py to contribute apply_rule windows; "
            "if pipelines fully delegate, adjust SCAN_DIRS or this assertion."
        )


class TestCanonicalPipelinesIntact:
    def test_canonical_pipelines_importable(self) -> None:
        import core.canonical_pipelines as cp

        assert cp is not None

