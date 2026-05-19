"""
8.3.78  इणः षीध्वंलुङ्लिटां धोऽङ्गात्  —  VIDHI

After iṇ (= i, particularly from iṭ-augment), in liṭ/luṅ, the `dh` (D in SLP1)
that begins the tiṅ ādeśa `dhvam`/`dhve` (from aṅga context) → `ḍh` (Q in SLP1).

Applied in karmani liṭ 2pl: i + dhve → i + ḍhve = iḍhve.
  babhūv + i + dhve → babhūviḍhve

Arm flag: state.meta["8_3_78_arm"] must be True.
Finds cross-term i (final of iṭ-residue) + D (initial of tiṅ ādeśa Dve).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _find_i_before_D(state: State):
    """Find i+D (iṭ-vowel followed by dh) within any term or at cross-term boundary."""
    if not state.meta.get("8_3_78_arm"):
        return None
    # Scan within each term (dvitva may have merged iṭ+tiṅ into one term)
    for ti, t in enumerate(state.terms):
        vs = t.varnas
        if t.meta.get("8_3_78_done"):
            continue
        for vi in range(len(vs) - 1):
            if vs[vi].slp1 == "i" and vs[vi + 1].slp1 == "D":
                return ("intra", ti, vi + 1)
    # Also scan cross-term boundary
    for i in range(len(state.terms) - 1):
        t1, t2 = state.terms[i], state.terms[i + 1]
        if not t1.varnas or not t2.varnas:
            continue
        if t1.meta.get("8_3_78_done"):
            continue
        if t1.varnas[-1].slp1 == "i" and t2.varnas[0].slp1 == "D":
            return ("cross", i, 0)
    return None


def cond(state: State) -> bool:
    return _find_i_before_D(state) is not None


def act(state: State) -> State:
    hit = _find_i_before_D(state)
    if hit is None:
        return state
    kind, ti, vi = hit
    if kind == "intra":
        state.terms[ti].varnas[vi] = _mk("Q")  # D (dha) → Q (ḍha)
        state.terms[ti].meta["8_3_78_done"] = True
    else:  # cross
        state.terms[ti + 1].varnas[0] = _mk("Q")
        state.terms[ti + 1].meta["8_3_78_done"] = True
    state.meta.pop("8_3_78_arm", None)
    state.samjna_registry["8.3.78_dha_dhva"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "iRaH zIDvaMluNliwAM Do'NgAt",
    text_dev              = "इणः षीध्वंलुङ्लिटां धोऽङ्गात्",
    padaccheda_dev        = "इणः षीध्वं-लुङ्-लिटाम् धः अङ्गात्",
    why_dev               = (
        "इट्-जन्य-इ-परे लिटि ध्वम्/ध्वे-आदि-प्रत्यये ध् → ढ् — "
        "बभूव् + इ + ध्वे → बभूविढ्वे।"
    ),
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
