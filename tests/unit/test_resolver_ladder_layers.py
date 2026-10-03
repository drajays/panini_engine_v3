"""Art. 21 Ladder 1 — apavāda displaces only what it names; antaraṅga outranks para (PŚ 50)."""
import sutras  # noqa: F401
from engine.resolver import resolve_with_reason
from engine.state import State
from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7
from engine import apply_rule


def _after_it_lopa(stem, vib, vac, linga):
    s = run_subanta_preflight_through_1_4_7(build_initial_state(stem, vib, vac, linga))
    s = apply_rule("4.1.2", s)
    for sid in ("1.3.2", "1.3.3", "1.3.7", "1.3.8", "1.3.9", "1.4.13", "1.4.14"):
        s = apply_rule(sid, s)
    return s


def test_apavada_displaces_only_the_rule_it_names():
    """rāma+jas: 6.1.97 is apavāda of 6.1.101 only; 6.1.102 (para) still contends and wins."""
    d = resolve_with_reason(["6.1.97", "6.1.101", "6.1.102"], _after_it_lopa("rAma", 1, 3, "pulliṅga"))
    assert d.winner == "6.1.102" and "6.1.101" in d.losers


def test_apavada_alone_wins_over_its_utsarga():
    d = resolve_with_reason(["6.1.97", "6.1.101"], _after_it_lopa("rAma", 1, 3, "pulliṅga"))
    assert (d.winner, d.layer) == ("6.1.97", "apavada")


def test_bhis_ais_is_declared_apavada_of_the_e_rules():
    from engine import SUTRA_REGISTRY

    assert {"7.3.102", "7.3.103"} <= set(SUTRA_REGISTRY["7.1.9"].apavada_of)


def test_antaranga_layer_is_modelled_and_cited():
    from engine.paribhasha import layer

    assert layer("antaranga").modelled and layer("antaranga").ps_num == "50"


def test_equal_reach_rules_fall_through_to_para():
    d = resolve_with_reason(["1.1.1", "1.1.2"], State(terms=[]))
    assert (d.winner, d.layer) == ("1.1.2", "para")
