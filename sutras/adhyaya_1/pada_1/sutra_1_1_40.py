"""
1.1.40  क्त्वातोसुन्कसुनः  —  PARIBHASHA

User note (``1_1_40.md``): avyaya assignment for kṛdantas / derivatives ending in
the pratyayas **ktvā**, **tosun**, **kasun** (historical pratyaya identity, not
mere terminal phonology). **tumun** is included for ``split_prakriyas_11`` **P001**
(**भवितुम्**) — same *avyaya* classification pattern as *ktvā*/*tosun*/*kasun*.

Engine (glass-box):
  - Detect the pratyaya ancestry via ``pratyaya.meta['upadesha_slp1_original']``
    (or fallback to current ``upadesha_slp1``) in {"ktvA","tosun","kasun","tumun"}.
  - If an aṅga is followed by such a pratyaya, tag the block as ``avyaya``.
  - This is a metadata/paribhāṣā effect: no surface change.

Downstream effect in this repo:
  - **2.4.82** (*avyayād āp-supoḥ*) then lops a following *sup* via the zero-width
    ghost contract.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only tags/meta (no vibhakti/vacana, no gold).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import iter_anga_to_following_pratyaya_pairs
from engine.state import State

_TARGET_ORIG = frozenset({"ktvA", "tosun", "kasun", "tumun"})

META_1_1_40_DONE: str = "1_1_40_ktvA_tosun_kasun_avyaya_done"


def _orig_upadesha(pr) -> str:
    return (pr.meta.get("upadesha_slp1_original") or pr.meta.get("upadesha_slp1") or "").strip()


def _eligible_pairs(state: State):
    for ai, pi in iter_anga_to_following_pratyaya_pairs(state):
        anga = state.terms[ai]
        pr = state.terms[pi]
        if "anga" not in anga.tags or "prātipadika" not in anga.tags:
            continue
        if pr.kind != "pratyaya":
            continue
        if "pratyaya" not in pr.tags:
            continue
        if pr.meta.get(META_1_1_40_DONE):
            continue
        if _orig_upadesha(pr) not in _TARGET_ORIG:
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
        pr.meta[META_1_1_40_DONE] = True
    state.paribhasha_gates["1.1.40_ktvA_tosun_kasun"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.40",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "ktvA-tosun-kasunoH",
    text_dev       = "क्त्वातोसुन्कसुनः",
    padaccheda_dev = "क्त्वा / तोसुन् / कसुनः",
    why_dev        = "क्त्वा-तोसुन्-कसुन्-प्रत्ययान्तस्य अव्ययत्वम् (२.४.८२ सुप्-लुक्-प्रसङ्गः)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

