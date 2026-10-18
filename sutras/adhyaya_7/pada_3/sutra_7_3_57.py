"""
7.3.57  सन्लिटोर्जेः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=73057
- Kāśikā: "सनि लिटि च प्रत्यये जेरङ्गस्य योऽभ्यासस्तस्मादुत्तरस्य कवर्गादेशो भवति" — जिगीषति, जिगाय
- Cross-validation: tests/regression/test_findings_probe_loop.py (जिगाय)

After the abhyāsa of the dhātu ji, its j becomes g (ku, 1.1.50) when the abhyāsa is due to san or liṭ: a
following san pratyaya, or a tiṅ that replaced liṭ (its `source_lakara_upadesha`). Before caṅ (ajījayat) or
yaṅ (jejīyate) no kutva.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _san_or_lit(t) -> bool:
    return (t.meta.get("upadesha_slp1") or "").strip() == "san" or \
        (t.meta.get("source_lakara_upadesha") or "").strip() == "liT"


def _site(state: State):
    for i, t in enumerate(state.terms[1:], start=1):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or "abhyasa" not in state.terms[i - 1].tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "j" or (t.meta.get("upadesha_slp1") or "").strip() != "ji":
            continue
        if any(_san_or_lit(u) for u in state.terms[i + 1:]):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[0] = mk("g")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.57",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "sanliworjeH",
    text_dev              = "सन्लिटोर्जेः",
    samagra_slp1          = "aNgasya sanliwoH jeH ku cajoH aByAsAt ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य सन्लिटोः जेः कु चजोः अभ्यासात् च",
    padaccheda_dev        = "सन्-लिटोः जेः",
    why_dev               = "सनि लिटि च अभ्यासात् परस्य जेः जकारस्य कुत्वम् (जिगाय, जिगीषति)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
