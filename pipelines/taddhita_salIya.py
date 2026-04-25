"""
pipelines/taddhita_salIya.py — *śālā* + *tatra bhava* → *śālīya* (तद्धित *Cha* → *īya*).

**चरण १ (प्रातिपदिक-ग्रहण एवं सुप्-उत्पत्ति):** the stem alone is the input; **4.1.1**
*ṅyāp-prātipadikāt* opens; **1.2.45** *arthavad… prātipadikam*; **4.1.3** *striyām*;
**4.1.4** *ajādyataḥ ṭāp* (for *śālā* the engine skips — *ā*-*anta*; pedagogical
“आप्-अन्त” = **4.1.1** *ṅyāp* + ā-anta *strī*; not a separate sūtra **4.1.46** in
this tree); then **4.1.2** attaches *su* (prathamā ekavacana: *śālā* + *su*).

**चरण २ (समर्थाधिकार एवं प्रथमा-विवक्षा):** with *śālā* + *su* (prathamā) in place, **4.1.82**
*samarthānāṃ prathamāt* opens the *samarthādhikāra* (optional *taddhita* from
the *prathamā* member); **4.1.83** *prāg dīvyataḥ aṇ*.

**चरण ३ (भव-अर्थ, आधार, सप्तमी-स्मृति):** **4.3.53** *tatra bhavaḥ* (SAMJNA in engine)
with ``META_ELIGIBLE``; then **1.4.23** *kārake* + **1.4.45** *ādhāro ’dhikaraṇam*
(``META_1_4_45_LOCUS`` → index ``0``); **2.3.36** records locative SLP1
``SAlAyAm`` in ``samjna_registry`` (no second *sup* on the running *prakriyā*).
*CaH* is appended only in **चरण ५** after **4.2.114** (not here).

**चरण ४ (वृद्धि / वृद्ध-पद):** **1.1.1** *vṛddhi* phoneme set; **1.1.73** *vṛddha-pada*
(first *ac* *ā*/*ai*/*au* on *śālā*); **1.1.62** *pratyayalakṣaṇam* (paribhāṣā gate
next to *lopa* *saṃjñā* in the usual preflight).  ``TAp_anta`` on the stem
marks ā-anta *strī* when **4.1.4** does not insert *ṭāp*.

**चरण ५ (तद्धित *Cha* — licence + structural *upadeśa*):** *Śāstra* **वृद्धाच्
छ** is **4.2.114** (not **4.2.71** *ora aṇ* in Aṣṭādhyāyī order).  Combine
**4.3.53** *tatra bhava* (already run) with **1.1.73** *vṛddha* and **4.2.92**
*śeṣe*; **4.2.114** registers *Cha* eligibility on index ``0``; **3.1.1–3.1.3**
*pratyaya*/*para*/*ādyudātta*; **4.1.76** *taddhite* *adhikāra* (pushes stack).
*CaH* is then appended (structural) after **4.2.71** (ओरञ् audit) + **4.2.113** (*na
dvyacaḥ* … — not *tatra-bhava*, which is **4.3.53**).

**चरण ६ (तद्धित-संज्ञा — 4.1.76 तद्धिताः, pedagogy):** after **4.1.76**, *vihita* *Cha* for
this *śālā* *prakriyā* is **4.2.114** (not 4.2.71 *oraṅ*). The *Ca* *Term* gets
``tags | {'taddhita'}`` in ``_append_taddhita_cah`` — engine **4.1.76** is
``SutraType.ADHIKARA`` (taddhita *scope*), not a *Term*-tag *samjna* sūtra.  That
*taddhita* *class* on the pratyaya is *anukūla* to **1.2.46** (prātipadika) and
**2.4.71** (sup *luk*); they run next, then *ṅit* / *bha* / *saṃdhi* on
*[aṅga, sup, taddhita]*.

**चरण ७ (1.2.46 *कृत्तद्धितसमासाश् च*, *prātipadika*):** *aṅga* is *prātipadika* from
**1.2.45**; with *taddhite* *Cha* attached, **1.2.46** *Case D* names the
*tad-dhite*-*anta* *śabda* and adds ``prātipadika`` to the *taddhita* ``Term``
(*C* in *upadeśa* *Cha*; *it* *lopa* and **7.1.2** *phadi* → *īya* are still
ahead). After **1.2.46**: ``pratipadika_avayava_ready`` enables **2.4.71**
(internal *sū* *luk*).

**चरण ८ (2.4.71 *सुपो धातुप्रातिपदिकयोः* — *luk*):** the *prathamā* *sū* coming from
**4.1.2** in the **4.1.82** *samarthā* frame (pedagogy: *Di* = *sū* *pratyaya* as
*upadeśa*) is a *sup* *avayava* on the *aṅga*; **1.1.60** *adarśana* = *lopa*
(disappearance, not a substitute phoneme); **1.1.62** *pratyayalakṣaṇam* places
*luk* in the *lopa* / *lup* family.  **2.4.71** *VIDHI* removes the *sup* ``Term``
from the live ``terms`` list — only *aṅga* + *taddhite* *Cha* *remain*; *Cha* is
still a separate ``Term`` in ``state.terms`` and the ``trace`` until *ṅit* / *bha* /
*saṃdhi*; surface still builds from *SAlA* + *CaH* → … *Iya*.

**चरण ९ (ऽछऽ *it* — 1.3.2…1.3.8, 1.3.9, *phadi* 7.1.2 / 1.3.10):** *upadeśa* *Cha*
(तद्धित) — **1.3.2** *anunāsikā* (N/A here); **1.3.3** *hal antyam* — first *hal* in *upadeśa* is
relevant; **1.3.7** *cuṭū* — the initial *C* (छ् / *ch*) in *ca*/*varga* is *it*.
Then **1.3.9** *upadeśe* *itasya* *lopaḥ*; **1.1.60** *adarśanam* = *lopa* of the *it*
*varṇa*.  The *Iya* / *īya* *rūpa* is not read off *śeṣa* *a* alone: **7.1.2** *pratyayādīnāṃ*
*pha-ḍha-kha-cha-gham* *ā*-*e*-*ī*-*ī*-*i* replaces the *Cha* opener, with **1.3.10** *tulyāsya* /
*yathāsaṅkhyam* in that block (``sutras/adhyaya_7/pada_1/sutra_7_1_2.py``).

*Engine (this recipe):* **1.3.2**…**1.3.8** and **1.3.9** are **not** *apply_rule*’d here;
``sutra_7_1_2`` documents *prayoga*: **7.1.2** is ordered **before** separate **1.3.7**
*it* on the same *C* (so the *taddhita* opener is **replaced** by the *Iya* *ādeśa* in
one *vidhi*, *not* *śūnya* after 1.3.9 *only*). The *trace* shows **7.1.2**
``SAlA``*+*``CaH`` → ``SAlAIya`` and **1.3.10** *APPLIED*; not **1.3.9** on the *ch* in
this *vṛtti* of the engine.

**चरण १० (1.4.13 *aṅga*; 6.4.1 *aṅgasya*; 7.1.2 *phadi*; 1.3.10
*yathāsaṅkhyam*):** **1.4.13** *yasmāt* … *pratyaye* *aṅgam* — *śālā* (=*nimitta* as
*prakriti*) is the *aṅga* to *Cha*; the stem is *aṅga*-*tag*ged in ``build_salIya`` and
**1.4.13** registers ``("1.4.13_anga", 0)`` in ``state.samjna_registry`` when *cond* holds.
**6.4.1** *aṅgasya* opens the *sūtra* *adhikāra* **6.4.1**–**7.4.97** so **7.1.2** can run.
**7.1.2** replaces *pha-ḍha-kha-cha-gh* openers; here *Cha* (4th) → *Iya* (4th) under
**1.3.10** in that *varga*; *Iya* is *i* + *Ī* + *y* + *a* (``parse_slp1...``) — pedagogy
*īy* as the *C* *slot* *ādeśa* family.  Trace order: **1.1.62** (re-preflight), **1.4.13**,
**6.4.1**, **7.1.2**, **1.3.10**.

**चरण ११ (1.4.18 *yaci* *bham*; *bhādhikāra*; 6.4.148 *yasyeti* *ca*):** after
**7.1.2** the *taddhite* *pratyaya* begins with *Ī* (*I* in SLP1) = *ac*-*ādi*; **1.4.18**
tags the preceding *aṅga* (*śālā*) with ``bha`` (same *sūtra* as *sup* *yaci* paths,
*Case B* in ``sutra_1_4_18``).  The *bhā*-*adhikāra* sūtra is **6.4.129** *bhasya* in
this engine (not implemented as 6.4.126; scope to **6.4.175** on ``adhikara_stack``)
— user handbooks that label “भस्य ६.४.१२६” may use a different *krame*; the *pāṭha* here
matches `ashtadhyayi-com` **6.4.129**).  **6.4.148** *yasyeti* *c* *lopa* of *aṅgāntya*
*ā* when the next *taddhite* onset is *I* / *i*; result *SAl* + *Iya* → *śālīya*;
**1.1.60** *adarśanam* *lopa* *anukūla* in a separate **1.1.60** *apply_rule* at the end
of the recipe.  Order: **1.4.18** → **6.4.129** → **6.4.148** → **1.1.60**.

**चरण १२ (शाल् + ईय्; *rūpa*; 1.2.46 *punaḥ*; 4.1.2 *optional*):** after **6.4.148** the
*saṃhitā* of *SAl* and *Iya* is *l* *+* *ī* → *lī* (no extra 8.2 *viśeṣa* *saṃdhi* here).  The
*śabda* is ``SAlIya`` from ``State.flat_slp1()``.  *Tad-dhite*-*anta* = *prātipadika* (again) by
**1.2.46**; this run does **not** a second *apply* of **1.2.46** (Case D already in *trace*).
``_annotate_carana_12`` sets ``taddhitānta`` on the *aṅga* and *taddhita* *terms* and
``meta['taddhitānta_pada_slp1']`` for UI.  *Subanta*: **4.1.2** *svauja…* would be *śālīya* *+* *su* → e.g. ``SAlIyaH`` in SLP1 (8.*x* *visarjanīya*); not
run; *mātra* *prātipadika* *śālīya* suffices.

**पूर्ण प्रक्रिया-सारणी (``derive_salIya`` / v3):** hand-charts often list *कुल* 25 *sūtra*; the
*trace* has **31** *APPLIED* steps.  **4.1.4** = *SKIPPED*; a second **1.1.62** after **2.4.71** is
in the *spine* but *SKIPPED* (*COND-FALSE*).  Major *śikṣ*–*engine* *antara*:
  • *वृद्धाच् छ* = **4.2.114**, not **4.2.71** (*ओरञ्* — **4.2.71** is only an audit in the recipe).
  • *छ* *it* (1.3.7) + 1.3.9: **not** separate *APPLIED*; **7.1.2** *phadi* *pre-empts* (see चरण ९).
  • *āp* / **4.1.46**: *strī* *ā*-*anta* is **4.1.1** + **4.1.3**; **4.1.4** *ajādi* *SKIPPED*; no **4.1.46** file in this *spine*.
  • *भस्य*: **6.4.129** in repo, not a separate **6.4.126** module.
  • चरण १३ (table *1.2.46* *antima*): not a second **1.2.46** *apply* — use ``_annotate_carana_12`` + चरण १२ doc.

*Resumé (rows match user चरण where possible; * engine column):*
  | चरण | engine *sūtra* (क्रमसूची) | रूप / टिप्पणी |
  |-----|--------------------------|--------------|
  | 1 | 4.1.1, 1.2.45, 4.1.3, 4.1.4 (skip), 4.1.2 | *śālā* + *su*; *prātipadika* |
  | 2 | 4.1.82, 4.1.83 | *samarthā* + *aṇ* *adhikāra* |
  | 3 | 4.3.53, 1.4.23, 1.4.45, 2.3.36 | *tatra bhava*; *SAlAyAm* in registry |
  | 4 | 1.1.1, 1.1.73, 1.1.62 | *vṛddha* *pada* |
  | 5 | 3.1.1–3, 4.1.76, 4.2.92, **4.2.114**, 4.2.71, 4.2.113, *CaH* | *vṛddhāc* *Cha* = **4.2.114** |
  | 6–7 | 1.2.46 | *taddhite* *prātipadika* on *Cha* *Term* |
  | 8 | 2.4.71; 1.1.62 (2nd) *SKIPPED* | *sū* *luk* |
  | 9 | 1.4.13, 6.4.1, 7.1.2, 1.3.10 | *aṅga* registry; *aṅgasya*; *phadi*; 1.3.10; no 1.3.7/9 *APPLIED* |
  | 11 | 1.4.18, 6.4.129, 6.4.148, 1.1.60 | *bha*; *ā* *lopa* → *SAl* + *Iya* |
  | 12 | ``_annotate_carana_12`` | ``SAlIya``; ``taddhitānta`` tags |
  | 13 | (pedagogy only) | *punaः* *1.2.46* — *no* second *apply* |

*APPLIED* *krame* (31) — *copy* from *trace*:
  4.1.1, 1.2.45, 4.1.3, 4.1.2, 4.1.82, 4.1.83, 4.3.53, 1.4.23, 1.4.45, 2.3.36, 1.1.1, 1.1.73,
  1.1.62, 3.1.1, 3.1.2, 3.1.3, 4.1.76, 4.2.92, 4.2.114, 4.2.71, 4.2.113, 1.2.46, 2.4.71, 1.4.13,
  6.4.1, 7.1.2, 1.3.10, 1.4.18, 6.4.129, 6.4.148, 1.1.60

*Antim* *siddha* (flow): *śālā* *+* *samarthā* → *śālā* *+* *su* → … → *śālā* *+* *CaH* → *luk* *sū* →
*SAlA* *+* *CaH* → *SAlA* *+* *Iya* (7.1.2) → *bha* *+* 6.4.148 → ``SAl`` *+* *Iya* → ``SAlIya`` (``flat_slp1``).

*तुलना* (भिन्न *upadeśa*, समान *śailī*):
  *śālā* *+* *Cha* (→ *Iya*) *vṛddha* *ā* *lopa* → *śālīya*; *grāma* *+* *Cha* (→ *Ina* from *Kha* slot) →
  *grāmīṇa*; *nagara* *taddhite* paths differ (*na* *+* *छ* in the same *vṛddhāc* *block* — *not* the *śālā* *recipe*).

Glass-box: only ``apply_rule`` + ``_pada_merge`` (CONSTITUTION Art. 7).
``meta['prakriya_sAlIya']`` arms **1.2.46** Case D; **6.4.129** before **6.4.148**.
"""
from __future__ import annotations

