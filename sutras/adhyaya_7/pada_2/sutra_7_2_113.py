"""
7.2.113  हलि लोपः  —  VIDHI (narrow: *idam* / *etad* + *hal*ādi *sup*)

*Śāstra* *prayoga* (Kāśikā/*prakriyā*): of **idam** / **etad**, the **i**+**d** and **e**+**t**
(``id``-``khaṇḍa``) *lops* when a *sup* *pratyaya* beginning with a consonant
(*hali* — including **B**+**y**+… of **B**+**y**+**A**+**m**) *pare*; *śeṣa* (final *a* of
the *aṅga* after **7.2.102** + **6.1.97**) remains, enabling **1.1.21** (एक-smin्
*ādeśa* for *dīrgha*) and **7.3.102** (सुपि च) → *ā* + *bhy*… → **AByAm** (आभ्याम्)
for **idam**+**B**+**y**+**A**+**m** — see user note `aabhyam.md`.

*Nyūna* v3: only the **i**+**d**+**a** and **e**+**t**+**a** *corpora* (SLP1 ``ida``, ``eta``) after
**6.1.97**; *no* *vibhakti*/*vacana* read in ``cond`` (Art. 2).  *Etad* is included so
*etad*+*bhyām* converges (note line 40–41).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import HAL


def _lopa_target(state: State) -> int | None:
    """
    If penultimate aṅga (terms[-2]) is ``i``+``d``+``a`` (``idam``) or
    ``e``+``t``+``a`` (``etad``), and last term is *sup* *hal*ī, return
    aṅga *term* index.  Else None.
    """
    if len(state.terms) < 2:
        return None
    an = state.terms[-2]
    su = state.terms[-1]
    if "anga" not in an.tags or "sup" not in su.tags:
        return None
    if an.meta.get("7_2_113_hali_lopa_done"):
        return None
    if not an.varnas or not su.varnas:
        return None
    if su.varnas[0].slp1 not in HAL:
        return None
    up = (an.meta.get("upadesha_slp1") or "").strip()
    v = an.varnas
    if up == "idam" and len(v) == 3:
        if v[0].slp1 == "i" and v[1].slp1 == "d" and v[2].slp1 == "a":
            return len(state.terms) - 2
    if up == "etad" and len(v) == 3:
        if v[0].slp1 == "e" and v[1].slp1 == "t" and v[2].slp1 == "a":
            return len(state.terms) - 2
    return None


def cond(state: State) -> bool:
    return _lopa_target(state) is not None


def act(state: State) -> State:
    ti = _lopa_target(state)
    if ti is None:
        return state
    t = state.terms[ti]
    u = t.varnas
    up = (t.meta.get("upadesha_slp1") or "").strip()
    if up == "idam" and [x.slp1 for x in u] == ["i", "d", "a"]:
        t.varnas = u[2:]
    elif up == "etad" and [x.slp1 for x in u] == ["e", "t", "a"]:
        t.varnas = u[2:]
    else:  # pragma: no cover — defensive; cond already filtered
        return state
    t.meta["7_2_113_hali_lopa_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id         = "7.2.113",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = "hali lopaH",
    text_dev         = "हलि लोपः",
    padaccheda_dev   = "हलि / लोपः",
    why_dev          = (
        "इदम्-एतद्-शब्दयोर् हल्-वर्णादौ सुपि परे 'इद्'-'एत्'-भागस्य लोपः, "
        "ततः 'अ' मात्रेण अदन्त-अङ्गं *सुपि* दीर्घ-योग्यम् (७.३.१०२, १.१.२१)।"
    ),
    anuvritti_from   = ("7.2.102",),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)
