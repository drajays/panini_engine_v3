"""
6.4.131  वसोः सम्प्रसारणम्  —  VIDHI

Padaccheda: वसोः सम्प्रसारणम्

वसोः सम्प्रसारणम् (6.4.131)
Pāṭha: ashtadhyayi.com data.txt row i=64131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_131_vasoH_131"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.131", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.131"
    return state


from engine.state import State
from phonology import mk

# SHORTCUT S85: the a that follows the v is dropped here (6.1.108 works only on a dhātu Term, and the stem is one flat Term)
def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        flat = [v.slp1 for v in t.varnas]
        if ({"anga", "bha"} <= t.tags and len(flat) >= 3 and flat[-3:] == ["v", "a", "s"] and not t.meta.get("6_4_131_done")
                and any(x.startswith("origin_pratyaya:") and "vasu" in x for x in t.tags)):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    t.varnas[-3] = mk("u")                  # विद्वस् → विदुस् (विदुषः): v → u, and 6.1.108 drops the a that follows
    del t.varnas[-2]
    t.meta["6_4_131_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasoH samprasAraRam",
    text_dev              = "वसोः सम्प्रसारणम्",
    samagra_slp1          = "vasoH Basya aNgasya samprasAraRam",
    samagra_dev           = "वसोः भस्य अङ्गस्य सम्प्रसारणम्",
    padaccheda_dev        = "वसोः सम्प्रसारणम्",
    why_dev               = "भसंज्ञकस्य वसु-अन्तस्य सम्प्रसारणम् (वकारस्य उकारः) — विदुषः, पेचुषः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
