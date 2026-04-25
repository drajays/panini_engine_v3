"""
6.1.88  वृद्धिरेचि  —  VIDHI

Operational *vṛddhi* (substitution) here; the **saṃjñā** *vṛddhi* ‘which
phonemes count’ is defined by **1.1.1** (not an adhikāra rule — universal).

"When अ (from a preceding stem) meets ec (= e/E/o/O), the combined
 result is vṛddhi (the long-e/long-o grade) — actually, specifically
 when the ec is E/O, the vṛddhi variant is used; when the ec is e/o,
 6.1.87 guṇa is used instead."

Operational meaning for our corpus:
  a + E → E       (rAma + Ow, after w-lopa: rAma + O → rAmO... wait)

Classical split:
  6.1.87  āt guṇaḥ     : a + i/u/f/x   → e/o/ar/al
  6.1.88  vṛddhir eci  : a + e/o        → E/O  (covered by 6.1.87 in our a+e case)
                       : a + E/O        → E/O  (vṛddhi)

For rāma cells 2-2 (rAma + O) and 8-2 (rAma + O) we have `a + O`.
Classical: `a + O → O` (the O subsumes the preceding a; operationally
identical to sav-dīrgha for vowels of different series, handled under
the umbrella of 6.1.88).

We implement narrowly: when the flat stream has 'a' followed by 'E'
or 'O', replace both with the E/O.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


_VRIDDHI_TARGET = {
    ("a", "E"): "E",
    ("a", "O"): "O",
    ("a", "e"): "E",  # vṛddhi before ec (e.g. 7.3.114 → kasyE / kasyai)
    # Also when preceding is 'A' (dīrgha), same outcome.
    ("A", "E"): "E",
    ("A", "O"): "O",
    ("A", "e"): "E",
}


def _find_pair(state: State):
    flat = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            flat.append((ti, vi, v))
    for k in range(len(flat) - 1):
        (ti1, vi1, v1) = flat[k]
        (ti2, vi2, v2) = flat[k + 1]
        target = _VRIDDHI_TARGET.get((v1.slp1, v2.slp1))
        if target is not None:
            return (ti1, vi1, ti2, vi2, target)
    return None


def cond(state: State) -> bool:
    return _find_pair(state) is not None


def act(state: State) -> State:
    hit = _find_pair(state)
    if hit is None:
        return state
    ti1, vi1, ti2, vi2, target = hit
    state.terms[ti1].varnas[vi1] = mk(target)
    del state.terms[ti2].varnas[vi2]
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.88",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "vfddhir eci",
    text_dev       = "वृद्धिरेचि",
    padaccheda_dev = "वृद्धिः एचि",
    why_dev        = "अ-वर्णात् परस्मिन् एच्-वर्णे (ए/ऐ/ओ/औ) एकादेश-रूपेण "
                     "वृद्धिः।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
