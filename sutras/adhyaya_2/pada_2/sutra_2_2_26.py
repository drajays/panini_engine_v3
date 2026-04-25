"""
2.2.26  दिङ्नामान्यन्तराले  —  VIDHI

पदच्छेदः  दिङ्-नामानि (प्रथमा-बहुवचनम्) / अन्तराले (सप्तमी-एकवचनम्)

अनुवृत्तिः  अनेकम् 2.2.24

अधिकारः (शास्त्रीय स्मरणार्थम्):
  • आकडारात् एका संज्ञा 1.4.1
  • प्राक्कडारात्समासः 2.1.3
  • सुप्सुपा 2.1.4
  • विभाषा 2.1.11

अनुवृत्तिसहितं सूत्रम्  दिङ्नामान्यन्तराले

Kāśikā (summary): *diṅ-nāmāni* are direction-name *subanta* forms; they compound
in the sense of *antarāla* ‘intermediate (direction)’; the compound is
*bahuvrīhi*.  Examples: *dakṣiṇapūrvā*, *pūrvottarā*, *uttarapaścimā*,
*paścimadakṣiṇā*.  *Nāma-grahaṇa* is for *rūḍhi*; **not** for ad hoc pairs
like *aiṅdryāś ca kauberyāś ca …* (Kāśikā *mā bhūt*) — modelled by
``Term.meta['dik_yaugika'] is True`` on either member.

**Kāśikā-vārttika (under 2.2.26):** *sarvanāmno vṛtti-mātre puṃ-vad-bhāvo
vaktavyaḥ* — when a sarvanāma (here: a *diṅ-nāman* in the sarvādi class)
enters any *vṛtti* (samāsa / taddhita / …), **puṃ-vat-bhāva** is to be stated:
the strī-like surface (e.g. *pūrvā*) stands **like a masculine** base (*pūrva*)
for the derivation (*pūrva-śālā* etc.).  In this engine, feminine-type
``dik_name`` inputs (SLP1 ending in ``A`` that still normalize to a cardinal)
trigger an immediate rewrite of each member’s ``varnas`` /
``meta['upadesha_slp1']`` to the puṃvad-shaped stem (e.g. *uttarā* → *uttara*)
before merge, and ``meta['vartika_sarvanAma_puMvat_vrtti']`` is set on the merged
term for audit.

After merge, **1.2.48** (*gostriyor upasarjanasya*) is applied to the
*bahuvrīhi* stem when the final vowel is *strī*-class *dīrgha* (e.g.
*uttarapūrvā* → *uttarapūrva*), tagging ``upasarjana`` / ``hrasva_final`` so
downstream **7.3.114** / **1.1.28** see the shortened *upasarjana* shape.
The tag ``TAp_anta`` (ṭāp-anta / feminine stem, from **4.1.4** when *upasarjana*)
is **not** set at compound merge — **4.1.4** (*ṭāp*) adds it when *strī* affixation
enters (see ``sutra_4_1_4``); **1.2.48** *hrasva* on the compound is recorded in
``meta['1_2_48_hrasva_applied']`` / ``hrasva_1_2_48``.
Downstream **1.1.28** still uses ``contains_sarvadi`` for optional
``sarvanāma`` tagging.

Engine (representative, mechanically blind):
  • **2.1.3** samāsa adhikāra must be open on ``adhikara_stack`` (note:
    ``purge_closed_adhikaras`` removes **2.1.3** once a sūtra **after**
    **2.2.38** runs — e.g. **2.4.71** — so a recipe may need to call
    ``apply_rule('2.1.3', …)`` again before **2.2.26**).
  • Recipe ``state.meta['diksamasa_compound'] = True`` arms the merge; after a
    successful merge the flag **stays** ``True`` and ``meta`` records
    ``bahuvrihi_formed``, ``vartika_puMvat_applied``, ``1_2_48_hrasva_applied``.
  • Two consecutive *prātipadika* *prakṛti* Terms with ``dik_name`` resolving
    to the four cardinal keys merge to the intermediate stem (unordered pair).
  • Optional tag **``diknama``** on members: if one member carries it, both must
    (recipe signal for *diṅ-nāma* *subanta* in scope); neither tag → unchanged
    behaviour for older demos.
  • ``contains_sarvadi`` on output supports **1.1.28** (dik-bahuvrīhau
    optional sarvanāma-saṃjñā; together with the vārttika this models
    *sarvanāmno vṛtti-mātre puṃ-vad-bhāvaḥ*).
  • ``meta['vartika_sarvanAma_puMvat_vrtti']`` when either member’s
    ``dik_name`` is a strī-type surface (see ``_dik_surface_invokes_puMvat``).

This does NOT attempt full *sup* reconstruction or full samāsa machinery;
it is a narrow, auditable slice.
"""
from __future__ import annotations

