"""7.1.35 तुह्योस्तातङ्ङाशिष्यन्यतरस्याम्: in the blessing sense tu / hi → tātaṅ, optionally.
Gold: Kāśikā 7.1.35 (जीवताद् भवान् · जीवतात् त्वम् · जीवतु भवान् · जीव त्वम्) and the user-supplied भू prakriyā."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from engine.vikalpa import choose
from tools.autonomy_report import run_autonomously, start_state


def _run(dhatu, purusha, vacana, *, ashis, take=True):
    case = NS(kind="tinanta", args=(dhatu, "loT", purusha, vacana), ashis=ashis)
    with choose({"7.1.35": take}):
        return run_autonomously(start_state(case), "", dhatu, 150)


@pytest.mark.parametrize("dhatu,gold", [("jIv", "jIvatAt"), ("BU", "BavatAt")])
@pytest.mark.parametrize("purusha", [3, 2])          # tu (3sg) and hi (2sg) alike
def test_blessing_takes_tAtaN(dhatu, purusha, gold):
    run = _run(dhatu, purusha, 1, ashis=True)
    assert run.surface == gold
    assert [s[0] for s in run.steps].count("7.1.35") == 1


def test_the_other_reading_is_the_ordinary_loT():
    assert _run("jIv", 3, 1, ashis=True, take=False).surface == "jIvatu"     # जीवतु भवान्
    assert _run("jIv", 2, 1, ashis=True, take=False).surface == "jIva"       # जीव त्वम्, via 6.4.105


@pytest.mark.parametrize("cell", [(3, 1), (2, 1)])
def test_without_the_blessing_sense_it_never_fires(cell):
    run = _run("BU", *cell, ashis=False)
    assert "7.1.35" not in [s[0] for s in run.steps]


def test_only_tu_and_hi_are_replaced():
    for cell in [(3, 2), (3, 3), (2, 2), (2, 3), (1, 1)]:
        assert "7.1.35" not in [s[0] for s in _run("BU", *cell, ashis=True).steps]
