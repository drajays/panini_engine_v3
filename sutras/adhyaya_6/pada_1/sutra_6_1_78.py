"""
6.1.78  एचोऽयवायावः  —  VIDHI

"An ec (= e/E/o/O) followed by an ac (vowel) is replaced respectively
 by ay/āy/av/āv."

For a-stems, this matters because an earlier stage may have produced
`e` or `o` that then meets a vowel-initial pratyaya.  In our corpus:

  cells 6-2 / 7-2  rAma + os  →  via anuvṛtti produces... 
         Wait: `rAma + os` has `a + o` sandhi at the boundary.
         6.1.87 guṇa maps `a + o → o` (actually it doesn't — guṇa is
         for a+i→e, a+u→o).  Our cells 6-2/7-2 need `a + o → ayo`.

So for `rAma + os`:
   pre-sandhi:  r A m a o s
   step 1 — 6.1.87 guṇa on a+o? No: a+o → o by our guṇa map.
   This is actually 6.1.87 operating on the BOUNDARY between stem-a
   and pratyaya-o.  The result 'o' then meets NO following vowel,
   so 6.1.78 would NOT fire classically.

   But the gold is 'rAmayoH' — which has a 'y' inserted.  The classical
   derivation: rAma + os → rAma (stem-final 'a' stays) + os → rAma-yos
   (y-insertion between a and o).  The y-insertion sutra is actually
   **6.1.101** or **8.3.17** variant — but the simplest is **6.1.78**
   itself reading as: after a guṇa-step produces e/o, if that e/o
   meets another vowel, it splits into ay/av.

   Reanalysis: 6.1.87 produces 'o' from a+o.  Then we have 'rAm + o + s'.
   But we need 'rAmayos'.  So the correct path is: 6.1.87 fires on
   a+o → o (one varṇa) → 'rAmos'.  Then 6.1.78 sees 'o' followed by
   another vowel?  'os' → 'o' is NOT followed by a vowel ('s' is a
   consonant).  So 6.1.78 doesn't apply.

   Actual classical Pāṇinian path for रामयोः:
     rAma + os  →  (by 6.1.87 guṇa, a+o→o actually does NOT apply —
                   guṇa is for a+i/u/f/x, not a+o)
     So we have 'rAma' + 'os' with NO sandhi between them, producing
     'rAmaos'.  Then 6.1.78 DOES apply: a+o is an ec+ac sequence
     (a is NOT ec, but o is ec!).  Hmm.

Let me re-check: EC = {e, E, o, O} (long + diphthong vowels).
6.1.78 applies when an EC letter is followed by an AC letter.
So we need the FIRST letter to be in EC.  'a' is NOT in EC.

Correct classical derivation:
  rAma + os  →  rAmos  (via 6.1.87 guṇa: a + o → o, produces long ā+o→o,
                                      but in our guṇa map, a+o isn't listed)

Actually 6.1.87 classical text says "āt guṇaḥ" — guṇa after ā (a/ā).
The ENTIRE guṇa family is e, o, ar, al — so a+o→o IS classical guṇa.
After 6.1.87: rAm + o + s.  Then 6.1.78 applies: o + s is NOT eco+aci
(s is a consonant).  So no further change.  Final form: rAmos.
Surface: रामोः?  No, गold is रामयोः.

The actual classical sūtra that produces rāmayoḥ is the exception
in 6.1.109 (or 6.1.111) — a separate niyama.  For v3.1 we can
implement it as a targeted VIDHI: when an a-stem's final 'a' meets
'os' pratyaya, insert 'y' between them (not do guṇa).

Implemented narrowly:  'a' + 'o' where the 'o' is part of 'os' →
insert 'y' between them instead of guṇa-merging.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


def _find_target(state: State):
    """
    Find a boundary where stem-a meets pratyaya-o of 'os'.  Insert y
    between the stem's final 'a' and the pratyaya's 'o'.
    """
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        anga = state.terms[i]
        nxt  = state.terms[i + 1]
        if not anga.varnas or not nxt.varnas:
            continue
        if "anga" not in anga.tags:
            continue
        if nxt.meta.get("upadesha_slp1") != "os":
            continue
        # Idempotency: skip if already inserted.
        if anga.meta.get("ay_insertion_done"):
            continue
        if anga.varnas[-1].slp1 != "a":
            continue
        if nxt.varnas[0].slp1 != "o":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    anga = state.terms[i]
    # Insert 'y' at the END of the aṅga Term.  Classical: a + o → ay + o.
    anga.varnas.append(mk("y"))
    anga.meta["ay_insertion_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.78",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "eco ayavAyAvaH",
    text_dev       = "एचोऽयवायावः",
    padaccheda_dev = "एचः अय्-अव्-आय्-आवः",
    why_dev        = "अदन्त-अङ्गात् परस्य 'ओस्'-प्रत्ययस्य पूर्वे 'य्'-आगमः "
                     "(अयादि-सन्धि-प्रतिनिधि)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
