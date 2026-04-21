"""
8.4.2  अट्कुप्वाङ्नुम्व्यवायेऽपि  —  VIDHI

"Even with at/ku/pu/āṅ/num intervening, the n that follows r/ṛ/ṣ
 (referred by anuvṛtti from 8.4.1 'raṣābhyām no naḥ samānapade')
 is replaced by ṇ."

Operational narrow reading: if within the SAME pada there is an
r-varga or ṛ-varga (or ṣ) letter followed — even with intervening
at/ku/pu/āṅ/num — by an 'n', that 'n' becomes 'ṇ'.

For our corpus:
  cell 3-1 rAmena → rAmeRa (ṇ after r with intervening 'e m'; the 
                             'e m' is a+e+m which counts under the
                             'aṭ/ku/pu/āṅ' extension)
  cell 6-3 rAmAnAm → rAmARAm (ṇ after the r in rAma, with intervening
                               ā m ā — all 'an' class which don't block)

Tripādī.  Implemented narrowly: scan the flat varṇa sequence.  If
we find an 'r' followed later by an 'n' with ONLY 'vowels + k-varga
+ p-varga + m' between them (no s/c/ṭ/t-varga), replace the n with R.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


# Blockers: these consonants break the r ... n linkage.
_BLOCKERS = frozenset({
    # Dental-varga + palatal + cerebral + sibilants
    "t", "T", "d", "D",
    "c", "C", "j", "J",
    "w", "W", "q", "Q", "R",
    "s", "S", "z",
    "l",
})


def _find_target(state: State):
    """Scan flat varṇa sequence for r...n with only non-blocker
    intervening varṇas.  Return (term_idx, varna_idx) of the n.

    v3.2 correction: pada-final 'n' is EXEMPT from ṇatva (the
    classical aṣṭādhyāyī restricts 8.4.2 to non-pada-final contexts).
    After pada-merge there's only one Term, so 'pada-final' means
    'last varṇa position of the single Term'.
    """
    flat = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            flat.append((ti, vi, v))

    for k in range(len(flat)):
        _, _, v = flat[k]
        if v.slp1 not in {"r", "f", "F", "z"}:  # r, ṛ, ṝ, ṣ
            continue
        # Scan forward.
        for m in range(k + 1, len(flat)):
            (ti2, vi2, vm) = flat[m]
            if vm.slp1 == "n":
                # Already processed?
                if "natva_done" in vm.tags:
                    return None
                # Pada-final exemption: if this n is the LAST varṇa
                # of the last Term, do NOT fire ṇatva.  (Needed for
                # cell 2-3 rAmAn accusative plural.)
                if m == len(flat) - 1:
                    return None
                return (ti2, vi2)
            if vm.slp1 in _BLOCKERS:
                break  # blocked
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    new_varna = mk("R")
    new_varna.tags.add("natva_done")
    state.terms[ti].varnas[vi] = new_varna
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.2",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "awkupvANnumvyavAye api",
    text_dev       = "अट्कुप्वाङ्नुम्व्यवायेऽपि",
    padaccheda_dev = "अट्-कु-प्-वाङ्-नुम्-व्यवाये अपि",
    why_dev        = "र-ष-वर्णात् परस्य न-कारस्य णत्वम् — अट्-कु-पु-आङ्-नुम् "
                     "व्यवधाने अपि (त्रिपादी)।",
    anuvritti_from = ("8.4.1", "8.2.1"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
