"""
7.4.53  यीवर्णयोर्दीधीवेव्योः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=704053
- Kāśikā: यीवर्णयोर्दीधीवेव्योः (ई-लोपः परे यि/इ-वर्णे)
- Cross-validation: tests/unit/test_dIdhye_dIdhi_lat_parasmin_lesson.py

*Narrow:* on *dīdhī* / *dīdhīve* roots, drop final ``ī`` (``I``) when the following
*pratyaya* begins with ``y`` or ``i``. **Blocked** when the neighbour is ``e`` from
**3.4.79** (*sva-nimitta* ādeśa — lupta ``i`` is **not** *sthānivat* under **1.1.57**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_DIDHI_STEMS = frozenset({"dIdhI", "dIDI", "dIdhIve", "dIDIve"})


def _is_didhi_dhatu(term) -> bool:
    if "dhatu" not in term.tags:
        return False
    up = (term.meta.get("upadesha_slp1") or "").strip()
    if up in _DIDHI_STEMS:
        return True
    return up.startswith("dIdh") or up.startswith("dIDI")


def _find_site(state: State) -> int | None:
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if not _is_didhi_dhatu(left):
            continue
        if not left.varnas or left.varnas[-1].slp1 != "I":
            continue
        if left.meta.get("7_4_53_ii_lopa_done"):
            continue
        if not right.varnas:
            continue
        if right.meta.get("3_4_79_sva_nimitta_adesha") and right.varnas[0].slp1 == "e":
            continue
        if right.varnas[0].slp1 not in ("y", "i"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_site(state) is not None


def act(state: State) -> State:
    i = _find_site(state)
    if i is None:
        return state
    left = state.terms[i]
    left.varnas.pop()
    left.meta["7_4_53_ii_lopa_done"] = True
    base = "".join(v.slp1 for v in left.varnas)
    left.meta["upadesha_slp1"] = base
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.53",
    sutra_type=SutraType.VIDHI,
    text_slp1="yIvarRayordIDIvevyoH",
    text_dev="यीवर्णयोर्दीधीवेव्योः",
    padaccheda_dev="यि-इवर्णयोः / दीधी-वेव्योः",
    why_dev="दीधी-धातोः परे यि/इ-वर्णे ई-लोपः; ३.४.७९-स्वनिमित्तक-ए-परे न (१.१.५७)।",
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
