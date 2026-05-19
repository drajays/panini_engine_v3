"""
6.4.88  भुवो वुग्लुङ्लिटोः  —  VIDHI

Padaccheda: भुवः वुक् लुङ्-लिटोः

For bhū in luṅ/liṭ, insert vuk (= v, after IT lopa of u and k) as an āgama
immediately after the dhātu term. vuk's u and k are both it → only v survives.

Engine:
  - cond: ``state.meta.get("6_4_88_arm") is True``
  - Find the LAST dhātu-tagged term; if the next term is already a vuk term,
    skip (already done).
  - act: insert a new Term(kind="agama") with varnas [v, u(it), k(it)] after
    the dhātu term, marked so 1.3.9 removes u and k leaving only v.
  - state.samjna_registry["6_4_88_vuk_inserted"] = True
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence, mk


def _find_dhatu_index(state: State) -> int | None:
    """Find the LAST dhātu-tagged term index."""
    for i in range(len(state.terms) - 1, -1, -1):
        if "dhatu" in state.terms[i].tags:
            return i
    return None


def _already_done(state: State) -> bool:
    return state.samjna_registry.get("6_4_88_vuk_inserted") is True


def _is_bhu_dhatu(state: State) -> bool:
    """True iff primary dhātu is BU (bhū) — the rule is 'bhuvō vuk'."""
    di = _find_dhatu_index(state)
    if di is None:
        return False
    d = state.terms[di]
    up = (d.meta.get("upadesha_slp1") or "").strip()
    return up in {"BU", "BU~"}


def cond(state: State) -> bool:
    if not state.meta.get("6_4_88_arm"):
        return False
    if _already_done(state):
        return False
    if not _is_bhu_dhatu(state):
        return False
    di = _find_dhatu_index(state)
    if di is None:
        return False
    # Check that the next term is not already a vuk term
    if di + 1 < len(state.terms):
        nxt = state.terms[di + 1]
        if nxt.meta.get("vuk_6_4_88"):
            return False
    return True


def act(state: State) -> State:
    di = _find_dhatu_index(state)
    if di is None:
        return state

    # Build vuk āgama: v + u(it) + k(it)
    # vuk upadesha: v is the residue; u and k are it-markers (1.3.3 halantyam → k is it;
    # 1.3.2/anunasika treatment: u in vuk is it by anuvṛtti from prior rules).
    # We build varnas manually: v stays, u gets it_candidate_halantyam-style tag,
    # k gets it_candidate_halantyam.
    v_varna = mk("v")
    u_varna = mk("u")
    u_varna.tags.add("it_candidate_halantyam")   # u is it in vuk (1.3.3 scope)
    k_varna = mk("k")
    k_varna.tags.add("it_candidate_halantyam")   # k is halantyam it

    vuk_term = Term(
        kind="agama",
        varnas=[v_varna, u_varna, k_varna],
        tags={"agama", "pratyaya"},
        meta={
            "upadesha_slp1": "vuk",
            "vuk_6_4_88": True,
        },
    )

    # Insert after dhātu
    state.terms.insert(di + 1, vuk_term)
    state.meta["6_4_88_arm"] = False
    state.samjna_registry["6_4_88_vuk_inserted"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Buvo vugluNliwoH",
    text_dev              = "भुवो वुग्लुङ्लिटोः",
    padaccheda_dev        = "भुवः वुक् लुङ्-लिटोः",
    why_dev               = "भू-धातोः लुङि लिटि च वुक्-आगमः; वुकः उ-क् इत्-लोपे केवलं व् अवशिष्यते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
