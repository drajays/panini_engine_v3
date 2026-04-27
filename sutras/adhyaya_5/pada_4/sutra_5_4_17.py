"""
5.4.17  सङ्ख्यायाः क्रियाभ्यावृत्तिगणने कृत्वसुच्  —  VIDHI (narrow *corpus*)

**Pāṭha (ashtadhyayi-com ``data.txt`` *i*≈54017):** *kṛtvasuṭ* after a *saṅkhyā*-class
*prātipadika* when counting repetitions of an action.

v3 *glass-box*: ``state.meta['5_4_17_kftvasuT_arm']``; exactly one *prātipadika* *Term*;
``upadesha_slp1`` (or flat) must satisfy ``pratipadika_slp1_in_sankhya_samjna`` after **1.1.23**;
appends *kṛtvasuṭ* *taddhita* (``kftvasT`` *upadeśa* — ``T`` *it* for *ṭ*); pops the arm.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_23 import pratipadika_slp1_in_sankhya_samjna


def _stem_key(t: Term) -> str:
    u = (t.meta.get("upadesha_slp1") or "").strip()
    if u:
        return u
    return "".join(v.slp1 for v in t.varnas)


def _site(state: State) -> int | None:
    if not state.meta.get("5_4_17_kftvasuT_arm"):
        return None
    if len(state.terms) != 1:
        return None
    t0 = state.terms[0]
    if "prātipadika" not in t0.tags:
        return None
    if any("taddhita" in t.tags for t in state.terms):
        return None
    sk = _stem_key(t0)
    if not sk or not pratipadika_slp1_in_sankhya_samjna(state, sk):
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    p = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("kftvasT"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "kftvasT"},
    )
    state.terms.append(p)
    state.meta.pop("5_4_17_kftvasuT_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="5.4.17",
    sutra_type=SutraType.VIDHI,
    text_slp1="saMkhyAyAH kriyAByAvfttigaRane kftvasuC",
    text_dev="सङ्ख्यायाः क्रियाभ्यावृत्तिगणने कृत्वसुच्",
    padaccheda_dev="सङ्ख्यायाः / क्रियाभ्यावृत्तिगणने / कृत्वसुच्",
    why_dev="संख्यावाचिनः क्रियावृत्तौ गणने कृत्वसुट्-प्रत्ययः (आर्म्ड-मेटा)।",
    anuvritti_from=("5.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
