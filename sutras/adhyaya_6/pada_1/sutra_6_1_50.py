"""
6.1.50  मीनातिमिनोतिदीङां ल्यपि च  —  VIDHI

Padaccheda: मीनाति-मिनोति-दीङाम् ल्यपि च

मीनातिमिनोतिदीङां ल्यपि च (6.1.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_ROOTS = frozenset({"mIY", "qumiY", "dIN"})     # मीनाति (mīñ), मिनोति (डुमिञ्), दीङ्


def _site(state: State):
    """The ī/i of mī, mi, dī becomes ā before an ārdhadhātuka that is not liṭ: मास्यति, मातुम्…, अमासीत्, दास्यते, दाता, अदास्त.
    (ashtadhyayi.com dhātu table; liṭ keeps it: दिदीये.)"""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_1_50_done"):
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() not in _ROOTS or not dh.varnas or dh.varnas[-1].slp1 not in ("I", "i"):
            continue
        after = state.terms[i + 1:]
        if any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in after):
            continue
        if any(("ardhadhatuka" in u.tags and "pratyaya" in u.tags) or "ashir_liG" in u.tags for u in after):
            return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    dh = _site(state)
    if dh is not None:
        old = dh.varnas[-1]
        dh.varnas[-1] = mk("A", *((old.tags - {"mula_dhatu_v"}) | {"dhatu_adesha_v"}))
        dh.meta["6_1_50_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "mInAtiminotidINAM lyapi ca",
    text_dev              = "मीनातिमिनोतिदीङां ल्यपि च",
    padaccheda_dev        = "मीनाति-मिनोति-दीङाम् ल्यपि च",
    why_dev               = "(सूत्रम् 6.1.50) मीनातिमिनोतिदीङां ल्यपि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
