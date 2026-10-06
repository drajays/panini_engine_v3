"""
2.4.53  ब्रुवो वचिः  —  VIDHI

Padaccheda: ब्रुवः वचिः

bruv root is replaced by vac.
Pāṭha: ashtadhyayi.com data.txt row i=24053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas


def _site(state: State):
    """ब्रुवो वचिः (ārdhadhātuke, anuvṛtti 2.4.35): brū → vac before an ārdhadhātuka — वक्ता, वक्ष्यति, उवाच, उच्यात्, अवोचत्."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("2_4_53_done") or (dh.meta.get("upadesha_slp1") or "").strip() != "brUY":
            continue
        after = state.terms[i + 1:]
        if any(("ardhadhatuka" in u.tags and "pratyaya" in u.tags) or "ashir_liG" in u.tags
               or (u.meta.get("source_lakara_upadesha") or "").strip() in ("liT", "luT", "lRT", "luG", "lRG") for u in after):
            return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    dh = _site(state)
    if dh is not None:
        adesha_substitute_varnas(dh, "vac", state, sutra_id="2.4.53", gunadharmas=frozenset({DHATUTVA}))
        dh.meta.update({"2_4_53_done": True, "anit_dhatu": True, "set_dhatu": False, "ekac_dhatu": True})     # vac is aniṭ (वक्ता), not seṭ like brū
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "bruvo vaciH",
    text_dev              = "ब्रुवो वचिः",
    samagra_slp1          = "ArDaDAtuke bruvaH vaciH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आर्धधातुके ब्रुवः वचिः",
    padaccheda_dev        = "ब्रुवः वचिः",
    why_dev               = "ब्रुवः वचिः (२.४.५३)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
