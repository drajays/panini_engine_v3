"""Periphrastic liṭ through the loop: 3.1.36 ām → 2.4.81 liṭ-luk → 3.1.40 kṛ's own liṭ (no word-specific code);
and kṛ's liṭ 1sg is cakāra (7.1.34 needs a final ā, not ṛ's vṛddhi pending rapara)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,want", [("qukfY", "cakAra"), ("idi~", "indAYcakAra"), ("uKi~", "uNKAYcakAra"),
                                        ("oKf~", "oKAYcakAra"), ("arda~", "Anarda"), ("agi~", "AnaNga")])
def test_liT_1sg(dhatu, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, "liT", 1, 1))), "", dhatu, 250).surface == want
