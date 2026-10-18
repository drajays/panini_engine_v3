"""
7.4.69  दीर्घ इणः किति  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=74069
- Kāśikā: "इणोऽभ्यासस्य किति लिटि परतो दीर्घो भवति" — ईयतुः, ईयुः; pratyudāharaṇa (not kit): इयाय, इययिथ
- Cross-validation: tests/regression/test_findings_probe_loop.py (ईयतुः)

In liṭ the abhyāsa of the dhātu iṇ takes a long vowel when the ending is kit (1.2.5 asaṃyogāl liṭ kit).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

from sutras.adhyaya_6.pada_1.sutra_6_1_17 import _liT_follows


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or len(t.varnas) != 1 or t.varnas[0].slp1 != "i":
            continue
        dh = state.terms[i + 1]
        if "dhatu" not in dh.tags or (dh.meta.get("upadesha_slp1") or "").strip() != "iR" or not _liT_follows(state, i):
            continue
        head = next((u for u in state.terms[i + 2:] if u.varnas and "agama" not in u.tags), None)
        if head is not None and "kngiti" in head.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[0] = mk("I")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.69",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "dIrGa iRaH kiti",
    text_dev              = "दीर्घ इणः किति",
    samagra_slp1          = "aNgasya aByAsasya dIrGaH iRaH kiti liwi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य दीर्घः इणः किति लिटि",
    padaccheda_dev        = "दीर्घः इणः किति",
    why_dev               = "इणः अभ्यासस्य किति लिटि दीर्घः (ईयतुः, ईयुः)।",
    anuvritti_from        = ('7.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
