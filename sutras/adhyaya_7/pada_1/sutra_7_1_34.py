"""
7.1.34  आत औ णलः  —  VIDHI

Padaccheda: आतः औ (लुप्तप्रथमान्तनिर्देशः) णलः

आत औ णलः (7.1.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    """आत औ णलः: णल् after an आ-final aṅga becomes औ (ददा+अ → ददा+औ → ददौ, 6.1.88)."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags:
            continue
        nxt = state.terms[i + 1]
        if dh.varnas and dh.varnas[-1].slp1 == "A" and not dh.meta.get("urN_rapara_pending") \
                and (nxt.meta.get("upadesha_slp1") or "").strip() == "Ral" \
                and [v.slp1 for v in nxt.varnas] == ["a"]:
            return nxt
        return None
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    _find(state).varnas = [mk("O")]
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.34",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "Ata O RalaH",
    text_dev              = "आत औ णलः",
    padaccheda_dev        = "आतः औ (लुप्तप्रथमान्तनिर्देशः) णलः",
    why_dev               = "आदन्तात् अङ्गात् परस्य णलः औकारादेशः (ददौ, जग्लौ)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
