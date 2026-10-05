"""
6.4.36  हन्तेर्जः  —  VIDHI

Padaccheda: हन्तेः जः

हन्तेर्जः (6.4.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    """हन्तेर्जः (hau, 6.4.35 anuvṛtti): han before the hi of loṭ → ja (जहि; the hatAt option is 7.1.35 tāt)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or t.meta.get("6_4_36_done"):
            continue
        flat = "".join(v.slp1 for v in t.varnas if "aT_agama_v" not in v.tags)
        nxt = state.terms[i + 1]
        if flat == "han" and (nxt.meta.get("upadesha_slp1") or "").strip() == "hi":
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        old = t.varnas
        new = parse_slp1_upadesha_sequence("ja")
        for v, o in zip(new, old[-2:]):                 # the ādeśa stays part of the dhātu (1.1.56)
            v.tags |= (o.tags & {"dhatu_v", "mula_dhatu_v"}) | {"dhatu_adesha_v"}
        new[-1].tags.add("sthanivat_non_a")             # ja's a is han's n for 'ato heḥ' (6.4.105): जहि, not *ज
        t.varnas = new
        t.meta["6_4_36_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "hanterjaH",
    text_dev              = "हन्तेर्जः",
    padaccheda_dev        = "हन्तेः जः",
    why_dev               = "(सूत्रम् 6.4.36) हन्तेर्जः।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.4.37",),        # han → ja before hi displaces the general nasal-lopa (hahi)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
