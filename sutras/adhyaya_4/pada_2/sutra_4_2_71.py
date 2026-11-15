"""
4.2.71  ओरञ्  —  SAMJNA (*o* + *aṇ* licence under **4.1.82**)

**Pāṭha (baked):** *samarthānām prathamāt ṅyāp-prātipadikāt paraḥ ādyudāttaḥ
taddhitaḥ vā prāg dīvyataḥ aṇ śeṣe oḥ aṇ* — *aṇ* after an *o*-final base in the
*śeṣa* block (**4.2.92** … **4.3.134** in the śāstra); *anuvṛtti* from **4.2.92**
is not re-opened here — **4.1.82** *samarthādhikāra* is the engine’s scope gate
for this file (so **4.2.71** < **4.2.92** in the Aṣṭādhyāyī order still parses).

**Engine:** one-shot audit in ``samjna_registry`` — ``True`` iff the first
*prātipadika* ``Term``’s last phoneme is SLP1 ``o`` (so *aṇ* from *o* is live);
``False`` for bases like *śālā* (ā-anta), without reading *vibhakti* (Art. 2).
Pāṭha: ashtadhyayi.com data.txt row i=42071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita


def _site(state: State):
    """Kāśikā 4.2.71: after an uvarṇānta prātipadika the pratyaya of the four senses (4.2.67 – 70: tad asmin asti, tena nirvṛttam, tasya nivāsaḥ, adūrabhavaḥ)
    is añ, the apavāda of aṇ (araḍu — āraḍavam, kakṣatu — kākṣatavam). `o` of the sūtra = the u-varṇa (u, ū)."""
    return taddhita_site(state, "cAturarTika", final=lambda f: f.endswith(("u", "U")))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return attach_taddhita(state, "aY") if _site(state) is not None else state

SUTRA = SutraRecord(
    sutra_id        = "4.2.71",
    sutra_type      = SutraType.VIDHI,
    text_slp1       = (
        'oraY'
    ),
    text_dev        = (
        'ओरञ्'
    ),
    samagra_slp1    = "tadasminnastIti deSe tannAmni tena nirvfttam tasya nivAsaH adUraBavaSca iti oH aY",
    samagra_dev     = "'तदस्मिन्नस्तीति देशे तन्नाम्नि', 'तेन निर्वृत्तम्', 'तस्य निवासः', 'अदूरभवश्च' इति ओः अञ्",
    padaccheda_dev  = "ओः (षष्ठी-एकवचनम्) / अञ् (प्रथमा-एकवचनम्)",
    why_dev         = (
        "उवर्णान्ताद् अञ् प्रत्ययः (अरडु — आरडवम्): अणोऽपवादः, तदस्मिन्नस्ति आदिषु चतुर्ष्वर्थेषु।"
    ),
    apavada_of      = ("4.1.83",),
    anuvritti_from  = ("4.1.82", "4.1.83", "4.2.92"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)
