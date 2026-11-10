"""6.4.34 शास इदङ्हलोः (Kāśikā: "हलादौ किति — शिष्टः ... ङिति — आवां शिष्वः"; "इत्वे कृते शासिवसिघसीनां च 8.3.60 षत्वम्").
The dhātupāṭha has two śāsu rows; 2.12 is āṅ-śāsu (icchāyām, āśāste) which 6.4.34 excludes, 2.70 is śāsu anuśiṣṭau."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


def loop(ref, lak, pu, vc, pada=None):
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface


def recipe(upadesha, lak, pu, vc, pada=None):
    from pipelines.tinanta import derive
    return derive(upadesha, lak, "kartari", pu, vc, pada=pada).render()

SAS = "Adadi_02_0070"


def test_hal_initial_ngit():
    assert loop(SAS, "laT", 3, 2) == "SizwaH"
    assert loop(SAS, "laT", 1, 2) == "SizvaH"
    assert loop(SAS, "laT", 1, 3) == "SizmaH"
    assert recipe(SAS, "laT", 3, 2) == "SizwaH"


def test_vowel_initial_and_pit_untouched():
    assert loop(SAS, "laT", 3, 1) == "SAsti"          # pit tip: no ṅidvat
    assert loop(SAS, "laT", 3, 3) == "SAsati"         # vowel-initial: no iṭva (Kāśikā: शासति)


def test_ang_laG():
    assert loop(SAS, "laG", 3, 2) == "aSizwAm"
