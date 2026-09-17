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


def _find_sto_t_ch(state: State):
    """t+C (→c) in tripadi. t immediately before C is a structural signal."""
    if not (state.tripadi_zone or state.meta.get("8_4_40_pre_tripadi_arm")):
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("8_4_40_sto_done"):
        return None
    for i in range(len(t.varnas) - 1):
        if t.varnas[i].slp1 == "t" and t.varnas[i + 1].slp1 == "C":
            return i
    return None


def _find_j_n(state: State):
    """
    j immediately before n → n becomes Y (ñ), e.g. rAjan-derived rAj+n+A
    → rAjYA (राज्ञा). श्चुना श्चुः reads either member adjacent to a श्चु
    letter, so a दन्त्य *after* ज् (a श्चु letter) palatalises the same as
    one *before* it (8.4.40's own udāharaṇa pair, वृक्षश्शेते/तच्शेते, is
    the दन्त्य-before-श्चु direction; राज्ञा is the reverse).
    """
    if not (state.tripadi_zone or state.meta.get("8_4_40_pre_tripadi_arm")):
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("8_4_40_jn_done"):
        return None
    for i in range(len(t.varnas) - 1):
        if t.varnas[i].slp1 == "j" and t.varnas[i + 1].slp1 == "n":
            return i + 1
    return None


def cond(state: State) -> bool:
    return (
        _find_zt(state) is not None
        or _find_sto_t_ch(state) is not None
        or _find_j_n(state) is not None
    )


def act(state: State) -> State:
    hit = _find_zt(state)
    if hit is not None:
        ti, i = hit
        state.terms[ti].varnas[i] = mk("w")
        state.terms[ti].meta["8_4_40_zw_done"] = True
        return state
    idx = _find_sto_t_ch(state)
    if idx is not None:
        t0 = state.terms[0]
        t0.varnas[idx] = mk("c")
        t0.meta["8_4_40_sto_done"] = True
        return state
    idx = _find_j_n(state)
    if idx is None:
        return state
    t0 = state.terms[0]
    t0.varnas[idx] = mk("Y")
    t0.meta["8_4_40_jn_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.40",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "stoH ScunA ScuH // zwunA zwuH (engine shard)",
    text_dev       = "स्तोः श्चुना श्चुः",
    padaccheda_dev = "स्तोः / श्चुना / श्चुः",
    why_dev        = "चवर्गे परे स्तोः श्चुनेन श्चुः (डेमो: दधि+छत्रम्); ष्टुणा-शाखा पुरातन-मार्ज्वि-मार्गे।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

