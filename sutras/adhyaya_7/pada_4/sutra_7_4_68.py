"""
7.4.68  व्यथो लिटि  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=74068
- Kāśikā: "व्यथेरभ्यासस्य लिटि परतः सम्प्रसारणं भवति" — विव्यथे, विव्यथाते, विव्यथिरे; "हलादिःशेषापवादः"
- Cross-validation: tests/regression/test_findings_probe_loop.py (विव्यथे)

In liṭ the abhyāsa of the dhātu vyath takes samprasāraṇa: its yaṇ that stands before a vowel becomes the ik vowel
and the vowel is absorbed (6.1.108): vya → vi. Kāśikā calls it the apavāda of 7.4.60 halādiḥ śeṣaḥ, which would
otherwise drop the y; the first consonant v stays.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

from sutras.adhyaya_6.pada_1.sutra_6_1_17 import _SAMPRASARANA, _VOWELS, _liT_follows


def _site(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "abhyasa" not in t.tags or t.meta.get("7_4_68_done"):
            continue
        dh = state.terms[i + 1]
        if "dhatu" not in dh.tags or (dh.meta.get("upadesha_slp1") or "").strip() != "vyaTa~" or not _liT_follows(state, i):
            continue
        for j in range(len(t.varnas) - 1):
            if t.varnas[j].slp1 in _SAMPRASARANA and t.varnas[j + 1].slp1 in _VOWELS:
                return t, j
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, j = _site(state)
    t.varnas[j] = mk(_SAMPRASARANA[t.varnas[j].slp1])
    del t.varnas[j + 1]
    t.meta["7_4_68_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.68",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "vyaTo liwi",
    text_dev              = "व्यथो लिटि",
    samagra_slp1          = "aNgasya aByAsasya vyaTaH liwi samprasAraRam",
    samagra_dev           = "अङ्गस्य अभ्यासस्य व्यथः लिटि सम्प्रसारणम्",
    padaccheda_dev        = "व्यथः लिटि",
    why_dev               = "लिटि व्यथेः अभ्यासस्य सम्प्रसारणम् (विव्यथे) — हलादिःशेषापवादः।",
    anuvritti_from        = ('7.4.58',),
    apavada_of            = ("7.4.60",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
