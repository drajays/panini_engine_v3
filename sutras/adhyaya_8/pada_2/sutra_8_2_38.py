"""
8.2.38  दधस्तथोश्च  —  VIDHI

Padaccheda: दधः त-थोः च

दधस्तथोश्च (8.2.38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_BAS_BHAS = {"b": "B", "g": "G", "q": "Q", "d": "D", "B": "B", "G": "G", "Q": "Q", "D": "D"}


def _site(state: State):
    """दधः (dhā, quDAY) before त्/थ्: the baś of its abhyāsa takes bhaṣ — धत्ते, धत्थ (data: `अभिधत्त`, `पिधध्वं`)."""
    if not state.tripadi_zone:
        return None
    for t in state.terms:
        if t.meta.get("dhatu_upadesha") != "quDAY":
            continue
        vs = t.varnas
        run = [i for i, v in enumerate(vs) if "abhyasa_v" in v.tags]
        if not run or "bhas_8_2_38" in vs[run[0]].tags or vs[run[0]].slp1 not in _BAS_BHAS:
            continue
        j = run[-1] + 1
        # root dh (+ t/th): the dh is the root's own, the next varṇa starts the tiṅ
        if j + 1 < len(vs) and vs[j].slp1 == "D" and vs[j + 1].slp1 in ("t", "T"):
            return t, run[0]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if (hit := _site(state)) is not None:
        t, i = hit
        old = t.varnas[i]
        t.varnas[i] = mk(_BAS_BHAS[old.slp1], *(old.tags - {"mula_dhatu_v"}), "bhas_8_2_38")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "daDastaToSca",
    text_dev              = "दधस्तथोश्च",
    padaccheda_dev        = "दधः त-थोः च",
    why_dev               = "(सूत्रम् 8.2.38) दधस्तथोश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
