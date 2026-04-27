"""
1.1.29  न बहुव्रीहौ  —  NIYAMA

*Anuvṛtti* of *sarvanāma* from **1.1.27** (Pāṇini; *Kāśikā* *vṛtti*): the
*sarvanāma*-*saṃjñā* from *sarvādi* does **not** apply to a *śabda* in a
*bahuvrīhi* (when that structural context is present on the aṅga *Term*).

v3: after **1.1.27** has tagged a *sarvādi* stem with ``sarvanama``, this rule
*removes* that tag when ``bahuvrihi`` is among the aṅga *Term*'s *tags*.

Engine:
  * ``cond`` / ``act`` read only *tags* and ``meta`` on *Terms* — not
    ``(vibhakti, vacana)`` (*CONSTITUTION* Art. 2).
  * *śāstrīya* relation: **1.1.28** (optional *dik*-*bahuvrīhau* *sarvānāmni*)
    must be applied **after* **1.1.29** in a recipe that uses both, so the
    *dik*-*vibhāṣā* can re-apply *sarvanāma* where *śāstra* allows.  In the
    default *subanta* *P01* (``canonical_pipelines``) only **1.1.27** + **1.1.29**
    are in sequence; **1.1.28** remains opt-in per *pipeline*.

*Cross-check* *pāṭha* / row *i* = 11029, *ashtadhyayi-com* *sutraani*, or local
``sutrANi.tsv`` — do not vendor reference JSON in ``cond``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

META_1_1_29_BAHUVRHITA_STRIPPED = "1_1_29_na_bahuvrIhau_sarvanama_stripped"


def _eligible_angas(state: State):
    for t in state.terms:
        if "anga" not in t.tags or "prātipadika" not in t.tags:
            continue
        if "bahuvrihi" not in t.tags:
            continue
        if "sarvanama" not in t.tags:
            continue
        if t.meta.get(META_1_1_29_BAHUVRHITA_STRIPPED):
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible_angas(state), None) is not None


def act(state: State) -> State:
    for t in _eligible_angas(state):
        t.tags.discard("sarvanama")
        t.meta[META_1_1_29_BAHUVRHITA_STRIPPED] = True
    state.samjna_registry["1_1_29_na_bahuvrIhau"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.29",
    sutra_type     = SutraType.NIYAMA,
    r1_form_identity_exempt=True,
    text_slp1      = "na bahuvrIhO",
    text_dev       = "न बहुव्रीहौ",
    padaccheda_dev = "न / बहुव्रीहौ (सर्वनाम-संज्ञा)",
    why_dev        = "बहुव्रीहि-समासे सर्वादि-सर्वनाम-संज्ञा न (अपवादः) — अतः ७.१.१४ादयः प्रबद्धा न।",
    anuvritti_from = ("1.1.27",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["META_1_1_29_BAHUVRHITA_STRIPPED", "SUTRA"]
