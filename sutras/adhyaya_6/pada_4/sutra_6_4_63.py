"""
6.4.63  दीङो युडचि क्ङिति  —  VIDHI

Padaccheda: दीङः युट् अचि क्ङिति

दीङो युडचि क्ङिति (6.4.63)
Pāṭha: ashtadhyayi.com data.txt row i=64063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_63_dINo_63"
_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """दीङो युडचि क्ङिति: dīṅ (dīyate) takes the āgama yuṭ before a vowel-initial kṅit affix — didIye, adIyi."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("6_4_63_yuT_done"):
            continue
        if (t.meta.get("upadesha_slp1") or "").replace("~", "") != "dIN" or not t.varnas or t.varnas[-1].slp1 != "I":
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and nxt.varnas[0].slp1 in _AC and ("kngiti" in nxt.tags or nxt.meta.get("is_apit")
                                                              or "it:Git" in nxt.tags or "it:Nit" in nxt.tags
                                                              or (nxt.meta.get("source_lakara_upadesha") or "") == "liT"):  # 1.2.5: liṭ after a non-conjunct is kit
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    from phonology import mk
    t.varnas.append(mk("y"))
    t.meta["6_4_63_yuT_done"] = True
    t.tags.discard("upadesha")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.63",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "dINo yuqaci kNiti",
    text_dev              = "दीङो युडचि क्ङिति",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke dINaH yuw aci kNiti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके दीङः युट् अचि क्ङिति",
    padaccheda_dev        = "दीङः युट् अचि क्ङिति",
    why_dev               = "(सूत्रम् 6.4.63) दीङो युडचि क्ङिति।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.4.82", "6.4.77"),   # dīṅ takes yuṭ, not yaṇ/iyaṅ
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
