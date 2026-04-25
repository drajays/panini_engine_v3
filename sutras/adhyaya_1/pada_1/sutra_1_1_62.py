"""
1.1.62  प्रत्ययलोपे प्रत्ययलक्षणम्  —  PARIBHASHA (*pratyaya-lakṣaṇa*)

**Padaccheda:** *pratyayalope* (saptamī ekavacanam), *pratyayalakṣaṇam*
(prathamā ekavacanam).

**Anuvṛtti:** none in the canonical *pāṭha* (the sūtra is self-contained).

**Adhikāra:** general *paribhāṣā* in **1.1** (no separate *adhikāra* sūtra id).

**Śāstra (laghu):** even after a *pratyaya* has undergone *lopa*, operations that
depend on that *pratyaya* (*pratyayāśritaṃ kāryam*) still apply — e.g. **1.4.14**
*pada* after **6.1.68** *su*-loss on *nadī* + *su*; **7.1.22** *luk* on *jas* after
*ṣaṣ* still allows *pada* then **8.2.39**; **7.2.106** on *adas* + *su* despite
*sulopa*; **6.1.71** *tuk* after *kvip* loss in *agnicid*; **7.3.86** *guṇa* and
Tripāḍī **8.2.32** / **8.2.37** after *ti*-*lopa* in *aduh* *laṅ* — all presuppose
this *paribhāṣā*.  **1.1.63** *na lumatāṅgasya* carves out *aṅga*-operations
blocked when the *lopa* is named *luk* / *ślu* / *lup*.

**Engine:** sets ``paribhasha_gates[PRATYAYALAKSHANAM_GATE]`` once in preflight
(next to **1.1.60** / **1.1.61**).  Individual *vidhi* *cond*/*act* still encode
their own phonology; this gate documents that the interpretive principle is in
force and is available for future checks via ``pratyayalakshanam_paribhasha_is_active``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_1.pratyayalakshanam_1_1_62 import PRATYAYALAKSHANAM_GATE


def cond(state: State) -> bool:
    return PRATYAYALAKSHANAM_GATE not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[PRATYAYALAKSHANAM_GATE] = True
    return state


_WHY = (
    "प्रत्ययस्य लोपे कृते अपि प्रत्ययाश्रितं कार्यम् अवश्यं भवति — "
    "यथा नदी+सुँ → नदी (६.१.६८) इत्यत्र पदम् १.४.१४; षष्+जस् → षड् (७.१.२२ लुक्); "
    "अदस्+सुँ → असौ (७.२.१०६); अग्निचित् (६.१.७१); अधुक् (७.३.८६, ८.२.३२)। "
    "अङ्गकार्ये अपवादः १.१.६३।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.62",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "pratyayalope pratyayalakzaNam",
    text_dev       = "प्रत्ययलोपे प्रत्ययलक्षणम्",
    padaccheda_dev = (
        "प्रत्ययलोपे (सप्तमी-एकवचनम्) / प्रत्ययलक्षणम् (प्रथमा-एकवचनम्)"
    ),
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
