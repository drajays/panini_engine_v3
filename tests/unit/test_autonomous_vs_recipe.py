"""
tests/unit/test_autonomous_vs_recipe.py — Phase 4: Autonomous loop infrastructure.

Tests:
  1. enumerate_candidates is robust to cond() exceptions (defensive guard).
  2. run_sapadasaptadhyayi raises ConvergenceError when the loop cannot halt.
  3. run_sapadasaptadhyayi halts immediately when no candidates are present.
  4. Scheduler discipline: PARIBHASHA/ADHIKARA excluded; Tripāḍī bidirectional.
  5. Full side-by-side comparison (aspirational; xfail until Phase 5).
"""
from __future__ import annotations

import sutras  # noqa: F401

import pytest

from engine.core_loop import run_sapadasaptadhyayi, ConvergenceError
from engine.scheduler import enumerate_candidates
from engine.state     import State, Term
from phonology        import mk


class TestSchedulerDiscipline:
    """Phase 4: Scheduler must exclude meta-rule types and apply Tripāḍī gate."""

    def test_paribhasha_not_in_candidates(self):
        """PARIBHASHA sūtras are interpretive meta-rules — excluded from loop."""
        from engine.sutra_type import SutraType
        from engine.registry import SUTRA_REGISTRY
        s = State()
        cands = enumerate_candidates(s)
        bad = [c for c in cands if SUTRA_REGISTRY.get(c) and
               SUTRA_REGISTRY[c].sutra_type is SutraType.PARIBHASHA]
        assert not bad, f"PARIBHASHA in candidates: {bad}"

    def test_adhikara_not_in_candidates(self):
        """ADHIKARA sūtras open scope stacks — excluded from loop."""
        from engine.sutra_type import SutraType
        from engine.registry import SUTRA_REGISTRY
        s = State()
        cands = enumerate_candidates(s)
        bad = [c for c in cands if SUTRA_REGISTRY.get(c) and
               SUTRA_REGISTRY[c].sutra_type is SutraType.ADHIKARA]
        assert not bad, f"ADHIKARA in candidates: {bad}"

    def test_tripadi_not_in_candidates_outside_zone(self):
        """Tripāḍī sūtras (8.2.1–8.4.68) excluded when not in Tripāḍī zone."""
        from engine.gates import is_tripadi
        s = State()
        assert not s.tripadi_zone
        cands = enumerate_candidates(s)
        bad = [c for c in cands if is_tripadi(c)]
        assert not bad, f"Tripāḍī sūtras in pre-Tripāḍī candidates: {bad[:5]}"

    def test_candidate_count_bounded(self):
        """Track scheduler false-positive count — tighten as Phase 4 progresses."""
        s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
        cands = enumerate_candidates(s)
        # Phase 4+ cond discipline (2026-05-31): phase pools + stub migration.
        assert len(cands) < 100, f"Scheduler regression: {len(cands)} candidates"

    def test_bu_dhatu_vidhi_candidates_bounded(self):
        """BU dhātu probe: filtered VIDHI must stay at discipline baseline."""
        from engine.sutra_type import SutraType
        from engine.registry import SUTRA_REGISTRY
        s = State(
            terms=[
                Term(
                    kind="prakriti",
                    varnas=[mk("B"), mk("U")],
                    tags={"dhatu", "anga", "prakriti"},
                    meta={"upadesha_slp1": "BU"},
                )
            ],
            phase="angakarya",
        )
        cands = enumerate_candidates(s)
        vidhi = [
            c for c in cands
            if SUTRA_REGISTRY.get(c)
            and SUTRA_REGISTRY[c].sutra_type is SutraType.VIDHI
        ]
        assert len(vidhi) <= 0, f"BU probe VIDHI candidates: {vidhi[:10]}"

    def test_tripadi_candidates_inside_zone(self):
        """Inside Tripāḍī zone: non-Tripāḍī sūtras excluded (asiddha gate)."""
        from engine.gates import is_tripadi
        s = State(terms=[Term(kind="pada", varnas=[mk("B"), mk("a")], tags={"pada"}, meta={})])
        s.tripadi_zone = True
        cands = enumerate_candidates(s)
        non_tripadi = [c for c in cands if not is_tripadi(c)]
        assert not non_tripadi, f"Non-Tripāḍī in Tripāḍī zone: {non_tripadi[:5]}"


