"""
3.3.103  गुरोश्च हलः  —  VIDHI

Padaccheda: गुरोः च हलः

krt-suffix rule: गुरोश्च हलः
Pāṭha: ashtadhyayi.com data.txt row i=33103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, bhava_site
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _gurumat_halanta(f: str) -> bool:
    """guroḥ halaḥ: a dhātu ending in a consonant that has a guru vowel in it (long, or short before a conjunct): īh, kuṇḍ — not bhaj."""
    if not f or f[-1] in "aAiIuUfFxXeEoO":
        return False
    for i, c in enumerate(f):
        if c in "AIUFXeEoO":
            return True
        if c in "aiufx" and len(f) - i - 1 >= 2 and f[i + 1] not in "aAiIuUfFxXeEoO" and f[i + 2] not in "aAiIuUfFxXeEoO":
            return True
    return False


def _site(state: State):
    return bhava_site(state, vivaksita(state, "artha", "BAva"), vivaksita(state, "linga", "strI"), final=_gurumat_halanta)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "a")


SUTRA = SutraRecord(
    sutra_id              = "3.3.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "guroSca halaH",
    text_dev              = "गुरोश्च हलः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm guroH ca halaH kft a",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् गुरोः च हलः कृत् अ",
    padaccheda_dev        = "गुरोः च हलः",
    why_dev               = "धातोः प्रत्ययः (३.3.103)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of     = ("3.3.94",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
