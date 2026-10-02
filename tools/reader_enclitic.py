"""
tools/reader_enclitic.py — judge yuṣmad/asmad words in a verse with 8.1.20–26 (tools layer, Art. 6).

The reader's annotation gives each word its (stem, vibhakti, vacana); the *sentence* comes from the verse
text itself: each line is split into two pādas at its syllable midpoint (anuṣṭubh 8+8, triṣṭubh 11+11, …),
and the pronoun's neighbours inside its pāda go on the tape (``pipelines.enclitic.derive_in_context``).
Neighbour facts are limited to what the text shows (surface, particle identity) plus the annotation's
vibhakti of the previous pada; *yukta* with a paśyārtha verb (8.1.25) is not derivable from the text, so a
verdict that depends on it carries a note instead of a claim.

Verdicts for a word whose attested form is X:
  * X is what some 8.1.26 reading of the context derives            → ``derived``
  * X is the full form but 8.1.20–23 would have licensed an ādeśa   → ``derived`` + ``enclitic_note``
    (the paradigm derives X; Pāṇini's ādeśa is expected here — ārṣa / contrastive use is the reader's call)
  * otherwise                                                        → ``differs``
"""
from __future__ import annotations

import difflib
import re
from functools import lru_cache

from core.transliterate import dev_to_slp1

PARTICLES = {"च": "ca", "वा": "vA", "ह": "ha", "अह": "aha", "एव": "eva"}
_AC = frozenset("aAiIuUfFxXeEoO")
_PRONOUNS = ("asmad", "yuzmad")


def _syl(dev: str) -> int:
    return sum(c in _AC for c in dev_to_slp1(dev))


def _tokens(line: str) -> list[str]:
    return [t for t in re.split(r"[\s।॥॰|]+", line) if t and not re.fullmatch(r"[०-९0-9]+", t)]


def _norm(s: str) -> str:  # त्वाम् / त्वां, सम्मूढ / संमूढ — spelling variants of the same letters
    return dev_to_slp1(s).replace("M", "m")


def _anv_key(w: dict) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", w.get("anvaya_no") or "0"))


def _cn(s: str) -> str:
    """Comparison key: SLP1 with every nasal and anusvāra folded to ``n``, spaces dropped."""
    return re.sub(r"[MNYRmn]", "n", dev_to_slp1(s)).replace(" ", "")


def padas(lines: list[str], words: list[dict]) -> list[dict] | None:
    """The verse as text-ordered padas, each placed in a (line, pāda): ``{"words", "dev", "vib", "pada_id"}``.

    ``anvaya_no`` is text order (``poem`` is the prose order). A pada ends at a word that is not a
    *samāsa_member*; a new sandhi token starts at each word carrying a ``sandhied_word``. Words numbered
    ``N.M.K`` are implied (absent from the text) and skipped. The annotation's tokens are aligned to the text
    by their concatenated letters (tolerating nasal spellings and split tokens); if they still do not
    line up, return None — better no verdict than a guessed one.
    """
    line_txt = ["".join(_cn(t) for t in _tokens(line)) for line in lines]
    line_off = [sum(len(x) for x in line_txt[:i]) for i in range(len(line_txt))]
    seq = sorted((w for w in words if len(_anv_key(w)) <= 2), key=_anv_key)
    tokens: list[list[dict]] = []
    for w in seq:
        if (w.get("sandhied_word") or "").strip() or not tokens:
            tokens.append([])
        tokens[-1].append(w)
    owners = [_cn(tok[0].get("sandhied_word") or tok[0]["word_dev"]) for tok in tokens]
    a, b = "".join(owners), "".join(line_txt)
    approx = a != b
    blocks = []
    if approx:  # the annotation holds unsandhied words where the text has sandhi: map offsets through the matches
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        if sm.ratio() < 0.9:
            return None
        blocks = sm.get_matching_blocks()

    def text_off(o: int) -> int:
        if not approx:
            return o
        best = max((m for m in blocks if m.a <= o), key=lambda m: m.a, default=None)
        return 0 if best is None else best.b + min(o - best.a, best.size)

    out, off = [], 0
    for tok, own in zip(tokens, owners):
        toff = min(text_off(off), len(b) - 1)
        li = max(i for i, o in enumerate(line_off) if o <= toff)
        txt = line_txt[li]
        half = sum(c in _AC for c in txt) // 2
        pos = sum(c in _AC for c in txt[: toff - line_off[li]])
        group: list[dict] = []
        tok_syl = sum(c in _AC for c in own)
        member_syl = max(1, sum(_syl(w["word_dev"]) for w in tok))
        cum = 0  # members sit proportionally inside their token: sandhi shortens the junctions
        for w in tok:
            group.append(w)
            if w.get("kind") == "samasa_member":
                continue
            at = pos + (cum * tok_syl) // member_syl
            out.append({"words": group, "dev": "".join(x["word_dev"].strip("-") for x in group),
                        "vib": (w.get("engine", {}).get("inputs") or {}).get("vibhakti") if w.get("kind") == "subanta" else None,
                        "pada_id": (li, 0 if at < half else 1), "approx": approx})
            cum += sum(_syl(x["word_dev"]) for x in group)
            group = []
        off += len(own)
    return out


