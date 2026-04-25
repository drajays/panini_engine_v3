"""
3.4.69 *laḥ* — *kartr̥i* / *karmaṇi* vs *bhāve* with *sakarmaka* / *akarmaka* *dhātu*.

Constitution: ``cond`` uses ``Term.meta['karmakatva']`` only — not *lakāra* / *puruṣa*.
"""
from __future__ import annotations

from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import AC_DEV, HAL_DEV

from sutras.adhyaya_3.pada_4.lakara_prayoga_3_4_69 import build_gates, effective_karmakatva_for_lac


def _varnas_from_slp1(slp1: str) -> list:
    out: list = []
    for ch in slp1:
        if ch in HAL_DEV or ch in AC_DEV or ch in "fF":
            out.append(mk(ch))
    return out


def _term_from_slp(slp1: str, karm: str, **meta_extra) -> Term:
    return Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(slp1),
        tags={"dhatu"},
        meta={"karmakatva": karm, **meta_extra},
    )


def test_effective_sakarmaka() -> None:
    t = _term_from_slp("paT", "sakarmaka")
    assert effective_karmakatva_for_lac(t) == "sakarmaka"


def test_effective_akarmaka() -> None:
    t = _term_from_slp("pat", "akarmaka")
    assert effective_karmakatva_for_lac(t) == "akarmaka"


def test_sakarmaka_with_avivakshita() -> None:
    t = _term_from_slp("paT", "sakarmaka", avivakshita_karma=True)
    assert effective_karmakatva_for_lac(t) == "sakarmaka_candra"


def test_gates_sakarmaka() -> None:
    g = build_gates("sakarmaka", "paT")
    assert g["prayoga_3_4_69_licenses_kartari"] is True
    assert g["prayoga_3_4_69_licenses_karmani"] is True
    assert g["prayoga_3_4_69_licenses_bhave"] is False


def test_gates_akarmaka() -> None:
    g = build_gates("akarmaka", "pat")
    assert g["prayoga_3_4_69_licenses_bhave"] is True
    assert g["prayoga_3_4_69_licenses_karmani"] is False


def test_gates_sakarmaka_candra() -> None:
    g = build_gates("sakarmaka_candra", "paT")
    assert g["prayoga_3_4_69_licenses_bhave"] is True
    assert g["prayoga_3_4_69_licenses_karmani"] is False


def test_registry() -> None:
    r = SUTRA_REGISTRY["3.4.69"]
    assert r.sutra_id == "3.4.69"


def test_apply_sutra_sets_paribhasha() -> None:
    t = _term_from_slp("paT", "sakarmaka")
    s0 = State(terms=[t])
    s1 = apply_rule("3.4.69", s0)
    assert s1.paribhasha_gates.get("prayoga_3_4_69_licenses_karmani") is True


def test_apply_skipped_if_no_dhatu_meta() -> None:
    t = _term_from_slp("paT", "sakarmaka")
    t.tags = set()  # not a dhātu
    s0 = State(terms=[t])
    s1 = apply_rule("3.4.69", s0)
    assert s1 is not None
    # cond false → step skipped, gates unchanged
    assert "prayoga_3_4_69_licenses_karmani" not in s1.paribhasha_gates
