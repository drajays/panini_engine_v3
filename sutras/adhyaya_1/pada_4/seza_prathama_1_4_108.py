"""
**1.4.108** *śeṣe … prathamaḥ* — helpers for the *ŚEṢA* default: *prathamapuruṣa* *tiṅ* row.

Not a sūtra file.  **1.4.108** (with *anuvṛtti* of **1.4.105** *samanādhikaraṇe*, *sthānini*, *api*)
constrains which *puruṣa* *tiṅ* *ādeśa* row ( **1.4.101** tripartite **A** = *prathama* in each block)
applies: in the *ŚEṢA* after the **1.4.105** / **1.4.107** *nimitta* cases, the verb takes the
*prathama*-*puruṣa* *tiṅ* (e.g. *tip* / *jhi* / *ta* / *jha* in the *ādeśa* that **1.4.101** marks as *A* ).

*Engine (CONSTITUTION Art. 2):* the engine does not parse *vākya* co-reference.  A recipe may set
``Term.meta[MADHYAMOTTAMA_105_107_BLOCK_META_KEY]`` to a truthy value when **1.4.105** (*madhyama* with
*yuṣmad*) or **1.4.107** (*uttama* with *asmat*) is active for the *kartṛ* / *karmadhīra* — then
*ŚEṢA* **1.4.108** is **out** and this gate is inactive.  When the flag is absent or false, the gate
``active`` is **true**: *1.4.101* *A*‑row *tiṅ* is the default licenced by **1.4.108** for the derivation.

*Cross-refs:* **1.4.101** (three triples and *A*/*B*/*C* *tags*), **2.4.85** (*luṭ* *prathama*), *śāstra*
examples for *karmaṇi* (user's item 4), *yuṣmad* (item 3), *asmat* (items 5–6).
"""
from __future__ import annotations

from typing import Final

from engine.state import State, Term

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import find_primary_dhatu

GATE_KEY: Final[str] = "prayoga_1_4_108_sheza_prathama_tin"

# Truthy on the primary *dhātu* *Term* ⇒ *madhyamottama* row from **1.4.105** / **1.4.107** (recipe),
# so *ŚEṢA* **1.4.108** does **not** licence *1.4.101* row **A** as the *nimitta* here.
MADHYAMOTTAMA_105_107_BLOCK_META_KEY: Final[str] = "1_4_108_madhyamottama_from_105_107"


def seza_108_licences_prathama_tin(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def _desired_108_active(d: Term) -> bool:
    return not bool(d.meta.get(MADHYAMOTTAMA_105_107_BLOCK_META_KEY))


def seza_prathama_108_gate_needs_update(state: State) -> bool:
    d = find_primary_dhatu(state)
    if d is None:
        return False
    desired = _desired_108_active(d)
    cur = state.paribhasha_gates.get(GATE_KEY, {}).get("active")
    return cur is None or cur is not desired
