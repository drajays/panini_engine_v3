"""
2.4.43  लुङि च  —  VIDHI (narrow)

Sources consulted:
- ashtadhyayi.com data.txt row i=24043
- Kāśikā: हन् लुङि च (वध-आदेशः)
- Cross-validation: tests/unit/test_avaDIt_luN_han.py,
  tests/unit/test_avadhIt_han_lun_ekavacana.py,
  tests/unit/test_bhattikavya_1_2.py (न्यवधीत्)

*Han* is replaced by *vadh* (अकारान्त आदेश) in *luṅ*. The dhātu may
follow an upasarga (नि+हन् → न्यवधीत्). Dhātupāṭha upadeśa is
``hana~`` (Adādi 02.0002); after *it*-lopa the surface is ``han``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas


def _han_dhatu(state: State):
    """हन् may follow an upasarga (न्यवधीत्); do not assume terms[0]."""
    if (state.meta.get("lakara") or "").strip() != "luG":
        return None
    for dh in state.terms:
        if "dhatu" not in dh.tags:
            continue
        up = (dh.meta.get("upadesha_slp1") or "").strip()
        flat = "".join(v.slp1 for v in dh.varnas)
        if up not in {"han", "hana~", "han~"} and flat != "han":
            continue
        if dh.meta.get("2_4_43_han_vadh_done"):
            continue
        return dh
    return None


def cond(state: State) -> bool:
    return _han_dhatu(state) is not None


def act(state: State) -> State:
    dh = _han_dhatu(state)
    if dh is None:
        return state
    adesha_substitute_varnas(
        dh, "vaDa", state,
        sutra_id="2.4.43",
        gunadharmas=frozenset({DHATUTVA}),
    )
    dh.meta["2_4_43_han_vadh_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.43",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1='luNi ca',
    text_dev='लुङि च',
    samagra_slp1="ArDaDAtuke luNi ca hanaH vaDa",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="आर्धधातुके लुङि च हनः वध",
    padaccheda_dev="हन् / लुङि / च",
    why_dev="लुङ्-लकारे हन्-धातोः स्थाने वध्-आदेशः (अवधीत्-प्रक्रिया)।",
    anuvritti_from=("2.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
