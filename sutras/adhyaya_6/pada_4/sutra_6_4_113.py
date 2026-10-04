"""
6.4.113  ई हल्यघोः  —  VIDHI (narrow: corrected-v2 **P009** *śnā* residue)

*Śāstra (laghu):* long **ī** replaces **ā** of an *aghu* *aṅga* before a following
*hal*‑initial affix — modelled here for **SnA** → **nā** before **ta**.

Engine:
  • ``corrected_v2_P009_6_4_113_arm`` (**P009**),
  • ``corrected_v2_P012_6_4_113_arm`` (**P012**) —
``n`` + ``A`` + following ``ta`` → ``n`` + ``I``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_META_P009 = "corrected_v2_P009_6_4_113_arm"
_META_P012 = "corrected_v2_P012_6_4_113_arm"


def _hit(state: State) -> tuple[int, int] | None:
    """Return (term_idx, vowel_idx) of ``A`` in ``…n A`` before ``ta``."""
    for i, t in enumerate(state.terms[:-1]):
        vs = t.varnas
        if len(vs) != 2:
            continue
        if vs[0].slp1 != "n" or vs[1].slp1 != "A":
            continue
        if "SnA_vikaraṇa" not in t.tags:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is None:
            continue
        if nxt.varnas[0].slp1 == "t" and "kngiti" not in nxt.tags and not nxt.meta.get("is_apit"):
            if (nxt.meta.get("upadesha_slp1") or "").strip() == "ta":
                return (i, 1)                       # legacy P009 (परिक्रीणीते)
        # ई हल्यघोः: before a hal-initial kṅit (weak) sārvadhātuka — क्रीणीतः, क्रीणीहि
        weak = "kngiti" in nxt.tags or nxt.meta.get("is_apit")
        # jh (झि/झ) is vowel-initial once 7.1.3 झोऽन्तः applies — 6.4.112's case
        jh = (nxt.meta.get("upadesha_slp1") or "").strip() in {"jhi", "Ji", "Ja", "jha"}
        if weak and not jh and nxt.varnas[0].slp1 not in "aAiIuUfFxXeEoO":
            return (i, 1)
    return None


def _hit_abhyasta(state: State) -> int | None:
    """ई हल्यघोः for an abhyasta root in ā that is not ghu (hā: jahITaH): before a hal-initial kṅit."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas or t.varnas[-1].slp1 != "A":
            continue
        if t.meta.get("6_4_113_I_done") or not any("abhyasa" in u.tags for u in state.terms):
            continue
        if "".join(v.slp1 for v in t.varnas) in {"dA", "DA"}:          # aghoḥ
            continue
        nxt = state.terms[i + 1]
        if ("kngiti" in nxt.tags or nxt.meta.get("is_apit")) and nxt.varnas and nxt.varnas[0].slp1 not in "aAiIuUfFxXeEoO" \
                and (nxt.meta.get("upadesha_slp1") or "").strip() not in {"jhi", "Ji", "Ja", "jha"}:
            return i
    return None


def cond(state: State) -> bool:
    return _hit(state) is not None or _hit_abhyasta(state) is not None


def act(state: State) -> State:
    h = _hit(state)
    if h is None:
        j = _hit_abhyasta(state)
        if j is not None:
            state.terms[j].varnas[-1] = mk("I")
            state.terms[j].meta["6_4_113_I_done"] = True
        return state
    ti, vi = h
    state.terms[ti].varnas[vi] = mk("I")
    state.samjna_registry["6.4.113_snA_nA_to_nI"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.113",
    sutra_type=SutraType.VIDHI,
    text_slp1='I halyaGoH',
    text_dev='ई हल्यघोः',
    padaccheda_dev="ई / हलि / अघोः",
    why_dev="अघोः अङ्गस्य हलि परे आत् ईत्वम् — प००९ / प०१२ *श्ना*-शेषः।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
