"""
7.3.55  अभ्यासाच्च  —  VIDHI

Padaccheda: अभ्यासात् च

अभ्यासाच्च (7.3.55)
Pāṭha: ashtadhyayi.com data.txt row i=73055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_55_aByAsAcca_55"


def _site(state: State):
    """अभ्यासाच्च (with 7.3.54, 7.3.56 हेरचङि): after an abhyāsa the h of han / hi is a ku — jaGAna, jiGAya, jiGAMsati."""
    for i, t in enumerate(state.terms[1:], start=1):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or "abhyasa" not in state.terms[i - 1].tags:
            continue
        if t.meta.get("7_3_55_ku_done") or not t.varnas or t.varnas[0].slp1 != "h":
            continue
        if (t.meta.get("upadesha_slp1") or "").replace("~", "") in {"hana", "hi", "han"}:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return state
    from phonology import mk
    t.varnas[0] = mk("G")
    t.meta["7_3_55_ku_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.55",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "aByAsAcca",
    text_dev              = "अभ्यासाच्च",
    samagra_slp1          = "aNgasya aByAsAt ca ku cajoH haH hanteH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासात् च कु चजोः हः हन्तेः",
    padaccheda_dev        = "अभ्यासात् च",
    why_dev               = "(सूत्रम् 7.3.55) अभ्यासाच्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
