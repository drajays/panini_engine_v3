"""AMENDMENT 30 — open vivakṣā: per-key schema fields, the read-only asked-key trace, probe-and-replay exploration."""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from engine.state import State
from engine.vivaksha import key_meta, record_asked, schema, vivaksita
from engine.vivaksha_explore import DEFAULT, OPEN, derive_all
from pipelines.tinanta import derive

ENTRIES = {"tinanta", "krdanta", "taddhita", "subanta", "samasa"}


def test_every_key_has_its_fields():
    for key in schema():
        meta = key_meta(key)
        assert meta["kind"] in ("intent", "context"), key
        assert meta["default"] is None, key              # the unmarked value: the key is not set
        assert meta["applies_to"] and set(meta["applies_to"]) <= ENTRIES, key
        assert isinstance(meta["requires"], list), key
        assert meta["gloss_dev"] and meta["gloss_en"], key


def test_new_keys_are_cited_and_context_is_marked():
    for key in ("vadArTa", "vyaktavAk", "samuccAraRa", "vipralApa", "karmakatva", "BujArTa"):
        assert all(e["sutras"] for e in schema()[key].values()), key
    assert {k for k in ("vyaktavAk", "samuccAraRa", "vipralApa", "karmakatva") if key_meta(k)["kind"] == "context"} == {
        "vyaktavAk", "samuccAraRa", "vipralApa", "karmakatva"}
    assert key_meta("vadArTa")["kind"] == key_meta("BujArTa")["kind"] == "intent"


def test_vivaksita_trace_is_read_only():
    state = State(terms=[])
    state.vivaksha["vadArTa"] = "yatna"
    assert vivaksita(state, "vadArTa", "yatna") is True               # no recorder: nothing recorded, same answer
    with record_asked() as asked:
        assert vivaksita(state, "vadArTa", "BAsana") is False
        assert vivaksita(state, "vadArTa", "yatna") is True
    assert asked == {"vadArTa"}
    assert state.vivaksha == {"vadArTa": "yatna"}


def test_a_derivation_asking_no_open_key_is_todays_single_branch():
    today = derive("BU", "laT", "kartari", 3, 1)
    (only,) = derive_all("tinanta", "BU", "laT", "kartari", 3, 1, vivaksha={"vadArTa": OPEN, "BujArTa": OPEN})
    assert only.surface_slp1 == today.flat_slp1() and only.choices == ()
    (only,) = derive_all("tinanta", "BU", "laT", "kartari", 3, 1)
    assert only.surface_slp1 == today.flat_slp1() and only.choices == ()


def test_default_is_the_unmarked_value():
    plain = derive("vada~", "laT", "kartari", 3, 1)
    (b,) = derive_all("tinanta", "vada~", "laT", "kartari", 3, 1, vivaksha={"vadArTa": DEFAULT})
    assert b.surface_slp1 == plain.flat_slp1() == "vadati" and b.choices == ()


def test_open_key_replays_once_per_value_and_tags_the_meaning():
    got = {b.choices: b.surface_slp1 for b in derive_all("tinanta", "vada~", "laT", "kartari", 3, 1, vivaksha={"vadArTa": OPEN})}
    assert got[()] == "vadati"
    senses = set(schema()["vadArTa"])
    assert {c[0][2] for c in got if c} == senses
    assert all(s == "vadate" for c, s in got.items() if c)


def test_context_key_is_never_open_and_unknown_values_are_refused():
    with pytest.raises(ValueError):
        derive_all("tinanta", "vada~", "laT", "kartari", 3, 1, vivaksha={"vipralApa": OPEN})
    with pytest.raises(ValueError):
        derive_all("tinanta", "vada~", "laT", "kartari", 3, 1, vivaksha={"vadArTa": "nonsense"})
    with pytest.raises(ValueError):
        derive_all("tinanta", "vada~", "laT", "kartari", 3, 1, vivaksha={"taddhitArtha": OPEN})      # applies to taddhita only


def test_tinanta_derive_takes_vivaksha_and_a_fixed_value_is_on_the_tape():
    assert derive("vada~", "laT", "kartari", 3, 1, vivaksha={"vadArTa": "BAsana"}).vivaksha["vadArTa"] == "BAsana"
    with pytest.raises(ValueError):
        derive("vada~", "laT", "kartari", 3, 1, vivaksha={"vadArTa": OPEN})          # OPEN is for derive_all, not a value
