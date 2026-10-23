"""
7.4.16  ऋदृशोऽङि गुणः  —  VIDHI

Padaccheda: ऋ-दृशः अङि गुणः

ऋदृशोऽङि गुणः (7.4.16)
Pāṭha: ashtadhyayi.com data.txt row i=74016 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.ang_adesha import stem
from phonology import mk

def _site(state: State):
    """ऋवर्णान्तानां दृशेश्च, before aṅ (the ṅit vikaraṇa of 3.1.52–58): असरत्, आरत्, अदर्शत्. The root is read after it-lopa."""
    ang = next((i for i, t in enumerate(state.terms) if (t.meta.get("upadesha_slp1") or "").strip() == "aG"), None)
    if ang is None:
        return None
    for t in state.terms[:ang]:
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("7_4_16_done"):
            continue
        root = stem(t)
        ix = [k for k, v in enumerate(t.varnas) if v.slp1 in "fF"]
        if ix and (root[-1:] in ("f", "F") or root == "dfS"):
            return t, ix[-1]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, k = _site(state)
    t.varnas[k:k + 1] = [mk("a"), mk("r")]            # guṇa a + rapara r (1.1.51)
    t.meta["7_4_16_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.16",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'fdfSoNi guRaH',
    text_dev              = 'ऋदृशोऽङि गुणः',
    samagra_slp1          = "aNgasya fdfSaH aNi guRaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऋदृशः अङि गुणः",
    padaccheda_dev        = "ऋ-दृशः अङि गुणः",
    why_dev               = "(सूत्रम् 7.4.16) ऋदृशोऽङि गुणः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
