"""
8.3.60  शासिवसिघसीनां च  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=83060
  padaccheda: शासि-वसि-घसीनाम् च · anuvṛtti: 8.2.108 संहितायाम् | 8.3.55 अपदान्तस्य मूर्धन्यः | 8.3.56 सः | 8.3.57 इण्कोः
- Kāśikā: "शासि वसि घसि इत्येतेषां चेण्कोरुत्तरस्य सकारस्य मूर्धन्यो भवति" — अन्वशिषत्, शिष्टः, शिष्टवान्; उषितः, उषितवान्; जक्षतुः, जक्षुः
- Cross-validation: tests/regression/test_findings_probe_loop.py (ऊषतुः);
  tests/unit/test_uditvA_uzitvA_ktvA_samprasaraNa.py (उषित्वा)

The s of the dhātus śās (śāsu~), vas (vasa~) and ghas (ghasḷ~) becomes ṣ when an iṇ letter (or its savarṇa,
1.1.69) or a ku letter stands immediately before it and the s is not pada-final (8.3.55 apadāntasya). The
dhātu's own varṇas are read structurally: before the pada-merge from the dhātu Term, after it from the
`dhatu_v` varṇa tags and the pada's `dhatu_upadesha`. Intervening num/visarga/śar (8.3.58) is not modelled.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import IN, KU_VARGA

_DHATUS = frozenset({"SAsu~", "SAs", "vasa~", "vas", "Gasx~", "Gas"})
_LEFT = IN | {"I", "U", "F", "X"} | KU_VARGA


def _dhatu_s_sites(state: State) -> list[tuple[int, int]]:
    """(term index, varṇa index) of every s that belongs to one of the named dhātus."""
    sites = []
    for ti, t in enumerate(state.terms):
        if "dhatu" in t.tags and "abhyasa" not in t.tags:
            if (t.meta.get("upadesha_slp1") or "").strip() in _DHATUS:
                sites += [(ti, vi) for vi, v in enumerate(t.varnas) if v.slp1 == "s"]
        elif "pada" in t.tags and (t.meta.get("dhatu_upadesha") or "").strip() in _DHATUS:
            sites += [(ti, vi) for vi, v in enumerate(t.varnas) if v.slp1 == "s" and "dhatu_v" in v.tags]
    return sites


def _find(state: State) -> tuple[int, int] | None:
    flat = [(ti, vi) for ti, t in enumerate(state.terms) for vi in range(len(t.varnas))]
    pos = {site: k for k, site in enumerate(flat)}
    for site in _dhatu_s_sites(state):
        k = pos[site]
        if k == 0 or k == len(flat) - 1:
            continue
        pti, pvi = flat[k - 1]
        if state.terms[pti].varnas[pvi].slp1 in _LEFT:
            return site
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ti, vi = _find(state)
    old = state.terms[ti].varnas[vi]
    new = mk("z")
    new.tags |= old.tags
    state.terms[ti].varnas[vi] = new
    return state


SUTRA = SutraRecord(
    sutra_id="8.3.60",
    sutra_type=SutraType.VIDHI,
    text_slp1='SAsivasiGasInAM ca',
    text_dev='शासिवसिघसीनां च',
    samagra_slp1="iRkoH SAsivasiGasinAM ca apadAntasya saHmUrDanyaH ",
    samagra_dev="इण्कोः शासिवसिघसिनां च अपदान्तस्य सःमूर्धन्यः ।",
    padaccheda_dev="शासि-वसि-घसि-नाम् / च",
    why_dev="इण्कोः परस्य शास्-वस्-घसां सकारस्य मूर्धन्यः (ऊषतुः, उषित्वा, शिष्टः, जक्षुः)।",
    anuvritti_from=("8.3.57",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
