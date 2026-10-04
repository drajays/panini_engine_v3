"""
7.2.77  ईशः से  —  VIDHI

Padaccheda: ईशः से (लुप्तषष्ठ्यन्तनिर्देशः)

ईशः से (7.2.77)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_77_ISaH_77"


_ROOTS = frozenset({"ISa~"})


def iT_site(state: State, roots: frozenset, dhve: bool):
    """The ātmanepada tiṅ term (``se``, and ``Dve`` when ``dhve``) right after a root of ``roots`` (by upadeśa): it takes
    an iṭ (ISize, IqiDve, janiSe). Returns the index of the tiṅ term or None."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").replace("~", "") not in {r.replace("~", "") for r in roots}:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas and "tin_adesha_3_4_78" in u.tags), None)
        if nxt is None or nxt.meta.get("it_agama_7_2_77_78_done"):
            continue
        vs = "".join(v.slp1 for v in nxt.varnas)
        if vs == "se" or (dhve and vs in ("Dve", "Dvam")):
            return state.terms.index(nxt)
    return None


def iT_act(state: State, roots: frozenset, dhve: bool) -> bool:
    j = iT_site(state, roots, dhve)
    if j is None:
        return False
    from phonology import mk
    v = mk("i")
    v.tags.add("it_agama")
    state.terms[j].varnas.insert(0, v)
    state.terms[j].meta["it_agama_7_2_77_78_done"] = True
    return True


def cond(state: State) -> bool:
    return iT_site(state, _ROOTS, False) is not None


def act(state: State) -> State:
    iT_act(state, _ROOTS, False)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.77",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ISaH se",
    text_dev              = "ईशः से",
    padaccheda_dev        = "ईशः से (लुप्तषष्ठ्यन्तनिर्देशः)",
    why_dev               = "(सूत्रम् 7.2.77) ईशः से।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
