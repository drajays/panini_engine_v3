"""
6.1.104  नादिचि  —  PRATISHEDHA

Padaccheda: न · आदिचि   ( न + आत् + इचि )

**Śāstra:** the *pūrva-savarṇa* ekādeśa taught by **6.1.102**
(*prathamayoḥ pūrvasavarṇaḥ*) does **not** happen when the *pūrva* is
*āt* (*a* / *ā*) and an *ic* vowel follows.

This is the निषेध that shapes the द्विवचन of *a*-stems::

    राम + औ   →  6.1.102 प्राप्तः  (प्रथमा, अक् + अच्)
               →  6.1.104 नादिचि — निषेधः          ← this sūtra
               →  6.1.88  वृद्धिरेचि  →  रामौ

Without it, *rāma + au* would take the पूर्वसवर्ण दीर्घ and yield *rāmā*.
The *i* / *u* stems are untouched (*hari + au → harī*, *vāyu + au → vāyū*),
because their *pūrva* is not *āt*.

R1-exempt: a प्रतिषेध writes ``state.blocked_sutras``; the form never changes.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.pratyahara import build_pratyahara

# इच् — every अच् except अ (अ इ उ ण् · ऋ ऌ क् · ए ओ ङ् · ऐ औ च् minus the अ).
_IC = build_pratyahara("i", "c")
# आत् — the *pūrva* that this निषेध names (short and long).
_AT = frozenset({"a", "A"})

_GATE_KEY: str = "6_1_104_nAdici"


def _at_before_ic(state: State) -> bool:
    """True iff the tape shows *āt* + *ic* at a प्रथमा/द्वितीया sup boundary."""
    if len(state.terms) < 2:
        return False
    anga, pratyaya = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "sup" not in pratyaya.tags:
        return False
    if not anga.varnas or not pratyaya.varnas:
        return False
    # 6.1.102's own locus: the प्रथमा/द्वितीया dual *au* (औ / औट्).
    if (pratyaya.meta.get("upadesha_slp1") or "") not in {"O", "Ow"}:
        return False
    return anga.varnas[-1].slp1 in _AT and pratyaya.varnas[0].slp1 in _IC


def cond(state: State) -> bool:
    return _at_before_ic(state)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.meta["__why_now_dev__"] = (
        "अङ्ग-अन्ते आत् (अ/आ), परतः इच् — अतः ६.१.१०२ पूर्वसवर्ण-दीर्घस्य निषेधः; "
        "अवकाशः ६.१.८८ वृद्धिरेचि इत्यस्य।"
    )
    return state


SUTRA = SutraRecord(
    sutra_id                = "6.1.104",
    sutra_type              = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1               = "nAdici",
    text_dev                = "नादिचि",
    padaccheda_dev          = "न · आत् · इचि",
    why_dev                 = "आत्-वर्णात् परे इच्-वर्णे ६.१.१०२ पूर्वसवर्ण-दीर्घः न भवति; "
                              "तेन राम+औ इत्यत्र वृद्धिः (६.१.८८) अवकाशं लभते।",
    anuvritti_from          = ("6.1.84", "6.1.102"),
    cond                    = cond,
    act                     = act,
    blocks_sutra_ids        = ("6.1.102",),
)

register_sutra(SUTRA)
