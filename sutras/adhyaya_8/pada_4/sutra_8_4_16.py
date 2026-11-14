"""
8.4.16  आनि लोट्  —  VIDHI

Padaccheda: आनि (लुप्तषष्ठ्यन्तनिर्देशः) लोट् (लुप्तषष्ठ्यन्तनिर्देशः)

Sources consulted:
- ashtadhyayi.com data.txt row i=84016 (samagra: उपसर्गात् रषाभ्यां लोट् आनि नः णः)
- Kāśikā: "आनीत्येतस्य लोडादेशस्योपसर्गस्थाद् निमित्तादुत्तरस्य नकारस्य णकारादेशो भवति। प्रवपाणि। परिवपाणि। प्रयाणि। परियाणि।"
  pratyudāharaṇa: "लोडिति किम्? प्रवपानि मांसानि॥"
- Cross-validation: LK cases tests/fixtures/lk_cases/a8.json (8.4.16: pravapARi, pariyARi; negative pravapAni).

The n of the loṭ ending आनि (uttama ekavacana नि with the āgama आट्, 3.4.92) becomes ṇ after an upasarga's r / ṣ (8.4.2 vyavāya).
The tiṅ's varṇas carry the lakāra they replace (`tin_src_loT`), so a homophonous āni that is not loṭ (प्रवपानि, the plural of a
noun) is left alone.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.natva import flat, upasarga_nimitta_before
from engine.state import State
from phonology    import mk


def _site(state: State):
    if not state.tripadi_zone:
        return None
    tape = flat(state)
    for k in range(1, len(tape) - 1):
        t, i, v = tape[k]
        if v.slp1 == "n" and "tin_src_loT" in v.tags and tape[k - 1][2].slp1 == "A" and tape[k + 1][2].slp1 == "i" \
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
    sutra_id              = "8.4.16",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "Ani low",
    text_dev              = "आनि लोट्",
    samagra_slp1          = "upasargAt razAByAM low Ani naH RaH",
    samagra_dev           = "उपसर्गात् रषाभ्यां लोट् आनि नः णः",
    padaccheda_dev        = "आनि (लुप्तषष्ठ्यन्तनिर्देशः) लोट् (लुप्तषष्ठ्यन्तनिर्देशः)",
    why_dev               = "(सूत्रम् 8.4.16) उपसर्गस्थाद् निमित्तात् लोडादेशस्य आनि इत्यस्य नस्य णः — प्रवपाणि, परियाणि।",
    anuvritti_from        = ('8.4.1', '8.4.2', '8.4.14'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
