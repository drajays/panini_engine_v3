"""
*Jayati* gold prakriyā — rule-scheduled *tin*anta driver (9 steps).  Human table:
``tinanta_gold/jayati_gold_sarani.md`` (see also ``jayati_prakriya.json`` key ``gold_sarani``).

**Step 1** (this module): *dhātupāṭha* row **BvAdi_01_0642** (*ji* / *jaye*), **1.1.60** *lopa*
saṃjñā, **1.3.1** *dhātu* saṃjñā, full **1.3.2**–**1.3.8** *it* scan, **1.3.9** *lopa* (no *it* on *ji* —
no phoneme change), **1.3.10** *yathāsaṅkhyam* paribhāṣā gate.

**Step 2:** *vivakṣā* (recipe ``meta['gold_jayati_vivaksha']`` only — no sūtra *cond* reads it),
**3.1.1** / **3.1.2** (*pratyaya* / *para* *adhikāra*), **3.4.69** (*prayoga* gates), **3.2.123** (*vartamāne*
*laṭ* *adhikāra*).  Rule order is **3.1.1 → 3.1.2 → 3.4.69 → 3.2.123** so **3.2.123** is not purged when
**3.4.69** runs (``purge_closed_adhikaras`` removes **3.2.123** if it were pushed *before* **3.4.69**).
Then a structural ``laT`` *pratyaya* ``Term`` is appended (abstract *lakāra* — **3.4.77**/**3.4.78** later).

**Step 3:** Re-run **1.3.2**–**1.3.9** on ``[ji, laT]`` — **1.3.3** *halantyam* gives *it*-*saṃjñā* on
final ``T`` (``State.flat_slp1()`` still ``jilaT``); **1.3.9** is the *lopa* *vidhi* that removes ``T``
(``jila``).  A recipe-only collapse ``la`` → ``l`` on the *lakāra* ``Term`` sets ``flat_slp1()`` to
``jil`` (pedagogical *lac* = ``l``; ``meta['upadesha_slp1']`` stays ``laT`` for later **3.4.78**).

**Step 4:** **3.4.77** *lasyādhikāra* → recipe ``tin_adesha_slp1`` / ``tin_adesha_pending`` → **3.4.78** (*lac* → *tip*),
then **1.4.99** / **1.4.100** / **1.3.78** / **1.4.101** / **1.4.108** / **1.4.102** / **1.4.22** (``1_4_22_affix_class=eka`` on *ji*).

**Step 5:** **3.1.91** (*dhātoḥ* *adhikāra* — required on ``adhikara_stack`` for **3.1.68**), **3.4.113** (*tiṅ-śit* *sārvadhātukam* tag on *tip*),
**3.1.68** (*śap* *vikaraṇa* between *ji* and *tip* in *kartari*) → ``ji`` + ``Sap`` + ``tip``.

**Step 6:** **1.3.2**–**1.3.9** on ``[ji, Sap, tip]`` — **1.3.3** tags final ``p`` of *Sap* and *tip*; **1.3.8** tags initial ``S`` of *Sap*; *saṃjñā* only — ``State.flat_slp1()`` stays ``jiSaptip`` until **1.3.9** (*lopa* of ``S``,
both ``p``'s) → ``jiati``; **1.1.60** *lopa* *saṃjñā* already in step 1.

**Step 7:** **1.4.13** (*aṅga*), **1.1.2** / **1.1.3** / **1.1.50** / **1.1.56** (*guṇa* / *ik* / *antaratama* / *sthānivad*), **6.4.1** (*aṅgasya* *adhikāra*), **7.3.84** (*ik* *aṅga* before *sārvadhātuka* *Sap*), **1.1.51** (*uḥ aṇ r aparaḥ* when **7.3.84** left ``urN_rapara_pending`` — *tṛ* / *ṝ* → ``ar``).  For *ji*, **1.1.51** *cond* false (last vowel ``e``); surface e.g. ``jeati``.

**Step 8:** **6.1.72** (*saṃhitā* *adhikāra*), **6.1.77** (*iko yaṇaci* — *SKIPPED* on this shape; *e* is *ECO* not *ik*), **6.1.78** (*echo ’yavāyāvḥ* — ``e``+``a`` → ``ay``) → surface ``jayati`` (``flat_slp1()``).  **1.1.50** for *antaratama* is already step 7.

**Step 9 (Tripāḍī audit):** **8.1.16** (*padasya* *adhikāra*), **8.2.1** (opens Tripāḍī / *pūrvatrāsiddham*), **8.2.66** (*SKIPPED* — no *pada*-final ``s``; *tin*anta shape is still multi-``Term``).  Form unchanged ``jayati``; other 8.3/8.4 *vidhi*s are N/A for this string (see JSON *pada_note_hi*).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Final, Tuple

import sutras  # noqa: F401

from engine       import apply_rule
from engine.it_phonetic import IT_LOPA_TAGS
from engine.state import State, Term
from phonology.varna import mk, parse_slp1_upadesha_sequence

from pipelines.dhatupatha import get_dhatu_row

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import find_primary_dhatu
from sutras.adhyaya_1.pada_4.dvi_eka_1_4_22 import DVI_EKA_NIMITTA_KEY

_GOLD_JSON = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "reference"
    / "tinanta_gold"
    / "jayati_prakriya.json"
)

JAYATI_DHATU_ROW_ID: Final[str] = "BvAdi_01_0642"

# Step 1 — mirrors pedagogy table (1.1.60 *adhikṛta* before *it* *prakaraṇa*).
STEP_1_RULE_IDS: Final[Tuple[str, ...]] = (
    "1.1.60",
    "1.3.1",
    "1.3.2",
    "1.3.3",
    "1.3.4",
    "1.3.5",
    "1.3.6",
    "1.3.7",
    "1.3.8",
    "1.3.9",
    "1.3.10",
)

# Step 2 — engine order (see module docstring on **3.2.123** vs ``purge_closed_adhikaras``).
STEP_2_RULE_IDS: Final[Tuple[str, ...]] = (
    "3.1.1",
    "3.1.2",
    "3.4.69",
    "3.2.123",
)

# Step 3 — *it* *prakaraṇa* on ``laT`` only (**1.1.60** / **1.3.1** already from step 1; not re-fired).
STEP_3_IT_RULE_IDS: Final[Tuple[str, ...]] = (
    "1.3.2",
    "1.3.3",
    "1.3.4",
    "1.3.5",
    "1.3.6",
    "1.3.7",
    "1.3.8",
    "1.3.9",
)

# Step 4 — after **3.4.77**, recipe sets ``tin_adesha_*`` then **3.4.78** runs alone.
STEP_4_POST_77_RULE_IDS: Final[Tuple[str, ...]] = (
    "3.4.78",
    "1.4.99",
    "1.4.100",
    "1.3.78",
    "1.4.101",
    "1.4.108",
    "1.4.102",
    "1.4.22",
)

# Step 5 — **3.1.68** needs **3.1.91** on stack (book order: **3.1.68** precedes **3.1.91**); **3.4.113** tags *tip*; **3.1.68** inserts *Sap*.
STEP_5_RULE_IDS: Final[Tuple[str, ...]] = (
    "3.1.91",
    "3.4.113",
    "3.1.68",
)

# Step 6 — same *it* spine as step 3; **1.1.60** not repeated (already registered in step 1).
STEP_6_IT_RULE_IDS: Final[Tuple[str, ...]] = STEP_3_IT_RULE_IDS

# Step 7 — *aṅga* + *guṇa* paribhāṣā block + **7.3.84** (*ik* → *guṇa* before *Sap*)
# + **1.1.51** (*uḥ aṇ r aparaḥ*) when **7.3.84** left ``urN_rapara_pending`` (ṛ/ṝ → *ar*).
STEP_7_RULE_IDS: Final[Tuple[str, ...]] = (
    "1.4.13",
    "1.1.2",
    "1.1.3",
    "1.1.50",
    "1.1.56",
    "6.4.1",
    "7.3.84",
    "1.1.51",
)

# Step 8 — *saṃhitā* block: **6.1.77** is a no-op for *jayati* (engine narrows to *os* for some paths;
# *e* is not *ik*); **6.1.78** splits *e* before *Sap*’s *a* → ``jay`` + ``a`` + ``ti`` = ``jayati``.
STEP_8_RULE_IDS: Final[Tuple[str, ...]] = (
    "6.1.72",
    "6.1.77",
    "6.1.78",
)

# Step 9 — *pad* *adhikāra* (8.1.16) + Tripāḍī entry (8.2.1); **8.2.66** *cond* false (no *pada*-final *s*).
STEP_9_TRIPADI_AUDIT_RULE_IDS: Final[Tuple[str, ...]] = (
    "8.1.16",
    "8.2.1",
    "8.2.66",
)


@lru_cache(maxsize=1)
def _gold_spec() -> dict:
    with _GOLD_JSON.open(encoding="utf-8") as f:
        return json.load(f)


def _karmakatva_from_row(row: dict) -> str:
    """Map ``karmatva_label_dev`` to engine ``karmakatva`` meta (for later *prayoga* steps)."""
    lab = (row.get("karmatva_label_dev") or "").strip()
    if "सकर्मक" in lab:
        return "sakarmaka"
    if "अकर्मक" in lab:
        return "akarmaka"
    return "sakarmaka"


def build_lat_tin_dhatu_state(*, dhatu_row_id: str) -> State:
    """
    One *dhātu* ``Term`` from ``dhatupatha_upadesha.json`` — tags ``dhatu`` + ``upadesha`` + ``anga``
    so **1.3.1** / *it* rules align with ``pipelines.krdanta.build_dhatu_state``.

    Used for *jayati* (*ji*), *nayati* (``RIY`` / णीञ्), and future *laṭ* *prathamā* *eka* gold rows.
    """
    row = get_dhatu_row(dhatu_row_id)
    up = (row.get("upadesha_slp1") or "").strip()
    if not up:
        raise ValueError(f"dhatu row {dhatu_row_id!r} has no upadesha_slp1")
    meta = {
        "upadesha_slp1": up,
        "dhatupatha_id": row.get("id"),
        "dhatupatha_serial": row.get("dhatupatha_id"),
        "artha_slp1": row.get("artha_slp1"),
        "karmakatva": _karmakatva_from_row(row),
    }
    if row.get("flags"):
        meta["dhatupatha_flags"] = dict(row["flags"])
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(up),
        tags={"dhatu", "anga", "upadesha"},
        meta=meta,
    )
    return State(terms=[dhatu])


def build_ji_dhatu_state(*, dhatu_row_id: str = JAYATI_DHATU_ROW_ID) -> State:
    """*ji* *dhātu* (``BvAdi_01_0642``) — thin wrapper over ``build_lat_tin_dhatu_state``."""
    return build_lat_tin_dhatu_state(dhatu_row_id=dhatu_row_id)


def seed_jayati_step2_vivaksha_meta(state: State) -> State:
    """
    Recipe-only *vivakṣā* for *jayati* (kartṛ, *vartamāna*, third person, singular).

    Stored under ``meta['gold_jayati_vivaksha']`` — not read by any **step 2** sūtra ``cond``.
    """
    state.meta["gold_jayati_vivaksha"] = {
        "artha_hi": "एकः तृतीय-पुरुषः वर्तमाने जयति",
        "kAla_hi": "वर्तमान (सामान्य, अनद्यतन-विशेषः न)",
        "prayoga": "kartari",
        "puruSha_third": True,
        "vacana_eka": True,
    }
    return state


def _enrich_adhikara_3_2_123_shows_jilaT_in_trace(state: State) -> None:
    """
    **3.2.123**'s *act* only records *adhikāra* on state; the recipe then appends
    the abstract *laT* ``Term`` here.  Reconcile the last **3.2.123** trace
    row so *form_after* matches ``State.flat_slp1()`` (e.g. ``jilaT``, ``RIlaT``).
    """
    flat = state.flat_slp1()
    for st in reversed(state.trace):
        if st.get("sutra_id") == "3.2.123" and st.get("status") in (
            "APPLIED",
            "APPLIED_VACUOUS",
        ):
            st["form_after"] = flat
            st["why_dev"] = (
                "अधिकारसूत्रम् (वर्तमानाधिकारः) — द्विकार्यम्: (१) वर्तमाने लट् "
                "प्रत्ययस्य विधानम् → धातु + laT; (२) 'वर्तमाने' पदस्य ३.२.१२३ तः "
                "३.३.१ पर्यन्तम् अनुवृत्तिः।"
            )
            st["adhikara_range"] = "3.2.123 – 3.3.1"
            st["vidhi_aspect"] = "laT added"
            st["type_label"] = "अधिकार"
            break


def _enrich_step3_1_3_3_jilaT_it_tags(state: State) -> None:
    """*Halantyam* on *laT* — surface unchanged; name which *varṇa* got *it* for UI."""
    for st in state.trace:
        fb = st.get("form_before") or ""
        if st.get("sutra_id") == "1.3.3" and fb.endswith("laT"):
            st["it_tagged_this_step"] = ["laT.T"]
            st["why_dev"] = (
                "laT के अन्त्य 'T' (ट्) — हलन्त्य-इत्-संज्ञा; लोपः १.३.९ करिष्यति।"
            )
            break


def _enrich_step6_1_3_3_8_Saptip_it_tags(state: State) -> None:
    for st in state.trace:
        fb = st.get("form_before") or ""
        if st.get("sutra_id") == "1.3.3" and "Saptip" in fb:
            st["it_tagged_this_step"] = ["Sap.p", "tip.p"]
            st["why_dev"] = (
                "Sap के अन्त्य 'p' तथा tip के अन्त्य 'p' — हलन्त्य-इत्-संज्ञा; "
                "लोपः १.३.९ करिष्यति।"
            )
        if st.get("sutra_id") == "1.3.8" and "Saptip" in fb:
            st["it_tagged_this_step"] = ["Sap.S"]
            st["why_dev"] = (
                "Sap के आदि 'S' (श्) — लशकु-वर्ण-इत्-संज्ञा; लोपः १.३.९ करिष्यति।"
            )


def append_lat_pratyaya_after_dhatu(state: State) -> State:
    """
    Append abstract *laṭ* ``Term`` immediately after the sole *dhātu* (``upadesha_slp1`` = ``laT``).

    Structural (not a registered sūtra).  Idempotent if ``laT`` is already the second ``Term``.
    ``upadesha`` tag is required so **1.3.3** *halantyam* applies to final ``T``.
    """
    out = state.clone()
    if len(out.terms) >= 2:
        if (out.terms[1].meta.get("upadesha_slp1") or "").strip() == "laT":
            out.terms[1].tags.add("upadesha")
            _enrich_adhikara_3_2_123_shows_jilaT_in_trace(out)
            return out
    if len(out.terms) != 1:
        raise ValueError("append_lat_pratyaya_after_dhatu expects exactly one Term before laṭ")
    if "dhatu" not in out.terms[0].tags:
        raise ValueError("first Term must be tagged dhatu")
    lat = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    out.terms = [out.terms[0], lat]
    _enrich_adhikara_3_2_123_shows_jilaT_in_trace(out)
    return out


def collapse_lat_residual_to_l_phoneme(state: State) -> State:
    """
    After **1.3.9** on *laṭ*, ``Term.varnas`` are typically ``[l, a]``; pedagogy treats the *lakāra*
    spine as **l** only — collapse to ``[l]`` while keeping ``meta['upadesha_slp1'] == 'laT'`` for
    **3.4.78** *cond* later.
    """
    out = state.clone()
    for t in out.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "laT":
            continue
        if len(t.varnas) == 2 and t.varnas[0].slp1 == "l" and t.varnas[1].slp1 == "a":
            t.varnas = [mk("l")]
            t.meta["gold_lat_post_it_lac"] = True
    return out


def apply_rule_chain(state: State, rule_ids: Tuple[str, ...]) -> State:
    """Sequential ``apply_rule`` — recipe spine for gold prakriyā."""
    s = state
    for sid in rule_ids:
        s = apply_rule(sid, s)
    return s


def run_jayati_gold_step1(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    Execute **step 1** only: **1.1.60** → **1.3.1** → **1.3.2**–**1.3.8** → **1.3.9** → **1.3.10**.

    If ``state`` is *None*, builds the *dhātu* ``Term`` from ``dhatu_row_id`` (default *ji* row).
    """
    s = build_lat_tin_dhatu_state(dhatu_row_id=dhatu_row_id) if state is None else state
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if not steps:
        ids = STEP_1_RULE_IDS
    else:
        s1 = steps[0]
        ids = tuple(s1.get("rule_ids") or STEP_1_RULE_IDS)
    return apply_rule_chain(s, ids)


