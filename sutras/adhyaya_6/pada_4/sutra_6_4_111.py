"""
6.4.111  श्नसोरल्लोपः  —  VIDHI (narrow for P028)

P028: ``as`` + ``tas`` (laṭ 3rd dual parasmaipada) with kṅit-like behaviour
via **1.2.4** → delete the initial vowel **a** of ``as`` giving ``s``.

v3 narrow slice:
  • recipe arms ``state.meta['P028_6_4_111_as_al_lopa_arm']``
  • expects dhātu term[0] with upadeśa snapshot ``as`` and leading ``a``
  • expects a following sārvadhātuka tiṅ term (here ``tas``) tagged ``kngiti``
    (by **1.2.4**) or having upadeśa ``tas``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site_p031(state: State) -> bool:
    if not state.meta.get("P031_6_4_111_sna_al_lopa_arm"):
        return False
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("P031_6_4_111_sna_done"):
            continue
        vs = t.varnas
        for j in range(len(vs) - 2):
            if vs[j].slp1 == "n" and vs[j + 1].slp1 == "a" and vs[j + 2].slp1 == "S":
                return True
    return False


def _site(state: State) -> bool:
    if not state.meta.get("P028_6_4_111_as_al_lopa_arm"):
        return False
    if len(state.terms) < 2:
        return False
    dh, tin = state.terms[0], state.terms[-1]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "as":
        return False
    if dh.meta.get("6_4_111_as_al_lopa_done"):
        return False
    if not dh.varnas or dh.varnas[0].slp1 != "a":
        return False
    if tin.kind != "pratyaya":
        return False
    up = (tin.meta.get("upadesha_slp1") or "").strip()
    if "kngiti" not in tin.tags and up != "tas":
        return False
    return True


def cond(state: State) -> bool:
    return _site_p031(state) or _site(state)


def act(state: State) -> State:
    if _site_p031(state):
        for t in state.terms:
            if "dhatu" not in t.tags or t.meta.get("P031_6_4_111_sna_done"):
                continue
            vs = t.varnas
            for j in range(len(vs) - 2):
                if vs[j].slp1 == "n" and vs[j + 1].slp1 == "a" and vs[j + 2].slp1 == "S":
                    del t.varnas[j + 1]
                    t.meta["P031_6_4_111_sna_done"] = True
                    state.meta.pop("P031_6_4_111_sna_al_lopa_arm", None)
                    return state
    if not _site(state):
        return state
    dh = state.terms[0]
    del dh.varnas[0]
    dh.meta["6_4_111_as_al_lopa_done"] = True
    state.meta.pop("P028_6_4_111_as_al_lopa_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.111",
    sutra_type=SutraType.VIDHI,
    text_slp1="Snasor allopaH",
    text_dev="श्नसोरल्लोपः",
    padaccheda_dev="श्नसोः / अल्-लोपः",
    why_dev="अस्-आदौ अकारस्य लोपः (P028 — अस्+तस् → स्तः)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

