"""
7.1.69  विभाषा चिण्णमुलोः  —  VIBHASHA

Padaccheda: विभाषा चिण्-णमुलोः

Kāśikā 7.1.69: labh takes num optionally before ciṇ and ṇamul — alābhi / alambhi, lābhaṃ lābham / lambhaṃ lambham
(vyavasthita-vibhāṣā: nitya after an upasarga, prālambhi; the upasarga case is not modelled here).
num is placed after the root's last vowel (1.1.47 vārttika / 7.1.58 model). The kept-off reading is the default (alābhi).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get("7_1_69_num_done"):
            continue
        if "".join(v.slp1 for v in t.varnas) != "laB" or (t.meta.get("upadesha_slp1") or "").strip().rstrip("~") not in ("qulaBaz", "qulaBa~z", "qulaBaz"):
            continue
        if (state.terms[i + 1].meta.get("upadesha_slp1") or "").strip() in ("ciR", "Ramul"):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    j = max(k for k, v in enumerate(t.varnas) if v.slp1 in _AC)
    t.varnas.insert(j + 1, mk("n", "num_agama"))
    t.meta["7_1_69_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.69",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "viBAzA ciRRamuloH",
    text_dev              = "विभाषा चिण्णमुलोः",
    samagra_slp1          = "aNgasya viBAzA cit-RamuloH num laBeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य विभाषा चित्-णमुलोः नुम् लभेः",
    padaccheda_dev        = "विभाषा चिण्-णमुलोः",
    why_dev               = "चिणि णमुलि च लभेः वा नुम् (अलाभि, अलम्भि)।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # alābhi is the default reading; explore() gives alambhi
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
