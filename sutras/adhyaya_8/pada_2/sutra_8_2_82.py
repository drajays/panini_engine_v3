"""
8.2.82  वाक्यस्य टेः प्लुत उदात्तः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=82082):** *vākyasya ṭeḥ pluta udāttaḥ* —
*vākyasya ṭeḥ pluta udātta ityadhikāraḥ* (scope through **8.2.108**
तयोर्य्वावचि संहितायाम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.2.82" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.2.82",
        "scope_end" : "8.2.108",
        "text_dev"  : "वाक्यस्य टेः प्लुत उदात्तः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.82",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "vAkyasya WeH pluta udAttaH",
    text_dev       = "वाक्यस्य टेः प्लुत उदात्तः",
    padaccheda_dev = "वाक्यस्य / टेः / प्लुतः / उदात्तः",
    why_dev        = "वाक्यस्य टेः प्लुत उदात्त इत्यधिकारः — ८.२.८२ तः ८.२.१०८ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.2.82", "8.2.108"),
)

register_sutra(SUTRA)

