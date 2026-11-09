"""
8.4.44  शात्  —  PRATISHEDHA

Padaccheda: शात् (न, तोः, श्चुना श्चुः by anuvṛtti)
After ś a tavarga letter does not take ścutva (8.4.40): प्रश्नः, विश्नः, अश्नाति, दाश्नोति, क्लिश्नाति.
The act tags the tavarga varṇa; 8.4.40 passes over a tagged varṇa.
Pāṭha: ashtadhyayi.com data.txt row i=84044 (Art. 14).
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

_TAVARGA = frozenset("tTdDn")
TAG = "scutva_barred_8_4_44"


def _sites(state: State):
    flat = [v for t in state.terms for v in t.varnas]
    return [b for a, b in zip(flat, flat[1:]) if a.slp1 == "S" and b.slp1 in _TAVARGA and TAG not in b.tags]


def cond(state: State) -> bool:
    return state.tripadi_zone and bool(_sites(state))


def act(state: State) -> State:
    for v in _sites(state):
        v.tags.add(TAG)
    return state


SUTRA = SutraRecord(
    sutra_id         = "8.4.44",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = 'SAt',
    text_dev         = 'शात्',
    samagra_slp1     = "stoH ScunA ScuH SAt na",
    samagra_dev      = "स्तोः श्चुना श्चुः शात् न",
    padaccheda_dev   = "शात्",
    why_dev          = "शकारात् परस्य तवर्गस्य श्चुत्वं न (प्रश्नः)।",
    anuvritti_from   = ("8.4.40",),
    blocks_sutra_ids = (),   # per-position bar by tag; a wholesale block of the target would stop its other sites
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
