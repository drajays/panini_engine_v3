"""
1.2.11  लिङ्सिचावात्मनेपदेषु  —  VIDHI (narrow demo)

Demo slice (भित्सीष्ट / BitzIzwa):
  Treat the āśīr-liṅ **sīyut** augment as *kitvat* in ātmanepada contexts,
  so downstream aṅga-kārya would be blocked by **1.1.5** (kṅiti/kit-locus).

Narrow v3:
  - recipe arms via ``state.meta['1_2_11_ling_sic_kitvat_arm']``.
  - when a ``ling_sIyuw`` pratyaya is present and the final *tiṅ* ādeśa is
    from the *taṅ* block (e.g. ``ta``), tag that augment with ``kngiti``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


_ATMANEPADA_TIN = frozenset({"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"})


def _find(state: State) -> int | None:
    if not state.meta.get("1_2_11_ling_sic_kitvat_arm"):
        return None
    if not state.meta.get("ashir_liG"):
        return None
    if len(state.terms) < 2:
        return None
    last = state.terms[-1]
    if "pratyaya" not in last.tags:
        return None
    up = (last.meta.get("upadesha_slp1") or "").strip()
    if up not in _ATMANEPADA_TIN:
        return None
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if "kngiti" in t.tags:
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.samjna_registry["1.2.11_ling_sIyuw_kitvat"] = True
    state.meta["1_2_11_ling_sic_kitvat_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.11",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="liG-sici-Av Atmanepadezu",
    text_dev="लिङ्सिचावात्मनेपदेषु",
    padaccheda_dev="लिङ्-सिचौ / आत्मनेपदेषु",
    why_dev="आशीर्लिङि आत्मनेपदे सीयुट्-आगमः किद्वत् (डेमो-संज्ञा)।",
    anuvritti_from=("1.2.9",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

