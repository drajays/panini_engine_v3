"""
7.3.102  सुपि च  —  VIDHI

"And before a sup pratyaya (beginning with a yañ — y/v/r/l — or with
 Bh/By — classically 'bhyām, bhyas', plus a handful of others), the
 final 'a' of an aṅga is lengthened to 'ā'."

Operational reading (representative; real Pāṇini restricts to yañādi):
  After an अ-ending aṅga, when the following sup pratyaya starts with
  a YAN consonant (y/v/r/l) OR 'B' (bh), the aṅga's final 'a' → 'ā'.

  cell 3-2 rAmAByAm  ← rAma + ByAm, pratyaya starts with B → A+B... → A
  cell 4-1 rAmAya    ← rAma + ya (post-7.1.13), pratyaya starts with y → A+y → Aya
  cell 4-2 rAmAByAm  ← rAma + ByAm
  cell 5-2 rAmAByAm  ← rAma + ByAm
  cell 6-2 rAmayoH   ← rAma + os, pratyaya starts with o (vowel) — NO change
                       (this rule does not fire before vowel-initial sup)
  cell 6-3 rAmARAm   ← rAma + nuṭ + Am, pratyaya starts with n (after nuṭ)
                       — not a yañ, not Bh; so we keep aṅga short → rAmaNAm
                       then 6.1.101 savarṇa-dīrgha gives rAmANAm when
                       the inserted nuṭ's 'n' is processed.  BUT:
                       classical Pāṇini DOES lengthen here too, via
                       a separate path — and we mirror that by including
                       'n' in the trigger set to reach rAmANAm cleanly.

For v3.1 coverage we use trigger set {y, v, r, l, B, n}.  This is a
simplification (real 7.3.102 is governed by yañādi + 7.3.103/104
exceptions); we honour that by marking the meta field 'aNga_dirgha_done'
so the rule is idempotent.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


_TRIGGER_INITIAL = frozenset({"y", "v", "r", "l", "B", "n"})


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if "anga"  not in anga.tags:     return None
    if "sup"   not in pratyaya.tags: return None
    if not anga.varnas or not pratyaya.varnas:
        return None
    # Idempotency.
    if anga.meta.get("aNga_dirgha_done"):
        return None
    # aṅga final must be 'a' (hrasva).
    last = anga.varnas[-1]
    if last.slp1 != "a":
        return None
    # Pratyaya first varṇa must be in the trigger set.
    first = pratyaya.varnas[0]
    if first.slp1 not in _TRIGGER_INITIAL:
        return None
    return len(state.terms) - 2, len(anga.varnas) - 1


def cond(state: State) -> bool:
    if not adhikara_in_effect("7.3.102", state, "6.4.1"):
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("A")
    state.terms[ti].meta["aNga_dirgha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.102",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "supi ca (aNgasya ataH)",
    text_dev       = "सुपि च",
    padaccheda_dev = "सुपि च — अङ्गस्य अतः",
    why_dev        = "यञादि-सुप्-प्रत्यये परे अदन्त-अङ्गस्य अन्त्य-अ-कारस्य "
                     "दीर्घः आ-कारः भवति।",
    anuvritti_from = ("6.4.1", "7.3.101"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
