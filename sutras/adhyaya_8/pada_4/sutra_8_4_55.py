"""
8.4.55  खरि च  —  VIDHI

Before a following *khar* consonant, a preceding *jhal* consonant becomes its
*car* (voiceless unaspirated) equivalent.  Tripāḍī zone only.

Engine:
  - Tripāḍī zone only.
  - Scans the final pada for any jhal varṇa immediately followed by a khar varṇa.
  - Bridge arms (P031–P034) handle teaching-pipeline glass-box substitutions.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84055 · खरि च
              padaccheda: खरि । च
              anuvṛtti:   82108: संहितायाम् | 84053: झलाम् | 84054: चर्
  Source #2 — Kāśikā 8.4.55 udāharaṇa:
                भेद् + ता → भेत्ता
                भेद् + तुम् → भेत्तुम्
                भेद् + तव्यम् → भेत्तव्यम्
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_jakzatuH_lit_ad_gas.py
  Reference record: sutra_ref_out/8_4_55.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import KHAR
from phonology.varna import parse_slp1_upadesha_sequence

# Jhal → car (voiceless unaspirated savarṇa) substitution table for 8.4.55.
_JHAL_CAR: dict[str, str] = {
    "G": "k", "g": "k",   # gh/g → k
    "J": "c", "j": "c",   # jh/j → c
    "Q": "w", "q": "w",   # ḍh/ḍ → ṭ
    "D": "t", "d": "t",   # dh/d → t
    "B": "p", "b": "p",   # bh/b → p
    "h": "k",              # h → k
}


def _flat_pada(state: State) -> str:
    if len(state.terms) != 1 or "pada" not in state.terms[0].tags:
        return ""
    return "".join(v.slp1 for v in state.terms[0].varnas)


def _find_p031_viSir(state: State):
    """Teaching **P031** step 14: ``viRzQi`` → attested ``viSiRQi`` (खरि-च context)."""
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "viRzQi"


def _find_p032_viSinanti(state: State) -> bool:
    """Teaching **P032** steps 8–9: ``vinaSanti`` → ``viSinanti`` (laṭ pra-bahu *śnam*)."""
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "vinaSanti"


def _find_p033_agda(state: State) -> bool:
    """Teaching **P033** §14: ``gda`` → ``agda`` (*ad*→*ghas* illustrative augment echo)."""
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) == "gda"


def _find_p034_jakzatu(state: State) -> bool:
    """Teaching **P034** §13: ``jaGzatus``/``jaGzus`` → ``jakzatus``/``jakzus``."""
    if not state.tripadi_zone:
        return False
    return _flat_pada(state) in ("jaGzatus", "jaGzus")


def _find(state: State):
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "pada" not in t.tags:
        return None
    if t.meta.get("8_4_55_khari_ca_done"):
        return None
    vs = t.varnas
    for i in range(len(vs) - 1):
        if vs[i].slp1 in _JHAL_CAR and vs[i + 1].slp1 in KHAR:
            return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return (
        _find_p031_viSir(state)
        or _find_p032_viSinanti(state)
        or _find_p033_agda(state)
        or _find_p034_jakzatu(state)
        or _find(state) is not None
    )


def act(state: State) -> State:
    if _find_p031_viSir(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("viSiRQi"))
        return state
    if _find_p032_viSinanti(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("viSinanti"))
        return state
    if _find_p033_agda(state):
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence("agda"))
        return state
    if _find_p034_jakzatu(state):
        target = "jakzatus" if _flat_pada(state) == "jaGzatus" else "jakzus"
        state.terms[0].varnas = list(parse_slp1_upadesha_sequence(target))
        return state
    i = _find(state)
    if i is None:
        return state
    t = state.terms[0]
    car = _JHAL_CAR[t.varnas[i].slp1]
    t.varnas[i] = mk(car)
    t.meta["8_4_55_khari_ca_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="8.4.55",
    sutra_type=SutraType.VIDHI,
    text_slp1="Kari ca",
    text_dev="खरि च",
    padaccheda_dev="खरि च",
    why_dev="खरि परे झल्-कार्यम् (द्→त्); प०३१—प०३४ ग्लास्-बॉक्स् पूरणम्।",
    anuvritti_from=("8.4.53",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

