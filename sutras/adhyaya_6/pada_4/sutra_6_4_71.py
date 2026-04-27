"""
6.4.71  लुङ्लङ्लृङ्क्ष्वडुदात्तः  —  VIDHI (narrow: aṭ augment)

Engine: in luṅ/laṅ/lṛṅ contexts, prepend 'a' to the dhātu term as aṭ-āgama
(ṭ-it handled by 1.3.3/1.3.9 elsewhere). No pipeline-side forcing flag.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk


def cond(state: State) -> bool:
    lakara = (state.meta.get("lakara") or "").strip()
    if lakara not in {"luG", "laG", "lRG"}:
        return False
    if not state.terms or "dhatu" not in state.terms[0].tags:
        return False
    if state.terms[0].meta.get("aT_agama_6_4_71_done"):
        return False
    # aṅgasya adhikāra not required for the augment itself in this narrow slice.
    return True


def act(state: State) -> State:
    dh = state.terms[0]
    dh.varnas.insert(0, mk("a"))
    dh.meta["aT_agama_6_4_71_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.71",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "luG-laG-lRG-kzu aT udAttaH",
    text_dev       = "लुङ्लङ्लृङ्क्ष्वडुदात्तः",
    padaccheda_dev = "लुङ्-लङ्-लृङ्-क्षु / अट् / उदात्तः",
    why_dev        = "लुङ्/लङ्/लृङ्-लकारे धातोः पूर्वं अट्-आगमः (इञ्जिन-स्थित्या निश्चीयते; no meta forcing)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

