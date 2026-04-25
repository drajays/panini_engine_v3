"""
1.1.63  लुमता प्रत्ययलोपे अङ्गस्य प्रत्ययलक्षणं न  —  PARIBHASHA (*apavāda* to **1.1.62**)

**Padaccheda:** *na* (avyayam), *lumatā* (tṛtīyā ekavacanam), *aṅgasya*
(ṣaṣṭhī ekavacanam); *pratyayalope* and *pratyayalakṣaṇam* by *anuvṛtti* from
**1.1.62**.

**Anuvṛtti:** *pratyayalope*, *pratyayalakṣaṇam* — both from **1.1.62**
*pratyayalope pratyayalakṣaṇam*.

**Adhikāra:** general *paribhāṣā* in **1.1** (no separate *adhikāra* id).

**Śāstra (laghu):** when a *pratyaya* is lost by one of the three named routes
(*luk* / *śluḥ* / *lup* — **1.1.61**), *aṅga*-operations occasioned **only** by
that *lupta pratyaya* do **not** apply — *apavāda* to **1.1.62**.  Plain *lopaḥ*
(**6.1.68**, …) does **not** trigger this block, so *aṅga-kārya* such as **6.4.13**
on *śaśin* + *su* or **7.2.115** *vṛddhi* under **6.4.51** *ṇer aniṭi* in *kāryate*
still runs.  Non-*aṅga* *pratyaya*-nimitta rules (e.g. **1.4.14** *pada*, **8.2.7**
after **7.1.22** *luk* on *pañcan* + *jas*) remain available; only *aṅgasya …
pratyayalakṣaṇam* is barred here.

**On *lumatā*:** *lumat* is the *matup* derivative (**5.2.94**) of *lu* as a cover
term for *luk*–*ślu*–*lup* teaching; the *tṛtīyā* *lumatā* “when loss is by a
*lu*-class instruction” scopes the *niṣedha*.

**Engine:** sets ``paribhasha_gates[NA_LUMATANGASYA_GATE]`` once in preflight
(immediately after **1.1.62**).  Requires **1.1.62** to have fired first.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_1.na_lumatangasya_1_1_63 import NA_LUMATANGASYA_GATE
from sutras.adhyaya_1.pada_1.pratyayalakshanam_1_1_62 import (
    pratyayalakshanam_paribhasha_is_active,
)


def cond(state: State) -> bool:
    if not pratyayalakshanam_paribhasha_is_active(state):
        return False
    return NA_LUMATANGASYA_GATE not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[NA_LUMATANGASYA_GATE] = True
    return state


_WHY = (
    "लुक्-श्लु-लुप्-संज्ञकेन प्रत्ययलोपे लुप्तप्रत्ययनिमित्तकम् अङ्गकार्यम् न — "
    "यथा इदम्+सुँ → इदम् (७.१.२३ लुक्, ७.२.११० यः सौ न); हु+शप् → झुहुतः (२.४.७५ श्लुः, ७.३.८४ गुणो न); "
    "पञ्चाल+अण् (४.२.८१ लुप्, ७.२.११७ आदिवृद्धिर्न)। केवल-लोपे (६.१.६८) १.१.६३ न, यथा शशिन्+सुँ → शशी (६.४.१३)। "
    "अङ्गस्यैव निषेधः — पदम्, नलोपः (८.२.७) आदयः अङ्गकार्यं विना १.१.६२-अनुसारेण (यथा पञ्चन्+जस् → पञ्च)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.63",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "lumatA pratyayalope aNgasya pratyayalakzaRaM na",
    text_dev       = "लुमता प्रत्ययलोपे अङ्गस्य प्रत्ययलक्षणं न",
    padaccheda_dev = (
        "न (अव्ययम्) / लुमता (तृतीया-एकवचनम्) / प्रत्ययलोपे (सप्तमी-एकवचनम्, अन्वा. १.१.६२) / "
        "अङ्गस्य (षष्ठी-एकवचनम्) / प्रत्ययलक्षणम् (प्रथमा-एकवचनम्, अन्वा. १.१.६२)"
    ),
    why_dev        = _WHY,
    anuvritti_from = ("1.1.62",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
