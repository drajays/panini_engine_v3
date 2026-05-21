"""
3.4.92  आडुत्तमस्य पिच्च  —  VIDHI

In loṭ (imperative) uttama (1st person) cells, after 3.4.93 has changed
the terminal 'e' to 'E' (ai), this rule prepends the āgama āṭ (A+T in SLP1)
before the tiṅ ādeśa term.  The pipeline then applies 1.3.3 + 1.3.9 to
drop the halantyam T, leaving just ā (A).

  1sg: [E]      → [āṭ][E]     → after IT-lopa → [A][E]
  1du: [vahE]   → [āṭ][vahE]  → after IT-lopa → [A][vahE]
  1pl: [mahE]   → [āṭ][mahE]  → after IT-lopa → [A][mahE]

Arm: state.meta["3_4_92_loT_karmani_arm"] must be True.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_uttama_tin(state: State):
    if not state.meta.get("3_4_92_loT_karmani_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_92_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "E":
            continue
        return ti
    return None


def cond(state: State) -> bool:
    return _find_uttama_tin(state) is not None


def act(state: State) -> State:
    ti = _find_uttama_tin(state)
    if ti is None:
        return state
    # Insert āṭ (A+T) before the tiṅ ādeśa term; pipeline will run 1.3.3+1.3.9
    at_term = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("AT"),
        tags={"pratyaya", "upadesha", "agama", "aTa_agama"},
        meta={"upadesha_slp1": "AT"},
    )
    state.terms.insert(ti, at_term)
    state.terms[ti + 1].meta["3_4_92_done"] = True
    state.meta.pop("3_4_92_loT_karmani_arm", None)
    state.samjna_registry["3.4.92_AT_uttama"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "Aquttamasya picca",
    text_dev              = "आडुत्तमस्य पिच्च",
    padaccheda_dev        = "आट् उत्तमस्य पित् च",
    why_dev               = (
        "लोट् उत्तम-आत्मनेपद-प्रत्ययेषु (ऐ, वहै, महै) पूर्वम् "
        "आट्-आगमः; प्रत्ययश्च पित् भवति।"
    ),
    anuvritti_from        = ('3.4.93',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
