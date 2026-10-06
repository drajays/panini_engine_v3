"""
6.4.13  सौ च  —  VIDHI

The upadhā of an aṅga ending in -in, -han, -pūṣan or -aryaman is lengthened before the nominative singular su
(6.4.12 limits the dīrgha of these four to śi; this sūtra adds sau): योगी, वृत्रहा, पूषा, अर्यमा.
(Before the other sarvanāmasthāna sups they keep the short vowel: योगिनौ, वृत्रहणौ, पूषणौ, अर्यमणौ.)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 6.4.13 (padaccheda: सौ च; anuvṛtti: इन्हन्पूषार्यम्णाम् 6.4.12, दीर्घः, उपधायाः, असम्बुद्धौ)
  Source #2 — Kāśikā 6.4.13: योगी, वृत्रहा, पूषा, अर्यमा

Engine: reads the aṅga's last letters (the four named stem-endings), the sup's identity (su) and the absence of sambuddhi.
Pāṭha: ashtadhyayi.com data.txt row i=64013 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_LONG = {"a": "A", "i": "I"}


def _site(state: State):
    if len(state.terms) < 2:
        return None
    anga, sup = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "sup" not in sup.tags or "sambuddhi" in sup.tags:
        return None
    if "napuṃsaka" in anga.tags:
        return None  # the neuter su is luk'd by 7.1.23 (देहि), so there is no sau
    if (sup.meta.get("upadesha_slp1") or "").strip() != "s~" or anga.meta.get("6_4_13_done"):
        return None
    flat = "".join(v.slp1 for v in anga.varnas)
    named = flat.endswith(("in", "pUzan", "aryaman")) or (flat.endswith("han") and "han_dhatu" in anga.tags)
    if not named or len(anga.varnas) < 3 or anga.varnas[-2].slp1 not in _LONG:
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    if anga is not None:
        anga.varnas[-2] = mk(_LONG[anga.varnas[-2].slp1])
        anga.meta["6_4_13_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.13",
    sutra_type=SutraType.VIDHI,
    text_slp1="sO ca",
    text_dev="सौ च",
    samagra_slp1="in-han-pUza-aryamRAmaNgasya asambudDO sO sarvanAmasTAne ca upaDAyAH dIrGaH",
    samagra_dev="इन्-हन्-पूष-अर्यम्णामङ्गस्य असम्बुद्धौ सौ सर्वनामस्थाने च उपधायाः दीर्घः",
    padaccheda_dev="सौ च",
    why_dev="इन्-हन्-पूषन्-अर्यमन् अङ्ग की उपधा दीर्घ, सु परे (योगी, वृत्रहा, पूषा, अर्यमा)।",
    anuvritti_from=("6.4.1", "6.4.7", "6.4.8", "6.4.12"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
