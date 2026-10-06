"""
8.4.40  स्तोः श्चुना श्चुः  —  VIDHI  (Tripāḍī)

संहितायाम् a स् or a तवर्ग letter that directly follows or precedes a श् or a चवर्ग
letter becomes the matching श् / चवर्ग letter (स→श, त→च, थ→छ, द→ज, ध→झ, न→ञ):

    रामस् + शेते → रामश्शेते      भवान् + शेते → भवाञ् च् शेते (8.3.31 तुक् then त→च)
    उत् + छ → उच्छ                 राजन् + जलसि → राजञ्जलसि       यज् + न → यज्ञ
    मस्ज् → मश्ज् (→ 8.4.53 मज्ज्)

Exception **8.4.44 शात्**: a तवर्ग after श् is not changed (प्रश्न).
Ordering is Tripāḍī's own: 8.2.30 (चोः कुः), 8.2.36, 8.2.39 and 8.2.66 precede, and
this rule is asiddha for them, so ``sat+cit`` takes jaśtva (``sad``) first and only then
``saj``; 8.4.55 follows.  ṣ+t is 8.4.41, not this rule.  Scans the flattened varṇa
stream, across Terms (saṃhitā).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84040 · स्तोः श्चुना श्चुः
              padaccheda: स्तोः · श्चुना · श्चुः
              anuvṛtti:   82108: संहितायाम्
  Source #2 — Kāśikā 8.4.40 udāharaṇa:
                वृक्षश्शेते
                तच्शेते
  Cross-check — surface pinned by: tests/unit/test_dadhiccChatram_samasa.py
  Reference record: sutra_ref_out/8_4_40.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_STU_TO_SCU = {"s": "S", "t": "c", "T": "C", "d": "j", "D": "J", "n": "Y"}
_SCU = frozenset("ScCjJY")
_TAVARGA = frozenset("tTdDn")


def _find_stu(state: State):
    """First (Term, index) that ścutva applies to, or None."""
    if not state.tripadi_zone:
        return None
    flat = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for k, (t, i) in enumerate(flat):
        c = t.varnas[i].slp1
        if c not in _STU_TO_SCU:
            continue
        prev = flat[k - 1][0].varnas[flat[k - 1][1]].slp1 if k else ""
        nxt = flat[k + 1][0].varnas[flat[k + 1][1]].slp1 if k + 1 < len(flat) else ""
        if prev == "S" and c in _TAVARGA:   # 8.4.44 शात्
            continue
        if nxt in _SCU or prev in _SCU:
            return t, i
    return None


def cond(state: State) -> bool:
    return _find_stu(state) is not None


def act(state: State) -> State:
    changes = []
    while (hit := _find_stu(state)) is not None:
        t, i = hit
        old = t.varnas[i].slp1
        t.varnas[i] = mk(_STU_TO_SCU[old])
        changes.append(f"{old}→{_STU_TO_SCU[old]}")
    if changes:
        state.meta["__why_now_dev__"] = (
            f"श्/चवर्गयोगे स्/तवर्गः श्चुः ({', '.join(changes)}); "
            "यथा रामस्+शेते → रामश्शेते, यज्+न → यज्ञ; शात् परस्य तवर्गे न (८.४.४४)। (८.४.४०)"
        )
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.40",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'stoH ScunA ScuH',
    text_dev       = 'स्तोः श्चुना श्चुः',
    samagra_slp1   = "stoH ScunA ScuH",
    samagra_dev    = "स्तोः श्चुना श्चुः",
    padaccheda_dev = "स्तोः / श्चुना / श्चुः",
    why_dev        = "श्/चवर्गयोगे संहितायां स्/तवर्गस्य श्/चवर्गादेशः; शात् परस्य तवर्गे न।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

