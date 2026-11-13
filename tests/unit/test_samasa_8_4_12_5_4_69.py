"""8.4.12 ekAjuttarapade RaH (vftrahaRO) and 5.4.69 na pUjanAt (surAjA), the samāsa seam kept as tags (docs/SAMASA_MACHINE.md)."""
import sutras  # noqa: F401
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.subanta import derive


def _t(slp1, tags=()):
    return Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence(slp1)), tags=set(tags), meta={"upadesha_slp1": slp1})


def test_8_4_12_vftrahaRO_and_trace():
    s = derive("vftrahan", 1, 2)
    assert s.flat_slp1() == "vftrahaRO"
    seen = {t["sutra_id"]: t["status"] for t in s.trace if t.get("sutra_id") in ("8.4.12", "8.4.2")}
    assert seen["8.4.12"] == "APPLIED"            # not 8.4.2: the seam is not samānapada


def test_8_4_12_needs_ekac_uttarapada_and_the_seam():
    s = derive("vftrahan", 1, 2)
    assert "samasa_purva_v" in s.terms[0].varnas[0].tags and "samasa_uttara_v" in s.terms[0].varnas[5].tags
    flat = State(terms=[_t("vftrahan")])          # one pada, no seam: 8.4.12 has nothing to read
    flat.tripadi_zone = True
    assert not __import__("engine").SUTRA_REGISTRY["8.4.12"].cond(flat)


def test_5_4_69_blocks_samasanta_after_su():
    def tape(tags):
        s = State(terms=[_t("su", tags), _t("rAjan", {"prātipadika"})])
        return apply_rule("5.4.68", s)

    pooja = tape({"samasa_purvapada", "tatpurusha", "lex:pUjana"})
    after = apply_rule("5.4.69", pooja)
    assert "5.4.91" in after.blocked_sutras and "5.4.113" not in after.blocked_sutras
    plain = tape({"samasa_purvapada", "tatpurusha"})        # su without the sense of honour
    from engine import SUTRA_REGISTRY
    assert not SUTRA_REGISTRY["5.4.69"].cond(plain)
