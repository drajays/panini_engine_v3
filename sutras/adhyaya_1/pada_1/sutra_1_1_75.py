"""
1.1.75  एङ् प्राचां देशे  (eN prAcAm deSe)  —  SAMJNA

Classical role:
  "EṄ (e, o) [is treated as pragṛhya] in the region/dialect of the
  Prācyas (eastern grammarians/dialect)."

  In the eastern dialectal tradition (prācya-deśa), the vowels e and o
  (eṄ = the pratyāhāra of 1.1.71, covering e and o) at the end of certain
  stem forms are treated as pragṛhya (1.1.11–14): i.e., they do not
  undergo sandhi / coalescence with a following vowel.

  More technically: in the prācya tradition, a dual-ending -e or -o (e.g.,
  vṛkṣe, vṛkṣo as dual forms in certain Vedic/prācya usage) is not
  subject to sandhi rules that would normally apply.

  This rule registers the set {e, o} (SLP1) under the key
  "1_1_75_eN_prAcAm" in samjna_registry, making it available for
  downstream rules (e.g., pragṛhya-related sandhi blocking).

v3 engine role:
  - Registers samjna_registry["1_1_75_eN_prAcAm"] = frozenset({"e", "o"})
    once per derivation (idempotent guard via cond).
  - cond() reads ONLY samjna_registry (Art. 2 compliant: no vibhakti,
    vacana, lakāra, surface Devanāgarī, data, or reference access).
  - No arm flags.  r1_form_identity_exempt=True (pure SAMJNA, no rewrite).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY   = "1_1_75_eN_prAcAm"
_EN_PHONEMES = frozenset({"e", "o"})


def cond(state: State) -> bool:
    return state.samjna_registry.get(_GATE_KEY) is None


def act(state: State) -> State:
    state.samjna_registry[_GATE_KEY] = _EN_PHONEMES
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.75",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "eN prAcAm deSe",
    text_dev                = "एङ् प्राचां देशे",
    padaccheda_dev          = "एङ् / प्राचाम् / देशे",
    why_dev                 = (
        "प्राचां देशे — पूर्वदेशीय-वैयाकरणानां मते — "
        "एङ् (ए, ओ) इत्येतौ वर्णौ प्रग्रह्य-संज्ञकौ भवतः। "
        "अर्थात् द्विवचने एकारान्त-ओकारान्त-रूपेषु संधिः न भवति "
        "— यथा वृक्षे + अत्र = वृक्षे अत्र (न तु वृक्षेऽत्र)।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
