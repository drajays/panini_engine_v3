"""A विभाषा reading chosen in one thread must not reach a derivation in another (engine/vikalpa.py).

The web UI serves requests on parallel threads. With a process-wide policy, two overlapping ``choose()`` blocks could
restore each other's snapshot, leaving 8.4.47 अनचि च switched on for every later request (भयम् → भयम्म्, the
Bhagavad-gītā 16.1 reader rows).
"""
from __future__ import annotations

import threading

from engine.vikalpa import _POLICY, choose, policy_choice


def _in_thread(fn):
    out = {}
    t = threading.Thread(target=lambda: out.setdefault("v", fn()))
    t.start()
    t.join()
    return out["v"]


def test_overlapping_choose_blocks_leave_no_policy_behind():
    a_in, b_in, a_out = threading.Event(), threading.Event(), threading.Event()

    def a():
        with choose({"8.4.47": True}):
            a_in.set()
            b_in.wait()
        a_out.set()

    def b():
        a_in.wait()
        with choose({"8.4.47": True}):
            b_in.set()
            a_out.wait()

    ts = [threading.Thread(target=a), threading.Thread(target=b)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    assert dict(_POLICY) == {}
    assert _in_thread(lambda: dict(_POLICY)) == {}


def test_choice_is_invisible_to_another_thread():
    with choose({"8.4.47": True}):
        assert policy_choice("8.4.47", False) is True
        assert _in_thread(lambda: policy_choice("8.4.47", False)) is False
    assert policy_choice("8.4.47", False) is False


def test_derivation_beside_a_held_choice_takes_the_default_reading():
    from pipelines.subanta import derive

    held, done = threading.Event(), threading.Event()

    def hold():
        with choose({"8.4.47": True}):
            held.set()
            done.wait()

    t = threading.Thread(target=hold)
    t.start()
    held.wait()
    try:
        assert derive("Baya", 1, 1, linga="napuṃsaka").flat_slp1() == "Bayam"
    finally:
        done.set()
        t.join()
