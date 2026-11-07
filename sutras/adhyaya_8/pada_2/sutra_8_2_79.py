"""
8.2.79  न भकुर्छुराम्  —  VIDHI

Padaccheda: न भ-कुर्-छुराम्

न भकुर्छुराम् (8.2.79)
Pāṭha: ashtadhyayi.com data.txt row i=82079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_ROOTS = frozenset({"kur", "Cur"})                   # by the dhātu's varṇas …
_UPADESHA = frozenset({"qukfY", "kfY", "Cura~"})     # … or by its upadeśa (the pada may begin with the aṭ: akurvan)
_BLOCKS = ("8.2.77", "8.2.78")                       # hali ca · upadhāyāṃ ca (dīrgha of the ik before r / v)


def cond(state: State) -> bool:
    """SHORTCUT S140: of the three the sūtra names (bha-kur-chur) only kur and chur are read; 'bha' has no source in the repo."""
    if not state.tripadi_zone or len(state.terms) != 1 or set(_BLOCKS) <= state.blocked_sutras:
        return False
    t = state.terms[0]
    return "".join(v.slp1 for v in t.varnas if "dhatu_v" in v.tags) in _ROOTS \
        or (t.meta.get("dhatu_upadesha") or "").strip() in _UPADESHA


def act(state: State) -> State:
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.79",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na BakurCurAm",
    text_dev              = "न भकुर्छुराम्",
    samagra_slp1          = "padasya pUrvatrAsidDam na BakurCurAm DAtoH rvoH dIrGa",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् न भकुर्छुराम् धातोः र्वोः दीर्घ",
    padaccheda_dev        = "न भ-कुर्-छुराम्",
    why_dev               = "न भकुर्छुराम् — भस्य कुर्-छुरोः उपधायाः दीर्घः न।",
    anuvritti_from        = ('8.1.1',),
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
