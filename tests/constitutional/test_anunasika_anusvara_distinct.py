"""
Art. 4 §2 (AMENDMENT 20) — anunāsika (ँ, SLP1 '~') and anusvāra (ं, SLP1 'M') are different phonemes.
1.3.2 उपदेशेऽजनुनासिक इत् depends on the difference, so no code path may merge them or move ँ off its vowel.
"""
from __future__ import annotations

import json
import pathlib

import pytest

from phonology.joiner import slp1_to_devanagari
from phonology.tokenizer import devanagari_to_slp1_flat, devanagari_to_varnas
from phonology.varna import parse_slp1_upadesha_sequence

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _tags(varnas):
    return [(v.slp1, "anunasika" in v.tags) for v in varnas]


def test_candrabindu_and_anusvara_tokenize_differently():
    a = devanagari_to_varnas("रुँ")
    m = devanagari_to_varnas("रुं")
    assert _tags(a) == [("r", False), ("u", True)]
    assert [v.slp1 for v in m] == ["r", "u", "M"] and not any("anunasika" in v.tags for v in m)
    assert devanagari_to_slp1_flat("नपुँसकात्") == "napu~sakAt" != devanagari_to_slp1_flat("नपुंसकात्")


@pytest.mark.parametrize("dev,slp", [
    ("रुँ", "ru~"), ("सुँ", "su~"), ("एधँ", "eDa~"), ("डुपचँष्", "qupaca~z"), ("ञिष्वपँ", "Yizvapa~"),
    ("गमॢँ", "gamx~"), ("सँस्कर्ता", "sa~skartA"), ("सँश्च", "sa~Sca"), ("नपुँसकात्", "napu~sakAt"),
    ("संहितायाम्", "saMhitAyAm"), ("अंश", "aMSa"),
])
def test_round_trip(dev, slp):
    assert devanagari_to_slp1_flat(dev) == slp
    assert slp1_to_devanagari(parse_slp1_upadesha_sequence(slp)) == dev
    assert slp1_to_devanagari(devanagari_to_varnas(dev)) == dev


def test_candrabindu_position_is_phonemic():
    # different upadeśas must render differently
    assert slp1_to_devanagari(parse_slp1_upadesha_sequence("Ga~wa")) == "घँट"
    assert slp1_to_devanagari(parse_slp1_upadesha_sequence("Gawa~")) == "घटँ"


@pytest.mark.parametrize("short,full", [("han~", "hana~"), ("jan~", "jana~"), ("qupac~z", "qupaca~z"), ("ad~", "ada~")])
def test_tilde_after_consonant_is_its_inherent_a(short, full):
    assert _tags(parse_slp1_upadesha_sequence(short)) == _tags(parse_slp1_upadesha_sequence(full))


def test_dhatupatha_upadesha_dev_and_slp1_agree_on_anunasika():
    """Every dhātu: its Devanāgarī and SLP1 upadeśa mark the same vowels anunāsika (same varṇa tags)."""
    d = json.loads((ROOT / "data/inputs/dhatupatha_upadesha.json").read_text(encoding="utf-8"))
    bad = []
    for e in d["entries"]:
        dev, slp = e.get("upadesha_dev") or "", e.get("upadesha_slp1") or ""
        if not dev or not slp:
            continue
        if dev.count("ँ") != slp.count("~") or dev.count("ं") != slp.count("M"):
            bad.append((e["id"], dev, slp))
    assert not bad, f"{len(bad)} dhātus disagree on anunāsika/anusvāra: {bad[:10]}"


def test_it_prakarana_applies_1_3_2_to_every_dhatu():
    """Run the engine's own it-prakaraṇa (1.3.2–1.3.9 sūtra files) on every dhātupāṭha upadeśa.
    Count what Pāṇini's rules say must go: anunāsika vowels (1.3.2), a final hal (1.3.3), initial ñi/ṭu/ḍu (1.3.5),
    and the vārttika इर इत्संज्ञा वाच्या. No anunāsika vowel may survive 1.3.9."""
    import sutras  # noqa: F401
    from phonology.varna import AC_DEV
    from pipelines.it_prakarana import run_it_prakarana
    from pipelines.krdanta import build_dhatu_state

    entries = json.loads((ROOT / "data/inputs/dhatupatha_upadesha.json").read_text(encoding="utf-8"))["entries"]
    bad = []
    for e in entries:
        vs = parse_slp1_upadesha_sequence(e["upadesha_slp1"].replace("\\", "").replace("^", ""))
        s = "".join(v.slp1 for v in vs)
        expect = (len(vs) - sum("anunasika" in v.tags for v in vs)
                  - (1 if vs and vs[-1].slp1 not in AC_DEV and vs[-1].slp1 not in ("M", "H") else 0)
                  - (2 if s[:2] in ("Yi", "wu", "qu") else 0)
                  - (1 if s.endswith("ir") and "anunasika" not in vs[-2].tags else 0))
        left = [v for t in run_it_prakarana(build_dhatu_state(e["id"])).terms for v in t.varnas]
        if len(left) != expect or any("anunasika" in v.tags for v in left):
            bad.append((e["id"], e["upadesha_slp1"], "".join(v.slp1 for v in left)))
    assert not bad, f"{len(bad)} dhātus: it-prakaraṇa disagrees with 1.3.2–1.3.5: {bad[:10]}"
