"""
3.4.115  लिट् च  —  VIDHI

Padaccheda: लिट् च

krt-suffix rule: लिट् च
Pāṭha: ashtadhyayi.com data.txt row i=34115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_115_liw_115"


def _structural_site(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind == "pratyaya" and "tin_adesha_3_4_78" in t.tags and "ardhadhatuka" not in t.tags \
                and (t.meta.get("source_lakara_upadesha") or "").strip() == "liT":
            return i
    return None


def cond(state: State) -> bool:
    if _structural_site(state) is not None:
        return True
    return tin_pratyaya_gate_eligible(state, "3.4.115", gate_key=_GATE_KEY)


def act(state: State) -> State:
    i = _structural_site(state)
    if i is not None:
        t = state.terms[i]
        t.tags.discard("sarvadhatuka")
        t.tags.discard("sarvadhatuka_3_4_113")
        t.tags.add("ardhadhatuka")
        state.meta["__why_now_dev__"] = "लिटः तिङ् आर्धधातुकसंज्ञः (तिङ्शित्सार्वधातुकम् ३.४.११३ इत्यस्य अपवादः) — अतः शप् नास्ति। (३.४.११५)"
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.115",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "liw ca",
    text_dev              = "लिट् च",
    samagra_slp1          = "liw ca tiN ArDaDAtukam",
    samagra_dev           = "लिट् च तिङ् आर्धधातुकम्",
    padaccheda_dev        = "लिट् च",
    why_dev               = "धातोः प्रत्ययः (३.4.115)।",
    apavada_of            = ("3.4.113",),   # liṭ's tiṅ is ārdhadhātuka
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
