"""
1.1.18  ऊँ  (U.N)  —  VIDHI (+ śāstrīya gate)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11018):** *ūṃ* — *Śākalya*’s optional *pragṛhya*
*ādeśa* for the *uÞ* (*uñ*) *nipāta* (continuing **1.1.11**, **1.1.16**, **1.1.17**) before
*avaidika* *iti* in *anārṣa* (non-Vedic) *prayoga*.

**Śāstra (summary):**
  • With **1.1.17** optional *pragṛhya* on *uñ* before *iti*, **1.1.18** may replace the
    final *u* by *ū* + *anunāsika* (*ūṃ*, here one ``Varna`` ``U`` + ``anunasika`` tag,
    SLP1 tape ``U~`` in ``parse_slp1_upadesha_sequence`` style).
  • That *ūṃ* substitute is itself *nitya* *pragṛhya*; **6.1.125** blocks *ac* sandhi
    (*iko yaṇ*, *ecoyavāyāvaḥ*, etc.).
  • Scope **anārṣe** (``ANARSHA_META_KEY``): recipe arms this in *laukika* / non-*ṛṣi*
    passages; omit in Vedic *chandas* so **1.1.18** does not apply there.

v3 **bootstrap** (preflight): first *prayoga* sets ``paribhasha_gates[GATE_KEY]`` only
(*śāstrīya* breadcrumb, unchanged from earlier v3). **r1_form_identity_exempt** allows
that gate-only pass.

v3 **operational** *prayoga*: recipe sets ``UUM_ADESA_ARM_META`` **and**
``ANARSHA_META_KEY``; ``cond`` is true; ``act`` replaces stem-final *u* before *iti* with
``U`` + ``anunasika`` (see ``phonology.varna.parse_slp1_upadesha_sequence("U~")``) and
adds ``pragrahya`` on the left *Term*.

CONSTITUTION Art. 2: ``cond`` reads only ``State.meta`` flags and ``paribhasha_gates``,
not *vibhakti* / *vacana*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

GATE_KEY: str = "1.1.18_UM"

# Non-Vedic scope (*anārṣa* — **1.1.18** *anuvṛtti* in *Kāśikā* reading).
ANARSHA_META_KEY: str = "1_1_18_anArSha"

# Recipe arms optional *ūṃ* *ādeśa* (Śākalya) after *uñ*/*u* + *iti* layout is on the tape.
UUM_ADESA_ARM_META: str = "1_1_18_UUma_desha_arm"


def Um_pragfhya_gate_is_set(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def _is_iti_term(t) -> bool:
    v = t.varnas
    return (
        len(v) >= 3
        and v[0].slp1 == "i"
        and v[1].slp1 == "t"
        and v[2].slp1 == "i"
    )


def _find_u_before_iti(state: State) -> int | None:
    """Return index ``i`` where ``terms[i]`` ends in ``u`` and ``terms[i+1]`` is *iti*."""
    for i in range(len(state.terms) - 1):
        L, R = state.terms[i], state.terms[i + 1]
        if not L.varnas or not R.varnas:
            continue
        if L.varnas[-1].slp1 != "u":
            continue
        if _is_iti_term(R):
            return i
    return None


def _apply_uum_adesha(state: State) -> None:
    j = _find_u_before_iti(state)
    if j is None:
        return
    left = state.terms[j]
    u_um = parse_slp1_upadesha_sequence("U~")[0]
    left.varnas[-1] = u_um
    left.tags.add(PRAGHYA_TERM_TAG)


def cond(state: State) -> bool:
    if state.meta.get(UUM_ADESA_ARM_META):
        return bool(state.meta.get(ANARSHA_META_KEY))
    return GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    if state.meta.pop(UUM_ADESA_ARM_META, None):
        _apply_uum_adesha(state)
    if GATE_KEY not in state.paribhasha_gates:
        state.paribhasha_gates[GATE_KEY] = {
            "active": True,
            "pATha": "1.1.18",
        }
    return state


_WHY = (
    "अनार्षे इति-परे उञः शाकल्यस्य मतेन वैकल्पिकः ऊँ-आदेशः, प्रगृह्यश्च; "
    "छान्दसे न।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.18",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "U.N",
    text_dev       = "ऊँ",
    padaccheda_dev = "ऊँ",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11", "1.1.16", "1.1.17"),
    cond           = cond,
    act            = act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
