"""
1.4.108  शेषे प्रथमः  —  PARIBHASHA

*Padaccheda:* *śeṣe* (saptamī), *prathamaḥ* (prathamā) — *puruṣa* of *tiṅ*.

*Baked* *anuvṛtti:* *upapade* **+** *samanādhikaraṇe* **+** *sthānini* **+** *api* (**1.4.105**); *kartari* chain and *1.4.1* *ekasañjñā*.

*Śāstra* *laghu:* where **1.4.105** / **1.4.107** do not force *madhyama* / *uttama* for *yuṣmad* / *asmat* in
*sāmanādhikaraṇya* with the *kāraka* the verb expresses, the *ŚEṢA* case is **1.4.108**: the *tiṅ* *ādeśa* must
be the *prathamapuruṣa* row ( **1.4.101** *A* triple — *tip* / *tas* / *jhi* and *tá* / *ātām* / *jha* in *par* / *ātmane* ).

*Engine:* ``paribhasha_gates``; recipe blocks with ``MADHYAMOTTAMA_105_107_BLOCK_META_KEY``; **R3**-safe
``cond``; no *vākyārtha* in ``cond`` (CONSTITUTION Art. 2).
Pāṭha: ashtadhyayi.com data.txt row i=14108 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import find_primary_dhatu


# --- helpers of this sūtra (formerly seza_prathama_1_4_108.py; one sūtra, one file) ---
from typing import Final

from engine.state import State, Term

from sutras.adhyaya_1.pada_3.sutra_1_3_78 import find_primary_dhatu

GATE_KEY: Final[str] = "prayoga_1_4_108_sheza_prathama_tin"

# Truthy on the primary *dhātu* *Term* ⇒ *madhyamottama* row from **1.4.105** / **1.4.107** (recipe),
# so *ŚEṢA* **1.4.108** does **not** licence *1.4.101* row **A** as the *nimitta* here.
MADHYAMOTTAMA_105_107_BLOCK_META_KEY: Final[str] = "1_4_108_madhyamottama_from_105_107"


def seza_108_licences_prathama_tin(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def _desired_108_active(d: Term) -> bool:
    return not bool(d.meta.get(MADHYAMOTTAMA_105_107_BLOCK_META_KEY))


def seza_prathama_108_gate_needs_update(state: State) -> bool:
    # 1.4.108's true locus is tiṅanta puruṣa-nirṇaya, not any bare dhātu Term.
    # cond() false-positive audit: audit/cond_discipline_auditor.py.
    if state.meta.get("derivation_class") != "tinanta":
        return False
    d = find_primary_dhatu(state)
    if d is None:
        return False
    # gaṇa-nirṇaya (P01_samjna_dhatu_class) has already run by the time the
    # real tiṅanta bootstrap reaches puruṣa-nirṇaya — a tape-init-only probe
    # (build_tinanta_initial_state, pre-P01) never sets this.
    if "gana" not in d.meta:
        return False
    desired = _desired_108_active(d)
    cur = state.paribhasha_gates.get(GATE_KEY, {}).get("active")
    return cur is None or cur is not desired



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
    sutra_type     = SutraType.VIDHI,
    text_slp1      = (
        'Seze praTamaH'
    ),
    text_dev       = 'शेषे प्रथमः',
    samagra_slp1   = "Seze upapade samAnADikaraRe sTAnini api praTamaH",
    samagra_dev    = "शेषे उपपदे समानाधिकरणे स्थानिनि अपि प्रथमः",
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
