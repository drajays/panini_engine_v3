"""Lowe 2021 context-reuse invariant (Nilakantha condition): a rule is never conditioned twice by the SAME context.

A rule may fire many times in one derivation (8.2.29 twice at different spots); what is banned is firing again on an unchanged
context. The State trace records, per APPLIED step, `sutra_id`, `form_before` and `form_after` (flat tape text) and no positions,
so the context key is (sutra_id, form_before): the same rule meeting the same tape again. That is a sound under-approximation
of Lowe's "same context": a repeat on an identical tape text is certainly a repeat; two firings at different spots of one
text, which already differ in form_before after the first firing, are not flagged.

Structural steps (`__MERGE__`, `__PHASE__`...) are bookkeeping, not rule applications, and are ignored."""
import json
import pathlib

import pytest

import sutras  # noqa: F401


def context_reuses(trace):
    """[(sutra_id, form_before)] that occur more than once among APPLIED sutra steps."""
    seen, dup = set(), []
    for t in trace:
        sid = str(t.get("sutra_id", ""))
        if t.get("status") != "APPLIED" or sid.startswith("__"):
            continue
        key = (sid, t.get("form_before"))
        if key in seen and key not in dup:
            dup.append(key)
        seen.add(key)
    return dup


def _step(sid, before, after):
    return {"sutra_id": sid, "status": "APPLIED", "form_before": before, "form_after": after}


# ---- the check itself: proofs ---------------------------------------------------------------------------------------

def test_toy_trace_with_repeated_rule_and_context_fails():
    bad = [_step("8.4.47", "avyaya", "avvyaya"), _step("8.4.47", "avyaya", "avvyaya")]
    assert context_reuses(bad) == [("8.4.47", "avyaya")]


def test_toy_trace_same_rule_different_context_passes():
    ok = [_step("8.2.29", "BUyAsst", "BUyAst"), _step("8.2.29", "BUyAst", "BUyAt")]    # same rule, two contexts
    assert context_reuses(ok) == []


def test_toy_structural_and_nonapplied_steps_ignored():
    t = [_step("__MERGE__", "x", "x"), _step("__MERGE__", "x", "x"),
         {"sutra_id": "1.1.1", "status": "SKIPPED", "form_before": "x"}, {"sutra_id": "1.1.1", "status": "SKIPPED", "form_before": "x"}]
    assert context_reuses(t) == []


def test_BUyAt_passes():
    from pipelines.tinanta import derive
    s = derive("BU", "AsIrliG", "kartari", 3, 1)
    assert s.flat_slp1() == "BUyAt"
    assert context_reuses(s.trace) == []
    assert sum(t["sutra_id"] == "8.2.29" and t["status"] == "APPLIED" for t in s.trace) >= 1


def test_avvyaya_fires_8_4_47_once():
    from pipelines.yar_anaci_dvitva_tripadi import _one_term, _with_dvitva
    s = _with_dvitva(_one_term("avyaya"))
    assert s.flat_slp1() == "avvyaya"
    assert [t["sutra_id"] for t in s.trace if t["status"] == "APPLIED"].count("8.4.47") == 1
    assert context_reuses(s.trace) == []


# ---- the corpus: existing derivations, violations are findings, not suppressed -------------------------------------

def _tinanta():
    from pipelines.tinanta import derive
    out = []
    for lak in ("laT", "loT", "liG", "AsIrliG", "luT", "lRG", "laG", "luG", "liT"):
        for p, v in ((3, 1), (2, 2), (1, 3)):
            out.append((f"BU-{lak}-{p}{v}", lambda lak=lak, p=p, v=v: derive("BU", lak, "kartari", p, v)))
    return out


def _subanta():
    from pipelines.subanta import derive
    cells = json.loads((pathlib.Path(__file__).parents[1] / "regression" / "data" / "brain_declension_cells.json").read_text(encoding="utf-8"))
    out = []
    for stem, vib, vac, want in cells[:: max(1, len(cells) // 24)][:24]:
        def run(stem=stem, vib=vib, vac=vac):
            for lg in ("pulliṅga", "strīliṅga", "napuṃsaka"):
                try:
                    return derive(stem, vib, vac, linga=lg)
                except Exception:
                    continue
            pytest.skip("no linga derives")
        out.append((f"{stem}-{vib}-{vac}", run))
    return out


CORPUS = _tinanta() + _subanta()      # 27 + 24 = 51 derivations


@pytest.mark.parametrize("name,run", CORPUS, ids=[c[0] for c in CORPUS])
def test_no_rule_conditioned_twice_by_same_context(name, run):
    s = run()
    assert context_reuses(s.trace) == [], f"{name}: {s.flat_slp1()}"
