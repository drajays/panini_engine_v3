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

    from pipelines.krdanta import derive_bhinnaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-A")
    assert hit["target"]["iast"] == "bhinnaḥ"
    assert derive_bhinnaH().flat_slp1() == "bhinnaH"


def test_P001_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-B** (*dhṛṣṭaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_DfzwaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-B")
    assert hit["target"]["iast"] == "dhṛṣṭaḥ"
    assert derive_DfzwaH().flat_slp1() == "DfzwaH"


def test_P001_C_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-C** (*svinnaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_svinnaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-C")
    assert hit["target"]["iast"] == "svinnaḥ"
    assert derive_svinnaH().flat_slp1() == "svinnaH"


def test_P001_D_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P001-D** (*iddhaḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_idDaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P001-D")
    assert hit["target"]["iast"] == "iddhaḥ"
    assert derive_idDaH().flat_slp1() == "idDaH"


def test_P002_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P002-A** (*vepathuḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_vepathuH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P002-A")
    assert hit["target"]["iast"] == "vepathuḥ"
    assert derive_vepathuH().flat_slp1() == "vepathuH"


def test_P002_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P002-B** (*śvayathuḥ*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_zvayathuH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P002-B")
    assert hit["target"]["iast"] == "śvayathuḥ"
    assert derive_zvayathuH().flat_slp1() == "zvayathuH"


def test_P003_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P003-A** (*paktrimam*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_paktrimam

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-A")
    assert hit["target"]["iast"] == "paktrimam"
    assert derive_paktrimam().flat_slp1() == "paktrimam"


def test_P003_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P003-B** (*kṛtrimam*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_krtrimam

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-B")
    assert hit["target"]["iast"] == "kṛtrimam"
    assert derive_krtrimam().flat_slp1() == "kftrimam"


def test_P003_C_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P003-C** (*uptrimam*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.krdanta import derive_uptrimam

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P003-C")
    assert hit["target"]["iast"] == "uptrimam"
    assert derive_uptrimam().flat_slp1() == "uptrimam"


def test_P008_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P008** (*āste*): canonical derive() ← Asa~ laṭ kartarī 3sg (adādi gaṇa 2)."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P008")
    assert hit["target"]["iast"] == "āste"
    assert derive("Asa~", "laT", "kartari", 3, 1).flat_slp1() == "Aste"


def test_P006_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P006** (*cayanam*): canonical krdanta.derive_cayanam()."""

    from pipelines.krdanta import derive_cayanam

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P006")
    assert hit["target"]["iast"] == "cayanam"
    assert derive_cayanam().flat_slp1() == "cayanam"


def test_P004_C_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-C** (*brāhmaṇāḥ*): canonical subanta.derive()."""

    from pipelines.subanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-C")
    assert hit["target"]["iast"] == "brāhmaṇāḥ"
    assert derive("brAhmaRa", vibhakti=1, vacana=3, linga="pulliṅga").flat_slp1() == "brAhmaRAH"


def test_P004_D_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-D** (*vācā*): canonical subanta.derive()."""

    from pipelines.subanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-D")
    assert hit["target"]["iast"] == "vācā"
    assert derive("vAc", vibhakti=3, vacana=1, linga="strīliṅga").flat_slp1() == "vAcA"


def test_P004_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-B** (*śāṇḍikyaḥ*): canonical taddhita.derive_SANqikyaH()."""

    from pipelines.taddhita import derive_SANqikyaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-B")
    assert hit["target"]["iast"] == "śāṇḍikyaḥ"
    assert derive_SANqikyaH().flat_slp1() == "SARqikyaH"


def test_P004_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P004-A** (*kauñjāyanyaḥ*): canonical taddhita.derive_kauYjAyanyaH()."""

    from pipelines.taddhita import derive_kauYjAyanyaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P004-A")
    assert hit["target"]["iast"] == "kauñjāyanyaḥ"
    assert derive_kauYjAyanyaH().flat_slp1() == "kOYjAyanyaH"


def test_P005_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P005-A** (*kurucarī*): canonical upapada_krt.derive_kurucarI()."""

    from pipelines.upapada_krt import derive_kurucarI

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P005-A")
    assert hit["target"]["iast"] == "kurucarī"
    assert derive_kurucarI().flat_slp1() == "kurucarI"


def test_P005_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P005-B** (*upasarajaḥ*): canonical upapada_krt.derive_upasarajaH()."""

    from pipelines.upapada_krt import derive_upasarajaH

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P005-B")
    assert hit["target"]["iast"] == "upasarajaḥ"
    assert derive_upasarajaH().flat_slp1() == "upasarajaH"


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
    """**P007** (*bhaṅguram*): canonical krdanta.derive_bhaNguram()."""

    from pipelines.krdanta import derive_bhaNguram

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P007")
    assert hit["target"]["iast"] == "bhaṅguram"
    assert derive_bhaNguram().flat_slp1() == "BaNguram"


def test_P013_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P013** (*śuśrūṣate*): canonical derive() ← Śru laṭ ātmanepada 3sg desiderative."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P013")
    assert hit["target"]["iast"] == "śuśrūṣate"
    assert derive("Sru", "laT", "kartari", 3, 1, san_recipe=True).flat_slp1() == "SuSrUzate"


def test_P015_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P015** (*pāyayate*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P015")
    assert hit["target"]["iast"] == "pāyayate"
    assert derive("pA", "laT", "kartari", 3, 1, nic_recipe=True).flat_slp1() == "pAyayate"


def test_P014_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P014** (*īkṣāñcakre*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.tinanta import derive_periphrastic_lit

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P014")
    assert hit["target"]["iast"] == "īkṣāñcakre"
    assert derive_periphrastic_lit("Ikz", 3, 1).flat_slp1() == "IkzAYcakre"


def test_P016_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P016** (*lohitāyati*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.tinanta import derive_denominative_laT

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P016")
    assert hit["target"]["iast"] == "lohitāyati"
    assert derive_denominative_laT("lohita", 3, 1).flat_slp1() == "lohitAyati"


def test_P017_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P017** (*paṭapaṭāyati*): bundle IAST ↔ engine SLP1 surface."""

    from pipelines.tinanta import derive_anukarana_laT

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P017")
    assert hit["target"]["iast"] == "paṭapaṭāyati"
    assert derive_anukarana_laT("pawat", 3, 1).flat_slp1() == "pawapawAyati"


def test_P018_A_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P018-A** (*vyadyutat*): canonical derive() ← vi + dyuta~ luṅ kartarī parasmaipada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P018-A")
    assert hit["target"]["iast"] == "vyadyutat"
    assert derive("dyuta~", "luG", "kartari", 3, 1, upasargas=["vi"]).flat_slp1() == "vyadyutat"


def test_P018_B_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P018-B** (*vyadyotiṣṭa*): canonical derive() ← vi + dyuta~ luṅ ātmanepada 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P018-B")
    assert hit["target"]["iast"] == "vyadyotiṣṭa"
    assert derive("dyuta~", "luG", "kartari", 3, 1, upasargas=["vi"], pada="atmane").flat_slp1() == "vyadyotizwa"


def test_P019_bundle_target_matches_pipeline(corrected_v2: dict) -> None:
    """**P019** (*avartsyat*): canonical derive() ← vftu~ lṛṅ kartarī 3sg."""

    from pipelines.tinanta import derive

    hit = next(p for p in corrected_v2["prakriyas"] if p["id"] == "P019")
    assert hit["target"]["iast"] == "avartsyat"
    assert derive("vftu~", "lRG", "kartari", 3, 1).flat_slp1() == "avartsyat"
