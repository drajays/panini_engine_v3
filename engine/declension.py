"""engine/declension.py — the site of a declension rule: the aṅga (a prātipadika) and the sup that follows it.

Pāṇini names some aṅgas by their word (सखि, गो, दिव्, चतुर्, पथिन् …): that is the stem's own upadeśa
(``Term.meta['upadesha_slp1']``, a lexical fact like the gaṇa), never the tape, which guṇa or an āgama may have changed.
Everything else a rule reads is a tag the saṃjñā sūtras wrote (sarvanamasthana, sambuddhi, vib_*, vac_*)."""
from __future__ import annotations

from engine.state import State, Term


def anga_and_sup(state: State, sutra_id: str | None = None):
    """(aṅga, sup) when the tape ends in a sup that follows a prātipadika aṅga, else None. With ``sutra_id``, the aṅgādhikāra
    (6.4.1, open from 6.4.1 to 7.4.97) must be in effect for that sūtra — as it is for every rule that begins with अङ्गस्य."""
    if len(state.terms) < 2:
        return None
    anga, sup = state.terms[-2], state.terms[-1]
    if "sup" not in sup.tags or "prātipadika" not in anga.tags or "anga" not in anga.tags or not anga.varnas:
        return None        # aṅga-saṃjñā (1.4.13) first: the aṅgakārya rules all begin with it (6.4.1)
    if sutra_id is not None:
        from engine.gates import adhikara_in_effect
        if not adhikara_in_effect(sutra_id, state, "6.4.1"):
            return None
    return anga, sup


def stem_of(anga: Term) -> str:
    return (anga.meta.get("upadesha_slp1") or "").strip()


def is_stem(anga: Term, *names: str, tadanta: bool = False) -> bool:
    """The aṅga is the named word (or, with tadantavidhi 1.1.72, ends in it: प्रियसखि)."""
    s = stem_of(anga)
    return s in names or (tadanta and any(s.endswith(n) for n in names))


_AC = frozenset("aAiIuUfFxXeEoO")


def vowel_initial(sup: Term) -> bool:
    return bool(sup.varnas) and sup.varnas[0].slp1 in _AC


def n_vowels(anga: Term) -> int:
    return sum(v.slp1 in _AC for v in anga.varnas)


def samyoga_purva(anga: Term) -> bool:
    """The final vowel stands after a conjunct (two consonants): श्री, सुश्री — not नी, ग्रामणी."""
    vs = anga.varnas
    return len(vs) >= 3 and vs[-2].slp1 not in _AC and vs[-3].slp1 not in _AC


def dhatu_aṅga(anga: Term) -> bool:
    """The aṅga is (a kṛdanta of) a dhātu: the lexicon's vyutpatti record says so (engine/origin), or it is the word भ्रू (6.4.77 names it)."""
    return any(t.startswith("origin_dhatu:") for t in anga.tags) or (anga.meta.get("upadesha_slp1") or "").strip() == "BrU"
