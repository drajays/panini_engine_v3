"""
6.4.81  इणो यण्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=64081
- Kāśikā: "इणोऽङ्गस्य अजादौ प्रत्यये परतो यणादेशो भवति" — यन्ति, यन्तु, आयन्; "इयङोऽपवादः"
- Cross-validation: tests/regression/test_findings_probe_loop.py (आयन्, ईयतुः)

The i of the dhātu iṇ becomes y before a vowel-initial pratyaya: the apavāda of iyaṅ (6.4.77). In liṭ the dvitva
(6.1.8, with 1.1.59 dvirvacane'ci) comes first, so the rule waits for the abhyāsa. Before a ṇit ending the
vṛddhi of 7.2.115 is para and wins (iyāya).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import is_tin_adesha
from engine.state import State
from phonology import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _find(state: State) -> int | None:
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags or (dh.meta.get("upadesha_slp1") or "").strip() != "iR":
            continue
        own = [v for v in dh.varnas if "aT_agama_v" not in v.tags]
        if len(own) != 1 or own[0].slp1 != "i":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or nxt.varnas[0].slp1 not in _AC:
            continue
        head = next((u for u in state.terms[i + 1:] if u.varnas and "agama" not in u.tags), nxt)
        if (is_tin_adesha(head) and "kngiti" not in head.tags and not head.meta.get("is_apit")
                and any(t.startswith("sarvadhatuka") for t in head.tags) and "7.3.84" not in state.blocked_sutras):
            continue                                   # a pit sārvadhātuka takes guṇa first: ayAni, not *yAni
        if (not any("abhyasa" in u.tags for u in state.terms)
                and any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms)):
            continue                                   # dvitva first in liṭ (1.1.59)
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    dh = state.terms[_find(state)]
    k = next(k for k, v in enumerate(dh.varnas) if "aT_agama_v" not in v.tags)
    dh.varnas[k] = mk("y")
    dh.tags.discard("upadesha")          # the new final y is no upadeśa-final (1.3.3 must not strip it)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.81",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "iRo yaR",
    text_dev              = "इणो यण्",
    samagra_slp1          = "iRaH aNgasya aci yaR",
    samagra_dev           = "इणः अङ्गस्य अचि यण्",
    padaccheda_dev        = "इणः यण्",
    why_dev               = "इणः अङ्गस्य अजादौ प्रत्यये यणादेशः (यन्ति, आयन्, ईयतुः)।",
    anuvritti_from        = ('6.4.77',),
    apavada_of            = ("6.4.77",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
