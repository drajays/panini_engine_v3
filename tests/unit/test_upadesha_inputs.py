"""Inputs enter the prakriyā in aupadeśika form, never as finished products.

- tiṅ: 3.4.78 gives every lakāra the same eighteen ādeśas (तिप्, तस्, झि …);
  lakāra-specific shapes (सीयुट्, सुट्, चिण् …) are made by sūtras, not stored.
- dhātu: the dhātupāṭha row carries its it-markers and anunāsika
  (ashtadhyayi.com/dhatu "औपदेशिकः" column, e.g. एधँ, गाधृँ, गमॢँ).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[2]


def _tin_table() -> dict:
    return json.loads((_ROOT / "data/inputs/tin_upadesha.json").read_text())


def test_every_lakara_has_the_same_eighteen_tin_upadesha():
    table = _tin_table()
    lat = {k.split("-", 1)[1]: v for k, v in table.items() if k.startswith("laT-")}
    assert len(lat) == 18
    for key, val in table.items():
        if key == "_doc":
            continue
        lakara, rest = key.split("-", 1)
        assert val == lat[rest], f"{key}: {val!r} is not the 3.4.78 upadeśa {lat[rest]!r}"


def test_jhi_is_slp1_Ji_not_j_h_i():
    assert "jhi" not in _tin_table().values()


def test_no_karmani_luG_shortcut_rows():
    assert not [k for k in _tin_table() if "karmani" in k]


# ashtadhyayi.com readings we deliberately do not follow:
#   01.0208 पेबृँ — upstream "पेबृ" drops the ँ its own neighbours (पेवृँ …) carry;
#   01.0925 छदँ — upstream "छदिः" is the इका निर्देश citation, not the upadeśa.
#   02.0007 चक्षिँङ् — upstream Devanāgarī "चक्षिङ्" drops the ँ its own SLP1 row (ca\kzi~\N) has; 1.3.2 decides:
#           only the anunāsika reading yields the attested चक्ष् (AMENDMENT 20 §2.3).
_KNOWN_DIVERGENCES = {"01.0208", "01.0925", "02.0007"}


def test_dhatupatha_upadesha_matches_ashtadhyayi_com_aupadeshik():
    upstream = json.loads((_ROOT / "data/upstream/ashtadhyayi_dhatu_data.json").read_text())
    aupadeshik = {r["baseindex"]: r["aupadeshik"] for r in upstream["data"]}
    entries = json.loads((_ROOT / "data/inputs/dhatupatha_upadesha.json").read_text())["entries"]
    bad = [
        (e["dhatupatha_id"], e["upadesha_dev"], aupadeshik[e["dhatupatha_id"]])
        for e in entries
        if e["dhatupatha_id"] in aupadeshik
        and e["dhatupatha_id"] not in _KNOWN_DIVERGENCES
        and e["upadesha_dev"] != aupadeshik[e["dhatupatha_id"]]
    ]
    assert not bad, bad[:20]


@pytest.mark.parametrize("dhatu_id, upadesha_dev", [("01.0002", "एधँ"), ("01.0004", "गाधृँ")])
def test_dhatupatha_examples(dhatu_id, upadesha_dev):
    entries = json.loads((_ROOT / "data/inputs/dhatupatha_upadesha.json").read_text())["entries"]
    assert [e["upadesha_dev"] for e in entries if e["dhatupatha_id"] == dhatu_id][0] == upadesha_dev


@pytest.mark.parametrize(
    "ref, upadesha_slp1",
    [
        ("qupaca~z", "qupaca~z"),        # डुपचँष् — anunāsika still on the tape
        ("gamx~", "gamx~"),             # गमॢँ
        ("Adadi_02_0059", "vida~"),     # विदँ
        ("BvAdi_01_1165", "wuo~Svi"),   # टुओँश्वि
    ],
)
def test_krdanta_tape_starts_from_upadesha(ref, upadesha_slp1):
    from pipelines.krdanta import build_dhatu_state

    s = build_dhatu_state(ref)
    assert s.terms[0].meta.get("upadesha_slp1") == upadesha_slp1
    assert s.flat_slp1() == upadesha_slp1
