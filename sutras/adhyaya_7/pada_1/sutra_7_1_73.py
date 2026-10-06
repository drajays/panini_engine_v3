"""
7.1.73  इकोऽचि विभक्तौ  —  VIDHI

Padaccheda: इकः अचि विभक्तौ

इकोऽचि विभक्तौ (7.1.73)
Pāṭha: ashtadhyayi.com data.txt row i=71073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_IK = frozenset("iIuUfFxX")
_AC = frozenset("aAiIuUfFxXeEoO")       # the pratyāhāra table is short-only; ac covers the dīrghas too


def _find(state: State):
    """इकोऽचि विभक्तौ (anuvṛtti napuṃsakasya, nuṃ — 7.1.72): a neuter aṅga ending in ik takes nuṃ before an
    ac-initial vibhakti (vāri + ṭā → vāriṇā, vāri + ṅe → vāriṇe, madhu + os → madhunoḥ). The nuṃ stands after the aṅga's last
    ac (1.1.47 mid aco'ntyāt paraḥ)."""
    for i in range(len(state.terms) - 1):
        anga, pr = state.terms[i], state.terms[i + 1]
        if not ({"anga", "prātipadika"} & anga.tags) or "napuṃsaka" not in anga.tags or "sup" not in pr.tags or not anga.varnas:
            continue
        if anga.meta.get("num_agama_done") or anga.varnas[-1].slp1 not in _IK:
            continue
        if (pr.meta.get("upadesha_slp1") or "") in ("su~", "su", "am", "Am"):
            continue          # su / am of a neuter are luk'd (7.1.23 svamornapuṃsakāt); ām takes nuṭ first (7.1.54): vārīṇām
        nxt = next((v for v in pr.varnas), None)
        if nxt is None or nxt.slp1 not in _AC:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is not None:
        anga = state.terms[i]
        anga.varnas.append(mk("n"))                    # last ac is the final here: nuṃ's n comes right after it
        anga.meta["num_agama_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = 'ikoci viBaktO',
    text_dev              = 'इकोऽचि विभक्तौ',
    samagra_slp1          = "ikaH napuMsakasya aci viBaktO num",
    samagra_dev           = "इकः नपुंसकस्य अचि विभक्तौ नुम्",
    padaccheda_dev        = "इकः अचि विभक्तौ",
    why_dev               = "(सूत्रम् 7.1.73) इकोऽचि विभक्तौ।",
    anuvritti_from        = ('7.1.1',),
    # the nuṃ stands between the aṅga's ik and the ṅit sup, so the guṇa of 7.3.111 / the au of 7.3.119 find no ik-final aṅga
    apavada_of            = ("7.3.111", "7.3.119"),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
