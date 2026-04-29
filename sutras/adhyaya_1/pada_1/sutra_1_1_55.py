"""
1.1.55  अनेकाल्शित् सर्वस्य  —  PARIBHASHA (narrow demo)

Demo slice (ईधे):
  When an ādeśa is multi-lettered and marked with it (śit), replace the whole
  sthānī. In our demos, **3.4.81** uses this to replace `ta` with `eS`.

Engine:
  - recipe-armed by ``state.meta['1_1_55_anekal_shit_sarvasya_arm']``.
  - identity-exempt (paribhāṣā bookkeeping).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("1_1_55_anekal_shit_sarvasya_arm")) and not state.paribhasha_gates.get("1.1.55")


def act(state: State) -> State:
    state.paribhasha_gates["1.1.55"] = True
    state.meta["1_1_55_anekal_shit_sarvasya_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.55",
    sutra_type=SutraType.PARIBHASHA,
    r1_form_identity_exempt=True,
    text_slp1="anekAlSit sarvasya",
    text_dev="अनेकाल्शित् सर्वस्य",
    padaccheda_dev="अनेकाल्-शित् / सर्वस्य",
    why_dev="अनेकाल्-शित्-आदेशः सम्पूर्ण-स्थानिनः (ईधे: त→एश्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