class TestEnumerateCandidatesGuard:
    def test_empty_state_does_not_raise(self):
        s = State()
        # The guard in enumerate_candidates catches cond() exceptions.
        cands = enumerate_candidates(s)
        assert isinstance(cands, list)

    def test_returns_list_of_strings(self):
        s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
        cands = enumerate_candidates(s)
        assert all(isinstance(c, str) for c in cands)

    def test_candidates_are_sorted_numerically(self):
        s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
        cands = enumerate_candidates(s)
        if len(cands) >= 2:
            tuples = [tuple(int(p) for p in c.split(".")) for c in cands]
            assert tuples == sorted(tuples), "candidates must be in Aṣṭādhyāyī order"

    def test_tripadi_zone_blocks_non_tripadi(self):
        s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
        s.tripadi_zone = True
        s.phase = "tripadi"
        cands = enumerate_candidates(s)
        non_tripadi = [c for c in cands if not c.startswith("8.")]
        assert non_tripadi == [], (
            f"Non-Tripāḍī candidates found while in tripadi zone: {non_tripadi[:5]}"
        )


class TestRunSapadasaptadhyayi:
    def test_convergence_error_on_no_halt(self, monkeypatch):
        """Loop must raise ConvergenceError when it never converges in a phase."""
        import engine.core_loop as cl_mod
        original_max = cl_mod.MAX_ITERATIONS
        cl_mod.MAX_ITERATIONS = 3  # small so the test is fast
        try:
            # Force a non-empty candidate list via monkeypatch so the loop
            # can't converge within MAX_ITERATIONS.
            call_count = [0]

            def always_one_candidate(state):
                call_count[0] += 1
                return ["3.1.68"]  # always one candidate — loop can't halt

            monkeypatch.setattr("engine.core_loop.enumerate_candidates",
                                always_one_candidate)

            def noop_apply(sid, state, **kw):
                return state  # don't change state — candidates stay infinite

            monkeypatch.setattr("engine.core_loop.apply_rule", noop_apply)

            s = State()
            with pytest.raises(ConvergenceError, match="no convergence after 3"):
                run_sapadasaptadhyayi(s)
        finally:
            cl_mod.MAX_ITERATIONS = original_max

    def test_halts_on_zero_candidates(self, monkeypatch):
        """If enumerate_candidates returns [], the loop exits immediately."""
        monkeypatch.setattr(
            "engine.core_loop.enumerate_candidates",
            lambda state: [],
        )
        s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
        result = run_sapadasaptadhyayi(s)
        assert result is s or result.flat_slp1() == s.flat_slp1()

    def test_fires_single_candidate_then_halts(self, monkeypatch):
        """With one candidate that changes state to convergence."""
        fired = []

        def mock_enumerate(state):
            # First call: return one candidate. Second call: return [] (converged).
            if not fired:
                return ["3.1.32"]
            return []

        def mock_apply_rule(sid, state, **kw):
            fired.append(sid)
            return state  # no-op for this test

        monkeypatch.setattr("engine.core_loop.enumerate_candidates", mock_enumerate)
        monkeypatch.setattr("engine.core_loop.apply_rule", mock_apply_rule)

        s = State()
        run_sapadasaptadhyayi(s)
        assert fired == ["3.1.32"], f"expected 3.1.32 fired once, got {fired}"

    def test_resolves_conflict_when_multiple_candidates(self, monkeypatch):
        """When > 1 candidate, resolver picks the winner."""
        fired = []
        call_count = [0]

        def mock_enumerate(state):
            call_count[0] += 1
            if call_count[0] == 1:
                return ["1.1.1", "3.1.32"]  # two candidates
            return []

        def mock_apply_rule(sid, state, **kw):
            fired.append(sid)
            return state

        monkeypatch.setattr("engine.core_loop.enumerate_candidates", mock_enumerate)
        monkeypatch.setattr("engine.core_loop.apply_rule", mock_apply_rule)

        s = State()
        run_sapadasaptadhyayi(s)
        assert len(fired) == 1, f"resolver should have picked exactly one winner, got {fired}"