from typing import Optional

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk
from phonology.gostriyor_upasarjana import apply_strI_pratyaya_final_hrasva, flat_slp1
from phonology.varna import AC_DEV, HAL_DEV


def _varnas_from_slp1(slp1: str):
    varnas = []
    i = 0
    while i < len(slp1):
        ch = slp1[i]
        if ch in HAL_DEV or ch in AC_DEV:
            varnas.append(mk(ch))
        i += 1
    return varnas


_DIR = frozenset({"dakziRa", "pUrva", "uttara", "paScima"})


def _in_samasa_adhikara(state: State) -> bool:
    return any(e.get("id") == "2.1.3" for e in state.adhikara_stack)


def _diknama_pair_ok(t1: Term, t2: Term) -> bool:
    """If either member is tagged *diknama*, both must be (recipe consistency)."""
    a = "diknama" in t1.tags
    b = "diknama" in t2.tags
    return a == b


def _yaugika_blocked(t1: Term, t2: Term) -> bool:
    """Kāśikā *nāma-grahaṇa* / *yaugika* exclusion (e.g. āindra–kubera dyads)."""
    return t1.meta.get("dik_yaugika") is True or t2.meta.get("dik_yaugika") is True


def _dik_surface_invokes_puMvat(raw: object) -> bool:
    """
    Structural proxy for the vārttika *sarvanāmno vṛtti-mātre puṃ-vad-bhāvaḥ*:
    a ``dik_name`` string whose last codepoint is SLP1 long ``A`` (strī-type
    surface) but still maps to a cardinal via ``_normalize_dik_name``.
    """
    if not isinstance(raw, str):
        return False
    s = raw.strip().replace(" ", "")
    if s.endswith("Ns"):
        s = s[:-2]
    if len(s) < 2 or s[-1] != "A":
        return False
    return _normalize_dik_name(s) is not None


def _normalize_dik_name(raw: str) -> Optional[str]:
    """
    Map common surface spellings / inflected stems to canonical direction keys.

    This is intentionally a small, explicit allowlist (no semantic parsing).
    """
    s = raw.strip().replace(" ", "")
    # Optional plural/locative-ish marker from user examples ("Ns").
    if s.endswith("Ns"):
        s = s[:-2]
    aliases = {
        # North / east-ish
        "uttara": "uttara",
        "uttarA": "uttara",
        "uttrA":  "uttara",
        "pUrva":  "pUrva",
        "pUrvA":  "pUrva",
        # South / west-ish
        "dakziRa": "dakziRa",
        "dakziRA": "dakziRa",
        "paScima": "paScima",
        "paScimA": "paScima",
    }
    return aliases.get(s)

# Canonical intermediate directions (unordered pair → stem_slp1)
_PAIR_TO_STEM = {
    frozenset({"dakziRa", "pUrva"}):   "dakziRapUrvA",
    frozenset({"uttara", "pUrva"}):   "uttarapUrvA",
    frozenset({"dakziRa", "paScima"}): "dakziRapaScimA",
    frozenset({"uttara", "paScima"}):  "uttarapaScimA",
}


def _rewrite_member_pumvat_surface(t: Term) -> None:
    """
    Kāśikā-vārttika *puṃ-vad-bhāva*: rewrite member ``varnas`` / ``upadesha_slp1``
    to the masculine-type stem (e.g. *uttarA* → *uttara*) before the compound
    ``Term`` is built so no stray feminine marker rides into the merged stem.
    """
    raw = t.meta.get("dik_name")
    if not _dik_surface_invokes_puMvat(raw):
        return
    canon = _normalize_dik_name(raw) if isinstance(raw, str) else None
    if canon is None:
        return
    t.varnas = _varnas_from_slp1(canon)
    t.meta["upadesha_slp1"] = canon


