"""3.1.60 3.1.61 3.1.70 3.1.82 2.4.78 2.4.79 2.4.49 (+ 7.3.35, 6.4.37 for tanādi): each reading of the Kāśikā's examples
(DB texts, source=kashika). ``choose`` fixes the vibhāṣā, the loop walks the rest."""
import pytest
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from engine.vikalpa import choose
from tools.autonomy_report import run_autonomously, start_state


def derive(dhatu, lakara, purusha, vacana, pada=None, **choices):
    case = NS(kind="tinanta", args=(dhatu, lakara, purusha, vacana), pada=pada)
    with choose(choices):
        return run_autonomously(start_state(case), "", dhatu, 250).state.flat_slp1()


CASES = [
    # (dhatu id, lakara, purusha, vacana, pada, {sutra: choice}, surface)
    ("04.0065", "luG", 3, 1, None, {}, "apAdi"),                          # 3.1.60 (Kāśikā: udapādi sasyam)
    ("04.0044", "luG", 3, 1, None, {"3.1.61": True}, "ajani"),            # 3.1.61 (+ 7.3.35: no vṛddhi of jan)
    ("04.0044", "luG", 3, 1, None, {"3.1.61": False}, "ajanizwa"),
    ("04.0045", "luG", 3, 1, None, {"3.1.61": True}, "adIpi"),
    ("04.0045", "luG", 3, 1, None, {"3.1.61": False}, "adIpizwa"),
    ("04.0011", "laT", 3, 1, None, {"3.1.70": True}, "trasati"),          # 3.1.70, divādi: śyan is itself optional
    ("04.0011", "laT", 3, 1, None, {"3.1.70": False}, "trasyati"),
    ("01.0545", "laT", 3, 1, None, {"3.1.70": True}, "krAmyati"),         # bhvādi: śyan instead of śap
    ("01.0545", "laT", 3, 1, None, {"3.1.70": False}, "krAmati"),
    ("06.0102", "laT", 2, 3, None, {"3.1.70": True}, "truwyaTa"),         # tudādi: śyan instead of śa
    ("06.0102", "laT", 2, 3, None, {"3.1.70": False}, "truwaTa"),
    ("09.0008", "laT", 3, 1, None, {"3.1.82": True}, "stuBnoti"),         # 3.1.82 śnu beside śnā
    ("09.0008", "laT", 3, 1, None, {"3.1.82": False}, "stuBnAti"),
    ("09.0009", "laT", 2, 3, None, {"3.1.82": True}, "skaBnuTa"),
    ("01.1075", "luG", 3, 1, None, {"2.4.78": True}, "aGrAt"),            # 2.4.78
    ("01.1075", "luG", 3, 1, None, {"2.4.78": False}, "aGrAsIt"),
    ("01.1075", "luG", 3, 3, None, {"2.4.78": True}, "aGruH"),            # 3.4.110 after the luk
    ("04.0042", "luG", 3, 1, None, {"2.4.78": True}, "asAt"),
    ("08.0001", "luG", 3, 1, "atmane", {"2.4.79": True}, "atata"),        # 2.4.79
    ("08.0001", "luG", 3, 1, "atmane", {"2.4.79": False}, "atanizwa"),
    ("08.0009", "luG", 3, 1, "atmane", {"2.4.79": True}, "amata"),        # 6.4.37 for udātta-marked tanādi manu~
    ("08.0003", "luG", 3, 1, "atmane", {"2.4.79": True}, "akzata"),       # ... and for ṇ-final kṣaṇu
    ("02.0041", "liT", 3, 1, None, {}, "jage"),                           # 2.4.49 (Kāśikā: adhijage)
    ("02.0041", "liT", 3, 3, None, {}, "jagire"),
]


@pytest.mark.parametrize("dhatu,lakara,pu,vac,pada,choices,want", CASES)
def test_reading(dhatu, lakara, pu, vac, pada, choices, want):
    assert derive(dhatu, lakara, pu, vac, pada, **choices) == want
