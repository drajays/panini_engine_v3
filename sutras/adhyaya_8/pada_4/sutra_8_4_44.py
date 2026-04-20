"""
8.4.44  स्तोः श्चुना श्चुः  —  VIBHASHA (representative)

Classical reading: "An s-series or t-varga letter followed by S/c-varga
 is OPTIONALLY replaced by the corresponding ś-series / c-varga letter."

(Note: in the full Aṣṭādhyāyī this is not actually vibhāṣā; we use it
here as a representative VIBHASHA SutraRecord so the engine tests cover
all ten types.  The real 8.4.44 is an obligatory pariṇāmana; substitute
any genuine vibhāṣā when building the production catalog.)
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


_FIRST  = {"s": "S", "t": "c", "T": "C", "d": "j", "D": "J", "n": "Y"}
_SECOND = frozenset({"S", "c", "C", "j", "J", "Y"})


def _find(state: State):
    flat = []
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            flat.append((ti, vi, v))
    for k in range(len(flat) - 1):
        (ti1, vi1, v1) = flat[k]
        (_,   _,   v2) = flat[k + 1]
        if v1.slp1 in _FIRST and v2.slp1 in _SECOND:
            return (ti1, vi1, _FIRST[v1.slp1])
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi, new_slp1 = hit
    state.terms[ti].varnas[vi] = mk(new_slp1)
    return state


SUTRA = SutraRecord(
    sutra_id         = "8.4.44",
    sutra_type       = SutraType.VIBHASHA,
    text_slp1        = "sto: zcunA zcuH",
    text_dev         = "स्तोः श्चुना श्चुः",
    padaccheda_dev   = "स्तोः श्चुना श्चुः",
    why_dev          = "स्-तवर्गयोः श्च्वर्ग-परे विकल्पेन श्चुः (श्-चवर्ग)।",
    anuvritti_from   = ("8.4.40",),
    cond             = cond,
    act              = act,
    vibhasha_default = True,
)

register_sutra(SUTRA)