def _apply_bahuvrihi_upasarjana_hrasva(merged: Term) -> None:
    """1.2.48-style *hrasva* on *upasarjana* *strī*-final *dīrgha* (glass-box)."""
    nv = apply_strI_pratyaya_final_hrasva(merged.varnas)
    if not nv:
        return
    merged.varnas = nv
    us = flat_slp1(nv)
    if us:
        merged.meta["upadesha_slp1"] = us
    merged.meta["hrasva_1_2_48"] = True
    merged.tags.add("upasarjana")
    merged.tags.add("hrasva_final")


def _dir_name(t: Term) -> Optional[str]:
    v = t.meta.get("dik_name")
    if not isinstance(v, str):
        return None
    canon = _normalize_dik_name(v)
    return canon if canon in _DIR else None


def _find_pair(state: State):
    if not state.meta.get("diksamasa_compound"):
        return None
    if not _in_samasa_adhikara(state):
        return None
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        t1, t2 = state.terms[i], state.terms[i + 1]
        if t1.kind != "prakriti" or t2.kind != "prakriti":
            continue
        if "prātipadika" not in t1.tags or "prātipadika" not in t2.tags:
            continue
        if not _diknama_pair_ok(t1, t2):
            continue
        if _yaugika_blocked(t1, t2):
            continue
        d1, d2 = _dir_name(t1), _dir_name(t2)
        if d1 is None or d2 is None:
            continue
        key = frozenset({d1, d2})
        stem = _PAIR_TO_STEM.get(key)
        if stem is None:
            continue
        return i, stem
    return None


def cond(state: State) -> bool:
    return _find_pair(state) is not None


def act(state: State) -> State:
    hit = _find_pair(state)
    if hit is None:
        return state
    i, stem = hit
    t1 = state.terms[i]
    t2 = state.terms[i + 1]

    _rewrite_member_pumvat_surface(t1)
    _rewrite_member_pumvat_surface(t2)

    puMvat_vrtti = (
        _dik_surface_invokes_puMvat(t1.meta.get("dik_name"))
        or _dik_surface_invokes_puMvat(t2.meta.get("dik_name"))
    )
    merged = Term(
        kind="prakriti",
        varnas=_varnas_from_slp1(stem),
        tags={"prātipadika", "anga", "diksamasa", "bahuvrihi"},
        meta={
            "upadesha_slp1": stem,
            "contains_sarvadi": True,  # structural signal for 1.1.28
            "diksamasa_pair": frozenset({_dir_name(t1), _dir_name(t2)}),
            "vartika_sarvanAma_puMvat_vrtti": puMvat_vrtti,
        },
    )
    _apply_bahuvrihi_upasarjana_hrasva(merged)

    state.terms = state.terms[:i] + [merged] + state.terms[i + 2 :]
    state.meta["diksamasa_compound"] = True
    state.meta["bahuvrihi_formed"] = True
    state.meta["vartika_puMvat_applied"] = bool(puMvat_vrtti)
    state.meta["1_2_48_hrasva_applied"] = merged.meta.get("hrasva_1_2_48") is True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.26",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "diN-nAmAny antarAle",
    text_dev       = "दिङ्नामान्यन्तराले",
    padaccheda_dev = (
        "दिङ्-नामानि (प्रथमा-बहुवचनम्) / अन्तराले (सप्तमी-एकवचनम्)"
    ),
    why_dev        = (
        "दिङ्नामानि सुबन्तान्यन्तराले वाच्ये समस्यन्ते, बहुव्रीहिश्च समासो भवति; "
        "नामग्रहणं रूढ्यर्थम् — यौगिक-दिशोर् न (Kāś.: ऐन्द्र्याश्च कौबेर्याश्च)। "
        "सर्वनाम्नो वृत्तिमात्रे पुंवद्भावो वक्तव्यः (Kāś. वा. अधि २.२.२६)।"
    ),
    anuvritti_from = ("2.2.24",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
