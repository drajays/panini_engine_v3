"""
6.1.2  एकाचो द्वे प्रथमस्य  —  VIDHI (narrow: *liṭ* *pā* + *atus*)

Teaching JSON **P035** step 8: after **6.4.64** the *dhātu* surface is **p** + *atus*;
with **1.1.59** *sthānivat* the elided **ā** is treated as present for *dvitva*, so the
first *ekāca* segment **pā** is doubled as **[pā]_{abhyāsa} + [p]_{dhātu} + atus**.

Narrow v3:
  - ``state.meta['P035_6_1_2_ekaca_dve_arm']`` and ``state.meta['lakara_liT']``.
  - First *dhātu* ``Term`` is exactly ``p`` (single *hal*), followed by the *liṭ*
    *atus* pratyaya (``lit_atus`` / ``upadesha_slp1 == 'atus'``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _site(state: State) -> bool:
    if not state.meta.get("P035_6_1_2_ekaca_dve_arm"):
        return False
    if not state.meta.get("lakara_liT"):
        return False
    di = _first_dhatu_index(state)
    if di is None or di + 1 >= len(state.terms):
        return False
    dh = state.terms[di]
    if dh.meta.get("P035_6_1_2_done"):
        return False
    if "".join(v.slp1 for v in dh.varnas) != "p":
        return False
    nxt = state.terms[di + 1]
    up = (nxt.meta.get("upadesha_slp1") or "").strip()
    if not (nxt.meta.get("lit_atus") is True or up == "atus"):
        return False
    if di > 0 and "abhyasa" in state.terms[di - 1].tags:
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    di = _first_dhatu_index(state)
    assert di is not None
    dh = state.terms[di]
    ab = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pA")),
        tags={"abhyasa", "anga"},
        meta={"P035_6_1_2_abhyasa": True},
    )
    state.terms.insert(di, ab)
    state.terms[di + 1].meta["P035_6_1_2_done"] = True
    state.meta.pop("P035_6_1_2_ekaca_dve_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.2",
    sutra_type=SutraType.VIDHI,
    text_slp1="ekAco dve prathamasya",
    text_dev="एकाचो द्वे प्रथमस्य",
    padaccheda_dev="एकाचः / द्वे / प्रथमस्य",
    why_dev="लिटि स्थानिवद्-आ-सहितस्य पा-इकाचो द्वित्वम् — प०३५।",
    anuvritti_from=("6.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
