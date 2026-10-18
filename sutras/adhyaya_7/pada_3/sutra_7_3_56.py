"""
7.3.56  हेरचङि  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=73056
- Kāśikā: "हिनोतेरभ्यासादुत्तरस्य कवर्गादेशो भवति अचङि" — प्रजिघीषति, प्रजिघाय; pratyudāharaṇa (caṅ): प्राजीहयत्
- Cross-validation: tests/regression/test_findings_probe_loop.py (जिघाय)

After an abhyāsa the h of the dhātu hi becomes gh (ku, 1.1.50), unless the pratyaya caṅ follows.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site(state: State):
    for i, t in enumerate(state.terms[1:], start=1):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or "abhyasa" not in state.terms[i - 1].tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "h" or (t.meta.get("upadesha_slp1") or "").strip() != "hi":
            continue
        if any((u.meta.get("upadesha_slp1") or "").strip() == "caN" for u in state.terms[i + 1:]):
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[0] = mk("G")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.56",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "heracaNi",
    text_dev              = "हेरचङि",
    samagra_slp1          = "aNgasya heH acaNi ku cajoH hanteH aByAsAt ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य हेः अचङि कु चजोः हन्तेः अभ्यासात् च",
    padaccheda_dev        = "हेः अ-चङि",
    why_dev               = "अभ्यासात् परस्य हिनोतेः हकारस्य कुत्वम्, न तु चङि (जिघाय; प्राजीहयत्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