def run_jayati_gold_step2(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 2** after step 1: *vivakṣā* meta → **3.1.1** / **3.1.2** / **3.4.69** / **3.2.123** → ``laT`` ``Term``.

    If ``state`` is *None*, runs ``run_jayati_gold_step1()`` first.
    """
    s = (
        run_jayati_gold_step1(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    seed_jayati_step2_vivaksha_meta(s)
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 2:
        ids = STEP_2_RULE_IDS
    else:
        s2 = steps[1]
        ids = tuple(s2.get("rule_ids") or STEP_2_RULE_IDS)
    s = apply_rule_chain(s, ids)
    return append_lat_pratyaya_after_dhatu(s)


def seed_jayati_gold_step4_recipe_meta(state: State) -> State:
    """
    *Vivakṣā* hooks for **1.4.22** (*ekavacana*) and **3.4.78** (*tip* *ādeśa*) — allowlisted *dhātu* meta only.
    """
    d = find_primary_dhatu(state)
    if d is None:
        raise ValueError("seed_jayati_gold_step4_recipe_meta: no dhātu Term")
    d.meta[DVI_EKA_NIMITTA_KEY] = "eka"
    return state


def run_jayati_gold_step3(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 3:** **1.3.2**–**1.3.9** on ``ji + laT`` → **1.3.9** drops ``T`` → collapse ``la`` → ``l``.

    If ``state`` is *None*, runs ``run_jayati_gold_step2()`` first.
    """
    s = (
        run_jayati_gold_step2(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 3:
        ids = STEP_3_IT_RULE_IDS
    else:
        s3 = steps[2]
        ids = tuple(s3.get("rule_ids") or STEP_3_IT_RULE_IDS)
    s = apply_rule_chain(s, ids)
    _enrich_step3_1_3_3_jilaT_it_tags(s)
    return collapse_lat_residual_to_l_phoneme(s)


def run_jayati_gold_step4(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 4:** **3.4.77** → *tip* via **3.4.78** (recipe meta) → **1.4.99** … **1.4.22** (*eka* *vivakṣā*).

    If ``state`` is *None*, runs ``run_jayati_gold_step3()`` first.
    """
    s = (
        run_jayati_gold_step3(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    seed_jayati_gold_step4_recipe_meta(s)
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 4:
        post77 = STEP_4_POST_77_RULE_IDS
    else:
        post77 = tuple(steps[3].get("rule_ids_after_lat") or STEP_4_POST_77_RULE_IDS)
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_slp1"] = "tip"
    s.meta["tin_adesha_pending"] = True
    return apply_rule_chain(s, post77)


def run_jayati_gold_step5(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 5:** **3.1.91** → **3.4.113** (*sārvadhātuka* on *tip*) → **3.1.68** (*Sap* *vikaraṇa* after *ji*).

    If ``state`` is *None*, runs ``run_jayati_gold_step4()`` first.
    """
    s = (
        run_jayati_gold_step4(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 5:
        ids = STEP_5_RULE_IDS
    else:
        ids = tuple(steps[4].get("rule_ids") or STEP_5_RULE_IDS)
    return apply_rule_chain(s, ids)


def run_jayati_gold_step6(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 6:** **1.3.2**–**1.3.9** on ``ji + Sap + tip`` — *it* on ``S``/``p`` (*Sap*) and ``p`` (*tip*); *lopa* → ``jiati``.

    If ``state`` is *None*, runs ``run_jayati_gold_step5()`` first.
    """
    s = (
        run_jayati_gold_step5(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 6:
        ids = STEP_6_IT_RULE_IDS
    else:
        ids = tuple(steps[5].get("rule_ids") or STEP_6_IT_RULE_IDS)
    s = apply_rule_chain(s, ids)
    _enrich_step6_1_3_3_8_Saptip_it_tags(s)
    return s


def run_jayati_gold_step7(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 7:** **1.4.13** → *guṇa* metarules → **6.4.1** → **7.3.84** (*ji* → ``je`` before *Sap*).

    If ``state`` is *None*, runs ``run_jayati_gold_step6()`` first.
    """
    s = (
        run_jayati_gold_step6(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 7:
        ids = STEP_7_RULE_IDS
    else:
        ids = tuple(steps[6].get("rule_ids") or STEP_7_RULE_IDS)
    return apply_rule_chain(s, ids)


def run_jayati_gold_step8(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 8:** **6.1.72** → **6.1.77** (skip) → **6.1.78** (*e*+``a`` at *aṅga*–*Sap* boundary) → ``jayati``.

    If ``state`` is *None*, runs ``run_jayati_gold_step7()`` first.
    """
    s = (
        run_jayati_gold_step7(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 8:
        ids = STEP_8_RULE_IDS
    else:
        ids = tuple(steps[7].get("rule_ids") or STEP_8_RULE_IDS)
    return apply_rule_chain(s, ids)


def run_jayati_gold_step9(
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """
    **Step 9:** **8.1.16** → **8.2.1** → **8.2.66** (skip) — Tripāḍī *gate* + *pada* *adhikāra* audit; surface ``jayati`` unchanged.

    If ``state`` is *None*, runs ``run_jayati_gold_step8()`` first.
    """
    s = (
        run_jayati_gold_step8(None, dhatu_row_id=dhatu_row_id)
        if state is None
        else state
    )
    spec = _gold_spec()
    steps = spec.get("steps") or []
    if len(steps) < 9:
        ids = STEP_9_TRIPADI_AUDIT_RULE_IDS
    else:
        ids = tuple(steps[8].get("rule_ids") or STEP_9_TRIPADI_AUDIT_RULE_IDS)
    s = apply_rule_chain(s, ids)
    s.meta["gold_jayati_step9_tripadi_audit"] = {
        "pada_adhikAra_8_1_16": True,
        "tripadi_8_2_1": True,
        "8_2_66_sasajuzo_ruH": "COND-FALSE (no final s; no pada-tagged single term)",
    }
    return s


def run_jayati_gold_through_step(
    n: int,
    state: State | None = None,
    *,
    dhatu_row_id: str = JAYATI_DHATU_ROW_ID,
) -> State:
    """Run steps ``1 .. n`` in order (all nine gold steps supported)."""
    if n == 1:
        return run_jayati_gold_step1(state, dhatu_row_id=dhatu_row_id)
    if n == 2:
        s1 = run_jayati_gold_step1(state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step2(s1, dhatu_row_id=dhatu_row_id)
    if n == 3:
        s2 = run_jayati_gold_through_step(2, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step3(s2, dhatu_row_id=dhatu_row_id)
    if n == 4:
        s3 = run_jayati_gold_through_step(3, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step4(s3, dhatu_row_id=dhatu_row_id)
    if n == 5:
        s4 = run_jayati_gold_through_step(4, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step5(s4, dhatu_row_id=dhatu_row_id)
    if n == 6:
        s5 = run_jayati_gold_through_step(5, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step6(s5, dhatu_row_id=dhatu_row_id)
    if n == 7:
        s6 = run_jayati_gold_through_step(6, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step7(s6, dhatu_row_id=dhatu_row_id)
    if n == 8:
        s7 = run_jayati_gold_through_step(7, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step8(s7, dhatu_row_id=dhatu_row_id)
    if n == 9:
        s8 = run_jayati_gold_through_step(8, state, dhatu_row_id=dhatu_row_id)
        return run_jayati_gold_step9(s8, dhatu_row_id=dhatu_row_id)
    raise ValueError(f"steps 1–9 supported; got n={n!r}")


def term_has_any_it_marker(t: Term) -> bool:
    return any((v.tags & IT_LOPA_TAGS) for v in t.varnas)