import sutras  # noqa: F401  (registry)

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_4.pada_3.sutra_4_3_53 import META_ELIGIBLE as META_4_3_53_ELIGIBLE
from sutras.adhyaya_4.pada_3.sutra_4_3_53 import META_JATI_BLOCK as META_4_3_25_JATI
from sutras.adhyaya_1.pada_4.sutra_1_4_45 import (
    META_LOCUS_INDICES as META_1_4_45_LOCUS,
)
from sutras.adhyaya_2.pada_3.sutra_2_3_36 import (
    META_LOCATIVE as META_2_3_36_LOCATIVE,
)
from sutras.adhyaya_4.pada_2.sutra_4_2_114 import (
    META_ELIGIBLE_INDICES as META_4_2_114_SHEcA,
)

from pipelines.subanta import _pada_merge


def build_salIya_initial_state() -> State:
    """
    *Śālā* (strī, ā-anta, SLP1 ``SAlA``) as *aṅga* only — *prātipadika* comes from
    **1.2.45**; *su* from **4.1.2** after *strī* adhikāra **4.1.3** / **4.1.4** slot.
    *Vibhakti/vacana* in ``state.meta`` is the one exception for **4.1.2**
    (Constitution).
    """
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("SAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    stem.tags.add("strīliṅga")
    stem.tags.add("TAp_anta")
    s = State(terms=[stem])
    s.meta["prakriya_sAlIya"] = True
    s.meta["linga"] = "strīliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s.meta[META_4_3_53_ELIGIBLE] = True
    s.meta.pop(META_4_3_25_JATI, None)
    s.meta[META_2_3_36_LOCATIVE] = "SAlAyAm"
    return s


def _annotate_carana_12(s: State) -> None:
    """
    *Tad-dhite*-*anta* *pada* surface: ``taddhitānta`` tag + ``taddhitānta_pada_slp1`` in ``meta`` (चरण १२).
    """
    if not s.meta.get("prakriya_sAlIya"):
        return
    s.meta["taddhitānta_pada_slp1"] = s.flat_slp1()
    if (
        len(s.terms) >= 2
        and s.terms[0].kind == "prakriti"
        and s.terms[1].kind == "pratyaya"
        and "taddhita" in s.terms[1].tags
    ):
        s.terms[0].tags.add("taddhitānta")
        s.terms[1].tags.add("taddhitānta")


def _append_taddhita_cah(s: State) -> None:
    """
    *CaH* after **4.2.114** *vṛddhāc chaḥ* licence (plus **3.1.1**–**3.1.3** /
    **4.1.76** / **4.2.92**); not yet a standalone *śabda*-insert *vidhi* sūtra.
    """
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("CaH"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "CaH"},
    )
    s.terms.append(pr)


