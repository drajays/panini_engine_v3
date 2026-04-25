"""
1.3.78  शेषात् कर्तरि परस्मैपदम्  —  PARIBHASHA

*Padaccheda:* *śeṣāt* (pañcamī), *kartari* (saptamī), *parasmaipadam* (prathamā).

*Anuvṛtti:* *kartari* **1.3.14** (metadata; **1.3.14** not implemented as a separate engine module here).

*Content:* for *dhātu* situations not covered by the *ātmanepada* block **1.3.12**–**1.3.77**,
*parasmaipada* *pratyaya* applies in *kartari*.

*Engine:* sets ``prayoga_1_3_78_seza_kartari_parasmaipada`` in ``paribhasha_gates``.  The recipe
signals *ātmanepada* licence with ``Term.meta['kartari_atmanepada_licensed']`` on the primary
*dhātu* *Term*; **cond** is false when the gate already matches the desired value (R3-safe).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import (
    ATMANE_LICENSE_META_KEY,
    GATE_KEY,
    find_primary_dhatu,
    seza_parasmaipada_gate_needs_update,
)


def cond(state: State) -> bool:
    return seza_parasmaipada_gate_needs_update(state)


def act(state: State) -> State:
    d = find_primary_dhatu(state)
    assert d is not None
    active = not bool(d.meta.get(ATMANE_LICENSE_META_KEY))
    state.paribhasha_gates[GATE_KEY] = {
        "active": active,
        "pATha": "1.3.78",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.78",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "SezAt kartrA parasmaipadam",
    text_dev       = "शेषात् कर्तरि परस्मैपदम् (कर्तरि १.३.१४)",
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
