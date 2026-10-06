"""
7.3.54  हो हन्तेर्ञ्णिन्नेषु  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=73054
- Kāśikā: "घातः, घातकः, घातनम्।"
- Cross-validation: tests/unit/test_bhattikavya_1_2.py (समूलघातम्)

ञित्/णित् परे हन्-धातोः हकारस्य घकारः।
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk

_GATE_KEY: str = "7_3_54_ho_54"


def _nit_follows(state: State, di: int) -> bool:
    for j in range(di + 1, len(state.terms)):
        pr = state.terms[j]
        if pr.kind != "pratyaya":
            continue
        itm = pr.meta.get("it_markers") or set()
        if "N" in itm or "R" in itm:
            return True
        if "nit" in pr.tags:
            return True
        up = (pr.meta.get("upadesha_slp1") or "").strip()
        if up in {"Ramul", "Namul", "Rvul"}:
            return True
    return False


def _body(t):
    """(index of the root's first varṇa, the root's letters) — an aṭ standing in the same pada is not the root's."""
    j = next((k for k, v in enumerate(t.varnas) if "aT_agama_v" not in v.tags), 0)
    return j, "".join(v.slp1 for v in t.varnas[j:])


def _site(state: State):
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return None
    if not adhikara_in_effect("7.3.54", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or not t.varnas:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        j0, flat = _body(t)
        if up == "hana~" and t.varnas[j0].slp1 == "h" and (flat == "hn" or _nit_follows(state, i)):
            return i               # हनस्तोऽचिण्णलोः … ghnanti: the n of the root itself follows the h (ñ-ṇi-n-eṣu: n)
        if up not in {"han", "vaDa", "vaD"} and flat not in {"han", "Gan", "han"}:
            if t.varnas[j0].slp1 != "h":
                continue
            if up not in {"han", "han~"}:
                continue
        if t.varnas[j0].slp1 != "h":
            continue
        if not _nit_follows(state, i):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[_body(t)[0]] = mk("G")
    t.meta["7_3_54_gh_done"] = True
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.54",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ho hanterYRinnezu",
    text_dev              = "हो हन्तेर्ञ्णिन्नेषु",
    samagra_slp1          = "hanteH aNgasya haH kuH YRit-nezu",
    samagra_dev           = "हन्तेः अङ्गस्य हः कुः ञ्णित्-नेषु",
    padaccheda_dev        = "हः हन्तेः ञ्णित्-नेषु",
    why_dev               = "ञिति णिति च परे हन्तेर् हकारस्य घकारः (घातम्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
