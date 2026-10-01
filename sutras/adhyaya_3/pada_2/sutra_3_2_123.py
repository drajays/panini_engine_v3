"""
3.2.123  वर्तमाने लट्  —  ADHIKARA (+ लट्-विधि)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=32123):** *vartamānādhikāraḥ* — present
stem (**laṭ**) after *vartamāne*, through **3.3.1** (type ``$33001``). Matches
v2 ``adhikara_prakarana.json`` sequence **20**.

The sūtra both opens the *vartamāne* scope and itself prescribes *laṭ*. When the
recipe arms ``laT_recipe`` (present-time *vivakṣā*), ``act`` also attaches the
*laṭ* *lac* placeholder (``la``, halantya ṭ pre-stripped) after the *dhātu* —
the sibling of 3.3.13 (*lṛṭ*) / 3.3.15 (*luṭ*). Idempotent on both counts.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 32123 · वर्तमाने लट्
              anuvṛtti: 31001: प्रत्ययः | 31002: परः च | 31091: धातोः
  Source #2 — Kāśikā 3.2.123 udāharaṇa:
                पचति, पठति
  Cross-check — Vidyut surface ✓ भवति / पचति; surface pinned by
                tests/unit/test_tinanta_bhu_bhave_all_lakaras.py, bench/run.py (laT rows)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _scope_open(state: State) -> bool:
    return any(e.get("id") == "3.2.123" for e in state.adhikara_stack)


def _needs_laT(state: State) -> bool:
    return bool(state.meta.get("laT_recipe")) and not any(
        (t.meta.get("upadesha_slp1") or "").strip() == "laT" for t in state.terms)


def cond(state: State) -> bool:
    return not _scope_open(state) or _needs_laT(state)


def act(state: State) -> State:
    if not _scope_open(state):
        state.adhikara_stack.append({
            "id"        : "3.2.123",
            "scope_end" : "3.3.1",
            "text_dev"  : 'वर्तमाने लट्',
        })
    if _needs_laT(state):
        vs = parse_slp1_upadesha_sequence("laT")
        if vs and vs[-1].slp1 == "T":
            vs = vs[:-1]
        state.terms.append(Term(
            kind="pratyaya",
            varnas=vs,
            tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
            meta={"upadesha_slp1": "laT"},
        ))
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.123",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'vartamAne law',
    text_dev       = 'वर्तमाने लट्',
    padaccheda_dev = "वर्तमाने लट्",
    why_dev        = "वर्तमाने काले धातोः लट्-लकारः; वर्तमानाधिकारः ३.२.१२३ तः ३.३.१ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.2.123", "3.3.1"),
)

register_sutra(SUTRA)
