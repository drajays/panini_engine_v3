"""
1.3.8  लशक्वतद्धिते  —  SAMJNA

Classical reading: "The initial ल्-श्-कु (= l, ś, k-varga) of a pratyaya
in a non-taddhita context are 'it'."

v3.1 representative implementation: we extend this to the broader
Pāṇinian family (1.3.5–1.3.8) that collectively handles pratyaya-
initial it-markers.  Specifically we tag the initial 'N' (ṅ) of sup
pratyayas that carry the tag 'has_initial_n_it' (set by 4.1.2 from
the JSON _meta block — which encodes the classical decisions).

After this tagging, 1.3.9 tasya lopaḥ deletes the marked varṇa.

This keeps the code dumb (reads the tag) while the grammatical
decisions about which pratyayas have initial-ṅ-its stay in data.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _eligible_terms(state: State):
    for i, t in enumerate(state.terms):
        if "has_initial_n_it" not in t.tags:
            continue
        if not t.varnas:
            continue
        first = t.varnas[0]
        if first.slp1 != "N":
            continue
        if ("it" in first.tags or
            "it_candidate_lasaku" in first.tags):
            continue
        yield i


def cond(state: State) -> bool:
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    for i in _eligible_terms(state):
        state.terms[i].varnas[0].tags.add("it_candidate_lasaku")
        key = ("it_lasaku", i)
        state.samjna_registry[key] = frozenset({state.terms[i].varnas[0].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.8",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "laSakv ataddhite",
    text_dev       = "लशक्वतद्धिते",
    padaccheda_dev = "ल-श-कु — अ-तद्धिते",
    why_dev        = "उपदेशे प्रत्ययस्य आदौ ल्-श्-कु-वर्णस्य इत्-संज्ञा "
                     "(अतद्धिते)। अत्र ङ्-वर्णान्तः प्रातिनिधिकः।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
