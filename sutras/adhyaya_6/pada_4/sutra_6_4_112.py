"""
6.4.112  श्नाऽभ्यस्तयोरातः  —  VIDHI

Padaccheda: श्ना-अभ्यस्तयोः आतः

श्नाऽभ्यस्तयोरातः (6.4.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_112_SnAByasta_112"


def _find(state: State) -> int | None:
    """श्नाभ्यस्तयोरातः (क्ङिति, अचि — 6.4.98/6.4.77): the ā of śnā (and of an
    abhyasta) drops before a vowel-initial kṅit ending — क्रीणन्ति, क्रीणन्तु."""
    for i, t in enumerate(state.terms[:-1]):
        if "SnA_vikaraṇa" not in t.tags or not t.varnas or t.varnas[-1].slp1 != "A":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        # jh counts as vowel-initial: 7.1.3 झोऽन्तः makes it अन्ति / अन्तु / अन्
        if nxt is None:
            continue
        jh = (nxt.meta.get("upadesha_slp1") or "").strip() in {"jhi", "Ji", "Ja", "jha"}
        if not jh and nxt.varnas[0].slp1 not in "aAiIuUfFxXeEoO":
            continue
        if "kngiti" in nxt.tags or nxt.meta.get("is_apit"):
            return i
    return None


_GHU_ROOTS = {"dA", "DA"}   # 1.1.20 दाधा घु सञ्ज्ञके — the "aghoḥ" exception 6.4.113 carves out


def _find_ghu_abhyasta(state: State) -> int | None:
    """गण-3 घु (दा/धा) अभ्यस्त: the dhātu's own final ā drops before a weak
    (kṅit) sārvadhātuka tiṅ — दत्तः, दद्वः, ददति — whether that tiṅ is
    hal-initial or vowel/jhi-initial (6.4.113's "aghoḥ" carve-out routes
    every *other* abhyasta root's hal-initial case to ī instead; घु has no
    such carve-out, so both cases fall to this लोप)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) not in _GHU_ROOTS:
            continue
        if not any("abhyasa" in u.tags for u in state.terms):
            continue
        nxt = state.terms[i + 1]
        if "kngiti" not in nxt.tags and not nxt.meta.get("is_apit"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "A":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _find_ghu_abhyasta(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is not None:
        state.terms[i].varnas = state.terms[i].varnas[:-1]
        # no longer an upadeśa: its new final न् must not be read as halantyam it
        state.terms[i].tags.discard("upadesha")
        return state
    i = _find_ghu_abhyasta(state)
    if i is not None:
        state.terms[i].varnas = state.terms[i].varnas[:-1]
        return state
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.112",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'SnAByastayorAtaH',
    text_dev              = 'श्नाऽभ्यस्तयोरातः',
    padaccheda_dev        = "श्ना-अभ्यस्तयोः आतः",
    why_dev               = "(सूत्रम् 6.4.112) श्नाऽभ्यस्तयोरातः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
