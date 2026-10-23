"""
7.1.90  गोतो णित्  —  VIDHI

Padaccheda: गोतः णित्

गोतो णित् (7.1.90)
Pāṭha: ashtadhyayi.com data.txt row i=71090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem
from engine.state import State

# गोतः: the word गो (tapara; चित्रगु is not it). द्यो is read the same way (Kāśikā: केचिद् ओतो णित् इति पठन्ति — द्यौः, द्यावौ, द्यावः).
def _site(state: State):
    hit = anga_and_sup(state, "7.1.90")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "go", "dyo") or "sarvanamasthana" not in sup.tags or "Nidvat" in sup.tags:
        return None
    return sup


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).tags.add("Nidvat")      # 7.2.115 then takes the aṅga's o to au: गौः, गावौ (6.1.78), गावः
    state.atidesha_map[("sup_after_go", "Nit")] = "Nidvat"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.90",
    sutra_type            = SutraType.ATIDESHA,
    text_slp1             = "goto Rit",
    text_dev              = "गोतो णित्",
    samagra_slp1          = "gotaH sarvanAmasTAne Rit",
    samagra_dev           = "गोतः सर्वनामस्थाने णित्",
    padaccheda_dev        = "गोतः णित्",
    why_dev               = "(सूत्रम् 7.1.90) गोतो णित्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
