"""
8.4.15  हिनुमीना  —  VIDHI

Padaccheda: हिनु (लुप्तषष्ठ्यन्तनिर्देशः) मीना (लुप्तषष्ठ्यन्तनिर्देशः)

Sources consulted:
- ashtadhyayi.com data.txt row i=84015 (samagra: रषाभ्यां उपसर्गात् हिनु मीना नः णः)
- Kāśikā: "हिनु मीना इत्येतयोरुपसर्गस्थाद् निमित्तादुत्तरस्य नकारस्य णकारादेशो भवति। प्रहिणोति, प्रहिणुतः। प्रमीणाति, प्रमीणीतः।
  हिनुमीनाग्रहणे विकृतस्यापि भवति, अजादेशस्य स्थानिवत्त्वात्॥"
- Cross-validation: LK cases tests/fixtures/lk_cases/a8.json (8.4.15: prahiRoti, prahiRutaH, pramIRAti; negative hinoti).

The n of हिनु (हि + श्नु) and of मीना (मी + श्ना) — the n that begins the vikaraṇa right after the dhātu हि / मीञ् — becomes ṇ after
an upasarga's r / ṣ (8.4.2 vyavāya). The vikaraṇa's own vowel may have changed (प्रहिणोति: nu → no by guṇa; sthānivat).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.natva import dhatu_upadesha, flat, upasarga_nimitta_before
from engine.state import State
from phonology    import mk

_HI_MI = frozenset({"hi", "mIY"})       # the dhātus the sūtra names: हि (5.12 hi gatau vṛddhau ca), मीञ् (9.4 hiṃsāyām)


def _site(state: State):
    if not state.tripadi_zone or dhatu_upadesha(state) not in _HI_MI:
        return None
    tape = flat(state)
    for k in range(1, len(tape)):
        t, i, v = tape[k]
        if v.slp1 == "n" and "dhatu_v" in tape[k - 1][2].tags and "dhatu_v" not in v.tags \
                and "natva_done" not in v.tags and upasarga_nimitta_before(tape, k):
            return t, i
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, i = _site(state)
    new = mk("R")
    new.tags |= t.varnas[i].tags | {"natva_done"}
    t.varnas[i] = new
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.15",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'hinumInA',
    text_dev              = 'हिनुमीना',
    samagra_slp1          = "razAByAM upasargAt hinu mInA naH RaH",
    samagra_dev           = "रषाभ्यां उपसर्गात् हिनु मीना नः णः",
    padaccheda_dev        = "हिनु (लुप्तषष्ठ्यन्तनिर्देशः) मीना (लुप्तषष्ठ्यन्तनिर्देशः)",
    why_dev               = "(सूत्रम् 8.4.15) उपसर्गस्थाद् निमित्तात् हिनु-मीनयोः नस्य णः — प्रहिणोति, प्रमीणाति।",
    anuvritti_from        = ('8.4.1', '8.4.2', '8.4.14'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
