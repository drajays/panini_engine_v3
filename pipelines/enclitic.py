"""
pipelines/enclitic.py — yuṣmad / asmad in a sentence: 8.1.20–26 (वाम् नौ वस् नस् ते मे त्वा मा).

``derive_in_context("asmad", 4, 1, before=[…])`` derives the full pada through 4.1.2 … 7.2.9x (the
pada stops at मह्यम्, *before* tripāḍī — 8.1.x precedes 8.2.1), puts the sentence on the tape, runs the
adhikāras 8.1.16–18, the pratiṣedhas 8.1.24 / 8.1.25, the vibhāṣā 8.1.26 and the ādeśas
8.1.23 → 8.1.22 → 8.1.20 → 8.1.21 (apavāda first), then the tripāḍī tail (8.2.66 / 8.3.15: वस् → वः).

Context item (``before`` / ``after``), one per neighbouring pada **in the same pāda**:
    {"slp1": "grAmaH", "vibhakti": 1, "lexeme": None, "paSyArTa": False, "AlocanArTa": False,
     "yukta": False}
``lexeme`` names a particle (ca vā ha aha eva); ``yukta`` + ``paSyArTa`` describe a following verb of
seeing (8.1.25). The first pada of the list is the pāda-initial one (*apādādau*, 8.1.18).

CONSTITUTION Art. 7: ``apply_rule`` only; the choices are the sūtras', not this file's.
"""
from __future__ import annotations

from typing import Iterable, Mapping

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from engine.vibhakti_names import VIBHAKTI_TAG
from engine.vikalpa import Branch, explore
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.asmad_subanta import _derive, finish_tripadi


def _pada(item: Mapping) -> Term:
    tags = {"pada"}
    if item.get("vibhakti"):
        tags.add(VIBHAKTI_TAG[item["vibhakti"]])
    for flag, tag in (("paSyArTa", "paSyArTa"), ("AlocanArTa", "AlocanArTa"), ("yukta", "yukta_pronoun")):
        if item.get(flag):
            tags.add(tag)
    meta = {"upadesha_slp1": item["lexeme"]} if item.get("lexeme") else {}
    return Term(kind="pada", varnas=list(parse_slp1_upadesha_sequence(item["slp1"])), tags=tags, meta=meta)


def derive_in_context(stem_slp1: str, vibhakti: int, vacana: int, *,
                      before: Iterable[Mapping] = (), after: Iterable[Mapping] = ()) -> State:
    s = _derive(stem_slp1, vibhakti, vacana, defer_tripadi=True)
    pending = dict(s.meta.get("_tripadi_pending") or {})
    pronoun = s.terms[0]

    ctx_before = [_pada(i) for i in before]
    ctx_after = [_pada(i) for i in after]
    (ctx_before[0] if ctx_before else pronoun).tags.add("pAdAdi")
    form = s.flat_slp1()
    s.terms = ctx_before + [pronoun] + ctx_after
    s.emit_structural("__PADA_CONTEXT__", form_before=form, form_after=s.flat_slp1(),
                      why_dev="वाक्य-सन्दर्भ — समीपवर्ती पद (८.१.१७ पदात्, ८.१.१८ अपादादौ के लिए)।",
                      type_label="पद-सन्दर्भः", event="CONTEXT")

    for sid in ("8.1.16", "8.1.17", "8.1.18",      # padasya, padāt, anudāttaṃ sarvam apādādau
                "8.1.24", "8.1.25", "8.1.26",       # pratiṣedhas and the vibhāṣā, before the ādeśas
                "8.1.23", "8.1.22", "8.1.20", "8.1.21"):   # 8.1.23 apavāda of 8.1.22 goes first
        s = apply_rule(sid, s)

    pronoun = next(t for t in s.terms if t.meta.get("stem_upadesha_slp1") == stem_slp1)
    form = s.flat_slp1()
    s.terms = [pronoun]
    s.emit_structural("__PADA_CONTEXT_CLOSE__", form_before=form, form_after=s.flat_slp1(),
                      why_dev="सन्दर्भ-पद हटाये गये; अब त्रिपादी (८.२.१ से) केवल इस पद पर।",
                      type_label="पद-सन्दर्भः", event="CONTEXT")
    if "enclitic" in pronoun.tags:  # vas / nas end in s; the rest in a vowel or m
        pending = {"need_visarga": pronoun.varnas[-1].slp1 == "s"}
    return finish_tripadi(s, pending)


def derive_in_context_branches(*args, **kw) -> list[Branch]:
    """Every vibhāṣā reading (8.1.26) — one Branch per distinct surface."""
    return explore(lambda: derive_in_context(*args, **kw))


__all__ = ["derive_in_context", "derive_in_context_branches"]
