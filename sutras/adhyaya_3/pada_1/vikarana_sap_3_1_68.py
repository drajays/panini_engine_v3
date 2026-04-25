"""
**3.1.68** *sārvadhātake kartari … śap* — helpers for *vikaraṇa* *śap* insertion.

Not a sūtra file.  *Śāstra:* after a *dhātu*, when the following affix is *sārvadhātuka* and the *prayoga*
is *kartari*, the *śap* *vikaraṇa* is *āgama* between *dhātu* and that affix (*it* on *ś* and *p* per **1.3.3**,
**1.3.8**; *lopa* **1.3.9** — not executed in this module).

*Engine:* ``find_sap_insertion_dhatu_index`` returns the index of the *dhātu* *Term* after which ``Sap`` should
be inserted, iff:

  * **3.1.91** *dhātoḥ* *adhikāra* is on ``adhikara_stack`` (``3.1.68`` precedes **3.1.91** in the
    *Aṣṭādhyāyī* order, so tuple-based ``adhikara_in_effect`` with this sūtra id is unsuitable — we only
    test stack membership),
  * *kartari* is licensed by **3.4.69** *paribhāṣā* **or** ``state.meta['3_1_68_kartari_recipe']`` is true (minimal tests),
  * the next *pratyaya*’s ``upadesha_slp1`` is *sārvadhātuka* per ``sarvadhatuka_3_4_113`` **and**
    is a *tiṅ* *ādeśa* or *kṛt* *śit* (not another *vikaraṇa* like *śyan*, **3.1.69** *apavāda*),
  * there is not already a ``Sap`` / ``3_1_68_sap`` *Term* immediately after the *dhātu*.

*Cross-refs:* **3.1.67** (*sārvadhātake* *anuvṛtti*), **3.4.113**, **3.4.69**, **1.3.3** / **1.3.8** / **1.3.9**, **6.1.97** (*guṇa* after *śap* *lopa*).
"""
from __future__ import annotations

from typing import Final

from engine.state import State

from sutras.adhyaya_3.pada_4.lakara_prayoga_3_4_69 import GATE_PFX
from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import (
    SIT_KRT_SARVADHATUKA_SLP1,
    SIT_VIK_SARVADHATUKA_SLP1,
    is_sarvadhatuka_upadesha_slp1,
)
from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_SET

# Recipe-only: when **3.4.69** has not run, allow *kartari* for unit tests / narrow demos.
KARTARI_RECIPE_META_KEY: Final[str] = "3_1_68_kartari_recipe"

SAP_INSERT_TAG: Final[str] = "3_1_68_sap"


def _norm_upadesha(up: str) -> str:
    t = up.strip()
    if t.endswith("~"):
        return t[:-1]
    return t


def _sap_trigger_next_pratyaya(up: str) -> bool:
    """
    *Śap* is inserted only before *tiṅ* *ādeśa* or *kṛt* *śit* (e.g. *śatṛ*), not before another
    *vikaraṇa* (*śyan* …) which is an *apavāda* to **3.1.68**.
    """
    k = _norm_upadesha(up)
    if k == "Sap":
        return False
    if k in SIT_VIK_SARVADHATUKA_SLP1:
        return False
    return k in TIN_ADESHA_SET or k in SIT_KRT_SARVADHATUKA_SLP1


def _kartari_ok(state: State) -> bool:
    if state.paribhasha_gates.get(f"{GATE_PFX}_licenses_kartari") is True:
        return True
    if state.meta.get(KARTARI_RECIPE_META_KEY) is True:
        return True
    return False


def _dhato_adhikara_3_1_91_open(state: State) -> bool:
    """**3.1.91** on stack ⇒ *kṛt* / *tiṅ* attach to *dhātu*; **3.1.68** is before **3.1.91** in the book."""
    return any(e.get("id") == "3.1.91" for e in state.adhikara_stack)


def find_sap_insertion_dhatu_index(state: State) -> int | None:
    if not _dhato_adhikara_3_1_91_open(state):
        return None
    if not _kartari_ok(state):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
            continue
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up == "Sap":
            continue
        if SAP_INSERT_TAG in nxt.tags:
            continue
        if not is_sarvadhatuka_upadesha_slp1(up):
            continue
        if not _sap_trigger_next_pratyaya(up):
            continue
        return i
    return None
