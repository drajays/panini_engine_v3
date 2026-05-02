"""
6.4.114  दद्धस्य च  —  VIDHI (narrow demo: *sic* residue after *iṭ* + *dh* → *ḍ*)

Engine scope (**P026** *avaDIt*): after *pada* merge, **before** **8.2.1**
(*Tripāḍī* — *aṣṭādhyāyī* 6.* rules are not ``is_tripadi`` and would otherwise
hit the *asiddha* gate once ``tripadi_zone`` is true):

  #. delete the *sic* ``s`` standing between a long *ī* (``I``) and apṛkta ``t``;
  #. replace cluster ``dh`` before ``I`` with retroflex ``D`` (SLP1 ``D``).

Pipelines must set ``state.meta['6_4_114_P026_arm']`` before applying.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _matches(state: State) -> bool:
    if not state.meta.get("6_4_114_P026_arm"):
        return False
    if len(state.terms) != 1:
        return False
    t = state.terms[0]
    if "pada" not in t.tags:
        return False
    if t.meta.get("6_4_114_P026_done"):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    t = state.terms[0]
    vs = t.varnas
    # (1) … I s t …  → drop s
    for i in range(len(vs) - 2):
        if vs[i].slp1 == "I" and vs[i + 1].slp1 == "s" and vs[i + 2].slp1 == "t":
            del vs[i + 1]
            break
    # (2) … d h I …  → D I …
    for i in range(len(vs) - 2):
        if vs[i].slp1 == "d" and vs[i + 1].slp1 == "h" and vs[i + 2].slp1 == "I":
            vs[i] = mk("D")
            del vs[i + 1]
            break
    t.meta["6_4_114_P026_done"] = True
    state.meta["6_4_114_P026_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.114",
    sutra_type=SutraType.VIDHI,
    text_slp1="dadDasya ca (P026 narrow)",
    text_dev="दद्धस्य च",
    padaccheda_dev="दद्धस्य / च",
    why_dev="सिच्-सकारस्य लोपः, धकारस्य ठत्वं च (अवधीत्-ट्रिपादी-डेमो)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
