"""
1.2.46  कृत्तद्धितसमासाश्च  —  SAMJNA

A stem formed by a kṛt / taddhita affix (or a compound) is called
*prātipadika* — licensing sup attachment under ``4.1.1`` / ``4.1.2``.

In glass-box recipes, **2.4.71** (*supo dhātūprātipadikayoḥ*) should run only
after *avayava* are *prātipadika*-tagged; this engine models that with
``meta['pratipadika_avayava_ready']`` before ``meta['2_4_71_luk_arm']`` arms
*luk* (see **2.4.71** module doc).

Engine: fires once a kṛt-augmented dhātu shape is ready (after ``7.2.116`` on
the agent-noun path); registry flag for trace only.  Case C records
prātipadika-saṃjñā for a single merged dik-samāsa from ``2.2.26`` (no
re-segmentation).  Case D tags the *taddhita* ``Term`` (e.g. *ChaH*) with ``prātipadika`` and sets
a registry flag for *śālīya* recipes (``pipelines/taddhita_salIya``) *before*
**2.4.71** *luk* and before *it*-*lopa* in the *phadi* chain **7.1.2** (pedagogy:
**1.2.46** names the *kṛt-taddhita*-*anta* *śabda*; *C* of *Cha* is *it* per
1.3.2–1.3.9).  Case E: same three-*Term* frame for *itika* + *phak*
(``pipelines/taddhita_itika_etikAyana``; ``prakriya_itika_phak``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


META_TADDHITA_AVAYAVA = "prakriya_taddhita_avayava"


def cond(state: State) -> bool:
    # Generic gate: any *vyutpanna* community containing kṛt / taddhita / samāsa
    # should be promoted to prātipadika here.  This is deliberately **tag-driven**
    # and does not read external corpora.
    if any(("krt" in t.tags) or ("taddhita" in t.tags) or ("samasa_member" in t.tags) for t in state.terms):
        if state.samjna_registry.get("1.2.46_generic_pratipadika"):
            return False
        return True
    # ── Case C: dik-samāsa already merged by 2.2.26 (single prātipadika) ───
    if len(state.terms) == 1:
        t0 = state.terms[0]
        # **Before** the dik-gaṇa check: **5.3.71** *akac* *vyutpanna* (``सर्वकः .md``).
        if t0.meta.get("5_3_71_akac_vyutpanna"):
            if state.samjna_registry.get("1.2.46_5_3_71_akac"):
                return False
            return True
        if state.samjna_registry.get("1.2.46_dik_pratipadika"):
            return False
        if (
            "dhatu" not in t0.tags
            and "diksamasa" in t0.tags
            and "bahuvrihi" in t0.tags
            and "prātipadika" in t0.tags
        ):
            return True
        return False

    # ── Case D: *śālīya* glass-box — stem + internal *sup* + *taddhita* … ───
    # ``meta['prakriya_sAlIya']`` is armed only by ``pipelines/taddhita_salIya``.
    if state.meta.get("prakriya_sAlIya") and len(state.terms) >= 3:
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        if (
            "dhatu" not in t0.tags
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "sup" in t1.tags
            and "pratyaya" in t2.tags
            and "taddhita" in t2.tags
            and "sup" not in t2.tags
        ):
            if state.samjna_registry.get("1.2.46_sAlIya_avayava"):
                return False
            return True

    # ── Case E: *itika* + *phak* (``pipelines/taddhita_itika_etikAyana``) —──
    if state.meta.get("prakriya_itika_phak") and len(state.terms) >= 3:
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        if (
            "dhatu" not in t0.tags
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "sup" in t1.tags
            and "pratyaya" in t2.tags
            and "taddhita" in t2.tags
            and "sup" not in t2.tags
        ):
            if state.samjna_registry.get("1.2.46_itika_avayava"):
                return False
            return True

    # ── Case F: generic taddhita *avayava* frame (caller opt-in) —──────────
    # Used by glass-box pipelines that keep [anga + sup + taddhita] as three Terms
    # until 2.4.71 removes the internal sup.
    if state.meta.get(META_TADDHITA_AVAYAVA) and len(state.terms) >= 3:
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        if (
            "dhatu" not in t0.tags
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "sup" in t1.tags
            and "pratyaya" in t2.tags
            and "taddhita" in t2.tags
            and "sup" not in t2.tags
        ):
            if state.samjna_registry.get("1.2.46_generic_taddhita_avayava"):
                return False
            return True

    # ── Case A: kṛdanta path (dhātu may follow upasarga: ``[A, dhātu, kṛt]``) ─
    if len(state.terms) >= 2 and "krt" in state.terms[-1].tags:
        di = next((i for i, t in enumerate(state.terms) if "dhatu" in t.tags), None)
        if di is not None:
            if state.samjna_registry.get("1.2.46_krit_pratipadika"):
                return False
            t_dh = state.terms[di]
            pr = state.terms[-1]
            if t_dh.meta.get("upadha_vrddhi_done") is True:
                return True
            if t_dh.meta.get("aco_nniti_vrddhi_done") is True:
                return True
            # tṛc / 7.3.84 guṇa on aṅga (e.g. चि → चे before ``tf``).
            if t_dh.meta.get("anga_guna_7_3_84") is True and "krt" in pr.tags:
                return True
            # ``6.1.77`` *iko yaṇ aci* on dhātu (e.g. ``dIDhI``+``ana`` → ``dIDhyana``).
            if t_dh.meta.get("iko_yanaci_done") is True:
                return True
            return False

    # ── Case B: samāsa path (devendra/sūryodaya demo) ─────────────────────
    if "dhatu" not in state.terms[0].tags:
        # Glass-box policy: we allow a compound state to be promoted to a
        # single prātipadika *and* structurally merged here, but only when
        # the state already represents a samāsa (members tagged).
        if state.samjna_registry.get("1.2.46_samasa_pratipadika"):
            return False
        if not state.terms:
            return False
        # Require at least two members and no pending sup pratyaya
        # (internal sups must already be deleted by 2.4.71).
        members = [t for t in state.terms if "samasa_member" in t.tags]
        if len(members) < 2:
            return False
        if any("sup" in t.tags for t in state.terms):
            return False
        return True

    return False


def act(state: State) -> State:
    if len(state.terms) == 1 and state.terms[0].meta.get("5_3_71_akac_vyutpanna"):
        if state.samjna_registry.get("1.2.46_5_3_71_akac"):
            return state
        state.samjna_registry["1.2.46_5_3_71_akac"] = True
        t0 = state.terms[0]
        t0.tags.add("prātipadika")
        t0.tags.add("anga")
        t0.meta["vyutpanna"] = True
        return state
    if any(("krt" in t.tags) or ("taddhita" in t.tags) or ("samasa_member" in t.tags) for t in state.terms):
        state.samjna_registry["1.2.46_generic_pratipadika"] = True
        # Promote all non-pratyaya terms to prātipadika; also allow the vyutpanna
        # pratyaya Term to be prātipadika for internal-luk recipes.
        for t in state.terms:
            if "pratyaya" not in t.tags:
                t.tags.add("prātipadika")
            if "taddhita" in t.tags or "krt" in t.tags:
                t.tags.add("prātipadika")
        # Do NOT return: specific glass-box branches may need to set their
        # own audit registry flags (e.g. 1.2.46_sAlIya_avayava).
    # Case C: record prātipadika-saṃjñā for dik compound (structure unchanged).
    if len(state.terms) == 1:
        t0 = state.terms[0]
        if "diksamasa" in t0.tags and "bahuvrihi" in t0.tags:
            state.samjna_registry["1.2.46_dik_pratipadika"] = True
            return state

    if state.meta.get("prakriya_sAlIya") and len(state.terms) >= 3:
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        if (
            "dhatu" not in t0.tags
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "sup" in t1.tags
            and "pratyaya" in t2.tags
            and "taddhita" in t2.tags
            and "sup" not in t2.tags
        ):
            state.samjna_registry["1.2.46_sAlIya_avayava"] = True
            t2.tags.add("prātipadika")
            return state

    if state.meta.get("prakriya_itika_phak") and len(state.terms) >= 3:
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        if (
            "dhatu" not in t0.tags
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "sup" in t1.tags
            and "pratyaya" in t2.tags
            and "taddhita" in t2.tags
            and "sup" not in t2.tags
        ):
            state.samjna_registry["1.2.46_itika_avayava"] = True
            t2.tags.add("prātipadika")
            return state

    if state.meta.get(META_TADDHITA_AVAYAVA) and len(state.terms) >= 3:
        t0, t1, t2 = state.terms[0], state.terms[1], state.terms[2]
        if (
            "dhatu" not in t0.tags
            and "anga" in t0.tags
            and "prātipadika" in t0.tags
            and "sup" in t1.tags
            and "pratyaya" in t2.tags
            and "taddhita" in t2.tags
            and "sup" not in t2.tags
        ):
            state.samjna_registry["1.2.46_generic_taddhita_avayava"] = True
            t2.tags.add("prātipadika")
            return state

    # Aṅga + *taddhita* (no *sup*): keep two *Term*s for **6.3.43** / *it*-*lopa* (e.g. **5.3.55** / **5.3.57** *śāstrīya* *corpus*).
    if len(state.terms) == 2 and "dhatu" not in state.terms[0].tags:
        t0, t1 = state.terms[0], state.terms[1]
        if (
            "taddhita" in t1.tags
            and "sup" not in t0.tags
            and "sup" not in t1.tags
            and "samasa_member" not in t0.tags
            and "samasa_member" not in t1.tags
        ):
            state.samjna_registry["1.2.46_anga_taddhita_two_term"] = True
            return state

    # Samāsa path: merge samāsa members into one prātipadika+aṅga term.
    if "dhatu" not in state.terms[0].tags:
        # ``[upasarga, dhātu, kṛt]`` — not a samāsa; kṛdanta merge happens elsewhere.
        if any("dhatu" in t.tags for t in state.terms) and any(
            "krt" in t.tags for t in state.terms
        ):
            state.samjna_registry["1.2.46_krit_pratipadika"] = True
            return state
        # Mark registry for audit.
        state.samjna_registry["1.2.46_samasa_pratipadika"] = True
        # Structural merge (changes Term segmentation but not surface).
        from engine.state import Term
        all_varnas = []
        for t in state.terms:
            all_varnas.extend(t.varnas)
        merged = Term(
            kind="prakriti",
            varnas=all_varnas,
            tags={"prātipadika", "anga"},
            meta={"upadesha_slp1": state.flat_slp1()},
        )
        state.terms = [merged]
        return state

    # Kṛdanta path (legacy behaviour).
    state.samjna_registry["1.2.46_krit_pratipadika"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.46",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "kft-taddhita-samAsAH ca",
    text_dev       = "कृत्तद्धितसमासाश्च",
    padaccheda_dev = "कृत्-तद्धित-समासाः च (प्रातिपदिकम्)",
    why_dev        = "कृत्-तद्धित-समासान्ताः शब्दाः प्रातिपदिक-संज्ञकाः।",
    anuvritti_from = ("1.2.45",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
