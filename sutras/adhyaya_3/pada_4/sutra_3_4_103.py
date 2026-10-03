"""
3.4.103  यासुट् परस्मैपदेषूदात्तो ङिच्च  —  VIDHI

Two operational paths:
  1. Arm ``3_4_103_arm``: legacy gate-setter (krt_kind = 3.4.103).
  2. Arm ``yasut_recipe``: vidhi-liṅ — insert the *yāsuṭ* augment
     Term ``[y, A, s]`` (pre-processed: u~ and T already conceptually removed)
     immediately before the rightmost tiṅ ādeśa Term.

The yāsuṭ Term is tagged ``yasut_agama`` (not ``upadesha``) so that 1.3.3 does
not mis-mark its 's' as halantyam-it before 7.2.79 drops it.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34103 · यासुट् परस्मैपदेषूदात्तो ङिच्च
              padaccheda: यासुट् परस्मैपदेषु उदात्तः ङित् च
              anuvṛtti:   34102: लिङः
  Source #2 — Kāśikā 3.4.103 udāharaṇa:
                सीयुटोऽपवादः
                कुर्यात्
                अचिनवम्
  Cross-check — surface pinned by: tests/unit/test_tinanta_ad_lig_kartari.py, tests/unit/test_tinanta_bhavet_ling.py
  Reference record: sutra_ref_out/3_4_103.json
"""
from __future__ import annotations

from engine                import SutraType, SutraRecord, register_sutra
from engine.krt_eligibility import tin_pratyaya_gate_eligible
from engine.state          import State, Term
from phonology             import mk

_GATE_KEY: str = "3_4_103_yAsuw_103"


def _find_tin_index(state: State) -> int | None:
    """Return index of the rightmost tiṅ ādeśa pratyaya after dhātu."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" in t.tags:
            return i
    return None


def _structural_site(state: State) -> int | None:
    """liṅ's parasmaipada tiṅ ādeśa that has not yet received the yāsuṭ (the lakāra is read from the
    affix's own provenance, not from the derivation)."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags or "parasmaipada" not in t.tags:
            continue
        if (t.meta.get("source_lakara_upadesha") or "").strip() != "liG":
            continue
        if t.meta.get("3_4_103_yasut_done") or "ashir_liG" in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if _structural_site(state) is not None:
        return True
    return tin_pratyaya_gate_eligible(state, "3.4.103", gate_key=_GATE_KEY)


def _insert_yasut(state: State, idx: int) -> None:
    # yāsuṭ upadeśa = y+ā+s+u~+ṭ; the u~ and ṭ (it) are taken as already gone, so the augment stands as [y, ā, s]
    # and carries ``yasut_agama`` (not ``upadesha``) lest 1.3.3 read its s as an it before 7.2.79 drops it.
    state.terms.insert(idx, Term(
        kind="pratyaya",
        varnas=[mk("y"), mk("A"), mk("s")],
        tags={"pratyaya", "yasut_agama", "kngiti"},
        meta={"upadesha_slp1": "yAsuT", "yasut_agama": True},
    ))
    state.terms[idx + 1].meta["3_4_103_yasut_done"] = True
    state.samjna_registry["3.4.103_yasut_inserted"] = True
    state.meta["__why_now_dev__"] = (
        "विधि-लिङः परस्मैपद-तिङः पूर्वं यासुट्-आगमः (उदात्तः ङित् च) — सीयुटोऽपवादः; "
        "भव + ति → भव + यास् + त् (भवेत्)। (३.४.१०३)"
    )


def act(state: State) -> State:
    idx = _structural_site(state)
    if idx is not None:
        _insert_yasut(state, idx)
        return state
    if state.meta.get("yasut_recipe") and not state.meta.get("3_4_103_yasut_done"):
        idx = _find_tin_index(state)
        if idx is None:
            return state
        _insert_yasut(state, idx)
        state.meta["3_4_103_yasut_done"] = True
        state.meta.pop("yasut_recipe", None)
        return state
    # Legacy gate path
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yAsuw parasmEpadezUdAtto Nicca",
    text_dev              = "यासुट् परस्मैपदेषूदात्तो ङिच्च",
    padaccheda_dev        = "यासुट् परस्मैपदेषु उदात्तः ङित् च",
    why_dev               = (
        "विधि-लिङि परस्मैपदे धातोः परे यासुट्-आगमः; "
        "उदात्तः ङिच्च — अनुदात्त-ङित्-संज्ञा।"
    ),
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
