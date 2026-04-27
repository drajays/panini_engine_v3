"""
pipelines/sarvaka_subanta.py — *सर्वकः* (and parallel *viśvakaः*) *prakriyā* from **5.3.71**.

User ``सर्वकः.md`` — *sarvādi* *adanta* *sarvanāma* + *anuṣṅa* (recipe-armed) **5.3.71**
*avyayasarvanāmnām akac prāk ṭeḥ* → infix *ak* *prāk* the final *ac* (*ṭi*; **1.1.64** in *śāstra*),
*it* **1.3.3** on *c*, **1.3.9** — here materialised as a direct *a* *k* *insert* in **5.3.71** *act*), then
**4.1.2** *sup* on the *navīna* *prātipadika* (**1.2.46**), *s* → *ru* + *visarga* (same tail as *subanta* **8.2.66** / **8.3.15**).

*CONSTITUTION*: no *gold* *shortcuts*; only ``apply_rule`` + the shared *P01* *bootstrap* and
*run_subanta_sup_attach_and_finish*; *5_3_71_akac_arm* is a *meta* *arm* (like **5.3.55**), not a
*cond* read of (vibhakti, vacana) — the cell is still fixed in *recipe* as 1-1 and passed through
``build_initial_state`` into ``state.meta`` as for any *subanta*.

*Cross-check* *pāṭha* for **5.3.71** / **5.3.70** *kram*: *ashtadhyayi-com* *sutraani* / local
``data/sutrANi.tsv`` if available.
"""
from __future__ import annotations

import sutras  # noqa: F401 — register all sūtra modules

from engine import apply_rule, State
from core.canonical_pipelines import (
    P01_subanta_bootstrap,
    run_subanta_sup_attach_and_finish,
)
from pipelines.subanta import build_initial_state
from sutras.adhyaya_5.pada_3.sutra_5_3_71 import META_5_3_71_AKAC_ARM


SARVAKA_DEFAULT_STEM: str = "sarva"
SARVAKA_LIṄGA: str = "pulliṅga"


def derive_sarvakaha(
    stem_slp1: str = SARVAKA_DEFAULT_STEM,
    vibhakti: int = 1,
    vacana: int = 1,
    *,
    linga: str = SARVAKA_LIṄGA,
) -> State:
    """
    *Prathama* *eka* of *-aka* (``5.3.71`` *akac* on *sarvādi* *a*-base), e.g. *sarva* → *sarvakaḥ* / ``sarvakaH`` (SLP1).
    *Viśvaka* — same with ``stem_slp1="viSva"`` (if in *sarvādi*; **1.1.27** in *P01*).
    """
    s = build_initial_state(stem_slp1, vibhakti, vacana, linga=linga)
    s = P01_subanta_bootstrap(s)
    s = apply_rule("5.3.70", s)
    s.meta[META_5_3_71_AKAC_ARM] = True
    s = apply_rule("5.3.71", s)
    s = apply_rule("1.2.46", s)
    return run_subanta_sup_attach_and_finish(s)


__all__ = [
    "SARVAKA_DEFAULT_STEM",
    "SARVAKA_LIṄGA",
    "derive_sarvakaha",
    "META_5_3_71_AKAC_ARM",
]
