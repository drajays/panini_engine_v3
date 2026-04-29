"""
1.4.59  उपसर्गाः क्रियायोगे  —  SAMJNA

Operational scope (v3):
  Tag an upadeśa-like prefix Term as ``upasarga`` when it is in *kriyā-yoga*
  with a dhātu in the same derivational State.

This eliminates pipeline-side hardcoding of ``upasarga`` tags for prefixes like
आङ् (SLP1 ``A~N``), प्र-, परि-, नि- used in glass-box recipes.

Blindness (CONSTITUTION Art. 2):
  - no semantic parsing; only adjacency/co-presence of a dhātu + known upadeśa
    prefix identities.
"""

from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State


# SLP1 identities used in this repository's pipelines (minimal, extendable).
# We normalise by removing '~' and trailing it letters (N/Y/R) for matching.
_UPASARGA_BASES: frozenset[str] = frozenset(
    {
        "pra",
        "pari",
        "ni",
        "A",  # āṅ base after it-lopa of A~N
        "upa",
        "prati",
        "abhi",
        "ud",
        "ava",
        "anu",
        "sam",
        "vi",
        "ati",
        "api",
        "adhi",
        "dur",
        "dus",
        "nir",
        "nis",
        "apa",
        "parA",
    }
)


def _normalize_base(up: str | None) -> str:
    if not up:
        return ""
    s = up.strip().replace("~", "")
    while s and s[-1] in {"N", "Y", "R"}:
        s = s[:-1]
    return s


def _eligible_prefix_indices(state: State):
    if not state.terms:
        return
    # Require a dhātu somewhere (kriyā-yoga: co-presence in this State).
    if not any("dhatu" in t.tags for t in state.terms):
        return
    for i, t in enumerate(state.terms):
        if "upasarga" in t.tags:
            continue
        # Prefer explicit kind, but allow generic prakṛti terms too.
        if t.kind not in {"upasarga", "prakriti"}:
            continue
        up = _normalize_base(t.meta.get("upadesha_slp1"))
        if up in _UPASARGA_BASES:
            yield i


def cond(state: State) -> bool:
    return next(_eligible_prefix_indices(state), None) is not None


def act(state: State) -> State:
    touched: list[int] = []
    for i in _eligible_prefix_indices(state):
        state.terms[i].tags.add("upasarga")
        touched.append(i)
        # Do not force 'anga' here; aṅga-saṃjñā is relative and comes from 1.4.13.
    if touched:
        state.samjna_registry["1.4.59_upasarga_indices"] = tuple(touched)
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.59",
    sutra_type=SutraType.SAMJNA,
    text_slp1="upasargAH kriyAyoge",
    text_dev="उपसर्गाः क्रियायोगे",
    padaccheda_dev="उपसर्गाः / क्रियायोगे",
    why_dev="क्रियायोगे उपसर्ग-संज्ञा (आङ्/प्र/परि/नि इत्यादयः) — पाइपलाइन-टैग-हैक् वर्जनीयः।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

