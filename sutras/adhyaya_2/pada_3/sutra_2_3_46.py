"""
2.3.46  प्रातिपदिकार्थलिङ्गपरिमाणवचनमात्रे प्रथमा  —  ANUVADA

**Pāṭha** (ashtadhyayi-com style, *anuvṛtti* from **2.3.1** *anabhihite* baked in):
*anabhihite prātipadikārtha-liṅga-parimāṇa-vacana-mātre prathamā*.

*Kāśikā (sense):* where the meaning is **only** that of a *prātipadika* (mere
*sattā* per **1.2.45**), or **only** gender, or **only** measure (*droṇa*,
*khārī*, *āḍhaka*, …), or **only** grammatical number (*eka* / *dvi* / *bahu*,
…), the **first** (*prathamā*) case-affix is used — *uccaiḥ*, *kumārī*,
*droṇaḥ*, *ekaḥ*, …; *nipāta* without meaning (*anarthaka*) is also
*prātipadika* (**1.2.45**).

*Engine:* **ANUVADA** — no phonological change.  *cond* is blind to
``vibhakti`` / ``vacana`` coordinates (CONSTITUTION Art. 2): it keys off
``state.meta['2_3_46_matra_prathama_eligible']``, set by the *subanta* recipe
when the caller opts into this *śāstra* slice, and requires **2.3.1**
*anabhihita* *adhikāra* on ``adhikara_stack``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _adhikara_2_3_1_open(state: State) -> bool:
    return any(e.get("id") == "2.3.1" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    if not _adhikara_2_3_1_open(state):
        return False
    return bool(state.meta.get("2_3_46_matra_prathama_eligible"))


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.3.46",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = (
        "anabhihite prAtipadikArTa-liFga-parimARa-vacanamAtre prathamA"
    ),
    text_dev       = "अनभिहिते प्रातिपदिकार्थलिङ्गपरिमाणवचनमात्रे प्रथमा",
    padaccheda_dev = (
        "अनभिहिते / प्रातिपदिकार्थ-लिङ्ग-परिमाण-वचनमात्रे / प्रथमा"
    ),
    why_dev        = (
        "प्रातिपदिकार्थमात्रे, लिङ्गमात्रे, परिमाणमात्रे, वचनमात्रे च "
        "प्रथमा विभक्तिः (काशिका) — अनुवादः, न ध्वनि-परिवर्तनम्।"
    ),
    anuvritti_from = ("2.3.1", "1.2.45"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