def context_for(pds: list[dict], word: dict) -> dict | None:
    """Same-pāda neighbours of ``word`` (before / the next pada) for ``derive_in_context``."""
    i = next((k for k, p in enumerate(pds) if any(x is word for x in p["words"])), None)
    if i is None:
        return None
    pid = pds[i]["pada_id"]
    before = [{"slp1": dev_to_slp1(p["dev"]), "vibhakti": p["vib"]} for p in pds[:i] if p["pada_id"] == pid]
    after = [{"slp1": dev_to_slp1(p["dev"]), "lexeme": PARTICLES.get(p["dev"])}
             for p in pds[i + 1:i + 2] if p["pada_id"] == pid]
    return {"before": before, "after": after, "approx": pds[i]["approx"]}


@lru_cache(maxsize=4096)
def _surfaces(stem: str, vib: int, vac: int, ctx_key: str) -> tuple[tuple[str, str], ...]:
    """(slp1, dev) for every vibhāṣā reading of the pronoun in this context."""
    import json

    from pipelines.enclitic import derive_in_context_branches

    c = json.loads(ctx_key)
    return tuple((b.surface_slp1, b.surface_dev)
                 for b in derive_in_context_branches(stem, vib, vac, before=c["before"], after=c["after"]))


def full_dev(stem: str, vib: int, vac: int) -> str:
    from pipelines.asmad_subanta import derive_asmad, derive_yuzmad

    return (derive_asmad if stem == "asmad" else derive_yuzmad)(vib, vac).flat_dev()


def judge(inputs: dict, attested_slp1: str, ctxs: list[dict]) -> dict | None:
    """Verdict fields to merge into ``engine`` for a pronoun word, or None when no context is available."""
    import json

    stem, vib, vac = inputs["stem_slp1"], inputs["vibhakti"], inputs["vacana"]
    if stem not in _PRONOUNS or not 1 <= vib <= 7 or not ctxs:
        return None
    from pipelines.asmad_subanta import derive_asmad, derive_yuzmad

    full = (derive_asmad if stem == "asmad" else derive_yuzmad)(vib, vac).flat_slp1()
    first = None
    for c in ctxs:
        key = json.dumps(c, sort_keys=True)
        got = _surfaces(stem, vib, vac, key)
        first = first or (c, got)
        hit = next((d for s, d in got if s == attested_slp1), None)
        if hit is None and attested_slp1 == full:  # the paradigm derives it; the ādeśa was expected
            hit = full_dev(stem, vib, vac)
        if hit is not None:
            note = None
            if attested_slp1 == full and all(slp != full for slp, _ in got):
                note = ("8.1.17–26 expect the ādeśa here (" + " / ".join(d for _, d in got) + "); the text has the "
                        "full form — ārṣa / contrastive use, or a yukta (8.1.24–25) the text does not show")
            return {"status": "derived", "produced_slp1": attested_slp1, "produced_dev": hit,
                    "enclitic_context": c, "enclitic_note": note, "readings": [d for _, d in got],
                    "boundary_approx": bool(c.get("approx"))}
    c, got = first
    return {"status": "differs", "produced_slp1": got[0][0], "produced_dev": got[0][1],
            "enclitic_context": c, "readings": [d for _, d in got],
            "boundary_approx": bool(c.get("approx")),
            "note": "8.1.17–26 derive " + " / ".join(d for _, d in got) + " in this context"
                    + (" (pāda boundary estimated: the text has sandhi the annotation does not)" if c.get("approx") else "")}
