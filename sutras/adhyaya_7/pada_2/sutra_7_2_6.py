"""
7.2.6  ऊर्णोतेर्विभाषा  —  PRATISHEDHA

Padaccheda: ऊर्णोतेः विभाषा

ऊर्णोतेर्विभाषा (7.2.6)
Pāṭha: ashtadhyayi.com data.txt row i=72006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

def _sic_dhatu(state: State, names, ends=()):
    """The dhātu (upadeśa in ``names``, or ending in one of ``ends``) that stands before a sic."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        raw = (t.meta.get("upadesha_slp1") or "").strip().replace("^", "").replace("\\", "")
        if not (raw.replace("~", "") in names or (ends and raw.endswith(ends))):
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and (nxt.meta.get("upadesha_slp1") or "").strip() == "sic" and "it_agama" in nxt.varnas[0].tags:
            return t      # only a sic that has its iṭ: an aniṭ root keeps its vṛddhi (अपाक्षीत्)
    return None

_NAMES = frozenset({"UrRuY"})


def _site(state: State):
    """ऊर्णोतेः — the vṛddhi reading is withheld (और्णवीत्); vibhāṣā's other reading (और्णावीत्) is not generated (SHORTCUT S144)."""
    t = _sic_dhatu(state, _NAMES, ())
    return None if t is None or t.meta.get("7_2_1_sici_vrddhi_done") else t


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.meta["7_2_1_sici_vrddhi_done"] = True      # 7.2.1 / 7.2.3 read this: no vṛddhi
        t.tags.add("no_sici_vrddhi")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.6",
    sutra_type            = SutraType.PRATISHEDHA,
    text_slp1             = "UrRoterviBAzA",
    text_dev              = "ऊर्णोतेर्विभाषा",
    samagra_slp1          = "aNgasya UrRoteH viBAzA sici vfdDiH parasmEpadezu na iwi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऊर्णोतेः विभाषा सिचि वृद्धिः परस्मैपदेषु न इटि",
    padaccheda_dev        = "ऊर्णोतेः विभाषा",
    why_dev               = "(सूत्रम् 7.2.6) ऊर्णोतेर्विभाषा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
