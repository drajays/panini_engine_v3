"""
1.4.19  तसौ मत्वर्थे  —  SAMJNA

**Pāṭha:** The suffixes *ta* and *su* (in *matvārtha* — possessive context)
[are called …].

v3: sets the interpretive gate ``1_4_19_tasau_matvArTe`` in
``state.paribhasha_gates`` to mark that the *ta*/*su*-in-matvārtha
designation is operative for downstream matvārtha processing.
Pāṭha: ashtadhyayi.com data.txt row i=14019 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from engine.subanta_eligibility import nominal_paribhasha_gate_eligible


def _legacy_cond(state: State) -> bool:
    return nominal_paribhasha_gate_eligible(state, "1_4_19_tasau_matvArTe")


def _sites(state: State):
    """The aṅga ending in t or s (tasau) just before a matvarthīya taddhita: the sense frame of 5.2.94 (tadasyāstyasminniti) is open."""
    from engine.taddhita_attach import sense_in
    if not sense_in(state, "5.2.94"):
        return
    for i in range(len(state.terms) - 1):
        a, p = state.terms[i], state.terms[i + 1]
        if "anga" in a.tags and "bha" not in a.tags and a.varnas and a.varnas[-1].slp1 in ("t", "s") \
                and "taddhita" in p.tags and "pratyaya" in p.tags and p.varnas:
            yield i


def cond(state: State) -> bool:
    return next(_sites(state), None) is not None or _legacy_cond(state)


def act(state: State) -> State:
    for i in list(_sites(state)):
        state.terms[i].tags.add("bha")           # tasau matvarthe bham: pada (1.4.17) is not given, so no jaś / rutva on yaśas, garut, vidyut
    state.paribhasha_gates["1_4_19_tasau_matvArTe"] = True
    state.samjna_registry["tasau_matvArTe"] = frozenset({"ta_su_matvArtha"})
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.19",
    sutra_type             = SutraType.SAMJNA,
    text_slp1              = 'tasO matvarTe',
    text_dev               = 'तसौ मत्वर्थे',
    samagra_slp1           = "ta-sO matvarTe Bam",
    samagra_dev            = "त-सौ मत्वर्थे  भम्",
    padaccheda_dev         = "तसौ / मत्वर्थे",
    why_dev                = "मत्वर्थे 'त' 'स' इति द्वयोः प्रत्यययोः संज्ञा।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
