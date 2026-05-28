"""
Integrity checks for ``data/reference/corrected_prakriyas_v2/prakriyas_corrected_v2.json``.

Source bundle was produced from ``Downloads/files (1)/`` (schema v3.0).  It lists
**31** glass-box prakriyās (expanded from **19** upstream JSON files).  Full
engine pipelines for each row are implemented incrementally under ``pipelines/``;
this module only pins the reference artifact and basic schema invariants.

CONSTITUTION Art. 6: tests may read ``data/reference/``; engine/sūtras must not.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

_BUNDLE = Path(__file__).resolve().parents[2] / "data" / "reference" / "corrected_prakriyas_v2" / "prakriyas_corrected_v2.json"

_EXPECTED_IDS = frozenset(
    {
        "P001-A",
        "P001-B",
        "P001-C",
        "P001-D",
        "P002-A",
        "P002-B",
        "P003-A",
        "P003-B",
        "P003-C",
        "P004-A",
        "P004-B",
        "P004-C",
        "P004-D",
        "P005-A",
        "P005-B",
        "P006",
        "P007",
        "P008",
        "P009",
        "P010",
        "P011-A",
        "P011-B",
        "P012",
        "P013",
        "P014",
        "P015",
        "P016",
        "P017",
        "P018-A",
        "P018-B",
        "P019",
    }
)


@pytest.fixture(scope="module")
def corrected_v2() -> dict:
    assert _BUNDLE.is_file(), f"missing bundle at {_BUNDLE}"
    with _BUNDLE.open(encoding="utf-8") as f:
        return json.load(f)


def test_bundle_schema_and_count(corrected_v2: dict) -> None:
    assert corrected_v2.get("schema_version") == "3.0"
    prs = corrected_v2["prakriyas"]
    assert isinstance(prs, list)
    assert len(prs) == 31
    ids = {p["id"] for p in prs}
    assert ids == _EXPECTED_IDS


@pytest.mark.parametrize("pid", sorted(_EXPECTED_IDS))
def test_each_prakriya_has_steps(pid: str, corrected_v2: dict) -> None:
    prs = corrected_v2["prakriyas"]
    hit = next(p for p in prs if p["id"] == pid)
    steps = hit["steps"]
    assert isinstance(steps, list) and len(steps) >= 1
    for st in steps:
        assert "n" in st and "operation_kind" in st


def test_P001_A_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """Golden-order spine from the bundle (AST-only refs), for future pipeline work."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-A")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.3",
        "1.3.2",
        "1.3.9",
        "3.2.102",
        "3.1.91",
        "3.1.1",
        "3.1.2",
        "1.3.8",
        "1.3.9",
        "7.2.35",
        "7.2.14",
        "8.2.42",
        "1.2.46",
        "4.1.1",
        "4.1.2",
        "8.2.66",
        "8.3.15",
    ]


def test_P001_C_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P001-C** (*svinnaḥ*), aligned with ``svinnaH_kta_*_P001_C`` demo."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-C")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.2",
        "1.3.9",
        "6.1.64",
        "3.2.102",
        "1.3.8",
        "1.3.9",
        "7.2.35",
        "7.2.14",
        "8.2.42",
        "1.2.46",
        "4.1.2",
        "1.3.2",
        "1.3.9",
        "8.2.66",
        "8.3.15",
    ]


def test_P001_D_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P001-D** (*iddhaḥ*), aligned with bundle JSON."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-D")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.2",
        "1.3.9",
        "3.2.102",
        "1.3.8",
        "1.3.9",
        "7.2.35",
        "7.2.14",
        "6.4.24",
        "8.2.40",
        "8.4.53",
        "1.2.46",
        "4.1.2",
        "1.3.2",
        "1.3.9",
        "8.2.66",
        "8.3.15",
    ]


def test_P002_A_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P002-A** (*vepathuḥ*)."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P002-A")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.2",
        "1.3.9",
        "3.3.89",
        "3.1.91",
        "1.3.3",
        "1.3.9",
        "1.2.46",
        "4.1.1",
        "4.1.2",
        "1.3.2",
        "1.3.9",
        "8.2.66",
        "8.3.15",
    ]


def test_P002_B_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P002-B** (*śvayathuḥ*)."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P002-B")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.2",
        "1.3.9",
        "3.3.89",
        "1.3.3",
        "1.3.9",
        "7.3.84",
        "1.1.2",
        "6.1.78",
        "1.2.46",
        "4.1.2",
        "1.3.2",
        "1.3.9",
        "8.2.66",
        "8.3.15",
    ]


