"""
7.4.15  आपोऽन्यतरस्याम्  —  VIDHI (narrow for P027)

P027 bahuvrīhi samāsānta: before adding **kap**, the feminine āp-ending member
``KaTvA`` is optionally shortened to ``KaTva``.

v3 narrow slice:
  • recipe arms ``state.meta['P027_7_4_15_Ap_hrasva_arm']``
  • expects the second samāsa member to have upadeśa snapshot ``KaTvA`` and end
    in long ``A``; replace that final ``A`` with ``a``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site(state: State) -> int | None:
    if not state.meta.get("P027_7_4_15_Ap_hrasva_arm"):
        return None
    if len(state.terms) < 2:
        return None
    b = state.terms[1]
    if b.kind != "prakriti" or "samasa_member" not in b.tags:
        return None
    if (b.meta.get("upadesha_slp1") or "").strip() != "KaTvA":
        return None
    if b.meta.get("P027_7_4_15_hrasva_done"):
        return None
    if not b.varnas or b.varnas[-1].slp1 != "A":
        return None
    return 1


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return state
    b = state.terms[i]
    b.varnas[-1] = mk("a")
    b.meta["P027_7_4_15_hrasva_done"] = True
    state.meta.pop("P027_7_4_15_Ap_hrasva_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.15",
    sutra_type=SutraType.VIDHI,
    text_slp1="Apo 'nyatarasyAm",
    text_dev="आपोऽन्यतरस्याम्",
    padaccheda_dev="आपः / अन्यतरस्याम्",
    why_dev="समासान्त-कप्-पूर्वं आप्-अन्तस्य ह्रस्वः विभाषा (P027 — खट्वा→खट्व)।",
    anuvritti_from=("7.4.14",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

