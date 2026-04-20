"""
7.1.12  टाङसिङसामिनात्स्याः  —  VIDHI

"After an अ-ending aṅga (= ato'ṅga), the pratyayas ṭā, ṅasi, and ṅas
 are replaced respectively by ina, āt, and sya."

  ṭā   → ina   (instrumental-singular, cell 3-1: rAma + TA → rAma + ina → rAmeRa after later rules)
  ṅasi → āt    (ablative-singular,    cell 5-1: rAma + Nasi → rAma + At → rAmAt)
  ṅas  → sya   (genitive-singular,    cell 6-1: rAma + Nas → rAma + sya → rAmasya)

Reads after anuvṛtti from 6.4.1 (aṅgasya).  The governing condition
"ato'ṅga" (after an a-ending aṅga) is spelt out here in the cond()
rather than left as a separate adhikāra, because 7.1.9 ("ato bhisa ais")
ran before and 7.1.10–7.1.11 don't carry forward to 7.1.12 as a single
baked anuvṛtti thread.  The condition read is purely phonemic: the
final varṇa of the aṅga must be SLP1 'a'.

Post-condition: state.terms[-1] (the sup pratyaya) has its upadeśa
replaced with one of the three sequences above.  We identify which
pratyaya we're replacing by the upadesha_slp1 meta field (set by the
sup-attacher at 4.1.2).

R1 is NOT exempt: if this fires, the form MUST change.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


# Pratyaya upadeśa (as set by 4.1.2) → replacement SLP1 sequence.
_REPLACEMENTS = {
    "wA"   : "ina",   # ṭā   → ina
    "Nasi" : "At",    # ṅasi → āt
    "Nas"  : "sya",   # ṅas  → sya
}


def _find_target(state: State):
    """
    Return (term_idx, replacement_slp1) if conditions are met, else None.
    Conditions:
      1. aṅgasya adhikāra (6.4.1) in effect.
      2. The last Term is a sup pratyaya whose upadeśa is one of wA / Nasi / Nas.
      3. The preceding aṅga Term ends in SLP1 'a'.
      4. This replacement has not already been done (the pratyaya still
         carries its original upadeśa-derived varṇas, not the replacement).
    """
    if len(state.terms) < 2:
        return None
    pratyaya = state.terms[-1]
    if "sup" not in pratyaya.tags:
        return None
    upa = pratyaya.meta.get("upadesha_slp1")
    if upa not in _REPLACEMENTS:
        return None

    # Idempotency: once we've replaced, the varṇas no longer look like
    # the original upadeśa — tag the pratyaya so we don't re-fire.
    if pratyaya.meta.get("ato_replacement_done"):
        return None

    anga = state.terms[-2]
    if "anga" not in anga.tags:
        return None
    if not anga.varnas:
        return None
    # "ato" = after an a-ending aṅga.  Final varṇa must be 'a'.
    # Careful: after it-lopa (1.3.9), the aṅga's final could be the
    # inherent-a of its last consonant (Varna slp1='a', dev='').
    last = anga.varnas[-1]
    if last.slp1 != "a":
        return None

    return len(state.terms) - 1, _REPLACEMENTS[upa]


def cond(state: State) -> bool:
    if not adhikara_in_effect("7.1.12", state, "6.4.1"):
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    idx, replacement_slp1 = hit
    pratyaya = state.terms[idx]
    pratyaya.varnas = [mk(ch) for ch in replacement_slp1]
    pratyaya.meta["ato_replacement_done"] = True
    # Update upadesha_slp1 for downstream rules that key off it.
    pratyaya.meta["upadesha_slp1_original"] = pratyaya.meta.get("upadesha_slp1")
    pratyaya.meta["upadesha_slp1"] = replacement_slp1
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.12",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "wANasiNasAm inAtsyAH (ataH aNgasya)",
    text_dev       = "टाङसिङसामिनात्स्याः",
    padaccheda_dev = "टा-ङसि-ङसाम् इन-आत्-स्याः",
    why_dev        = "अदन्त-अङ्गात् परेषां टा/ङसि/ङसाम् क्रमेण "
                     "इन/आत्/स्य-आदेशाः भवन्ति।",
    anuvritti_from = ("6.4.1", "7.1.9"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
