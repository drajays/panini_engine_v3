"""
pipelines/tinanta.py — tiṅanta derivation driver (stub).
──────────────────────────────────────────────────────────

Parallel to pipelines/subanta.py.  Fully fleshed out in v3.1 once
sutras/adhyaya_3/pada_*/* are populated with the laT / laN / liT
machinery.  For now this is a placeholder that raises a clear
NotImplementedError so tests/forward can mark tiṅanta cells 'xfail'.
"""
from engine.state import State


def derive(
    dhatu_upadesha: str,
    lakara: str,
    prayoga: str,  # "kartari" | "karmani" | "bhave"
    purusha: int,
    vacana: int,
    *,
    upasargas: list[str] | None = None,
) -> State:
    raise NotImplementedError(
        "tiṅanta pipeline is scheduled for v3.1; subanta coverage first "
        "(CONSTITUTION Article 8 — depth before breadth). "
        "Design constraint: pada must be resolved internally from prayoga + dhātu markers + upasargas "
        "(no external 'pada' argument)."
    )
