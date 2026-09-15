"""
6.4.111  श्नसोरल्लोपः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=604111
- Kāśikā: श्नोः अलोपः (अस्-धातोः आद्यचः लोपः णित्-सार्वधातुके)
- Cross-validation: tests/unit/test_phalAni_santi_as_lat_padanta_lesson.py (*as*+झि → *s*+अन्ति);
  pipelines/kO_staH_vakya.py (*as*+तस् → स्तः, P028 arm grandfathered)

*Śnasor al lopaḥ:* delete the initial vowel **a** of **as** when an **a-pit**
*sārvadhātuka* *tiṅ* follows (after **1.2.4** *kṅit* on the *tiṅ*).  The lopa is
*para-nimitta* (apit *tiṅ*), not *pūrva-vidhi* — see **1.1.58** blocking **6.1.77**
at a *pūrvapada* boundary in the *phalāni santi* lesson.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1

_META_PADADI_AC_LOPA = "padadi_ac_lopa_para_nimitta"


def _apit_sarvadhatuka_tin_after(state: State, dhatu_i: int) -> bool:
    for j in range(dhatu_i + 1, len(state.terms)):
        pr = state.terms[j]
        if "pratyaya" not in pr.tags:
            continue
        if pr.meta.get("pit") is True:
            continue
        up = (pr.meta.get("upadesha_slp1") or "").strip()
        if is_sarvadhatuka_upadesha_slp1(up):
            return True
        if "tin_adesha_3_4_78" in pr.tags or "kngiti" in pr.tags:
            return True
    return False


def _find_as_al_lopa(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "as":
            continue
        if t.meta.get("6_4_111_as_al_lopa_done"):
            continue
        if not t.varnas or t.varnas[0].slp1 != "a":
            continue
        if not _apit_sarvadhatuka_tin_after(state, i):
            continue
        return i
    return None


def _site_p031(state: State) -> bool:
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


def cond(state: State) -> bool:
    return _site_p031(state) or _find_as_al_lopa(state) is not None


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
                    return state
    di = _find_as_al_lopa(state)
    if di is None:
        return state
    dh = state.terms[di]
    del dh.varnas[0]
    dh.meta["6_4_111_as_al_lopa_done"] = True
    dh.meta[_META_PADADI_AC_LOPA] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.111",
    sutra_type=SutraType.VIDHI,
    text_slp1="Snasor allopaH",
    text_dev="श्नसोरल्लोपः",
    padaccheda_dev="श्नसोः / अल्-लोपः",
    why_dev="अस्-आद्यचः लोपः अपित्-सार्वधातुके (फलानि सन्ति, कौ स्तः)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

META_PADADI_AC_LOPA = _META_PADADI_AC_LOPA

__all__ = ["META_PADADI_AC_LOPA", "SUTRA"]