def test_P003_A_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P003-A** (*paktrimam*)."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-A")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.3",
        "1.3.2",
        "1.3.9",
        "3.3.88",
        "1.3.8",
        "1.3.9",
        "8.2.30",
        "1.1.50",
        "1.2.46",
        "4.1.2",
        "7.1.24",
        "6.1.107",
    ]


def test_P003_B_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P003-B** (*kṛtrimam*)."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-B")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.3",
        "1.3.9",
        "3.3.88",
        "1.3.8",
        "1.3.9",
        "7.3.84",
        "1.1.5",
        "1.2.46",
        "4.1.2",
        "7.1.24",
        "6.1.107",
    ]


def test_P003_C_astadhyayi_spine_order(corrected_v2: dict) -> None:
    """AST spine for **P003-C** (*uptrimam*)."""

    def _ast_nums(step: dict) -> list[str]:
        out: list[str] = []
        for su in step.get("sutras") or []:
            if su.get("type") == "ASTADHYAYI" and su.get("number"):
                out.append(str(su["number"]))
        return out

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-C")
    flat: list[str] = []
    for st in hit["steps"]:
        flat.extend(_ast_nums(st))
    assert flat == [
        "1.3.1",
        "1.3.5",
        "1.3.2",
        "1.3.9",
        "3.3.88",
        "1.3.8",
        "1.3.9",
        "6.1.15",
        "1.2.46",
        "4.1.2",
        "7.1.24",
        "6.1.107",
    ]