def derive_salIya(*, pada_merge: bool = False) -> State:
    """
    Run the *śālīya* *prakriyā* (user-supplied *sūtra* spine, plus engine gates).

    Returns final ``State``; surface ``SAl`` + ``Iya`` → ``SAlIya`` after **6.4.148**.
    """
    s = build_salIya_initial_state()

    # चरण १ — *sup* from **4.1.2** (after *prātipadika* + *strī* slot).
    s = apply_rule("4.1.1", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("4.1.3", s)
    s = apply_rule("4.1.4", s)
    s = apply_rule("4.1.2", s)

    # चरण २ — *samarthādhikāra* + *tatra-bhava* licence, then *CaH* (structural).
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.83", s)
    s = apply_rule("4.3.53", s)
    s.meta[META_1_4_45_LOCUS] = (0,)
    s = apply_rule("1.4.23", s)
    s = apply_rule("1.4.45", s)
    s = apply_rule("2.3.36", s)

    # चरण ४ — *vṛddhi* / *vṛddha-pada* (+ **1.1.62** *pratyayalakṣaṇa* paribhāṣā)
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = apply_rule("1.1.62", s)

    # चरण ५ — *vṛddhāc cha* regime (**4.2.114**) + 3.1.1–3, **4.1.76**, *CaH*
    s = apply_rule("3.1.1", s)
    s = apply_rule("3.1.2", s)
    s = apply_rule("3.1.3", s)
    s = apply_rule("4.1.76", s)
    s = apply_rule("4.2.92", s)
    s.meta[META_4_2_114_SHEcA] = (0,)
    s = apply_rule("4.2.114", s)
    s = apply_rule("4.2.71", s)
    s = apply_rule("4.2.113", s)
    # *Cha* in **4.1.76** scope: ``taddhita`` on Term (``_append_taddhita_cah``) — चरण ६.
    _append_taddhita_cah(s)
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    # चरण ८ — **2.4.71** *sū* *luk* (``sup`` ``Term`` elided; *aṅga* + *taddhite* *Cha* *only*).
    s = apply_rule("2.4.71", s)
    s = apply_rule("1.1.62", s)
    # चरण १०a — *aṅga* **1.4.13**; चरण १०b — **6.4.1** *aṅgasya* *adhikāra*; then **7.1.2** + **1.3.10** below.
    s = apply_rule("1.4.13", s)
    s = apply_rule("6.4.1", s)
    # चरण १०c/d + चरण ९: *phadi* 7.1.2, 1.3.10 (see *it* *śikṣā* + चरण ९ in module doc).
    s = apply_rule("7.1.2", s)
    s = apply_rule("1.3.10", s)
    # चरण ११ — **1.4.18** *bha*; **6.4.129** *bhasya*; **6.4.148** *ā*-lopa before *Iya*; **1.1.60** *lopa* *punaḥ*.
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = apply_rule("1.1.60", s)
    _annotate_carana_12(s)  # चरण १२: ``flat_slp1`` + *tad-dhite*-*anta* tags

    if pada_merge:
        _pada_merge(s)  # optional UI merge — leaves ``Term`` as ``pada``, not *prātipadika*
    return s
