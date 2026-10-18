"""
6.4.42  जनसनखनां सञ्झलोः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=64042
- Kāśikā: "जनसनखनाम् अङ्गानां सनि झलादौ क्ङिति च आकारादेशो भवति" — जातः, जातवान्; सातः, सातवान्; खातः, खातवान्;
  सिषासति; pratyudāharaṇa (ajādi): जज्ञे (6.4.98)
- Cross-validation: tests/regression/test_findings_probe_loop.py (जजातः)

The final nasal of the dhātus jan, san, khan becomes ā (6.4.41 viḍvanor anunāsikasyāt) before a jhal-initial san,
or before a jhal-initial kit/ṅit pratyaya (kṅiti, 6.4.15/6.4.37). An āgama (iṭ) belongs to the pratyaya it
stands before, so the head is the first non-āgama Term: with iṭ in front (jijaniṣate) the head is ac-initial
and the rule does not apply.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import JHAL

_ROOTS = frozenset({"jan", "san", "Kan"})


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas if "aT_agama_v" not in v.tags) not in _ROOTS:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or "agama" in nxt.tags or nxt.varnas[0].slp1 not in JHAL:
            continue
        if (nxt.meta.get("upadesha_slp1") or "").strip() == "san" or "kngiti" in nxt.tags:
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = state.terms[_find(state)]
    t.varnas[-1] = mk("A")            # the dispatcher stamps origin:6.4.42 — asiddhavat for 6.4.113 (6.4.22): jajātaḥ
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.42",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "janasanaKanAM saYJaloH",
    text_dev              = "जनसनखनां सञ्झलोः",
    samagra_slp1          = "aNgasya asidDavadatrABAt jana-sana-KanAm san-JaloH nalopaH At",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् जन-सन-खनाम् सन्-झलोः नलोपः आत्",
    padaccheda_dev        = "जन-सन-खनाम् सन्-झलोः",
    why_dev               = "जन्-सन्-खनां झलादौ सनि क्ङिति च नकारस्य आत्वम् (जातः, जजातः, खातः)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
