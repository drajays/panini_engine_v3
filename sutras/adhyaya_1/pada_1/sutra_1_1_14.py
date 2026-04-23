"""
1.1.14  —  *pragṅhya* **saṃjñā** for *ekāc* *nipāta* (anāṅ)  [SAMJNA]

**Aṣṭādhyāyī — authority rows (ashtadhyayi-com ``sutraani/data.txt``, *i* = 11014)**

* **Pāṭhāntara / saṃkṣipta** (index *s* line, *sutrANi* TSV *anukrama*): ``निपात एकाजनाङ्`` —
  analysed as *nipāta* + *ekāj* + *anāṅ*; *anāṅ* excludes the *gā*-*gaṇa* *nipāta* **आङ्** (surface *ā* after
  *it* *lopa* of *ṅ*), to be read with the *Kārikā* that distinguishes **आ** and **आङ्**.

* **Pāda-cheda (śāstrīya *vigraha*)**
  * ``निपातः`` (prathamā-ekavacanam) · ``एकाच्`` (prathamā-ekavacanam) · ``अनाङ्`` (prathamā-ekavacanam).

* **Anuvṛtti:** ``प्रगृह्यम्`` ← **1.1.11** (*Ī-Ū-…* *dvivacana* *block*); no separate *adhikāra*
  bracket; this is the fourth sūtra in the *pragṅhya* *sūtra* *śreṇi* of nine **1.1.x** rules
  in the *śāstra* (conventional count including **1.1.11** and extensions up through **1.1.19** in v3's index).

* **Anuvṛtti-sahita sūtrārtha (``ss`` in the same row):** ``एकाच् अनाङ् निपातः प्रगृह्यम्`` —
  *ekāc* *anāṅ* *nipātaḥ* receive the name *pragṅhya* (*anuvṛtti* *pragṅhyam* from **1.1.11**).

* **Sūtra-prakāra:** *saṃjñā* (*pragṅhya*-*saṃjñā*; index ``type`` in ``data.txt``).

**Artha (Kāśikā / siddhānta one-locus gloss)**

* **Āṅ** *varjana* (exclusion of **आङ्**):** except **आङ्**, every *nipāta* that is *ekāc* (exactly one *svara*) and
  *nir-vyañjana* (no *vyañjana* / consonant) is *pragṅhya*; **आङ्** looks like *ekāc* after *it* *lopa*
  of *ṅ*, but is explicitly excluded, so *sandhi* (e.g. *āṅ* + *uṣṇam* → *oṣṇam*) applies. The
  *Kārikā* *īṣad…* (excerpt in the sources you cited) marks **आ** (exclamation / *smaraṇa*) vs
  **आङ्** (īṣat, *kriyāyoga* / *maryādā* / *abhividhi*, …).

* **One-line English (standard gloss):** except for the word āṅ, all *nipāta* that have only one vowel
  and no consonant are *pragṅhya*.

  (Nipāta *saṃjñā* is taught **1.4.56**–**1.4.97**; for *pluta* and *ac* *sandhi* *prakṛti* on *pragṅhya* see
  **6.1.125** in the *śāstra* — the engine defers to later *vidhi* sūtras in the recipe.)

v3 **R2** — ``samjna_registry['pragrahya_nipata_ekac_anang'] = True``; *vidhi* combines this with
**1.1.11**; **1.1.100** = *Kāśikā* *na mātrā samāse* (*paribhāṣā*, different id in this engine).

**CONSTITUTION Art. 4** — ``text_slp1`` / ``text_dev`` use the *anuvṛtti*-*sahita* pāṭha (``ss``),
not the *saṃkṣipta* ``s``; *s* is documented above for *anukrama* cross-checks.

See also **1.1.11**; **1.1.15** *ot*; **1.1.100** for *mātrā* *samāsa* *vṛtti* on *prayoga* *bādha*.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

SAMJNA_KEY: str = "pragrahya_nipata_ekac_anang"

# Index *s* (short pāṭha) for grep / ``sutrANi.tsv``; engine ``SutraRecord`` uses *ss* below.
SANKSIPTA_PATHA_DEV: str = "निपात एकाजनाङ्"

# Index *ss* — *anuvṛtti* of *pragṅhyam* (1.1.11); full *sūtrārtha* string.
ANUVRITTI_SAHITA_DEV: str = "एकाच् अनाङ् निपातः प्रगृह्यम्"


def nipata_ekajang_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(SAMJNA_KEY) is True


def cond(state: State) -> bool:
    return not nipata_ekajang_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry[SAMJNA_KEY] = True
    return state


_WHY = (
    "आङ्-व्यतिरेक-एकस्वर-निर्व्यञ्जन-निपातानां प्रगृह्य-संज्ञा; "
    "अच्-सन्धि-नित्य-प्रकृतिभावे च (यथा ६.१.१२५)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.14",
    sutra_type     = SutraType.SAMJNA,
    # Spaced SLP1 to match ``ANUVRITTI_SAHITA_DEV``; compact index ``e`` = ``nipaatekaajanaang``.
    text_slp1      = "ekAc anA~G nipAtaH pragfhyam",
    text_dev       = ANUVRITTI_SAHITA_DEV,
    padaccheda_dev = (
        "निपातः (प्र. ए.) / एकाच् (प्र. ए.) / अनाङ् (प्र. ए.); "
        "अन्वितं प्रगृह्यम् (१.१.११)"
    ),
    why_dev        = _WHY,
    anuvritti_from = ("1.1.11",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
