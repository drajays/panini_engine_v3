"""
8.2.77  हलि च  —  VIDHI

र्वोरुपधाया दीर्घ इकः (8.2.76) continues: the ik before a dhātu's र्/व् is
lengthened when an affix-initial hal follows (दिव् + य → दीव्यति). 8.2.79 न भकुर्छुराम् excepts कुर्/छुर् (कुर्वः).
Operates on the merged pada; dhātu varṇas carry ``dhatu_v`` (pada_merger).
Pāṭha: ashtadhyayi.com data.txt row i=82077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_IK_DIRGHA = {"i": "I", "u": "U", "f": "F", "x": "X"}
_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")
_NA_BHA_KUR_CHUR = {"kur", "Cur"}


def _dhatu_flat(vs) -> str:
    return "".join(v.slp1 for v in vs if "dhatu_v" in v.tags)


def _find(state: State):
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    vs = state.terms[0].varnas
    # 8.2.79 न भकुर्छुराम्: कुर् (कृ, 6.4.110) and छुर् — by the dhātu's upadeśa,
    # since the pada may begin with the aṭ (अकुर्वन्)
    up = (state.terms[0].meta.get("dhatu_upadesha") or "").strip()
    if _dhatu_flat(vs) in _NA_BHA_KUR_CHUR or up in {"qukfY", "kfY", "Cura~"}:
        return None
    for i in range(len(vs) - 2):
        a, rv, nxt = vs[i], vs[i + 1], vs[i + 2]
        if a.slp1 not in _IK_DIRGHA or rv.slp1 not in "rv" or "dhatu_v" not in rv.tags:
            continue
        if "dhatu_v" not in a.tags or nxt.slp1 not in _HAL:
            continue
        # हलि: the r/v is the dhātu's last varṇa and a hal (of the affix) follows
        if "dhatu_v" not in nxt.tags:
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[0].varnas[i] = mk(_IK_DIRGHA[state.terms[0].varnas[i].slp1])
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.77",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hali ca",
    text_dev       = "हलि च",
    samagra_slp1   = "rvoH DAtoH upaDAyAH ikaH hali dIrGaH",
    samagra_dev    = "र्वोः  धातोः उपधायाः इकः हलि दीर्घः",
    padaccheda_dev = "हलि च",
    why_dev        = "धातोः र्वोः पूर्वस्य इकः दीर्घः हलि परे (दीव्यति)।",
    anuvritti_from = ("8.2.76",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