class TestAutonomousVsRecipe:
    """
    Side-by-side comparison: autonomous path vs recipe pipeline.

    BU bhvādi kartari/karmani/bhave uses shared bootstrap + dispatch (Phase 5 M5).
    """

    def test_bhu_lat_kartari_converges(self):
        from engine.core_loop import derive_autonomous_tinanta

        auto_state = derive_autonomous_tinanta("BU", "laT", "kartari")
        assert auto_state.meta.get("derivation_class") == "tinanta"
        assert auto_state.flat_dev() == "भवति"

    @pytest.mark.parametrize(
        "lakara",
        ["laT", "liT", "luT", "lRT", "loT", "laG", "liG", "AsIrliG", "luG", "lRG"],
    )
    def test_bhu_kartari_3sg_surface_matches_recipe(self, lakara: str):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("BU", lakara, "kartari", 3, 1)
        auto_state = derive_autonomous_tinanta("BU", lakara, "kartari")
        assert auto_state.flat_dev() == recipe_state.flat_dev()

    @pytest.mark.parametrize(
        "lakara,prayoga",
        [
            ("laT", "karmani"),
            ("laT", "bhave"),
            ("liT", "bhave"),
        ],
    )
    def test_bhu_karmani_bhave_surface_matches_recipe(self, lakara: str, prayoga: str):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("BU", lakara, prayoga, 3, 1)
        auto_state = derive_autonomous_tinanta("BU", lakara, prayoga)
        assert auto_state.flat_dev() == recipe_state.flat_dev()

    def test_pac_lat_kartari_3sg_surface_matches_recipe(self):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("pac", "laT", "kartari", 3, 1)
        auto_state = derive_autonomous_tinanta("pac", "laT", "kartari")
        assert recipe_state.flat_dev() == auto_state.flat_dev() == "पचत"


class TestAutonomousAdadi:
    """Adādi ``ada~`` kartari — shared dispatch (no separate spine needed)."""

    @pytest.mark.parametrize(
        "lakara",
        ["laT", "liT", "luT", "lRT", "loT", "liG", "AsIrliG", "luG", "lRG"],
    )
    def test_ad_kartari_3sg_surface_matches_recipe(self, lakara: str):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("ada~", lakara, "kartari", 3, 1)
        auto_state = derive_autonomous_tinanta("ada~", lakara, "kartari")
        assert auto_state.flat_dev() == recipe_state.flat_dev()


class TestAutonomousSpecialSpines:
    """Upasarga / adādi-special laṭ paths via ``upasargas`` on autonomous entry."""

    def test_asa_lat_kartari_3sg_matches_recipe(self):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("Asa~", "laT", "kartari", 3, 1)
        auto_state = derive_autonomous_tinanta("Asa~", "laT", "kartari")
        assert auto_state.flat_dev() == recipe_state.flat_dev() == "आस्ते"

    def test_yama_Anga_lat_matches_recipe(self):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("yama~", "laT", "kartari", 3, 1, upasargas=["A~N"])
        auto_state = derive_autonomous_tinanta(
            "yama~", "laT", "kartari", upasargas=["A~N"]
        )
        assert auto_state.flat_slp1() == recipe_state.flat_slp1() == "AyacCate"

    def test_jYA_apa_lat_matches_recipe(self):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("jYA", "laT", "kartari", 3, 1, upasargas=["apa"])
        auto_state = derive_autonomous_tinanta(
            "jYA", "laT", "kartari", upasargas=["apa"]
        )
        assert auto_state.flat_slp1() == recipe_state.flat_slp1() == "apajAnIte"


