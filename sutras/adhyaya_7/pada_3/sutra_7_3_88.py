"""
7.3.88  भूसुवोस्तिङि  —  PRATISHEDHA

Sources consulted:
- ashtadhyayi.com data.txt row i=73088
- Kāśikā: "भू सू इत्येतयोस्तिङि सार्वधातुके गुणो न भवति" — अभूत्, अभूः, अभूवम्; सुवै, सुवावहै, सुवामहै
  pratyudāharaṇa: भवति (śap stands between bhū and the tiṅ)
- Cross-validation: tests/regression/test_findings_probe_loop.py (सुवामहै)

A tiṅ stands directly after the dhātu bhū or sū only because their vikaraṇa was luk'd (ṣūṅ is adādi: śap, 2.4.72;
bhū in luṅ: sic, 2.4.77); then the guṇa of 7.3.84 is forbidden for that aṅga. The luk rule tags the aṅga
`vikarana_luk`, so before the vikaraṇa stage (bhū + tiṅ, śap not yet added) this rule cannot fire. The āṭ of
3.4.92 is part of the tiṅ (1.1.46 ādyantau ṭakitau).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.nimitta_predicates import is_tin_adesha
from engine.state import State

_DHATUS = frozenset({"BU", "zUN"})


def _bhu_su_before_tin(state: State) -> bool:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in _DHATUS or "vikarana_luk" not in t.tags:
            continue
        rest = [u for u in state.terms[i + 1:] if u.varnas]
        if rest and "agama" in rest[0].tags:      # a ṭit āgama (āṭ 3.4.92) is the tiṅ's own beginning (1.1.46)
            rest = rest[1:]
        if rest and is_tin_adesha(rest[0]):
            return True
    return False


def cond(state: State) -> bool:
    return _bhu_su_before_tin(state)


def act(state: State) -> State:
    state.meta["__why_now_dev__"] = "भू-सू-धात्वोः परतः साक्षात् तिङि ७.३.८४ गुणस्य निषेधः (सुवामहै, अभूत्)।"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.88",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "BUsuvostiNi",
    text_dev              = "भूसुवोस्तिङि",
    samagra_slp1          = "BUsuvoH tiNi guRaH na",
    samagra_dev           = "भूसुवोः तिङि गुणः न",
    padaccheda_dev        = "भू-सुवोः तिङि",
    why_dev               = "भू-सू-धात्वोः तिङि सार्वधातुके गुणो न (अभूत्, सुवै)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
    blocks_sutra_ids      = ("7.3.84",),
)

register_sutra(SUTRA)
