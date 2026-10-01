"""
7.2.58  गमेरिट् परस्मैपदेषु  —  VIDHI

Padaccheda: गमेः इट् परस्मैपदेषु
Anuvṛtti: अङ्गस्य (6.4.1), आर्धधातुकस्य (7.2.35), से (7.2.57).

Sources consulted:
- ashtadhyayi.com data.txt row i=72058
- Kāśikā: "गमिष्यति। अगमिष्यत्। जिगमिषति।"
  pratyudāharaṇa: "गमेरिति किम्? चेष्यति"
- Cross-validation: Vidyut surface ✓ for गमिष्यति (path … 3.1.33 3.4.114
  7.2.58 … 8.3.59); regression test: tests/unit/test_gam_lrt_7_2_58.py

गम् is anudātta in upadeśa (गमॢँ), so 7.2.10 एकाच उपदेशेऽनुदात्तात्
forbids the general iṭ of 7.2.35. This sūtra re-grants iṭ — as a vidhi of
its own, after the pratiṣedha has taken effect — to a sakārādi ārdhadhātuka
(स्य, सन्) that follows the dhātu गम्, when a parasmaipada affix is present.

cond reads only structure: a dhātu Term whose upadeśa is गमॢँ, a following
ārdhadhātuka Term whose first varṇa is स् and which has no iṭ yet, and a
Term tagged ``parasmaipada`` (1.4.99). act prepends इ (iṭ āgama) to that
ārdhadhātuka Term; 8.3.59 then gives ष: गम् + इस्य + ति → गमिष्यति.
Ātmanepada (संगंस्यते) keeps the 7.2.10 niṣedha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_GAMI_UPADESHA = frozenset({"gamx~"})


def _find(state: State) -> int | None:
    dh = next((i for i, t in enumerate(state.terms)
               if "dhatu" in t.tags and "abhyasa" not in t.tags
               and (t.meta.get("upadesha_slp1") or "").strip() in _GAMI_UPADESHA), None)
    if dh is None:
        return None
    if not any("parasmaipada" in t.tags for t in state.terms):
        return None
    for j in range(dh + 1, len(state.terms)):
        t = state.terms[j]
        if "ardhadhatuka" not in t.tags or not t.varnas:
            continue
        if t.meta.get("it_agama_7_2_35_done"):
            return None
        return j if t.varnas[0].slp1 == "s" else None
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = state.terms[_find(state)]
    it_v = mk("i")
    it_v.tags.add("it_agama")
    t.varnas.insert(0, it_v)
    t.meta["it_agama_7_2_35_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.58",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "gameriw parasmEpadezu",
    text_dev              = "गमेरिट् परस्मैपदेषु",
    padaccheda_dev        = "गमेः इट् परस्मैपदेषु",
    why_dev               = "गम्-धातोः परस्य सकारादेः आर्धधातुकस्य इट्, परस्मैपदे परे (७.२.१० इत्यस्य अपवादः)।",
    anuvritti_from        = ("6.4.1", "7.2.35", "7.2.57"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
