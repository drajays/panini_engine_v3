"""
6.4.66  घुमास्थागापाजहातिसां हलि  —  VIDHI (narrow demo)

Demo slice (अध्यगीष्ट):
  After dhātu substitute ``gAN`` (from 2.4.45) when a following pratyaya is
  treated as **ṅit** (via 1.2.1 atideśa) and is **hal-ādi**, replace the dhātu
  vowel ``A`` with ``I`` (ga → gI).

Engine:
  - looks for a dhātu term with ``upadesha_slp1 == 'gAN'`` and a following
    pratyaya term whose first phoneme is HAL.
  - requires atideśa map entry set by **1.2.1**:
      state.atidesha_map[('pratyaya_after_gaN_or_kutAdi','pratyaya')] == 'ṅit'
  - performs the concrete rewrite A→I on the dhātu term.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import HAL, mk


def _find_gAN_dhatu_and_next_pratyaya(state: State):
    """Find gAN dhatu and the immediately following pratyaya, by tag (not position)."""
    for i, dh in enumerate(state.terms):
        if "dhatu" not in dh.tags:
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() != "gAN":
            continue
        if dh.meta.get("6_4_66_iitva_done"):
            continue
        for j in range(i + 1, len(state.terms)):
            pr = state.terms[j]
            if "pratyaya" not in pr.tags:
                continue
            if not pr.varnas or pr.varnas[0].slp1 not in HAL:
                return None
            return (dh, pr)
    return None


def _find(state: State):
    if (
        state.atidesha_map.get(("pratyaya_after_gaN_or_kutAdi", "pratyaya"))
        != "ṅit"
    ):
        return None
    result = _find_gAN_dhatu_and_next_pratyaya(state)
    if result is None:
        return None
    dh, _pr = result
    # Expect g + A (+ possible other varnas) on tape (demo slice).
    vs = dh.varnas
    for i, v in enumerate(vs):
        if v.slp1 == "A":
            return (dh, i)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    result = _find(state)
    if result is None:
        return state
    dh, i = result
    dh.varnas[i] = mk("I")
    dh.meta["6_4_66_iitva_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.66",
    sutra_type=SutraType.VIDHI,
    text_slp1="GumA-sTA-gA-pA-jahAti-sAM hali",
    text_dev="घुमास्थागापाजहातिसां हलि",
    padaccheda_dev="घु-मा-स्था-गा-पा-जहतिसाम् / हलि",
    why_dev="ङित्-हलादि-प्रत्यये परे घुमा-स्था-गा-पा-जहि-धातूनां ईत्वादि-आदेशः (अध्यगीष्ट)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

