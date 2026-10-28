"""
1.3.78  शेषात् कर्तरि परस्मैपदम्  —  PARIBHASHA

*Padaccheda:* *śeṣāt* (pañcamī), *kartari* (saptamī), *parasmaipadam* (prathamā).

*Anuvṛtti:* *kartari* **1.3.14** (metadata; **1.3.14** not implemented as a separate engine module here).

*Content:* for *dhātu* situations not covered by the *ātmanepada* block **1.3.12**–**1.3.77**,
*parasmaipada* *pratyaya* applies in *kartari*.

*Engine:* sets ``prayoga_1_3_78_seza_kartari_parasmaipada`` in ``paribhasha_gates``.  The recipe
signals *ātmanepada* licence with ``Term.meta['kartari_atmanepada_licensed']`` on the primary
*dhātu* *Term*; **cond** is false when the gate already matches the desired value (R3-safe).
Pāṭha: ashtadhyayi.com data.txt row i=13078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


# --- helpers of this sūtra (formerly kartari_pada_1_3_78.py; one sūtra, one file) ---
from typing import Final

from engine.state import State, Term

GATE_KEY: Final[str] = "prayoga_1_3_78_seza_kartari_parasmaipada"

# Recipe / 1.3.12–77 chain: truthy ⇒ *ātmanepada* licensed for *kartari* for this *dhātu*.
ATMANE_LICENSE_META_KEY: Final[str] = "kartari_atmanepada_licensed"


def find_primary_dhatu(state: State) -> Term | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def kartari_parasmaipada_seza_active(state: State) -> bool:
    """True iff the **1.3.78** gate says *śeṣa* → *parasmaipada* in *kartari*."""
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def _desired_gate_active(dhatu: Term) -> bool:
    val = dhatu.meta.get(ATMANE_LICENSE_META_KEY)
    # "ubhaya" = dhātu can take both padas; 1.3.78 śeṣa still gives parasmaipada
    # as the default in kartari (ātmanepada requires a specific 1.3.12–77 context).
    if val == "ubhaya":
        return True
    return not bool(val)


def seza_parasmaipada_gate_needs_update(state: State) -> bool:
    # 1.3.78's true locus is tiṅanta pada-nirṇaya, not any bare dhātu Term
    # (a kṛdanta/subanta derivation over the same dhātu never reaches this
    # gate). cond() false-positive audit: audit/cond_discipline_auditor.py.
    if state.meta.get("derivation_class") != "tinanta":
        return False
    d = find_primary_dhatu(state)
    if d is None:
        return False
    # gaṇa-nirṇaya (P01_samjna_dhatu_class) has already run by the time the
    # real tiṅanta bootstrap reaches pada-nirṇaya — a tape-init-only probe
    # (build_tinanta_initial_state, pre-P01) never sets this.
    if "gana" not in d.meta:
        return False
    desired = _desired_gate_active(d)
    cur = state.paribhasha_gates.get(GATE_KEY, {}).get("active")
    return cur is None or cur is not desired




def cond(state: State) -> bool:
    return seza_parasmaipada_gate_needs_update(state)


def act(state: State) -> State:
    d = find_primary_dhatu(state)
    assert d is not None
    state.paribhasha_gates[GATE_KEY] = {
        "active": _desired_gate_active(d),
        "pATha": "1.3.78",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.78",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'SezAt kartari parasmEpadam',
    text_dev       = 'शेषात् कर्तरि परस्मैपदम्',
    samagra_slp1   = "SezAt kartari parasmEpadam",
    samagra_dev    = "शेषात् कर्तरि परस्मैपदम्",
    padaccheda_dev = "शेषात् (पञ्चमी) / कर्तरि (सप्तमी) / परस्मैपदम् (प्रथमा)",
    why_dev        = (
        "१.३.१२–७७ इत्यादिष्व् आत्मनेपद-विषयं विहाय अन्येभ्यो धातुभ्यः कर्तरि परस्मैपदम्; "
        "१.४.९९ इत्यादौ परस्मैपद-संज्ञा।"
    ),
    anuvritti_from = ("1.3.14",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
