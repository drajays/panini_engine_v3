"""
7.3.35  जनिवध्योश्च  —  PRATISHEDHA

Padaccheda: जनि-वध्योः च

जनिवध्योश्च (7.3.35)
Pāṭha: ashtadhyayi.com data.txt row i=73035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_META: str = "vrddhi_nishedha_7_3_35"     # read by 7.2.116 (the vṛddhi "yad uktam" of the root's upadhā)


def _site(state: State):
    """jan, vadh (Kāśikā: vadhiḥ prakṛtyantaram vyañjanānto 'sti) before ciṇ or a ñit/ṇit kṛt: ajani, janakaḥ, prajanaḥ, avadhi."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or t.meta.get(_META):
            continue
        if "".join(v.slp1 for v in t.varnas) not in ("jan", "vaD"):
            continue
        nxt = state.terms[i + 1]
        itm = nxt.meta.get("it_markers") or set()
        if ("Y" in itm or "R" in itm) and ("c" in itm or "krt" in nxt.tags):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    t.meta[_META] = True
    t.tags.add("vrddhi_nishedha")
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.35",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "janivaDyoSca",
    text_dev              = "जनिवध्योश्च",
    samagra_slp1          = "aNgasya janivaDyoH ca vfdDiH YRiti ciRkftoH na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य जनिवध्योः च वृद्धिः ञ्णिति चिण्कृतोः न",
    padaccheda_dev        = "जनि-वध्योः च",
    why_dev               = "(सूत्रम् 7.3.35) जनिवध्योश्च।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = (),     # tag-barred (7.2.116 reads the tag), not a wholesale block (S146)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
