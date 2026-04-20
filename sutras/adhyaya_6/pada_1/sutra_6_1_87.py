"""
6.1.87  आद्गुणः  —  VIDHI

"(When an 'a' follows an 'a' on either side —) a guṇa-vowel replaces
 both."

Operative meaning: a + [a/e/o i u ...] → guṇa of the second member.
For representative testing: this fires when TWO consecutive varṇas
in the flat stream are 'a' + [i,u,f,x], replacing both with the
corresponding guṇa vowel.

    a + a → a     (trivial; tested separately under 6.1.101 sav-dīrgha)
    a + i → e
    a + u → o
    a + f → af   (ar) — handled with 1.1.51 later
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


_GUNA = {
    ("a", "i"): "e",
    ("a", "I"): "e",
    ("a", "u"): "o",
    ("a", "U"): "o",
}


def _find_pair(state: State):
    """Scan flat varṇa sequence across Term boundaries; return
    (term_idx_1, varna_idx_1, term_idx_2, varna_idx_2, guṇa) or None."""
    flat = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            flat.append((ti, vi, v))
    for k in range(len(flat) - 1):
        (ti1, vi1, v1) = flat[k]
        (ti2, vi2, v2) = flat[k + 1]
        g = _GUNA.get((v1.slp1, v2.slp1))
        if g is not None:
            return (ti1, vi1, ti2, vi2, g)
    return None


def cond(state: State) -> bool:
    return _find_pair(state) is not None


def act(state: State) -> State:
    hit = _find_pair(state)
    if hit is None:
        return state
    ti1, vi1, ti2, vi2, g = hit
    # Replace the FIRST varṇa with the guṇa and DELETE the second.
    state.terms[ti1].varnas[vi1] = mk(g)
    # Delete the second varṇa.
    del state.terms[ti2].varnas[vi2]
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.87",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Ad guRaH",
    text_dev       = "आद्गुणः",
    padaccheda_dev = "आत् गुणः",
    why_dev        = "अ-कारात् परे इक् वर्णे एकादेश-रूपेण गुणः।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
