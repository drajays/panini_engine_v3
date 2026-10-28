"""
1.4.104  विभक्तिश्च  —  SAMJNA

*Padaccheda:* *supaḥ* (ṣaṣṭhī), *tiṅ* ( *pratyāhāra* ), *ca* ( *avyaya* ), *vibhaktiḥ* ( *prathamā-ekavacanam* ).

*Anuvṛtti:* *tiṅaḥ trīṇi trīṇi* **1.4.101** ( *tiṅ* ); **1.4.103** ( *sup* triples — *śāstra* ); **1.4.1** *ekasañjñā*.

*Śāstra:* *sup* *pratyaya* and *tiṅ* *pratyaya* receive the name *vibhakti* (seven *sup* triples, six *tiṅ* triples
in fixed order).

*Engine:* tags ``samjna_1_4_104_vibhakti`` on qualifying *pratyaya* ``Term``s; *registry* documents triple groupings
(R2).  *cond* is blind to ``vibhakti_vacana`` *meta* (Art. 2).
Pāṭha: ashtadhyayi.com data.txt row i=14104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


# --- helpers of this sūtra (formerly vibhakti_samjna_1_4_104.py; one sūtra, one file) ---
from typing import Final, Tuple

from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from engine.state import State, Term

from sutras.adhyaya_3.pada_4.sutra_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# One *Term* tag: *sup* / *tiṅ* *ādeśa* both receive the same *sañjñā* name in *śāstra*.
TAG_1_4_104_VIBHAKTI: Final[str] = "samjna_1_4_104_vibhakti"

# Seven triples = *sup* *upadeśa* SLP1 strings (``data/inputs/sup_upadesha.json``, *vibhakti* 1–7 × *vacana*).
SUP_VIBHAKTI_TRIPLES_SLP1: Final[Tuple[Tuple[str, str, str], ...]] = (
    ("s~", "O", "jas"),
    ("am", "Ow", "Sas"),
    ("wA", "ByAm", "Bis"),
    ("Ne", "ByAm", "Byas"),
    ("Nasi", "ByAm", "Byas"),
    ("Nas", "os", "Am"),
    ("Ni", "os", "sup"),
)

SUP_VIBHAKTI_UPADESHA_SLP1: Final[frozenset[str]] = frozenset(
    p for triple in SUP_VIBHAKTI_TRIPLES_SLP1 for p in triple
)

# Six triples of *tiṅ* *ādeśa* in **3.4.78** order.
TIN_VIBHAKTI_TRIPLES_SLP1: Final[Tuple[Tuple[str, str, str], ...]] = tuple(
    tuple(TIN_ADESHA_18[i : i + 3]) for i in range(0, len(TIN_ADESHA_18), 3)
)


def _norm_upadesha_slp1(s: str) -> str:
    t = s.strip()
    if t in TIN_ADESHA_SET or t in SUP_VIBHAKTI_UPADESHA_SLP1:
        return t
    if t.endswith("~"):
        u = t[:-1]
        if u in TIN_ADESHA_SET or u in SUP_VIBHAKTI_UPADESHA_SLP1:
            return u
    return t


def is_sup_vibhakti_pratyaya(t: Term) -> bool:
    """``Term`` tagged ``sup`` by **4.1.2** (or compatible loaders)."""
    if t.kind != "pratyaya" or "sup" not in t.tags:
        return False
    # **2.4.71** *luk* leaves a zero-width *sup* ghost — not a *vibhakti* bearer.
    return LUK_LOPA_GHOST_TAG not in t.tags


# **3.4.101** *tas* → **tām** in *laṅ* / *lit* … — surface *tiṅ* not in ``TIN_ADESHA_18``.
TIN_SURFACE_AADESHA_SLP1_EXTRA: Final[frozenset[str]] = frozenset({"tAm", "hi", "Qi", "ran"})


def is_tin_vibhakti_pratyaya(t: Term) -> bool:
    """*Tiṅ* *ādeśa* replacers of *lac* only (**3.4.78**), not *śap* / *śyan* / *lakāra* *upadeśa*."""
    if t.kind != "pratyaya":
        return False
    up = _norm_upadesha_slp1(t.meta.get("upadesha_slp1") or "")
    if up in TIN_ADESHA_SET:
        return True
    if up in TIN_SURFACE_AADESHA_SLP1_EXTRA and "tin_adesha_3_4_78" in t.tags:
        return True
    # **3.4.82** liṭ-parasmaipada ādeśas: atus/us/aTus/a/va/ma/Ral/Tal are vibhakti.
    # The meta flag 'lit_tin_adesha' marks these as tiṅ-vibhakti so 1.3.4 protection
    # (na vibhaktau tusmāḥ) applies to the tusma-final 's' in atus/us/aTus.
    return bool(t.meta.get("3_4_82_done"))


def term_has_1_4_104_vibhakti(t: Term) -> bool:
    return TAG_1_4_104_VIBHAKTI in t.tags


def terms_needing_1_4_104_vibhakti(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if term_has_1_4_104_vibhakti(t):
            continue
        if is_sup_vibhakti_pratyaya(t) or is_tin_vibhakti_pratyaya(t):
            out.append(t)
    return out




def cond(state: State) -> bool:
    return bool(terms_needing_1_4_104_vibhakti(state))


def _apply_104(t: Term) -> None:
    t.tags.add(TAG_1_4_104_VIBHAKTI)


def act(state: State) -> State:
    pending = terms_needing_1_4_104_vibhakti(state)
    state.samjna_registry["1.4.104_sup_vibhakti_triples_slp1"] = SUP_VIBHAKTI_TRIPLES_SLP1
    state.samjna_registry["1.4.104_tin_vibhakti_triples_slp1"] = TIN_VIBHAKTI_TRIPLES_SLP1
    # Monotonic stamp so a second pass (new *tiṅ* / *sup* ``Term``s) still satisfies R2 — same pattern
    # issue as **1.4.101** when static registry values are re-written.
    state.samjna_registry["1.4.104_apply_stamp"] = (
        int(state.samjna_registry.get("1.4.104_apply_stamp", 0)) + 1
    )
    for t in pending:
        _apply_104(t)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.104",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'viBaktiSca',
    text_dev       = 'विभक्तिश्च',
    samagra_slp1   = "supaH tiNaH viBaktiH ca",
    samagra_dev    = "सुपः तिङः विभक्तिः च",
    padaccheda_dev = "सुपः / तिङ् / च / विभक्तिः",
    why_dev        = (
        "सुप्-तिङ्-प्रत्ययानां विभक्ति-संज्ञा; सुप्-सप्त-त्रिकाः, तिङ्-षट्-त्रिकाः (३.४.७८)।"
    ),
    anuvritti_from = ("1.4.1", "1.4.101", "1.4.103"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
