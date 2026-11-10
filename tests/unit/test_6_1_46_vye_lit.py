"""6.1.46 na vyo liṭi: vyeñ keeps its e in liṭ (Kāśikā 6.1.46: संविव्याय। संविव्ययिथ); 6.1.17 samprasāraṇa of the abhyāsa,
7.2.115 vṛddhi of the final e (ec -> aic, 1.1.50), 6.1.78 ay -> vivyāya. (The brain calls it a vārttika; the DB has it as the sūtra.)"""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


def loop(ref, lak, pu, vc, pada=None):
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface


def recipe(upadesha, lak, pu, vc, pada=None):
    from pipelines.tinanta import derive
    return derive(upadesha, lak, "kartari", pu, vc, pada=pada).render()

VYE = "BvAdi_01_1162"


def test_loop_vivyaya():
    assert loop(VYE, "liT", 3, 1, "parasmai") == "vivyAya"
    assert loop(VYE, "liT", 2, 1, "parasmai") == "vivyayiTa"      # Kāśikā 7.2.66 saṃvivyayitha
    assert loop(VYE, "liT", 3, 2, "parasmai") == "vivyatuH"       # Bhāṣya 8.2.78 saṃvivyatuḥ


def test_recipe_derive_vivyaya():
    assert recipe("vyeY", "liT", 3, 1, "parasmai") == "vivyAya"
    assert recipe("vyeY", "liT", 2, 1, "parasmai") == "vivyayiTa"


def test_vrddhi_of_e_final_ang():
    from sutras.adhyaya_7.pada_2.sutra_7_2_115 import _vrddhi_vowel
    from engine.state import State
    assert _vrddhi_vowel("e", State(terms=[])) == "E" and _vrddhi_vowel("o", State(terms=[])) == "O"
