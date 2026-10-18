"""
7.2.114  मृजेर्वृद्धिः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=72114
- Kāśikā: "मृजेरिको वृद्धिर्भवति" — मार्ष्टा, मार्ष्टुम्, मार्ष्टव्यम्; "गुणप्रसङ्गे वृद्धिः" — not before kit/ṅit: मृष्टः, मृष्टवान्
- Cross-validation: tests/regression/test_findings_probe_loop.py (मार्ष्टि)

Where guṇa (7.3.84) would apply to the dhātu mṛj — before a sārvadhātuka or ārdhadhātuka pratyaya that is not
kit/ṅit (an āgama such as iṭ belongs to the pratyaya after it) — its ṛ takes vṛddhi instead: ṛ → ā, and 1.1.51
uraṇ raparaḥ adds r (mārj). Apavāda of 7.3.84. The vārttika's optional vṛddhi before a vowel-initial kṅit
(mārjanti beside mṛjanti) is not modelled.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_1.pada_1.sutra_1_1_4 import ik_guna_vriddhi_blocked_by_1_1_4

_MRJ = frozenset({"mfjU~", "mfjU~z", "mfj", "mFjU~z"})     # mFjU~z: the legacy recipe spelling (pipelines/mArzwi_lat_mFj.py)


def _find(state: State):
    if ik_guna_vriddhi_blocked_by_1_1_4(state):
        return None
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or "abhyasa" in dh.tags or dh.meta.get("7_2_114_mrje_vrddhi_done"):
            continue
        if (dh.meta.get("upadesha_slp1") or "").strip() not in _MRJ and "".join(v.slp1 for v in dh.varnas) != "mfj":
            continue
        head = next((u for u in state.terms[i + 1:] if u.varnas and "agama" not in u.tags), None)
        if head is None or "kngiti" in head.tags or head.meta.get("is_apit"):
            continue
        if not ("ardhadhatuka" in head.tags or any(t.startswith("sarvadhatuka") for t in head.tags)):
            continue
        j = next((j for j, v in enumerate(dh.varnas) if v.slp1 in ("f", "F")), None)
        if j is not None:
            return i, j
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    ti, j = _find(state)
    dh = state.terms[ti]
    dh.varnas[j] = mk("A")
    dh.meta["urN_rapara_pending"] = "r"
    dh.meta["urN_rapara_after_index"] = j
    dh.meta["7_2_114_mrje_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.114",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'mfjervfdDiH',
    text_dev       = 'मृजेर्वृद्धिः',
    samagra_slp1   = "mfjeH aNgasya vfdDiH",
    samagra_dev    = "मृजेः अङ्गस्य वृद्धिः",
    padaccheda_dev = "मृजेः / वृद्धिः",
    why_dev        = "मृजेः इकः गुणप्रसङ्गे वृद्धिः (मार्ष्टि, मार्ष्टा); क्ङिति न (मृष्टः)।",
    anuvritti_from = ("1.1.1", "1.1.3", "1.1.50", "1.1.51"),
    apavada_of     = ("7.3.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
