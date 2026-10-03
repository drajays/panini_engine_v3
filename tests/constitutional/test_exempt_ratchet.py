"""A6 (docs/SUTRA_COVERAGE_100_PLAN.md S0): operational sūtras may not hide behind
r1_form_identity_exempt. The count may only go down."""
import sutras  # noqa: F401
from engine import SUTRA_REGISTRY

OPERATIONAL = {"VIDHI", "NIYAMA", "NIPATANA", "ATIDESHA", "VIBHASHA"}
BASELINE = 3205  # 2026-10-03; lower it whenever a placeholder becomes a real rule


def test_operational_exempt_count_never_rises():
    n = sum(1 for r in SUTRA_REGISTRY.values()
            if getattr(r, "r1_form_identity_exempt", False) and r.sutra_type.name in OPERATIONAL)
    assert n <= BASELINE, f"{n} operational sūtras are R1-exempt (ceiling {BASELINE})"
