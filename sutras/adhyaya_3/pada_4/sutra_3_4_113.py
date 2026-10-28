"""
3.4.113  तिङ्शित्सार्वधातुकम्  —  SAMJNA

*Padaccheda:* *tiṅ-śit* (prathamā = compound *pratyāhāra*), *sārvadhātukam* (nominative).

*Anuvṛtti:* *pratyayaḥ* **3.1.1**; *paraś ca* **3.1.2**; *ādyudāttaś ca* **3.1.3**; *dhātoḥ* **3.1.91** — a
*tiṅ* or *śit* *pratyaya* immediately *para* to a *dhātu* is *sārvadhātukam*.

*Engine (CONSTITUTION Art. 2):* ``cond`` only checks ``upadesha_slp1`` and *dhātu* *adjacency*; see
``sarvadhatuka_3_4_113`` for the *tiṅ* and *śit* *SLP1* *inventory*.

*Cross-refs:* **3.4.114** ( *ārdhadhātuka* *śeṣa* ), **3.4.115** / **3.4.116** ( *liṭ* / āśīr *liṅ* *ārdhadhākatva* in *tiṅ* ) —
not implemented in this sūtra’s *act* (see module docstring).
Pāṭha: ashtadhyayi.com data.txt row i=34113 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


# --- helpers of this sūtra (formerly sarvadhatuka_3_4_113.py; one sūtra, one file) ---
from typing import Final, FrozenSet, Tuple

from sutras.adhyaya_1.pada_4.sutra_1_4_104 import TIN_SURFACE_AADESHA_SLP1_EXTRA
from sutras.adhyaya_3.pada_4.sutra_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# Vikaraṇa (śit).
_SIT_VIK: Final[Tuple[str, ...]] = (
    "Sap",
    "Syan",
    "Snu",
    "SnuM",
    "Sa",
    "Snam",
    "SnA",
)
# *Kṛt* (śit) — *Sa* may coincide with vik. *upadeśa* in the *śāstra* list.
_SIT_KRT: Final[Tuple[str, ...]] = (
    "Satf",
    "SAnac",
    "SAnan",
    "cAnaS",
    "Khas",
    "KaS",
    "eS",
    "zadhyE",
    "zadhyOn",
)

SIT_VIK_SARVADHATUKA_SLP1: Final[FrozenSet[str]] = frozenset(_SIT_VIK)
SIT_KRT_SARVADHATUKA_SLP1: Final[FrozenSet[str]] = frozenset(_SIT_KRT)
SIT_SARVADHATUKA_SLP1: Final[FrozenSet[str]] = SIT_VIK_SARVADHATUKA_SLP1 | SIT_KRT_SARVADHATUKA_SLP1
# *anti* (**7.1.3** *ādeśa* for *jhi*) — *sārvadhātuka* *tiṅ*-class for narrow inventory checks.
_TIN_713_EXTRA: Final[Tuple[str, ...]] = ("anti",)
# **3.4.79** टेरे / **3.4.80** थासः से rewrite a taṅ ādeśa's upadeśa (ta → te,
# AtAm → Ate, TAs → se …); by **1.1.56** स्थानिवत् it stays sārvadhātuka. Without
# these, 1.2.4 missed Ate (no ṅit → no 7.2.81: एधिष्यआते) and 3.1.68 missed te.
TIN_3_4_79_ADESHA: Final[Tuple[str, ...]] = (
    "te", "Ate", "Je", "se", "ATe", "Dve", "e", "vahe", "mahe",
)
SARVADHATUKA_UPADESHA_SLP1: Final[FrozenSet[str]] = (
    TIN_ADESHA_SET | SIT_SARVADHATUKA_SLP1 | frozenset(_TIN_713_EXTRA)
    | frozenset(TIN_3_4_79_ADESHA) | TIN_SURFACE_AADESHA_SLP1_EXTRA
)

TIN_COUNT: Final[int] = len(TIN_ADESHA_18)
SIT_COUNT: Final[int] = len(SIT_SARVADHATUKA_SLP1)
# Union size (32 if one overlap between vik/kṛt in set theory).
SARVADHATUKA_INVENTORY_N: Final[int] = len(SARVADHATUKA_UPADESHA_SLP1)


def is_sarvadhatuka_upadesha_slp1(s: str) -> bool:
    t = s.strip()
    if t in SARVADHATUKA_UPADESHA_SLP1:
        return True
    if t.endswith("~") and t[:-1] in SARVADHATUKA_UPADESHA_SLP1:
        return True
    return False


# Sthānin lakāras whose tiṅ are sārvadhātuka (liṭ's are ārdhadhātuka by 3.4.115, āśīr-liṅ by 3.4.116).
_SARVADHATUKA_STHANIN = frozenset({"laT", "loT", "laG", "liG"})


def tin_by_sthanin(term) -> bool:
    """A tiṅ ādeśa that replaced a sārvadhātuka tiṅ (e.g. 3.4.83's ṇal for laṭ's tip) is still that tiṅ — 1.1.56."""
    return ("tin_adesha_3_4_78" in term.tags
            and (term.meta.get("source_lakara_upadesha") or "").strip() in _SARVADHATUKA_STHANIN
            and "tin_before_3_4_83" in term.meta)


def sthanin_was_pit(term) -> bool:
    """1.1.56: the ādeśa inherits the sthānin's pit-ness (ṇal for tip, thal for sip, ṇal for mip)."""
    return (term.meta.get("tin_before_3_4_83") or "").endswith(("p", "P"))




