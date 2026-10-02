"""
6.1.17  लिट्यभ्यासस्योभयेषाम्  —  VIDHI

In liṭ the *abhyāsa* of the roots that take samprasāraṇa by 6.1.15 (वच्, स्वप्, and the यजादि: यज् वप् वह् वस् वे व्ये ह्वे वद् श्वि)
takes samprasāraṇa itself, whether or not the ending is kit — so the root keeps its yaṇ before ṇal (उवाच, इयाज, सुष्वाप, उवाह)
while the abhyāsa changes. Before a kit ending the root has already changed by 6.1.15 (ऊचतुः, ईजतुः).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 6.1.17 (padaccheda: लिटि अभ्यासस्य उभयेषाम्)
  Source #2 — ashtadhyayi.com dhātu table, liṭ: वच् उवाच ऊचतुः ऊचुः · यज् इयाज ईजतुः · स्वप् सुष्वाप सुषुपतुः · वह् उवाह ऊहतुः

Engine: the abhyāsa Term (tag ``abhyasa``) directly before a root of the 6.1.15 class whose tiṅ has liṭ as its sthānin (a saṃjñā
3.4.78 stamped). The abhyāsa's yaṇ + vowel becomes the ik vowel and the following vowel is absorbed (6.1.108): va → u, ya → i, sva → su.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_STEMS = frozenset({"vac", "svap"})
# yajādi members whose own ādeśas come first and are not derived yet — वेञ् (2.4.41 वयादेश → उवाय), व्येञ्, ह्वेञ्, श्वि (the
# optional vārttika: शिश्वाय / शुशाव). They stay on the unmodified path (and out of 6.1.15 in liṭ) until those rules exist.
NOT_YET_DERIVED = frozenset({"veY", "vyeY", "hveY", "wuo~Svi"})
_SAMPRASARANA = {"y": "i", "v": "u", "r": "f", "l": "x"}
_VOWELS = frozenset("aAiIuUfFxXeEoO")


def _root_class(t) -> bool:
    stem = "".join(v.slp1 for v in t.varnas)
    if (t.meta.get("upadesha_slp1") or "").strip() in NOT_YET_DERIVED:
        return False
    return "dhatu" in t.tags and "abhyasa" not in t.tags and (
        stem in _STEMS or "यजादिः" in (t.meta.get("antarganas") or ()))


def _liT_follows(state: State, i: int) -> bool:
    return any("pratyaya" in t.tags and (t.meta.get("source_lakara_upadesha") or "").strip() == "liT"
               for t in state.terms[i + 1:])


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or t.meta.get("6_1_17_done") or not _root_class(state.terms[i + 1]):
            continue
        if not _liT_follows(state, i):
            continue
        for j in range(len(t.varnas) - 1):
            if t.varnas[j].slp1 in _SAMPRASARANA and t.varnas[j + 1].slp1 in _VOWELS:
                return t, j
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    site = _site(state)
    if site is not None:
        t, j = site
        t.varnas[j] = mk(_SAMPRASARANA[t.varnas[j].slp1])
        del t.varnas[j + 1]          # 6.1.108 samprasāraṇāc ca: the vowel after it is absorbed (pūrvarūpa)
        t.meta["6_1_17_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.17",
    sutra_type=SutraType.VIDHI,
    text_slp1="liwyaByAsasyoBayezAm",
    text_dev="लिट्यभ्यासस्योभयेषाम्",
    padaccheda_dev="लिटि अभ्यासस्य उभयेषाम्",
    why_dev="लिट् में वच्-स्वप्-यजादि धातुओं के अभ्यास को भी सम्प्रसारण (उवाच, इयाज, सुष्वाप, उवाह)।",
    anuvritti_from=("6.1.15",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
