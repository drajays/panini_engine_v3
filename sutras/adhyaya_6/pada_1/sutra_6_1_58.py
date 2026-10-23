"""
6.1.58  सृजिदृशोर्झल्यमकिति  —  VIDHI

Padaccheda: सृजि-दृशोः झलि अम् अ-किति

सृजिदृशोर्झल्यमकिति (6.1.58)
Pāṭha: ashtadhyayi.com data.txt row i=61058 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.nimitta_predicates import is_kit
from phonology import JHAL, mk

# सृजि-दृशोः: the two roots the sūtra names (Kāśikā: सृज विसर्गे, दृशिर् प्रेक्षणे), read as the dhātu stands after it-lopa
_ROOTS = {"sfj", "dfS"}


def _site(state: State):
    """The dhātu followed by a non-kit affix that begins with a jhal (the iṭ of 7.2.35 is a vowel: dadarSiTa takes no am)."""
    for i, t in enumerate(state.terms[:-1]):
        lopa = t.meta.get("it_lopa_done")       # the root as it stood after it-lopa — guṇa may already have changed the tape
        stem = lopa[-1] if lopa else "".join(v.slp1 for v in t.varnas)
        if "dhatu" not in t.tags or t.meta.get("6_1_58_done") or stem not in _ROOTS:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None or nxt.varnas[0].slp1 not in JHAL or is_kit(nxt) or "it:kit" in nxt.tags:
            continue
        return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    # अम् is mit (1.1.47): its a stands after the last vowel; yaṇ (6.1.77) then gives sra-j, dra-ś
    k = max(n for n, v in enumerate(t.varnas) if v.slp1 in "aAiIuUfFxXeEoO")
    t.varnas.insert(k + 1, mk("a", "am_agama"))
    t.meta["6_1_58_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.58",
    sutra_type            = SutraType.VIDHI,
        text_slp1             = "sfjidfSorJalyamakiti",
    text_dev              = "सृजिदृशोर्झल्यमकिति",
    samagra_slp1          = "sfji-dfSoH Jali am akiti upadeSe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "सृजि-दृशोः झलि अम् अकिति उपदेशे",
    padaccheda_dev        = "सृजि-दृशोः झलि अम् अ-किति",
    why_dev               = "(सूत्रम् 6.1.58) सृजिदृशोर्झल्यमकिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
