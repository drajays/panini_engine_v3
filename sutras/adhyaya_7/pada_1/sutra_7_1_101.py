"""
7.1.101  उपधायाश्च  —  VIDHI

Padaccheda: उपधायाः च

उपधायाश्च (7.1.101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    """ॠत इद्धातोः (7.1.100) continues: a dhātu whose upadhā is ॠ — it becomes इ,
    and 1.1.51 उरण् रपरः makes it इर् (कॄत् → किर्त्; 8.2.78 → कीर्त्: कीर्तयति)."""
    for t in state.terms:
        vs = t.varnas
        if "dhatu" in t.tags and len(vs) >= 2 and vs[-2].slp1 == "F" and vs[-1].slp1 not in "aAiIuUfFxeEoO":
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    j = len(t.varnas) - 2
    t.varnas[j:j + 1] = [mk("i"), mk("r")]      # इ + रपर (1.1.51)
    for v in t.varnas[j:j + 2]:
        v.tags.update({"dhatu_v", "mula_dhatu_v"})
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.101",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "upaDAyASca",
    text_dev              = "उपधायाश्च",
    padaccheda_dev        = "उपधायाः च",
    why_dev               = "धातोः उपधाभूतस्य ॠकारस्य इकारः (रपरः) — कॄत् → कीर्तयति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
