"""
7.1.16  पूर्वादिभ्यो नवभ्यो वा  —  VIDHI

Padaccheda: पूर्व-आदिभ्यः नवभ्यः वा

पूर्वादिभ्यो नवभ्यो वा (7.1.16)
Pāṭha: ashtadhyayi.com data.txt row i=71016 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_7.pada_1.sutra_7_1_15 import PURVADI, _TABLE


def _site(state: State):
    """pūrva, para, avara, dakṣiṇa, uttara, apara, adhara, sva, antara + ṅasi / ṅi: smāt / smin, or not (pūrvāt, pūrve — Kāśikā 7.1.16)."""
    if len(state.terms) < 2:
        return None
    anga, pr = state.terms[-2], state.terms[-1]
    if "anga" not in anga.tags or "sup" not in pr.tags or pr.meta.get("smat_smin_done"):
        return None
    if pr.meta.get("upadesha_slp1") not in _TABLE or "".join(v.slp1 for v in anga.varnas) not in PURVADI:
        return None
    return pr


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    pr = _site(state)
    up = pr.meta["upadesha_slp1"]
    pr.varnas = [mk(x) for x in _TABLE[up]]
    pr.meta["smat_smin_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", up)
    pr.meta["upadesha_slp1"] = "smAt" if up == "Nasi" else "smin"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.16",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvAdiByo navaByo vA",
    text_dev              = "पूर्वादिभ्यो नवभ्यो वा",
    samagra_slp1          = "pUrvAdiByaH navaByaH sarvanAmnaH uttarasya Nasi-NyoH vA smAt-sminO",
    samagra_dev           = "पूर्वादिभ्यः नवभ्यः सर्वनाम्नः उत्तरस्य ङसि-ङ्योः वा स्मात्-स्मिनौ",
    padaccheda_dev        = "पूर्व-आदिभ्यः नवभ्यः वा",
    why_dev               = "(सूत्रम् 7.1.16) पूर्वादिभ्यो नवभ्यो वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
