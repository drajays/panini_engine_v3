"""Unit tests for ``pipelines/paYcendra_prakriya_42_demo.py`` (``prakriya_42``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.paYcendra_prakriya_42_demo import derive_paYcendra_prakriya_42


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_42_json_note_and_spine():
    """JSON lists **2.1.50**; canonical *taddhitārthottarapada* rule is **2.1.51** (*ashtadhyayi-com*)."""
    s = derive_paYcendra_prakriya_42()
    ids = _trace_ids(s)
    assert ids.index("2.1.3") < ids.index("2.1.51")
    assert ids.index("2.1.51") < ids.index("4.1.76")
    assert ids.index("4.1.76") < ids.index("4.1.88")
    assert s.samjna_registry.get("2.1.51_taddhitartha_samAhAra_prakriya_42") is True
    assert s.samjna_registry.get("4.1.88_dvigor_lug_anapatye_prakriya_42") is True
    assert s.flat_slp1() == "paYcendra"