class TestAutonomousSanNic:
    """Ṣan/Ṇic recipe flags — early exit in bootstrap."""

    def test_sru_san_lat_matches_recipe(self):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("Sru", "laT", "kartari", 3, 1, san_recipe=True)
        auto_state = derive_autonomous_tinanta(
            "Sru", "laT", "kartari", san_recipe=True
        )
        assert auto_state.flat_slp1() == recipe_state.flat_slp1() == "SuSrUzate"

    def test_pa_nic_lat_matches_recipe(self):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("pA", "laT", "kartari", 3, 1, nic_recipe=True)
        auto_state = derive_autonomous_tinanta(
            "pA", "laT", "kartari", nic_recipe=True
        )
        assert auto_state.flat_slp1() == recipe_state.flat_slp1() == "pAyayate"


class TestAutonomousBhaveParadigm:
    """Bhāve laṭ 9-cell — mirrors ``test_tinanta_bhave_lat.py``."""

    _BHU_BHAVE_LAT = {
        (3, 1): "भवते",
        (3, 2): "भवेते",
        (3, 3): "भवन्ते",
        (2, 1): "भवसे",
        (2, 2): "भवेथे",
        (2, 3): "भवध्वे",
        (1, 1): "भवे",
        (1, 2): "भवावहे",
        (1, 3): "भवामहे",
    }

    @pytest.mark.parametrize(
        "purusha,vacana,expected",
        [(pu, va, exp) for (pu, va), exp in _BHU_BHAVE_LAT.items()],
    )
    def test_bhu_bhave_lat_matches_recipe(
        self, purusha: int, vacana: int, expected: str
    ):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("BU", "laT", "bhave", purusha, vacana)
        auto_state = derive_autonomous_tinanta("BU", "laT", "bhave", purusha, vacana)
        assert recipe_state.flat_dev() == expected
        assert auto_state.flat_dev() == recipe_state.flat_dev()


class TestBhuPrayogaParity:
    """
    Regression: former bridge-registry (lakara, prayoga) paths for BU 3sg.

    ``pipelines/recipes/tinanta_bridges.py`` was deleted 2026-05-31 after parity
    with ``derive_autonomous_tinanta`` was verified.  Keep this matrix green.
    """

    def test_bridge_registry_empty(self):
        from pipelines.recipes import list_bridges

        assert list_bridges() == []

    @pytest.mark.parametrize(
        "lakara,prayoga",
        [
            ("liT", "kartari"),
            ("luT", "kartari"),
            ("laG", "kartari"),
            ("luG", "kartari"),
            ("AsIrliG", "kartari"),
            ("liG", "kartari"),
            ("lRT", "kartari"),
            ("lRG", "kartari"),
            ("loT", "kartari"),
            ("laT", "karmani"),
            ("liT", "karmani"),
            ("laG", "karmani"),
            ("liG", "karmani"),
            ("AsIrliG", "karmani"),
            ("luG", "karmani"),
            ("luT", "karmani"),
            ("lRT", "karmani"),
            ("lRG", "karmani"),
            ("loT", "karmani"),
            ("laT", "bhave"),
            ("liT", "bhave"),
        ],
    )
    def test_bu_former_bridge_path_matches_autonomous(self, lakara: str, prayoga: str):
        from engine.core_loop import derive_autonomous_tinanta
        from pipelines.tinanta import derive

        recipe_state = derive("BU", lakara, prayoga, 3, 1)
        auto_state = derive_autonomous_tinanta("BU", lakara, prayoga)
        assert auto_state.flat_dev() == recipe_state.flat_dev()
