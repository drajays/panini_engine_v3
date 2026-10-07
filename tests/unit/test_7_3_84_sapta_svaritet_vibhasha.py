"""7.3.84, सप्त स्वरितेतः (ऋणु/तृणु/क्षिणु): SK (upstream/sutraani/kaumudi.txt
i=24079) gives both forms for each — ऋणोति/अर्णोति, तृणोति/तर्णोति,
क्षिणोति/क्षेणोति — citing "संज्ञापूर्वको विधिरनित्यः": आत्रेयादयः treat the
root-vowel (उपधा-ish) guṇa as अनित्य, अन्ये as नित्य. docs/PARKED_ISSUES.md
item (b): the loṭ 2sg cell (अर्णुहि / ऋणु) is this same vikalpa seen through
6.4.106's asaṃyogapūrva test — the guṇa branch's root cluster rR blocks hi-luk,
the declined branch's single ण् does not.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.vikalpa import choose, explore
from pipelines.dhatupatha import resolve_dhatu_identifier
from pipelines.tinanta import derive

_VIBHASHA_ID = "7.3.84_sapta_svaritet_upadha_guna"


def _derive(upadesha: str, lakara: str, purusha: int, vacana: int):
    row = resolve_dhatu_identifier(upadesha)
    return lambda: derive(row["id"], lakara, "kartari", purusha, vacana, pada="parasmai")


def test_fRu_laT_3sg_both_forms() -> None:
    branches = explore(_derive("fRu~", "laT", 3, 1))
    surfaces = {b.surface_slp1 for b in branches}
    assert surfaces == {"arRoti", "fRoti"}


def test_fRu_loT_2sg_both_forms_matches_vidyut() -> None:
    branches = explore(_derive("fRu~", "loT", 2, 1))
    surfaces = {b.surface_slp1 for b in branches}
    assert surfaces == {"arRuhi", "fRu"}


def test_tfRu_laT_3sg_both_forms() -> None:
    branches = explore(_derive("tfRu~", "laT", 3, 1))
    surfaces = {b.surface_slp1 for b in branches}
    assert surfaces == {"tarRoti", "tfRoti"}


def test_kziRu_laT_3sg_both_forms() -> None:
    branches = explore(_derive("kziRu~", "laT", 3, 1))
    surfaces = {b.surface_slp1 for b in branches}
    assert surfaces == {"kzeRoti", "kziRoti"}


def test_unrelated_tanadi_root_unaffected() -> None:
    """tanu~^ (तनु) is not in the SK-attested pair-list — single form only."""
    row = resolve_dhatu_identifier("tanu~")
    s = derive(row["id"], "laT", "kartari", 3, 1, pada="parasmai")
    assert s.flat_slp1() == "tanoti"
    ids = [e.get("sutra_id") for e in s.trace]
    assert _VIBHASHA_ID not in ids


def test_declined_branch_still_gunas_the_vikarana_u() -> None:
    """The declined (no root-guṇa) branch still shows उ→ओ (वृत्ति-स्तरीय दूसरा गुण) —
    ऋणोति, not ऋणुति."""
    with choose({_VIBHASHA_ID: False}):
        row = resolve_dhatu_identifier("fRu~")
        s = derive(row["id"], "laT", "kartari", 3, 1, pada="parasmai")
    assert s.flat_slp1() == "fRoti"