SARVADHATUKA_113 = "sarvadhatuka_3_4_113"


def _dhatu_adjacent_sarvadhatuka_untagged(state: State) -> list[Term]:
    out: list[Term] = []
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        # An āgama (āṭ, 3.4.92) belongs to the affix it precedes (1.1.46): look past it for the dhātu.
        k = i - 1
        # तिङ् is sārvadhātuka whatever stands between it and the dhātu — āgama, vikaraṇa (luṅ: dhātu + sic + tiṅ)
        while k >= 0 and ("dhatu" not in state.terms[k].tags) and (
                {"aTa_agama", "yasut_agama", "agama"} & state.terms[k].tags or state.terms[k].kind == "pratyaya"
                and "tin_adesha_3_4_78" not in state.terms[k].tags):
            k -= 1
        if k < 0 or "dhatu" not in state.terms[k].tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not (is_sarvadhatuka_upadesha_slp1(up) or tin_by_sthanin(t)):
            continue
        if SARVADHATUKA_113 in t.tags or "ardhadhatuka" in t.tags:      # already classified (3.4.116 आशिषि)
            continue
        out.append(t)
    return out


def cond(state: State) -> bool:
    return bool(_dhatu_adjacent_sarvadhatuka_untagged(state))


def act(state: State) -> State:
    pending = _dhatu_adjacent_sarvadhatuka_untagged(state)
    # Canonical registry entry (present on first AND later firings).
    state.samjna_registry["3.4.113_sarvadhatuka_slp1"] = SARVADHATUKA_UPADESHA_SLP1
    for t in pending:
        t.tags.add(SARVADHATUKA_113)
        # Per-term entry so each call visibly changes samjna_registry (R2 invariant):
        # a second firing (e.g. for vikaraṇa śap after tiṅ ādeśa was already tagged)
        # adds a different key → registry IS changed → no R2 violation.
        up = (t.meta.get("upadesha_slp1") or "").strip() or "unknown"
        state.samjna_registry[f"3.4.113_tagged_{up}"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.113",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = (
        'tiNSitsArvaDAtukam'
    ),
    text_dev       = 'तिङ्शित्सार्वधातुकम्',
    samagra_slp1   = "DAtoH paraH tiNSit-pratyayaH sArvaDAtukam",
    samagra_dev    = "धातोः परः तिङ्/शित्-प्रत्ययः सार्वधातुकम्",
    padaccheda_dev = "धातोः (३.१.९१) / परः / तिङ्-शित्-प्रत्ययः / सार्वधातुकम्",
    why_dev        = (
        "तिङ्-तथा-शित्-प्रत्ययः सार्वधातुक-संज्ञकः, आर्धधातुकानि ३.४.११४-अग्रे।"
    ),
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
