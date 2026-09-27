"""अभ्यास: every question type is well-formed and only asks verified cells."""
import pytest

from core.practice import KINDS, question, verified_keys


@pytest.mark.parametrize("qtype", KINDS)
@pytest.mark.parametrize("kind,lemma", [("subanta", "rAma"), ("tinanta", "BU")])
def test_question_shape(kind, lemma, qtype):
    if not verified_keys():
        pytest.skip("bench/oracle/practice_verified.json not built")
    q = question(kind, qtype, lemma=lemma, seed=3)
    assert q["accepted"] and q["cell_label"]
    if qtype == "mcq":
        assert sum(o["dev"] in q["accepted"] for o in q["options"]) == 1
        assert len({o["dev"] for o in q["options"]}) == len(q["options"])
    if qtype == "tf":
        assert (q["claim"] in q["accepted"]) == q["answer"]
    if qtype == "sutra":
        assert q["answer_sutra"] in {o["sutra_id"] for o in q["options"]}
