"""
7.2.82  आने मुक्  —  VIDHI

Padaccheda: आने मुक्

आने मुक् (7.2.82)
Pāṭha: ashtadhyayi.com data.txt row i=72082 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology import mk

_GATE_KEY: str = "7_2_82_Ane_82"


def _site(state: State):
    """आने मुक्: an a-final aṅga (dhātu + śap / śa / śyan …) before the ātmanepada participle āna takes muk — pacamānaḥ, tudamānaḥ, divyamānaḥ."""
    for k, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").strip() in ("SAnac", "SAnan", "cAnaS") and t.varnas and t.varnas[0].slp1 == "A" and k > 0 \
                and state.terms[k - 1].varnas and state.terms[k - 1].varnas[-1].slp1 == "a" and not t.meta.get("7_2_82_muk_done"):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    k = state.terms.index(t)
    state.terms[k - 1].varnas.append(mk("m"))          # kit: muk is the aṅga's final āgama (1.1.46), so 7.3.101 does not see a yañ-initial affix
    state.terms[k - 1].tags.discard("upadesha")           # the new final m is no halantyam it (as 6.1.79)
    t.meta["7_2_82_muk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ane muk",
    text_dev              = "आने मुक्",
    samagra_slp1          = "aNgasya Ane muk ataH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य आने मुक् अतः",
    padaccheda_dev        = "आने मुक्",
    why_dev               = "(सूत्रम् 7.2.82) आने मुक्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
