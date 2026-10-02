"""
The ṇalādi set of 3.4.82 (ṇal atus us ṭhal aṭhus a ṇal va ma) as a replacement for the nine parasmaipada tiṅ, shared by
3.4.83 (विदो लटो वा: all nine, after vid) and 3.4.84 (ब्रुवः पञ्चानामादित आहो ब्रुवः: the first five, after brū).
Reads Term tags / identities only (Art. 2).
"""
from __future__ import annotations

from engine.state import State
from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas

# tiṅ ādeśa of 3.4.78 → its ṇalādi replacement; order is the sūtra's: tip tas jhi sip thas tha mip vas mas
ADESHA = {"tip": "Ral", "tas": "atus", "Ji": "us", "sip": "Tal", "Tas": "aTus", "Ta": "a",
          "mip": "Ral", "vas": "va", "mas": "ma"}
FIRST_FIVE = ("tip", "tas", "Ji", "sip", "Tas")
_IT_AT = {"Ral": [(0, "it_candidate_cutu"), (2, "it_candidate_halantyam")], "Tal": [(2, "it_candidate_halantyam")]}


def ident(t) -> str:
    return (t.meta.get("upadesha_slp1") or "").strip()   # the tiṅ ādeśa 3.4.78 put on the tape: tip, tas, Ji …


def lat_parasmai_tin(state: State, among) -> list[int]:
    """Indices of parasmaipada tiṅ Terms whose sthānin is laṭ and whose ādeśa is one of ``among`` (not yet replaced)."""
    return [i for i, t in enumerate(state.terms)
            if "pratyaya" in t.tags and "tin_adesha_3_4_78" in t.tags and not t.meta.get("nal_adi_done")
            and (t.meta.get("source_lakara_upadesha") or "").strip() == "laT"
            and "parasmaipada" in t.tags and ident(t) in among]


def replace_tin(state: State, i: int, sutra_id: str) -> None:
    """1.1.56 sthānivadādeśo'nalvidhau: the ādeśa inherits the sthānin's it-saṃjñā — ṇal/ṭhal replace the pit
    tip/sip/mip (so 1.2.4 does not make them kṅit: वेद, वेत्थ); atus/aṭhus/us/a/va/ma replace apit endings (kṅit)."""
    term = state.terms[i]
    before = ident(term)
    form = ADESHA[before]
    adesha_substitute_varnas(term, form, state, sutra_id=sutra_id, gunadharmas=frozenset({TING_PRATYAYATVA}))
    for idx, tag in _IT_AT.get(form, []):
        term.varnas[idx].tags.add(tag)
    term.meta["tin_before_3_4_83"] = before   # key read by 3.4.113 / 1.2.4 (tin_by_sthanin); name kept for both sūtras
    term.meta["nal_adi_done"] = True
