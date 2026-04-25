"""
1.4.108  शेषे प्रथमः  (full *anuvṛtti* of **1.4.105** baked)  —  PARIBHASHA

*Padaccheda:* *śeṣe* (saptamī), *prathamaḥ* (prathamā) — *puruṣa* of *tiṅ*.

*Baked* *anuvṛtti:* *upapade* **+** *samanādhikaraṇe* **+** *sthānini* **+** *api* (**1.4.105**); *kartari* chain and *1.4.1* *ekasañjñā*.

*Śāstra* *laghu:* where **1.4.105** / **1.4.107** do not force *madhyama* / *uttama* for *yuṣmad* / *asmat* in
*sāmanādhikaraṇya* with the *kāraka* the verb expresses, the *ŚEṢA* case is **1.4.108**: the *tiṅ* *ādeśa* must
be the *prathamapuruṣa* row ( **1.4.101** *A* triple — *tip* / *tas* / *jhi* and *tá* / *ātām* / *jha* in *par* / *ātmane* ).

*Engine:* ``paribhasha_gates``; recipe blocks with ``MADHYAMOTTAMA_105_107_BLOCK_META_KEY``; **R3**-safe
``cond``; no *vākyārtha* in ``cond`` (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import find_primary_dhatu
from sutras.adhyaya_1.pada_4.seza_prathama_1_4_108 import (
    GATE_KEY,
    MADHYAMOTTAMA_105_107_BLOCK_META_KEY,
    seza_prathama_108_gate_needs_update,
)


def cond(state: State) -> bool:
    return seza_prathama_108_gate_needs_update(state)


def act(state: State) -> State:
    d = find_primary_dhatu(state)
    assert d is not None
    active = not bool(d.meta.get(MADHYAMOTTAMA_105_107_BLOCK_META_KEY))
    state.paribhasha_gates[GATE_KEY] = {
        "active": active,
        "pATha": "1.4.108",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.108",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = (
        "Seze upapade samAnADhikaraRe sthAnin api prathamaH"
    ),
    text_dev       = "शेषे उपपदे समानाधिकरणे स्थानिनि अपि प्रथमः (एकसंज्ञा, १.४.१०१)",
    padaccheda_dev = "शेषे (सप्तमी) / उपपदे (समानाधिकरण-चर्चा) / प्रथमः (विकल्पित-पठितम्)",
    why_dev        = (
        "मध्यमोत्तम-निमित्ते १.४.१०५, १.४.१०७ — अन्येभ्यो वाक्येभ्यः "
        "कर्तरि / कर्मण्यनुरोधि प्रथम-वचनीयः तिङ् (१.४.१०१- क्रमेण)।"
    ),
    anuvritti_from = ("1.4.1", "1.4.101", "1.4.105", "1.4.107"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
