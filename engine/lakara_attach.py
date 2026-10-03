"""
engine/lakara_attach.py — लकार-प्रत्ययः on its own: the structural form of the attach sūtras
(3.2.110 luṅ · 3.2.111 laṅ · 3.2.115 liṭ · 3.3.13 lṛṭ · 3.3.15 luṭ · 3.3.139 lṛṅ · 3.3.161 liṅ ·
3.3.162 loṭ · 3.3.173 āśīrliṅ).

Which lakāra the speaker wants is the *meaning* (वर्तमाने, परोक्षे, अनद्यतने, आशिषि …), so it enters the
derivation as an input: the dhātu carries ``<lakāra>_derivation`` (set when the tape is built, like the
puruṣa/vacana that 3.4.78 later consumes). The sūtra then reads that tag — never ``state.meta['lakara']``
(Art. 2). Until now each attach sūtra only fired when a recipe armed it with a ``*_recipe`` meta key and
appended the placeholder by hand; this is the rule-driven path.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

AT_AGAMA_CONTEXT_TAG_NAME = "aT_agama_context"


@lru_cache(maxsize=1)
def _lakara_scope() -> str:
    """धातोः — the adhikāra under which a lakāra attaches (data, not a literal in the engine)."""
    path = Path(__file__).resolve().parent.parent / "data" / "inputs" / "phase_adhikaras.json"
    return json.loads(path.read_text(encoding="utf-8"))["lakara_scope"][0]


def lakara_site(state: State, derivation_tag: str, sutra_id: str, legacy_keys: tuple = ()) -> bool:
    """The dhātu has the vivakṣā for this lakāra, धातोः (3.1.91) governs, and no lakāra stands yet."""
    if any(state.meta.get(k) for k in legacy_keys):      # a recipe has armed this sūtra the old way
        return False
    if not adhikara_in_effect(sutra_id, state, _lakara_scope()):
        return False
    if not any("dhatu" in t.tags and derivation_tag in t.tags for t in state.terms):
        return False
    return not any(t.kind == "pratyaya" and "lakAra_pratyaya_placeholder" in t.tags for t in state.terms) \
        and not any((t.meta.get("source_lakara_upadesha") or "") != "" for t in state.terms)


def attach_lakara(state: State, upadesha: str, *, at_context: bool = False, tags: frozenset = frozenset()) -> State:
    """Append the lakāra placeholder (its it-letter stays; 1.3.3 → 1.3.9 take it away, as for every affix)."""
    if at_context:                       # 6.4.71 अट् reads this: laṅ · luṅ · lṛṅ
        for t in state.terms:
            if "dhatu" in t.tags:
                t.tags.add(AT_AGAMA_CONTEXT_TAG_NAME)
    state.terms.append(Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(upadesha),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"} | set(tags),
        meta={"upadesha_slp1": upadesha},
    ))
    return state
