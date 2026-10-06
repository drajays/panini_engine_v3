"""
7.4.11  ऋच्छत्यॄताम्  —  VIDHI

Padaccheda: ऋच्छति-ऋ-ॠताम्

ऋच्छत्यॄताम् (7.4.11)
Pāṭha: ashtadhyayi.com data.txt row i=74011 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _lit_dhatu(state: State):
    """The non-abhyāsa dhātu of a liṭ derivation, or None."""
    if not any("abhyasa" in t.tags for t in state.terms):
        return None
    if not any((t.meta.get("source_lakara_upadesha") or "").strip() == "liT" or "lit_derivation" in t.tags
               or t.meta.get("upadesha_slp1") == "liT" for t in state.terms):
        return None            # लिटि: not every abhyasta (juhotyādi iyarti has no 7.4.11)
    return next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)


def _guna_ar(t, j: int) -> None:
    t.varnas[j:j + 1] = [mk("a"), mk("r")]          # गुण + उरण् रपरः (1.1.51)


def _find(state: State):
    """ऋच्छत्यॄताम् (लिटि गुणः): ऋच्छ्, ऋ and ॠ-final roots — आनर्च्छ, आरतुः,
    ननरे (नॄ), जगरतुः (गॄ)."""
    t = _lit_dhatu(state)
    if t is None or not t.varnas:
        return None
    st = "".join(v.slp1 for v in t.varnas)
    if st in ("f", "fcC", "ftC") or t.varnas[-1].slp1 == "F":
        return t, (0 if st != "f" and st.startswith("f") else len(t.varnas) - 1)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t, j = _find(state)
    _guna_ar(t, j)
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.4.11",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "fcCatyFtAm",
    text_dev              = "ऋच्छत्यॄताम्",
    samagra_slp1          = "aNgasya fcCatyFtAm liwi guRaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऋच्छत्यॄताम् लिटि गुणः",
    padaccheda_dev        = "ऋच्छति-ऋ-ॠताम्",
    why_dev               = "ऋच्छ्-ऋ-ॠदन्तानां लिटि गुणः (ननरे, आरतुः)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
