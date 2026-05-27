"""
8.4.2  अट्कुप्वाङ्नुम्व्यवायेऽपि  —  VIDHI

"Even with at/ku/pu/āṅ/num intervening, the n that follows r/ṛ/ṣ
 (referred by anuvṛtti from 8.4.1 'raṣābhyām no naḥ samānapade')
 is replaced by ṇ."

Operational narrow reading: if within the SAME *Term* (model for *samānapade*)
there is an r/ṛ/ṣ letter followed — even with intervening *aṭ* / *ku* / *pu* /
*āṅ* / *num* — by an *n*, that *n* becomes *ṇ*, **provided** the *n* is **not**
immediately after *r* / *ṛ* / *ṣ* (that adjacent *saṃhitā* subcase is **8.4.1**;
this file is the *vyavāya* extension *apī*).

*Cross-term:* the flat scan must **not** link *r* at the end of one *Term* with
*n* at the start of the next (e.g. *agnir* + *nayati* — *ṇ* does not apply).

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
META_P009_NATVA = "corrected_v2_P009_8_4_2_arm"


def _find_p009_natva(state: State):
    """
    **P009** *parikrīṇīte*: *ṛ*-like ``r`` in ``krI`` and word-initial ``n`` of the
    ``SnA`` residue ``nI`` — permitted *vyavāya* with only ``I`` between — ṇatva even
    though ``krI`` and ``nI`` sit in adjacent ``Term``s (bundle convention).
    """
    if not state.meta.get(META_P009_NATVA):
        return None
    for i in range(len(state.terms) - 1):
        t0, t1 = state.terms[i], state.terms[i + 1]
        f0 = "".join(v.slp1 for v in t0.varnas)
        if not f0.endswith("krI"):
            continue
        if "dhatu" not in t0.tags:
            continue
        if not t1.varnas or t1.varnas[0].slp1 != "n":
            continue
        if "SnA_vikaraṇa" not in t1.tags:
            continue
        if "natva_done" in t1.varnas[0].tags:
            continue
        return (i + 1, 0)
    return None


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
        (ti0, _vi0, v) = flat[k]
        if v.slp1 not in {"r", "f", "F", "z"}:  # r, ṛ, ṝ, ṣ
            continue
        # Scan forward, **within the same Term only** (samānapade / one pada).
        for m in range(k + 1, len(flat)):
            (ti2, vi2, vm) = flat[m]
            if ti2 != ti0:
                break
            if vm.slp1 == "n":
                if m == k + 1:
                    # 8.4.1: adjacent *r* / *ṛ* / *ṣ* + *n*; *apī* of 8.4.2
                    # extends only *vyavāya* cases.
                    continue
                if "natva_done" in vm.tags:
                    continue
                if m == len(flat) - 1:
                    # Pada-final *n*; representative exemption (see 8.4.1).
                    continue
                return (ti2, vi2)
            if vm.slp1 in _BLOCKERS:
                break
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    if _find_p009_natva(state) is not None:
        return True
    return _find_target(state) is not None


def act(state: State) -> State:
    hit09 = _find_p009_natva(state)
    if hit09 is not None:
        ti, vi = hit09
        t = state.terms[ti]
        form_before = "".join(v.dev for v in t.varnas if v.dev)
        new_varna = mk("R")
        new_varna.tags.add("natva_done")
        t.varnas[vi] = new_varna
        state.meta.pop(META_P009_NATVA, None)
        form_after = "".join(v.dev for v in t.varnas if v.dev)
        state.meta["__why_now_dev__"] = (
            f"ऋ-कारोत्तरम् न → ण (P009 क्री-SnA context); "
            f"{form_before!r} → {form_after!r}। (काशिका ८।४।२)"
        )
        return state
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    trigger_slp1 = "?"
    for i in range(vi - 1, -1, -1):
        if t.varnas[i].slp1 in {"r", "f", "F", "z"}:
            trigger_slp1 = t.varnas[i].slp1
            break
    form_slp1_before = "".join(v.slp1 for v in t.varnas)
    new_varna = mk("R")
    new_varna.tags.add("natva_done")
    t.varnas[vi] = new_varna
    form_slp1_after = "".join(v.slp1 for v in t.varnas)
    state.meta["__why_now_dev__"] = (
        f"निमित्तम् {trigger_slp1} (र/ऋ/ष-वर्णः); न → ण (व्यवाय-अपि); "
        f"{form_slp1_before} → {form_slp1_after}। (काशिका ८।४।२)"
    )
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
