"""
6.1.101  अकः सवर्णे दीर्घः  —  VIDHI

"When an 'ak' phoneme (a/i/u/f/x) is followed by its savarṇa, the
 two are replaced by the corresponding dīrgha (long vowel)."

  a + a = A    i + i = I    u + u = U    f + f = F    x + x = X
  a + A = A    A + a = A    (etc.)
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk
from phonology.savarna import is_savarna, dirgha_of

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


_AK = frozenset({"a", "A", "i", "I", "u", "U", "f", "F", "x", "X"})


def _find_pair(state: State):
    flat = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            flat.append((ti, vi, v))
    for k in range(len(flat) - 1):
        (ti1, vi1, v1) = flat[k]
        (ti2, vi2, v2) = flat[k + 1]
        if v1.slp1 in _AK and v2.slp1 in _AK and is_savarna(v1.slp1, v2.slp1):
            if ti1 != ti2 and PRAGHYA_TERM_TAG in state.terms[ti1].tags:
                # Pragṛhya ‖ ac — no savarṇa-dīrgha across the *pada* boundary
                # (6.1.125 prakṛti-bhāva; 1.1.11 tag on the left *term*).
                continue
            # Replacement = dīrgha of the common series.
            return (ti1, vi1, ti2, vi2, dirgha_of(v1.slp1))
    return None


def cond(state: State) -> bool:
    return _find_pair(state) is not None


def act(state: State) -> State:
    hit = _find_pair(state)
    if hit is None:
        return state
    ti1, vi1, ti2, vi2, d = hit
    state.terms[ti1].varnas[vi1] = mk(d)
    del state.terms[ti2].varnas[vi2]
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.101",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "akaH savarRe dIrghaH",
    text_dev       = "अकः सवर्णे दीर्घः",
    padaccheda_dev = "अकः सवर्णे दीर्घः",
    why_dev        = "अक् वर्णस्य परस्मिन् सवर्णे एकादेशः सवर्ण-दीर्घः भवति।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
