"""
7.1.100  ॠत इद्धातोः  —  VIDHI

Padaccheda: ॠतः इत् धातोः

For a **dhātu** ending in **long ṝ** (SLP1 ``F``), when a *sārvadhātuka* or
*ārdhadhātuka* affix follows, the ṝ is replaced by **i** (not the guṇa
substitute *a* that **7.3.84** would otherwise give). **1.1.51** *uraṇ
raparaḥ* then inserts the following *r* — कॄ (विक्षेपे, तुदादिः) + श + ति →
कि + र् + अ + ति → किरति (not करति, which **7.3.84**'s guṇa would give).

Scope is phonological, not root-name-based: a *dhātu* ending in **short ṛ**
(SLP1 ``f`` — डुकृञ्, तृ, भृ, हृ…) is untouched by this sūtra and continues
to take ordinary guṇa (7.3.84) → कर्, तर्, भर्, हर्… — the sūtra's own text
names **ॠ** (long), not **ऋ** (short); Kāśikā 1.1.51 groups किरति alongside
कर्ता/हर्ता precisely to contrast the two outcomes for the two vowel lengths.

Once this fires, the term carries ``anga_guna_7_3_84`` (the same "already
handled" flag **7.3.84** sets for itself) so 7.3.84 does not also try to
guṇify the same aṅga — an apavāda blocking its utsarga by marking the
locus done, not by narrowing 7.3.84's own condition (CONSTITUTION
utsarga/apavāda principle).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 71100 · ॠत इद्धातोः
              padaccheda: ॠतः इत् धातोः
              anuvṛtti:   64001: अङ्गस्य
  Source #2 — Yudhiṣṭhira Mīmāṃsaka, Aṣṭādhyāyī-Bhāṣya, pariśiṣṭa, PDF p.643-644
              (1.1.51 उरण् रपरः section): कॄ (विक्षेपे) → कृ+श+ति → 7.3.84
              guṇa blocked (श is a-pit sārvadhātuka) → 7.1.100 ॠ→इ →
              1.1.51 rapara → किरति; गृ (निगरणे) → गिरति, same mechanism.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1

_DONE = "7_1_100_Fta_id_done"


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get(_DONE) or t.meta.get("anga_guna_7_3_84"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "F":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if not (
            is_sarvadhatuka_upadesha_slp1(up)
            or "ardhadhatuka" in nxt.tags
            or "sarvadhatuka" in nxt.tags
            or "sarvadhatuka_3_4_113" in nxt.tags
        ):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    d0 = state.terms[i]
    d0.varnas[-1] = mk("i")
    d0.meta["urN_rapara_pending"] = "r"
    d0.meta[_DONE] = True
    d0.meta["anga_guna_7_3_84"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.100",
    sutra_type            = SutraType.VIDHI,
    text_slp1              = "Fta idDAtoH",
    text_dev               = "ॠत इद्धातोः",
    padaccheda_dev         = "ॠतः इत् धातोः",
    why_dev                = "दीर्घ-ॠ-अन्त धातोः सार्वधातुके आर्धधातुके वा इकारादेशः (न गुणः) — किरति, गिरति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
