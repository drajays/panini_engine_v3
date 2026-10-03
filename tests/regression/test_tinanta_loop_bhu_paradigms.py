"""Gate C, tiṅanta: every parasmaipada bhū cell of the ten lakāras is derived by the loop (scheduler → resolver →
apply_rule), with no recipe choosing the order. After vivakṣā has chosen the lakāra and the tiṅ, everything else is the loop's.

Gold: laṭ · liṭ · laṅ · loṭ · lṛṭ — the independent Vidyut oracle (`bench/oracle/vidyut.csv`, Art. 19: it can prove us
wrong, never right). luṭ · luṅ · liṅ · āśīrliṅ · lṛṅ — the standard paradigm (the recipe's, which the oracle does not cover)."""
import csv
from pathlib import Path
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state

CELLS = [(p, v) for p in (3, 2, 1) for v in (1, 2, 3)]
STANDARD = {
    "luT": ["BavitA", "BavitArO", "BavitAraH", "BavitAsi", "BavitAsTaH", "BavitAsTa", "BavitAsmi", "BavitAsvaH", "BavitAsmaH"],
    "luG": ["aBUt", "aBUtAm", "aBUvan", "aBUH", "aBUtam", "aBUta", "aBUvam", "aBUva", "aBUma"],
    "liG": ["Bavet", "BavetAm", "BaveyuH", "BaveH", "Bavetam", "Baveta", "Baveyam", "Baveva", "Bavema"],
    "AsIrliG": ["BUyAt", "BUyAstAm", "BUyAsuH", "BUyAH", "BUyAstam", "BUyAsta", "BUyAsam", "BUyAsva", "BUyAsma"],
    "lRG": ["aBavizyat", "aBavizyatAm", "aBavizyan", "aBavizyaH", "aBavizyatam", "aBavizyata", "aBavizyam",
            "aBavizyAva", "aBavizyAma"],
}


def _oracle():
    out = {}
    with (Path(__file__).resolve().parents[2] / "bench" / "oracle" / "vidyut.csv").open(encoding="utf-8") as fp:
        for row in csv.DictReader(fp):
            kind, dhatu, lak, p, v = (row["key"].split(":") + [None] * 5)[:5]
            if kind == "tinanta" and dhatu == "BU":
                out[(lak, int(p), int(v))] = [f for f in row["forms"].split("|") if f]
    return out


ORACLE = _oracle()


def _loop(lakara, p, v):
    return run_autonomously(start_state(NS(kind="tinanta", args=("BU", lakara, p, v))), "", "BU", 250).surface


@pytest.mark.parametrize("lakara,p,v", sorted(ORACLE), ids=lambda x: str(x))
def test_bhu_cell_matches_the_oracle(lakara, p, v):
    assert _loop(lakara, p, v) in ORACLE[(lakara, p, v)]


@pytest.mark.parametrize("lakara", sorted(STANDARD))
def test_bhu_paradigm_matches_the_standard_forms(lakara):
    assert [_loop(lakara, p, v) for p, v in CELLS] == STANDARD[lakara]
