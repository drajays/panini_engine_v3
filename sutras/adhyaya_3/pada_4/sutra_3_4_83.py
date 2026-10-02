"""
3.4.83  विदो लटो वा  —  VIBHASHA

After the root विद् (jñāne), the nine parasmaipada endings of laṭ are optionally replaced by the ṇalādi set of 3.4.82:
tip→ṇal, tas→atus, jhi→us, sip→thal, thas→aṭhus, tha→a, mip→ṇal, vas→va, mas→ma.
  वेद विदतुः विदुः वेत्थ विदथुः विद वेद विद्व विद्म   (the other branch: वेत्ति वित्तः विदन्ति वेत्सि वित्थः वित्थ वेद्मि विद्वः विद्मः)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 3.4.83 (padaccheda: विदः लटः वा; anuvṛtti: परस्मैपदानाम् 3.4.82, णल्-आदयः)
  Source #2 — ashtadhyayi.com dhātu table, root विद् (adādi, jñāne), laṭ parasmaipada — both readings listed;
              Gītā 2.29 / 4.5 / 7.26 attestations (विदुः, वेद, वेत्थ)

Engine: ``cond`` reads the root's lexical identity (विद् जाने = adādi, upadeśa ``vida~``) and, on the tape, a
parasmaipada tiṅ Term whose sthānin (``source_lakara_upadesha``) is laṭ — a saṃjñā 3.4.78 stamped, not the
lakāra coordinate. The ādeśa is sarvādeśa per tiṅ (1.1.55); the replacement keeps the sthānin, so the new endings
are still laṭ's (sārvadhātuka by 3.4.113) and their kit-ness is 1.2.5's, as for the same endings in liṭ — that is why
विदतुः / विदुः carry no guṇa while वेद / वेत्थ do (ṇit / pit). ``engine.vikalpa.explore`` yields both readings.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas

_ROOT = "vida~"
_GANA_JNANA = 2  # adādi vid (jñāne); not the divādi sattāyām or the tudādi lābhe vid
_ADESHA = {"tip": "Ral", "tas": "atus", "Ji": "us", "sip": "Tal", "Tas": "aTus", "Ta": "a",
           "mip": "Ral", "vas": "va", "mas": "ma"}
_IT_AT = {"Ral": [(0, "it_candidate_cutu"), (2, "it_candidate_halantyam")], "Tal": [(2, "it_candidate_halantyam")]}


def _ident(t) -> str:
    return (t.meta.get("upadesha_slp1") or "").strip()   # the tiṅ ādeśa 3.4.78 put on the tape: tip, tas, Ji …


def _is_vid(state: State) -> bool:
    return any("dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == _ROOT
               and t.meta.get("gana") == _GANA_JNANA for t in state.terms)


def _targets(state: State) -> list[int]:
    if not _is_vid(state):
        return []
    return [i for i, t in enumerate(state.terms)
            if "pratyaya" in t.tags and "tin_adesha_3_4_78" in t.tags and not t.meta.get("3_4_83_done")
            and (t.meta.get("source_lakara_upadesha") or "").strip() == "laT"
            and "parasmaipada" in t.tags and _ident(t) in _ADESHA]


def cond(state: State) -> bool:
    return bool(_targets(state))


def act(state: State) -> State:
    for i in _targets(state):
        term = state.terms[i]
        before = _ident(term)
        form = _ADESHA[before]
        # 1.1.56 sthānivadādeśo'nalvidhau: the ādeśa inherits the sthānin's it-saṃjñā — ṇal/ṭhal replace the pit tip/sip/mip
        # (so 1.2.4 does not make them kṅit: वेद, वेत्थ), atus/aṭhus/us/a/va/ma replace apit endings (kṅit: विदतुः).
        adesha_substitute_varnas(term, form, state, sutra_id="3.4.83", gunadharmas=frozenset({TING_PRATYAYATVA}))
        for idx, tag in _IT_AT.get(form, []):
            term.varnas[idx].tags.add(tag)
        term.meta["tin_before_3_4_83"] = before
        term.meta["3_4_83_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.83",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="vido lawo vA",
    text_dev="विदो लटो वा",
    padaccheda_dev="विदः लटः वा",
    why_dev="विद् धातु से परे लट् के परस्मैपद तिङ् विकल्प से णल्-आदि (णल् अतुस् उस् थल् अथुस् अ णल् व म) होते हैं।",
    anuvritti_from=("3.4.82",),
    vibhasha_default=False,
    vibhasha_scope=cond,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
