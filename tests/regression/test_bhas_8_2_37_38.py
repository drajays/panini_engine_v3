"""8.2.37 bhaṣ for an ekāc dhātu whose last letter is jhaṣ (after 8.2.32 dugh-): Dokzi; 8.2.38 dadhaḥ + 8.2.40 adhaḥ:
DattaH, DatTa. Evidence: ashtadhyayi.com sutra_prayogas (विजिघृक्षु, अधाक्षीत्, अभिधत्त, अन्तर्धत्स्व) — AMENDMENT 18."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [
    ("duha~", "laT", 2, 1, "Dokzi"), ("diha~", "laT", 2, 1, "Dekzi"),
    ("quDAY", "laT", 3, 2, "DattaH"), ("quDAY", "laT", 2, 2, "DatTaH"), ("quDAY", "laT", 2, 3, "DatTa"),
    ("quDAY", "laT", 3, 1, "daDAti"), ("quDAY", "laT", 1, 2, "daDvaH"),
])
def test_cell(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want
