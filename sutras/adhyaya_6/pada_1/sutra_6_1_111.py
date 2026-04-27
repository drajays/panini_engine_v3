"""
6.1.111  —  VIDHI (engine glass-box: *nn* + initial *t* of *ktavatu* residue)

Classical *bhid* + *ktavatu~* yields a stem ending in *n* that meets the *t* of
the *tavat* piece; this repo’s tape keeps that *t* as an explicit ``t`` *varṇa*
until this narrow step (armed only by ``state.meta["6_1_111_nn_t_lopa_arm"]``)
deletes it so the following vowel ``a`` surfaces as the *avat* onset
(*Binn* + *avat* → *Binnavat* … *bhinnavān*).

Full *śāstra* justification belongs in a later *Tripāḍī* / *saṁhitā* pass; the
recipe meta keeps *cond* mechanically blind to paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _eligible(state: State) -> bool:
    if not state.meta.get("6_1_111_nn_t_lopa_arm"):
        return False
    if len(state.terms) != 2:
        return False
    a0, pr = state.terms[0], state.terms[1]
    vs0, vs1 = a0.varnas, pr.varnas
    if len(vs0) < 2 or len(vs1) < 2:
        return False
    if vs0[-2].slp1 != "n" or vs0[-1].slp1 != "n":
        return False
    if vs1[0].slp1 != "t":
        return False
    if "krt" not in pr.tags:
        return False
    if pr.meta.get("6_1_111_t_lopa_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _eligible(state)


def act(state: State) -> State:
    if not _eligible(state):
        return state
    pr = state.terms[1]
    del pr.varnas[0]
    pr.meta["6_1_111_t_lopa_done"] = True
    state.samjna_registry["6.1.111_nn_t_lopa"] = True
    state.meta.pop("6_1_111_nn_t_lopa_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.111",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nn-t-lopa ktavatu-bhin-glass",
    text_dev       = "ण्ण्-त-लोपः (भिद्+क्तवतु, यन्त्र-सङ्केतः)",
    padaccheda_dev = "ण्ण् / त् / लोपः",
    why_dev        = "भिन्न्-अन्ताद् अग्रिमः तकारः लुप्यते (क्तवतु-शेषे अवदेशाय)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
