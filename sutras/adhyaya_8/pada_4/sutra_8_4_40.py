"""
8.4.40  —  VIDHI (narrow; two engineering slices on one index)

(A) Canonical Pāṇini **8.4.40** *stoḥ ścunā ścuḥ* (recipe arm
    ``meta['8_4_40_sto_tCh_arm']``): ``t`` + ``C`` (= ``छ``) → ``c`` after **8.2.1**;

(B) Older glass-box shard modelled elsewhere as ṭuṇā (``z``+``t`` → ``z``+``w``)
    for ``mArzwi``, etc.—unchanged behaviour.

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


def _find_zt(state: State):
    """
    *Tripāḍī* zone **or** ``state.meta["8_4_40_pre_tripadi_arm"]`` (e.g. *mṛṣ*+*t*
    before **8.2.1**) so *ṣ*+*t* → *ṣ*+*ṭ* does not trip the non–8.x *asiddha* gate.
    """
    if not (state.tripadi_zone or state.meta.get("8_4_40_pre_tripadi_arm")):
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("8_4_40_zw_done"):
        return None
    for i in range(1, len(t.varnas)):
        if t.varnas[i - 1].slp1 == "z" and t.varnas[i].slp1 == "t":
            return (0, i)
    return None


_STU_TO_SCU = {"s": "S", "t": "c", "T": "C", "d": "j", "D": "J", "n": "Y"}
_SCU = frozenset("ScCjJY")


def _find_stu(state: State):
    """
    स्तोः श्चुना श्चुः — a स्/तवर्ग letter next to a श्/चवर्ग letter (either
    side) becomes the matching श्/चवर्ग letter: षस्ज् → सश्ज् (→ 8.4.53 सज्ज्),
    उत्+छ → उच्छ, राज्+ना → राज्ञा. **8.4.44 शात्**: not a तवर्ग after श् (प्रश्नः).
    Scans the whole tape in order, across term boundaries (saṃhitā).
    """
    if not (state.tripadi_zone or state.meta.get("8_4_40_pre_tripadi_arm")):
        return None
    flat = [(t, i) for t in state.terms for i in range(len(t.varnas))]
    for k, (t, i) in enumerate(flat):
        c = t.varnas[i].slp1
        if c not in _STU_TO_SCU:
            continue
        prev = flat[k - 1][0].varnas[flat[k - 1][1]].slp1 if k else ""
        nxt = flat[k + 1][0].varnas[flat[k + 1][1]].slp1 if k + 1 < len(flat) else ""
        if nxt in _SCU or (prev in _SCU and not (prev == "S" and c != "s")):
            return t, i
    return None


def cond(state: State) -> bool:
    return _find_zt(state) is not None or _find_stu(state) is not None


def act(state: State) -> State:
    hit = _find_zt(state)
    if hit is not None:
        ti, i = hit
        state.terms[ti].varnas[i] = mk("w")
        state.terms[ti].meta["8_4_40_zw_done"] = True
        return state
    while (hit := _find_stu(state)) is not None:
        t, i = hit
        t.varnas[i] = mk(_STU_TO_SCU[t.varnas[i].slp1])
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.40",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'stoH ScunA ScuH',
    text_dev       = 'स्तोः श्चुना श्चुः',
    padaccheda_dev = "स्तोः / श्चुना / श्चुः",
    why_dev        = "चवर्गे परे स्तोः श्चुनेन श्चुः (डेमो: दधि+छत्रम्); ष्टुणा-शाखा पुरातन-मार्ज्वि-मार्गे।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

