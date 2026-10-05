"""
6.4.67  एर्लिङि  —  VIDHI

Padaccheda: एः लिङि

एर्लिङि (6.4.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

# the 6.4.66 list after 6.1.45 (दे/धे/मे/गै/षो → दा/धा/मा/गा/सा); examples धेयात्, देयात् (ashtadhyayi.com 6.4.67: स्थेयाः, धेया)
_STEMS = frozenset({"dA", "DA", "mA", "sTA", "gA", "pA", "hA", "sA"})
_NOT = frozenset({"dAp", "dEp", "o~hAN", "dIN", "mIY", "qumiY"})      # dīṅ/mī/mi's ā is 6.1.50's, not the ghu-ā


def _site(state: State):
    """एर्लिङि: the ā of the 6.4.66 roots becomes e before the yāsuṭ of āśīr-liṅ (kit, ārdhadhātuka), the later rule over 6.4.66."""
    if not any("ashir_liG" in t.tags for t in state.terms):
        return None
    if not any("yasut_agama" in t.tags for t in state.terms):
        return None        # क्ङिति: the kit yāsuṭ of parasmaipada; ātmanepada's sīyuṭ is not kit (दासीष्ट, मासीष्ट)
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_4_67_done"):
            continue
        up = (dh.meta.get("upadesha_slp1") or "").strip()
        if "".join(v.slp1 for v in dh.varnas) not in _STEMS or up in _NOT:
            continue
        if up == "pA" and dh.meta.get("gana") == 2:          # पा रक्षणे
            continue
        if state.terms[i + 1].varnas:
            return dh
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    dh = _site(state)
    if dh is not None:
        old = dh.varnas[-1]
        dh.varnas[-1] = mk("e", *((old.tags - {"mula_dhatu_v"}) | {"dhatu_adesha_v"}))      # an ādeśa, no longer upadeśa: 6.1.45 leaves it
        dh.meta["6_4_67_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "erliNi",
    text_dev              = "एर्लिङि",
    padaccheda_dev        = "एः लिङि",
    why_dev               = "(सूत्रम् 6.4.67) एर्लिङि।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.4.66",),        # liṅ's e over the general ī (धेयात्, not *धीयात्)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
