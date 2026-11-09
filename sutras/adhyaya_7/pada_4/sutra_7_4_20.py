"""
7.4.20  वच उम्  —  VIDHI

Padaccheda: वचः उम्

वच उम् (7.4.20)
Pāṭha: ashtadhyayi.com data.txt row i=74020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_DONE = "7_4_20_um_done"


def _find(state: State):
    """वच् before the aṅ of luṅ: the dhātu term and the index of its a (Kāśikā: अवोचत्)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" in t.tags and "abhyasa" not in t.tags and not t.meta.get(_DONE) \
                and "".join(v.slp1 for v in t.varnas if "aT_agama_v" not in v.tags) == "vac" \
                and (state.terms[i + 1].meta.get("upadesha_slp1") or "").strip() == "aG":
            return t, next(k for k, v in enumerate(t.varnas) if v.slp1 == "a" and k and t.varnas[k - 1].slp1 == "v")
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t, j = _find(state)
    t.varnas.insert(j + 1, mk("u"))        # mit: after the last ac (1.1.47)
    t.meta[_DONE] = True
    state.meta[_DONE] = True               # the spine then runs 6.1.87 (a + u → o)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.20",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "vaca um",
    text_dev              = "वच उम्",
    samagra_slp1          = "aNgasya vacaH um aNi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य वचः उम् अङि",
    padaccheda_dev        = "वचः उम्",
    why_dev               = "(सूत्रम् 7.4.20) वच उम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