def test_P001_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-A** (*bhinnaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.bhinnaH_kta_Bidi_corrected_P001_A_demo import derive_bhinnaH_kta_Bidi_corrected_P001_A

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-A")
    assert hit["target"]["iast"] == "bhinnaḥ"
    assert derive_bhinnaH_kta_Bidi_corrected_P001_A().flat_slp1() == "bhinnaH"


def test_P001_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-B** (*dhṛṣṭaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.dhRSTaH_kta_YiDfzf_corrected_P001_B_demo import derive_dhRSTaH_kta_YiDfzf_corrected_P001_B

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-B")
    assert hit["target"]["iast"] == "dhṛṣṭaḥ"
    assert derive_dhRSTaH_kta_YiDfzf_corrected_P001_B().flat_slp1() == "DfzwaH"


def test_P001_C_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-C** (*svinnaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.svinnaH_kta_YizvidA_corrected_P001_C_demo import derive_svinnaH_kta_YizvidA_corrected_P001_C

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-C")
    assert hit["target"]["iast"] == "svinnaḥ"
    assert derive_svinnaH_kta_YizvidA_corrected_P001_C().flat_slp1() == "svinnaH"


def test_P001_D_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-D** (*iddhaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.iddhaH_kta_YiinDI_corrected_P001_D_demo import derive_iddhaH_kta_YiinDI_corrected_P001_D

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-D")
    assert hit["target"]["iast"] == "iddhaḥ"
    assert derive_iddhaH_kta_YiinDI_corrected_P001_D().flat_slp1() == "idDaH"


def test_P002_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P002-A** (*vepathuḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.vepathuH_athuc_wuvepf_corrected_P002_A_demo import (
        derive_vepathuH_athuc_wuvepf_corrected_P002_A,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P002-A")
    assert hit["target"]["iast"] == "vepathuḥ"
    assert derive_vepathuH_athuc_wuvepf_corrected_P002_A().flat_slp1() == "vepathuH"


def test_P002_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P002-B** (*śvayathuḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.zvayathuH_athuc_wzvi_corrected_P002_B_demo import derive_zvayathuH_athuc_wzvi_corrected_P002_B

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P002-B")
    assert hit["target"]["iast"] == "śvayathuḥ"
    assert derive_zvayathuH_athuc_wzvi_corrected_P002_B().flat_slp1() == "zvayathuH"


def test_P003_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P003-A** (*paktrimam*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.paktrimam_ktri_qupac_corrected_P003_A_demo import derive_paktrimam_ktri_qupac_corrected_P003_A

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-A")
    assert hit["target"]["iast"] == "paktrimam"
    assert derive_paktrimam_ktri_qupac_corrected_P003_A().flat_slp1() == "paktrimam"


def test_P003_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P003-B** (*kṛtrimam*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.kRtrimam_ktri_kf_corrected_P003_B_demo import derive_kRtrimam_ktri_kf_corrected_P003_B

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-B")
    assert hit["target"]["iast"] == "kṛtrimam"
    assert derive_kRtrimam_ktri_kf_corrected_P003_B().flat_slp1() == "kftrimam"


def test_P003_C_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P003-C** (*uptrimam*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.uptrimam_ktri_quvap_corrected_P003_C_demo import derive_uptrimam_ktri_quvap_corrected_P003_C

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-C")
    assert hit["target"]["iast"] == "uptrimam"
    assert derive_uptrimam_ktri_quvap_corrected_P003_C().flat_slp1() == "uptrimam"


def test_P008_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P008** (*āste*): canonical derive() ← Asa~ laṭ kartarī 3sg (adādi gaṇa 2)."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P008")
    assert hit["target"]["iast"] == "āste"
    assert derive("Asa~", "laT", "kartari", 3, 1).flat_slp1() == "Aste"


def test_P006_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P006** (*cayanam*): reference row matches the corrected-v2 demo pipeline."""

    from pipelines.cayanam_ciY_lyuw_corrected_P006_demo import derive_cayanam_corrected_P006

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P006")
    assert hit["target"]["iast"] == "cayanam"
    assert derive_cayanam_corrected_P006().flat_slp1() == "cayanam"


def test_P004_C_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-C** (*brāhmaṇāḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.brAhmaRAH_prathamA_bahu_corrected_P004_C_demo import (
        derive_brAhmaRAH_prathamA_bahu_corrected_P004_C,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-C")
    assert hit["target"]["iast"] == "brāhmaṇāḥ"
    assert derive_brAhmaRAH_prathamA_bahu_corrected_P004_C().flat_slp1() == "brAhmaRAH"


def test_P004_D_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-D** (*vācā*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.vAcA_tRtIyA_strI_corrected_P004_D_demo import (
        derive_vAcA_tRtIyA_strI_corrected_P004_D,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-D")
    assert hit["target"]["iast"] == "vācā"
    assert derive_vAcA_tRtIyA_strI_corrected_P004_D().flat_slp1() == "vAcA"


def test_P004_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-B** (*śāṇḍikyaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.SANDikyaH_Yya_SRqika_corrected_P004_B_demo import (
        derive_SANDikyaH_Yya_SRqika_corrected_P004_B,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-B")
    assert hit["target"]["iast"] == "śāṇḍikyaḥ"
    assert derive_SANDikyaH_Yya_SRqika_corrected_P004_B().flat_slp1() == "SARqikyaH"


def test_P004_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-A** (*kauñjāyanyaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.kauYjAyanayaH_caPaY_yal_corrected_P004_A_demo import (
        derive_kauYjAyanayaH_caPaY_yal_corrected_P004_A,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-A")
    assert hit["target"]["iast"] == "kauñjāyanyaḥ"
    assert derive_kauYjAyanayaH_caPaY_yal_corrected_P004_A().flat_slp1() == "kOYjAyanyaH"


def test_P005_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P005-A** (*kurucarī*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.kurucarI_upapada_corrected_P005_A_demo import (
        derive_kurucarI_upapada_corrected_P005_A,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P005-A")
    assert hit["target"]["iast"] == "kurucarī"
    assert derive_kurucarI_upapada_corrected_P005_A().flat_slp1() == "kurucarI"


def test_P005_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P005-B** (*upasarajaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.upasarajaH_upapada_corrected_P005_B_demo import (
        derive_upasarajaH_upapada_corrected_P005_B,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P005-B")
    assert hit["target"]["iast"] == "upasarajaḥ"
    assert derive_upasarajaH_upapada_corrected_P005_B().flat_slp1() == "upasarajaH"


def test_P009_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P009** (*parikrīṇīte*): canonical derive() ← pari + krIY laṭ ātmanepada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P009")
    assert hit["target"]["iast"] == "parikrīṇīte"
    assert derive("krIY", "laT", "kartari", 3, 1, upasargas=["pari"]).flat_slp1() == "parikrIRIte"


def test_P010_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P010** (*āyacchate*): canonical derive() ← āṅ + yam laṭ ātmanepada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P010")
    assert hit["target"]["iast"] == "āyacchate"
    assert derive("yam", "laT", "kartari", 3, 1, upasargas=["A"]).flat_slp1() == "AyacCate"


def test_P011_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P011-A** (*utkurute*): canonical derive() ← ud + qukfY laṭ ātmanepada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P011-A")
    assert hit["target"]["iast"] == "utkurute"
    assert derive("qukfY", "laT", "kartari", 3, 1, upasargas=["ud"]).flat_slp1() == "utkurute"


def test_P011_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P011-B** (*upaskurute*): canonical derive() ← upa + qukfY laṭ ātmanepada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P011-B")
    assert hit["target"]["iast"] == "upaskurute"
    assert derive("qukfY", "laT", "kartari", 3, 1, upasargas=["upa"]).flat_slp1() == "upaskurute"


def test_P012_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P012** (*apajānīte*): canonical derive() ← apa + jYA laṭ ātmanepada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P012")
    assert hit["target"]["iast"] == "apajānīte"
    assert derive("jYA", "laT", "kartari", 3, 1, upasargas=["apa"]).flat_slp1() == "apajAnIte"


def test_P007_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P007** (*bhaṅguram*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.bhaNguram_Ghurac_corrected_P007_demo import derive_bhaNguram_corrected_P007

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P007")
    assert hit["target"]["iast"] == "bhaṅguram"
    assert derive_bhaNguram_corrected_P007().flat_slp1() == "BaNguram"


def test_P013_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P013** (*śuśrūṣate*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.zuSrUzate_san_Sru_corrected_P013_demo import (
        derive_zuSrUzate_san_Sru_corrected_P013,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P013")
    assert hit["target"]["iast"] == "śuśrūṣate"
    assert derive_zuSrUzate_san_Sru_corrected_P013().flat_slp1() == "SuSrUzate"


def test_P015_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P015** (*pāyayate*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.pAyayate_pa_Nic_corrected_P015_demo import (
        derive_pAyayate_pa_Nic_corrected_P015,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P015")
    assert hit["target"]["iast"] == "pāyayate"
    assert derive_pAyayate_pa_Nic_corrected_P015().flat_slp1() == "pAyayate"


def test_P014_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P014** (*īkṣāñcakre*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.IkzAYcakre_lit_Ikz_kf_corrected_P014_demo import (
        derive_IkzAYcakre_lit_Ikz_kf_corrected_P014,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P014")
    assert hit["target"]["iast"] == "īkṣāñcakre"
    assert derive_IkzAYcakre_lit_Ikz_kf_corrected_P014().flat_slp1() == "IkzAYcakre"


def test_P016_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P016** (*lohitāyati*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.lohitAyati_lat_lohita_kyaz_corrected_P016_demo import (
        derive_lohitAyati_lat_lohita_kyaz_corrected_P016,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P016")
    assert hit["target"]["iast"] == "lohitāyati"
    assert derive_lohitAyati_lat_lohita_kyaz_corrected_P016().flat_slp1() == "lohitAyati"


def test_P017_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P017** (*paṭapaṭāyati*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.pawapawAyati_anukaraNa_corrected_P017_demo import (
        derive_pawapawAyati_anukaraNa_corrected_P017,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P017")
    assert hit["target"]["iast"] == "paṭapaṭāyati"
    assert derive_pawapawAyati_anukaraNa_corrected_P017().flat_slp1() == "pawapawAyati"


def test_P018_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P018-A** (*vyadyutat*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.vyadyutat_luN_dyut_corrected_P018_A_demo import (
        derive_vyadyutat_luN_dyut_corrected_P018_A,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P018-A")
    assert hit["target"]["iast"] == "vyadyutat"
    assert derive_vyadyutat_luN_dyut_corrected_P018_A().flat_slp1() == "vyadyutat"


def test_P018_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P018-B** (*vyadyotiṣṭa*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.vyadyotizwa_luN_dyut_corrected_P018_B_demo import (
        derive_vyadyotizwa_luN_dyut_corrected_P018_B,
    )

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P018-B")
    assert hit["target"]["iast"] == "vyadyotiṣṭa"
    assert derive_vyadyotizwa_luN_dyut_corrected_P018_B().flat_slp1() == "vyadyotizwa"


def test_P019_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P019** (*avartsyat*): canonical derive() ← vftu~ lṛṅ kartarī 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P019")
    assert hit["target"]["iast"] == "avartsyat"
    assert derive("vftu~", "lRG", "kartari", 3, 1).flat_slp1() == "avartsyat"
