"""
8.4.54  अभ्यासे चर्च  —  VIDHI

In the abhyāsa (reduplicant), the initial jhal consonant becomes its carc
(unaspirated / palatal-shift) equivalent:
  - Voiced aspirates (jhaṣ) → voiced unaspirated (jaś): bh→b, dh→d, gh→j, jh→j
  - Velar unvoiced → palatal unvoiced: k→c, kh→c
  - Velar voiced → palatal voiced: g→j, gh→j

Engine:
  - applies to the first varṇa of an `abhyasa` term (after 7.4.60 trim), or —
    once the pada is merged — to the first consonant of the ``abhyasa_v`` run.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84054 · अभ्यासे चर्च्च
              padaccheda: अभ्यासे चर् च
              anuvṛtti:   82108: संहितायाम् | 84053: झलाम् जश्
  Source #2 — Kāśikā 8.4.54 udāharaṇa:
                चिखनिषति
                चिच्छित्सति
                टिठकारयिषति
  Cross-check — surface pinned by: tests/unit/test_kf_lit_karmani_bhave.py, tests/unit/test_kf_lit_kartari.py, tests/unit/test_vibhidatuH_lit.py
  Reference record: sutra_ref_out/8_4_54.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


_JHAS_TO_JAS = {
    # Velar → palatal (kavar → cavar)
    "k": "c",  # kṛ → cakṛ (cakāra)
    "K": "c",  # kha-initial → ca (rare, e.g. khyā)
    "g": "j",  # gam → jagāma
    "G": "j",  # gha → ja
    # Voiced aspirates → voiced unaspirated (jhaṣ → jaś)
    "B": "b",  # bhū → babhūva
    "D": "d",  # dhāv → dadhāva; dhṛ → dadhre
    "G": "j",  # gh → j (above handles this too)
    "J": "j",  # jha → ja (rare)
    "Q": "q",  # ḍha → ḍa (डुढौके)
    # चर् for the voiceless aspirates: छ → च (चखाद, after 7.4.62), फ → प
    # (पुस्फूर्ज), ठ → ट, थ → त
    "C": "c", "P": "p", "W": "w", "T": "t",
}


def _find(state: State):
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("8_4_54_carc_done"):
            continue
        if not t.varnas:
            continue
        ch = t.varnas[0].slp1
        rep = _JHAS_TO_JAS.get(ch)
        if rep is None:
            continue
        return ti, rep
    return None


_AC = frozenset("aAiIuUfFxXeEoO")


def _find_merged(state: State):
    """After the pada merge the abhyāsa survives only as ``abhyasa_v`` varṇas
    (अभभक्षत् ← caṅ): its first consonant, before any root varṇa."""
    for t in state.terms:
        if "abhyasa" in t.tags:
            continue
        run = [i for i, v in enumerate(t.varnas) if "abhyasa_v" in v.tags]
        if not run or any(tg in t.varnas[i].tags for i in run for tg in ("carc_done", "bhas_8_2_38")):
            continue
        i = next((i for i in run if t.varnas[i].slp1 not in _AC), None)
        if i is not None and t.varnas[i].slp1 in _JHAS_TO_JAS:
            return t, i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _find_merged(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is not None:
        ti, rep = hit
        state.terms[ti].varnas[0] = mk(rep)
        state.terms[ti].meta["8_4_54_carc_done"] = True
        return state
    m = _find_merged(state)
    if m is not None:
        t, i = m
        old = t.varnas[i]
        t.varnas[i] = mk(_JHAS_TO_JAS[old.slp1], *(old.tags - {"mula_dhatu_v"}), "carc_done")
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.54",
    sutra_type=SutraType.VIDHI,
    text_slp1='aByAse carca',
    text_dev='अभ्यासे चर्च',
    padaccheda_dev="अभ्यासे / चर्च",
    why_dev="अभ्यास-स्थिते झश्-वर्णस्य जश्-आदेशः (भि→बि) — विभिदतुः।",
    anuvritti_from=("8.4.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

