"""8.3.78 names ṣīdhvam: the dh of āśīr-liṅ's ṣīdhvam turns ḍh after an iṇ-final aṅga (ashtadhyayi.com examples
कृषीढ्वं, नाध्यगीढ्वं; AMENDMENT 18). After an iṭ it is 8.3.79 विभाषेटः (default: unchanged). Vidyut gives kfzIDvam — outvoted."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,lakara,want", [
    ("qukfY", "AsIrliG", "kfzIQvam"),      # kṛṣīḍhvam
    ("eDa~", "AsIrliG", "eDizIDvam"),      # iṭ: 8.3.79 vibhāṣā, default no ḍhatva
    ("eDa~", "liG", "eDeDvam"),            # vidhi-liṅ has no ṣīdhvam
])
def test_sidhvam(dhatu, lakara, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, 2, 3), pada="atmane")), "", dhatu, 250).surface == want
