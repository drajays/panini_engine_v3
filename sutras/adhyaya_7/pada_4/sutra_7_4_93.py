"""
7.4.93  सन्वल्लघुनि चङ्परेऽनग्लोपे  —  VIDHI (narrow: P037 *caṅ*-pare *abhyāsa*)

Teaching **P037** step 13: before the non-geminate *caṅ* context, the *laghu*
*abhyāsa* for *aṭ* is shaped like the *san* pattern — here modelled as initial
``a`` → ``i`` on the *abhyāsa* copy **aw** (``A`` → ``a`` already via **7.4.59**).

Narrow: ``state.meta['P037_7_4_93_sanvat_arm']`` + first ``abhyasa`` ``Term``
with varṇas ``a`` + ``w`` (*aṭ* segment) → ``i`` + ``w``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 74093 · सन्वल्लघुनि चङ्परेऽनग्लोपे
              padaccheda: सन्-वत् लघुनि चङ्‍-परे अन्-अक्-लोपे
              anuvṛtti:   64001: अङ्गस्य | 74058: अभ्यासस्य
  Source #2 — Kāśikā 7.4.93 udāharaṇa:
                इत्युक्तम्
                अचीकरत्
                अपीपचत्
  Cross-check — surface pinned by: tests/unit/test_AwIwat_luN_aT_Nic_caN_tip.py
  Reference record: sutra_ref_out/7_4_93.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _abhyasa_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "abhyasa" in t.tags:
            return i
    return None


def _site(state: State) -> bool:
    i = _abhyasa_index(state)
    if i is None:
        return False
    t = state.terms[i]
    if t.meta.get("P037_7_4_93_done"):
        return False
    if len(t.varnas) != 2:
        return False
    return t.varnas[0].slp1 == "a" and t.varnas[1].slp1 == "w"


_AC = frozenset("aAiIuUfFxXeEoO")
_HRASVA = frozenset("aiufx")


def _general(state: State):
    """सन्वल्लघुनि चङ्परेऽनग्लोपे: before a caṅ-para ṇi whose aṅga is laghu (and lost
    no ak), the abhyāsa is treated as before san (7.4.79, 7.4.94): अचूचुरत्."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "caG" for t in state.terms):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or t.meta.get("sanvat"):
            continue
        dh = state.terms[i + 1]
        if not (dh.meta.get("nijanta") or dh.meta.get("ni_lopa_done")) or dh.meta.get("aglopa"):
            return None
        vs = dh.varnas
        j = next((k for k, v in enumerate(vs) if v.slp1 in _AC), None)
        if j is None or vs[j].slp1 not in _HRASVA:
            return None
        if j + 2 < len(vs) and vs[j + 1].slp1 not in _AC and vs[j + 2].slp1 not in _AC:
            return None                                   # guru: followed by a conjunct
        return t
    return None

def cond(state: State) -> bool:
    if _general(state) is not None:
        return True
    return _site(state)


def act(state: State) -> State:
    g = _general(state)
    if g is not None:
        g.meta["sanvat"] = True
        return state
    if not _site(state):
        return state
    i = _abhyasa_index(state)
    assert i is not None
    t = state.terms[i]
    t.varnas[0] = mk("i")
    t.meta["P037_7_4_93_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.93",
    sutra_type=SutraType.ATIDESHA,
    r1_form_identity_exempt=True,         # atideśa: 7.4.79/7.4.94 change the form
    text_slp1='sanvallaGuni caNparenaglope',
    text_dev='सन्वल्लघुनि चङ्परेऽनग्लोपे',
    padaccheda_dev="सनिवत् लघुनि चङ्परि",
    why_dev="चङ्परे अभ्यास-laghu-संस्कारः (प०३७ *aṭ*: ``aw``→``iw``)।",
    anuvritti_from=("7.4.92",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
