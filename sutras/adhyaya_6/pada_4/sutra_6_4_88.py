"""
6.4.88  भुवो वुग्लुङ्लिटोः  —  VIDHI

Padaccheda: भुवः वुक् लुङ्-लिटोः

For bhū in luṅ/liṭ, insert vuk (= v, after IT lopa of u and k) as an āgama
immediately after the dhātu term.  vuk's u and k are both it → only v survives.

cond (structural — no lakāra read):
  - dhātu upadesha is BU/BU~
  - luṅ context: dhātu has ``aT_agama_context`` tag (set by 3.2.110)
    OR liṭ context: an abhyāsa term is on the tape (set by 6.1.4 dvitva)
  - vuk not already inserted
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import mk


def _find_dhatu_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1, -1, -1):
        if "dhatu" in state.terms[i].tags and "abhyasa" not in state.terms[i].tags:
            return i
    return None


def _already_done(state: State) -> bool:
    return state.samjna_registry.get("6_4_88_vuk_inserted") is True


def _is_bhu_dhatu(state: State) -> bool:
    di = _find_dhatu_index(state)
    if di is None:
        return False
    up = (state.terms[di].meta.get("upadesha_slp1") or "").strip()
    return up in {"BU", "BU~"}


def _luN_or_liT_context(state: State) -> bool:
    """True for luṅ or liṭ — using structural Term tags only (no lakāra read).

    luṅ: dhātu carries ``aT_agama_context`` tag (before 6.4.71 fires)
         OR ``aT_agama_6_4_71_done`` meta (after 6.4.71 fires and consumes the tag).
    liṭ: an ``abhyasa`` term is on the tape (set by 6.1.4 dvitva).
    """
    for t in state.terms:
        if "aT_agama_context" in t.tags:       # pre-6.4.71 luṅ
            return True
        if t.meta.get("aT_agama_6_4_71_done"): # post-6.4.71 luṅ
            return True
    for t in state.terms:
        if "abhyasa" in t.tags:                # liṭ dvitva context
            return True
    return False


def cond(state: State) -> bool:
    if _already_done(state):
        return False
    if not _is_bhu_dhatu(state):
        return False
    if not _luN_or_liT_context(state):
        return False
    di = _find_dhatu_index(state)
    if di is None:
        return False
    if di + 1 < len(state.terms) and state.terms[di + 1].meta.get("vuk_6_4_88"):
        return False
    return True


def act(state: State) -> State:
    di = _find_dhatu_index(state)
    if di is None:
        return state

    v_varna = mk("v")
    u_varna = mk("u")
    u_varna.tags.add("it_candidate_halantyam")
    k_varna = mk("k")
    k_varna.tags.add("it_candidate_halantyam")

    vuk_term = Term(
        kind="agama",
        varnas=[v_varna, u_varna, k_varna],
        tags={"agama", "pratyaya"},
        meta={"upadesha_slp1": "vuk", "vuk_6_4_88": True},
    )
    state.terms.insert(di + 1, vuk_term)
    state.samjna_registry["6_4_88_vuk_inserted"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Buvo vugluNliwoH",
    text_dev              = "भुवो वुग्लुङ्लिटोः",
    padaccheda_dev        = "भुवः वुक् लुङ्-लिटोः",
    why_dev               = "भू-धातोः लुङि लिटि च वुक्-आगमः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
