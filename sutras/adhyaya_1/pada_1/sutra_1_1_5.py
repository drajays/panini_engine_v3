"""
1.1.5  क्ङिति  (KNGiti)  —  PARIBHASHA

**Paribhāṣā (niyama on 1.1.3, with *na* carried from 1.1.4):** in the scope of
a *kit* pratyāhāra affix (the *k* … *it* family), the *ik* *sthāyin* convention
of **1.1.3** for *guṇa* / *vṛddhi* (when those words *utsarga*-order the
operation) is **excluded** here.  (Traditional *kṅiti* — pratyāya in *kit*—
*ca* = “also” after **1.1.4**.)

v3 *silico*:
  * **kṅiti** context: at least one *pratyāya* ``Term`` carries
    ``"kngiti"`` in ``.tags`` (pratyāya-attach or kṛd rules should set it),
    **or** ``state.samjna_registry["1.1.5_kngiti"] is True`` when the recipe
    records global *kit* after **3.4.67**-class steps.

**Resolver contract:** use ``ik_guna_vriddhi_blocked_by_1_1_5(state)`` in *vidhi*
*cond* paths (with **1.1.3** / **1.1.4** helpers).  Explicit *apply_rule* also
freezes a breadcrumb in ``paribhasha_gates[GATE_KEY]``.

See also: ``sutra_1_1_3`` / ``sutra_1_1_4``, then ``sutra_1_1_6`` (*dīdhī*…).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

GATE_KEY: str = "1.1.5_kngiti"


def _kngiti_signal(state: State) -> bool:
    if state.samjna_registry.get("1.1.5_kngiti") is True:
        return True
    return any("kngiti" in t.tags for t in state.terms)


def ik_guna_vriddhi_blocked_by_1_1_5(state: State) -> bool:
    """
    When True, **1.1.3** *ik* *guṇa* / *vṛddhi* *sthāyin* is **out of scope** for
    the *utsarga* ordering (*kṅiti* locus), per 1.1.5.
    """
    return _kngiti_signal(state)


# ═══════════════════════════════════════════════════════════════
# Sūtra
# ═══════════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    if not ik_guna_vriddhi_blocked_by_1_1_5(state):
        return False
    if state.paribhasha_gates.get(GATE_KEY, {}).get("ik_guna_vrddhi_kngiti") is True:
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = {
        "ik_guna_vrddhi_kngiti": True,
        "kngiti": True,
    }
    return state


_WHY = (
    "क्‍ङ्-परिच्छिन्ने प्रत्यय-क्षेपे, तस्मिन् आङ्ग-कार्ये, "
    "यः १.१.३-उत्सर्ग-इक-नियमः, सो न।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.5",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "KNGiti",
    text_dev       = "क्ङिति",
    padaccheda_dev = "क्‍ङ् इति",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.4", "1.1.3"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
