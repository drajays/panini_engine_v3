"""
1.1.57  अचः परस्मिन् पूर्वविधौ  —  PARIBHASHA

Sources consulted:
- ashtadhyayi.com data.txt row i=101057
- Kāśikā: अचः परस्मिन् पूर्वविधौ (लोपितस्य अचः स्थानिवत्-भावः)
- Cross-validation: tests/unit/test_kathi_kath_nic.py (lupta *a* blocks **7.2.116**);
  tests/unit/test_agaty_gam_lyap_acah_lesson.py (lupta *m* does **not** block **6.1.71**);
  tests/unit/test_dIdhye_dIdhi_lat_parasmin_lesson.py (**3.4.79** *sva-nimitta* ``e``)

*Acaḥ parasmin pūrvavidhau* — an *ac* (vowel) elided by a *pūrva-vidhi* is
*sthānivat* for a following *para* rule. **Hal** lopa and **sva-nimitta** *ac* ādeśa
(e.g. **3.4.79** ``i``→``e``) are not covered — **6.1.71** / **7.4.53** lessons.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "1.1.57_aca_parasmin_purvavidhau"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.57",
    sutra_type=SutraType.PARIBHASHA,
    text_slp1="acaH parasmin pUrvavidhO",
    text_dev="अचः परस्मिन् पूर्वविधौ",
    padaccheda_dev="अचः / परस्मिन् / पूर्वविधौ",
    why_dev="पूर्वविधि-लोपितस्य अचः स्थानिवत्-भावः (P025)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
