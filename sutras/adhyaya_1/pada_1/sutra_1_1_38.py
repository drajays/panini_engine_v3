"""
1.1.38  तद्धितश्चासर्वविभक्तिः  —  SAMJNA (avyaya eligibility in v3 slice)

User note (``1.1.38.md``): taddhita endings that are **not** *sarva-vibhakti*
behave as *avyaya* for the purpose of *sup*-*luk* via **2.4.82**.

Engine (glass-box):
  - A *taddhita* pratyaya ``Term`` whose own definition marks it as
    ``asarva_vibhakti_taddhita`` triggers an avyaya-tag on the taddhitānta block.
  - This is a **metadata** assignment only (no surface change).

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only structural tags/meta on Terms, not vibhakti/vacana, not gold.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import iter_anga_to_following_pratyaya_pairs
from engine.state import State

META_1_1_38_AVYAYA_DONE: str = "1_1_38_taddhita_asarvavibhakti_avyaya_done"
META_ASARVA_VIBHAKTI_TADDHITA: str = "asarva_vibhakti_taddhita"


def _eligible_pairs(state: State):
    for ai, pi in iter_anga_to_following_pratyaya_pairs(state):
        anga = state.terms[ai]
        pr = state.terms[pi]
        if "anga" not in anga.tags or "prātipadika" not in anga.tags:
            continue
        if "pratyaya" not in pr.tags or "taddhita" not in pr.tags:
            continue
        if pr.meta.get(META_1_1_38_AVYAYA_DONE):
            continue
        if pr.meta.get(META_ASARVA_VIBHAKTI_TADDHITA) is not True:
            continue
        # Already avyaya: idempotent.
        if "avyaya" in pr.tags and "avyaya" in anga.tags:
            continue
        yield ai, pi


def cond(state: State) -> bool:
    return next(_eligible_pairs(state), None) is not None


def act(state: State) -> State:
    for ai, pi in _eligible_pairs(state):
        anga = state.terms[ai]
        pr = state.terms[pi]
        anga.tags.add("avyaya")
        pr.tags.add("avyaya")
        pr.meta[META_1_1_38_AVYAYA_DONE] = True
    state.samjna_registry["1_1_38_taddhita_asarvavibhakti"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.38",
    sutra_type     = SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1      = "taddhitaH ca asarva-vibhaktiH",
    text_dev       = "तद्धितश्चासर्वविभक्तिः",
    padaccheda_dev = "तद्धितः / च / असर्व-विभक्तिः",
    why_dev        = "असर्व-विभक्तिक-तद्धितान्तः अव्ययवत् (२.४.८२ सुप्-लुक्-प्रसङ्गः)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["META_ASARVA_VIBHAKTI_TADDHITA", "SUTRA"]

