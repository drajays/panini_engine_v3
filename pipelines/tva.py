"""
pipelines/tva.py — ``prakriya_23`` (*tvā* for *tvām*), now through the real context mechanism.

``tvām`` (yuṣmad, dvitīyā ekavacana, derived by 4.1.2 … 7.2.9x) stands after ``grāmaḥ`` in the same pāda:
**8.1.17** *padāt*, **8.1.18** *anudāttaṃ sarvam apādādau* open, **8.1.23** *tvāmau dvitīyāyāḥ* gives ``tvA``
(apavāda of 8.1.22), with ``sarva_anudAtta_8_1_18`` on the ādeśa.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only (see ``pipelines/enclitic.py``).
"""
from __future__ import annotations

from engine.state import State
from pipelines.enclitic import derive_in_context


def derive_tva_prakriya_23() -> State:
    return derive_in_context("yuzmad", 2, 1, before=[{"slp1": "grAmaH", "vibhakti": 1}],
                             after=[{"slp1": "paSyati", "yukta": True, "paSyArTa": True, "AlocanArTa": True}])


__all__ = ["derive_tva_prakriya_23"]
