"""
7.3.55  अभ्यासाच्च  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=73055
- Kāśikā: "अभ्यासादुत्तरस्य हन्तेर्हकारस्य कवर्गादेशो भवति" — जघान, जघनिथ, जिघांसति
- Cross-validation: tests/regression/test_findings_probe_loop.py; Vidyut floor fires 7.3.55 for han liṭ

After an abhyāsa the h of the dhātu han becomes a ku letter (gh, by 1.1.50 sthāne'ntaratamaḥ). The hi case is
7.3.56 and the ji case 7.3.57, each in its own file.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_HAN = frozenset({"hana", "han"})


def _site(state: State):
    for i, t in enumerate(state.terms[1:], start=1):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or "abhyasa" not in state.terms[i - 1].tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "h":
            continue
        if (t.meta.get("upadesha_slp1") or "").replace("~", "") in _HAN:
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[0] = mk("G")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.55",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "aByAsAcca",
    text_dev              = "अभ्यासाच्च",
    samagra_slp1          = "aNgasya aByAsAt ca ku cajoH haH hanteH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासात् च कु चजोः हः हन्तेः",
    padaccheda_dev        = "अभ्यासात् च",
    why_dev               = "अभ्यासात् परस्य हन्तेः हकारस्य कुत्वम् (जघान, जिघांसति)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
