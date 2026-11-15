"""
engine/agama.py — an āgama uttered as taught, inside the term it belongs to.

A vidhi that teaches an āgama (इट्, नुट्, तुक् …) says where it stands: a ṭit āgama is the first avayava of the term it is
taught for, a kit the last, a mit after the last vowel (आद्यन्तौ टकितौ / मिदचोऽन्त्यात्परः — consulted by the vidhi, as
``phonology.agama_placement_1_1_46`` records). This module only utters it there **as its upadeśa**: the letters keep one
segment tag, so the it-saṃjñā sūtras judge the segment exactly as they judge a dhātu or pratyaya upadeśa, the lopa
sūtra deletes and records what they named, and the record belongs to the āgama — never to its host (an इट् inside
आथाम् does not make आथाम् ṭit).

A vowel the tradition calls *uccāraṇārtha* — there only so the āgama can be pronounced, not an anubandha — is not uttered
(Kāśikā on सीयुट्: "टकारो देशविध्यर्थः। उकार उच्चारणार्थः।"; Bālamanoramā: "नुटि टकार इत्। उकार उच्चारणार्थः।",
"वुकि ककार इत्, उकार उच्चारणार्थः।"; Nyāsa: "उकार उच्चारणार्थः — अनुबन्धत्वमस्य निरस्यति"). Each entry of
``UCCARANARTHA`` is such a cited reading; nothing is guessed from the shape of the upadeśa.

Engine bookkeeping only: no sūtra id appears here, and nothing here decides whether an āgama applies.
"""
from __future__ import annotations

from typing import Dict, List, Optional

from phonology.varna import parse_slp1_upadesha_sequence

SEG_PREFIX = "agama_seg:"          # varṇa tag: agama_seg:<upadeśa>#<n> — one uttered āgama
SEG_DONE = "agama_it_done"         # set on the segment's remaining varṇas once its it-letters are named and deleted
_COUNTER = "agama_seg_counter"

# āgama upadeśa → the vowel that is uccāraṇārtha (see the module docstring for the sources).
UCCARANARTHA: Dict[str, str] = {
    "nuw": "u", "tuk": "u", "vuk": "u", "suw": "u", "sIyuw": "u", "yAsuw": "u", "muk": "u", "yuk": "u",
    "kuk": "u", "wuk": "u", "Duw": "u", "ruw": "u", "yuw": "u", "num": "u", "zuk": "u", "puk": "u",
}


def utter_into(state, term, at: int, upadesha: str) -> List:
    """Insert the āgama ``upadesha`` (SLP1, as taught) into ``term.varnas`` at ``at``; return its varṇas."""
    vs = list(parse_slp1_upadesha_sequence(upadesha))
    drop = UCCARANARTHA.get(upadesha)
    if drop:
        k = next((i for i, v in enumerate(vs) if i > 0 and v.slp1 == drop), None)
        if k is not None:
            del vs[k]
    n = int(state.meta.get(_COUNTER) or 0) + 1
    state.meta[_COUNTER] = n
    tag = f"{SEG_PREFIX}{upadesha}#{n}"
    for v in vs:
        v.tags.add(tag)
        v.tags.add("agama")
    term.varnas[at:at] = vs
    return vs


def seg_tag(v) -> Optional[str]:
    return next((t for t in v.tags if t.startswith(SEG_PREFIX)), None)


def seg_upadesha(tag: str) -> str:
    return tag[len(SEG_PREFIX):].split("#", 1)[0]


def segments(term) -> Dict[str, List[int]]:
    """segment tag → varṇa indices in ``term`` (tape order)."""
    out: Dict[str, List[int]] = {}
    for i, v in enumerate(term.varnas):
        t = seg_tag(v)
        if t:
            out.setdefault(t, []).append(i)
    return out


def pending_segments(state) -> bool:
    """Some uttered āgama whose it-letters have not been judged and deleted yet."""
    return any(seg_tag(v) and SEG_DONE not in v.tags for t in state.terms for v in t.varnas)


def is_agama_letter(v) -> bool:
    """A varṇa that belongs to an uttered āgama (not to its host's own upadeśa)."""
    return seg_tag(v) is not None or "it_agama" in v.tags


def close_judged(state) -> None:
    """After the it-prakaraṇa has run: an uttered āgama with no it-letter left to delete is closed as judged."""
    from engine.it_phonetic import IT_LOPA_TAGS
    for t in state.terms:
        for v in t.varnas:
            if seg_tag(v) and not (v.tags & IT_LOPA_TAGS):
                v.tags.add(SEG_DONE)


def utter_num(state, term, at: int):
    """नुम् as taught (उच्चारणार्थ उ not uttered); leftover न् keeps ``num_agama`` so 6.4.24 still sees it."""
    vs = utter_into(state, term, at, "num")
    for v in vs:
        if v.slp1 == "n":
            v.tags.add("num_agama")
    return vs
