"""
1.1.4  न धातुलोप आर्धधातुके  (naDAtulopa ArDADAtuke)  —  PARIBHASHA

**Paribhāṣā (niyama on 1.1.3):** when an *ārdhadhātuka* pratyāya is in play
and a **dhātu lopa** has applied to the aṅga, the 1.1.3 *ik*–*guṇa* / *vṛddhi*
*sthāyin* convention does **not** govern (Kāśikā-style gloss: *nā* negates
application in that locus to the *guṇa* / *vṛddhi* ordered by a *vidhi* in the
*utsarga* sense).

v3 *silico*:
  * **ārdhadhātuka:** from ``Term.tags`` (``"ardhadhatuka"``) and/or
    ``samjna_registry["3.4.114_ardhadhatuka"]`` (see 3.4.114).
  * **dhatulopa:** lopa rules that trim the root set ``"dhatulopa" in Term.tags`` on
    the relevant *aṅga* (Term).

Use ``ik_guna_vriddhi_blocked_by_1_1_4(state)`` in *vidhi* *cond* paths (e.g. 7.3.84)
together with 1.1.3’s gate. If this rule is **explicitly** *apply_rule*’d, the
same information is also stored under ``GATE_KEY`` in ``paribhasha_gates`` for
audit / replay.

See also: ``sutra_1_1_3.GATE_KEY``, then ``sutra_1_1_5`` (*kṅiti*), then ``sutra_1_1_6`` (*dīdhī*…).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# R3: single interpretive key when 1.1.4 is applied via apply_rule.
GATE_KEY: str = "1.1.4_naDAtulopa_ardhadhatuke"


def _ardhadhatuka_signal(state: State) -> bool:
    if state.samjna_registry.get("3.4.114_ardhadhatuka") is True:
        return True
    return any("ardhadhatuka" in t.tags for t in state.terms)


def _dhatulopa_signal(state: State) -> bool:
    return any("dhatulopa" in t.tags for t in state.terms)


def ik_guna_vriddhi_blocked_by_1_1_4(state: State) -> bool:
    """
    When True, the 1.1.3 *ik* *sthāyin* suppletion does **not** co-control a
    *guṇa* / *vṛddhi* *ādeśa* (dhātu-lopa in *ārdhadhātuke*), per 1.1.4.
    """
    return _ardhadhatuka_signal(state) and _dhatulopa_signal(state)


# ═══════════════════════════════════════════════════════════════
# Sūtra — record the restriction when recipe invokes it; cond matches.
# ═══════════════════════════════════════════════════════════════


def cond(state: State) -> bool:
    if not ik_guna_vriddhi_blocked_by_1_1_4(state):
        return False
    if state.paribhasha_gates.get(GATE_KEY, {}).get("ik_guna_vrddhi_ardhatu_lopa") is True:
        return False
    return True


def act(state: State) -> State:
    # Immutable merge-friendly payload (R3: must change ``paribhasha_gates``).
    state.paribhasha_gates[GATE_KEY] = {
        "ik_guna_vrddhi_ardhatu_lopa": True,
        "dhatulopa_ardhadhatuke": True,
    }
    return state


_WHY = (
    "आर्धधातुके क्षेपे सति यदि धातु-लोपः, तदा १.१.३-वर्णितः इक-स्थानिन्-"
    "नियमो गुण-वृद्धि-क्रियायै न प्रवर्तते।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.4",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "naDAtulopa ArDADAtuke",
    text_dev       = "न धातुलोप आर्धधातुके",
    padaccheda_dev = "न धातु-लोपे आर्धधातुके",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.3",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
