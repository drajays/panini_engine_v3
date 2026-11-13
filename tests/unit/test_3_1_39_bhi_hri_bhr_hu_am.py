"""3.1.39 भीह्रीभृहुवां श्लुवच्च — Kāśikā: बिभयाञ्चकार, बिभाय। जिह्रयाञ्चकार, जिह्राय। बिभराञ्चकार, बभार। जुहवाञ्चकार, जुहाव।
ām (optional) + ślāviva dvitva / ittva; anuprayoga kṛ / bhū / as (3.1.40)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def _all(dhatu):
    return {b.surface_slp1 for b in explore(lambda: derive(dhatu, "liT", "kartari", 3, 1))}


@pytest.mark.parametrize("dhatu,plain,stem", [
    ("03.0002", "biBAya", "biBay"),      # ञिभी
    ("03.0003", "jihrAya", "jihray"),    # ह्री
    ("03.0006", "baBAra", "biBar"),      # डुभृञ्
    ("03.0001", "juhAva", "juhav"),      # हु
])
def test_am_readings(dhatu, plain, stem):
    assert _all(dhatu) == {plain, stem + "AYcakAra", stem + "AmAsa", stem + "AmbaBUva"}
