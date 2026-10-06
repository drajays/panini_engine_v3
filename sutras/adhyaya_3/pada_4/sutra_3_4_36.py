"""
3.4.36  समूलाकृतजीवेषु हन्कृञ्ग्रहः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=34036
- Kāśikā: "समूलघातं हन्ति, अकृतघातं करोति, जीवग्रहं गृह्णाति।"
- Cross-validation: tests/unit/test_bhattikavya_1_2.py (समूलघातम्)

समूल / अकृत / जीव उपपद रहते हन्-कृञ्-ग्रह् take **णमुल्**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.krt_eligibility import krt_insertion_eligible, requested_krt_upadesha
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "3_4_36_samUlAkfta_36"
_HAN = frozenset({"han", "haR", "han~"})
_UPAPADA = frozenset({"samUla", "samUlam", "akfta", "jIva"})


def _dhatu(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags), None)


def _has_samula_upapada(state: State) -> bool:
    for t in state.terms:
        up = (t.meta.get("upadesha_slp1") or "").strip()
        flat = "".join(v.slp1 for v in t.varnas)
        if up in _UPAPADA or flat in _UPAPADA:
            return True
        if "upapada" in t.tags and (flat.startswith("samUla") or up.startswith("samUla")):
            return True
    return False


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.4.36", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    if requested_krt_upadesha(state) not in {"Ramul", "Namul", "am"}:
        return False
    if any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    dh = _dhatu(state)
    if dh is None:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").strip()
    flat = "".join(v.slp1 for v in dh.varnas)
    if up not in _HAN and flat not in {"han", "ha"}:
        return False
    return _has_samula_upapada(state)


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ramul")),
        tags={"pratyaya", "krt", "upadesha", "ardhadhatuka", "nit"},
        meta={"upadesha_slp1": "Ramul", "it_markers": {"N", "u", "l"}},
    )
    for v in pr.varnas:
        if v.slp1 in {"R", "u", "l"}:
            v.tags.add("it")
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.36",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "samUlAkftajIvezu hankfYgrahaH",
    text_dev              = "समूलाकृतजीवेषु हन्कृञ्ग्रहः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH samUla-akfta-jIvezu han-kfY-grahaH kft Ramul karmaRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः समूल-अकृत-जीवेषु हन्-कृञ्-ग्रहः कृत् णमुल् कर्मणि",
    padaccheda_dev        = "समूल-अकृत-जीवेषु हन्-कृञ्-ग्रहः",
    why_dev               = "समूलोपपदे हन्तेः णमुल् (समूलघातम्)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
