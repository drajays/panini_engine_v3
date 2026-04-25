"""
7.3.114  सर्वनाम्नः स्याट् ह्रस्वश्च  —  VIDHI

पदच्छेदः  सर्वनाम्नः (पञ्चमी-एकवचनम्), स्याट् (प्रथमा-एकवचनम्),
          ह्रस्वः (प्रथमा-एकवचनम्), च (अव्ययम्)

अनुवृत्तिः  ङिति 7.3.111, आपः 7.3.113

अधिकारः  अङ्गस्य 6.4.1

अनुवृत्तिसहितं सूत्रम्  सर्वनाम्नः आपः ङिति सुपि स्याट् अङ्गस्य ह्रस्वः च

After a **sarvanāma** *aṅga* whose final is **ā** (*ā-banta*, *āp*), before **ṅit**
*sup*: shorten **ā** → **a** (*hrasva*) and replace **Ne** by **syāṭ** residue
**s** + **y** + **ā** + **e** (ṅ dropped) so **6.1.88** sees **ā** + **e** on the
pratyaya term (then **a** + … sandhi with the *aṅga* as needed).  **Nas** /
**Nasi** keep remainder-only shaping (no **sy**-prefix in this slice).  Meta
``syat_7_3_114_agama == 'syAw'`` records the full **syāṭ**; **1.1.46** (*ṭit*
before *āgamin*) is reflected by **s**/**y** preceding the **ṅe** vowel **e**.

**ṅiti** (**7.3.111**) is read as **ṅit‑pratyayasya** (not “ṅit‑pratyaye pare”):
the locative scopes the **ṅit** pratyaya itself because this sūtra has no
ṣaṣṭhī‑sthānin for the pratyaya.

Blindness: ``cond`` reads only tags, ``upadesha_slp1``, and final varṇa letters
— no ``vibhakti`` / ``vacana``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.ngit_sup_locator import indices_last_anga_before_ngit_sup
from engine.state import State, Term
from phonology    import mk
from phonology.sarvanama_syat_7_3_114 import is_abanta_flat, ngit_sup_match
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not adhikara_in_effect("7.3.114", state, "6.4.1"):
        return False
    hit = indices_last_anga_before_ngit_sup(state)
    if hit is None:
        return False
    _ai, _pj = hit
    anga = state.terms[_ai]
    pr = state.terms[_pj]
    if "anga" not in anga.tags or "sarvanama" not in anga.tags:
        return False
    if "ghi" in anga.tags:
        return False
    if "sup" not in pr.tags:
        return False
    if not ngit_sup_match(pr.meta.get("upadesha_slp1")):
        return False
    if pr.meta.get("syat_7_3_114_done"):
        return False
    if not anga.varnas or not pr.varnas:
        return False
    flat = "".join(v.slp1 for v in anga.varnas)
    if not is_abanta_flat(flat):
        return False
    return anga.varnas[-1].slp1 == "A"


# Phonetic remainder after **ṅ** in each **ṅit** *sup* (ṅ dropped).  **Ne** alone
# carries the **syāṭ** prefix **s** + **y** + **ā** before **e** in ``act``.
_NGIT_REMAINDER_SLP1 = {"Ne": "e", "Nas": "as", "Nasi": "asi"}


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    hit = indices_last_anga_before_ngit_sup(state)
    if hit is None:
        return state
    ai, pj = hit
    anga = state.terms[ai]
    pr = state.terms[pj]
    up = pr.meta.get("upadesha_slp1")
    if not isinstance(up, str) or up not in _NGIT_REMAINDER_SLP1:
        return state
    rem = _NGIT_REMAINDER_SLP1[up]
    anga.varnas[-1] = mk("a")
    anga.meta["hrasva_7_3_114_anga"] = True
    pr.meta["syat_7_3_114_agama"] = "syAw"
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1", up)
    if up == "Ne":
        pr.varnas = [mk("s"), mk("y"), mk("A"), mk("e")]
        pr.meta["upadesha_slp1"] = "syAe"
    else:
        pr.varnas = parse_slp1_upadesha_sequence(rem)
        pr.meta["upadesha_slp1"] = rem
    pr.meta["syat_7_3_114_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.114",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sarvanAmnaH ApaH Niti supi syAw aNgasya hrasvaH ca",
    text_dev       = "सर्वनाम्नः आप ङिति सुपि स्याट् अङ्गस्य ह्रस्वश्च",
    padaccheda_dev = (
        "सर्वनाम्नः (पञ्चमी-एकवचनम्), स्याट् (प्रथमा-एकवचनम्), "
        "ह्रस्वः (प्रथमा-एकवचनम्), च (अव्ययम्)"
    ),
    why_dev        = (
        "आबन्तात् सर्वनाम्नः परे ङिति सुपि स्याट्-आगमः, अङ्गस्य च ह्रस्वः; "
        "ततः वृद्धिः (६.१.८८) इति क्रमः।"
    ),
    anuvritti_from = ("7.3.111", "7.3.113"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
