"""
1.1.55  अनेकाल्शित् सर्वस्य  —  PARIBHASHA (narrow demo)

Demo slice (ईधे):
  When an ādeśa is multi-lettered and marked with it (śit), replace the whole
  sthānī. In our demos, **3.4.81** uses this to replace `ta` with `eS`.

Engine:
  - recipe-armed by ``state.meta['anekal_shit_recipe']``.
  - identity-exempt (paribhāṣā bookkeeping).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 11055 · अनेकाल्शित्सर्वस्य
              padaccheda: अनेक-अल्-शित् · सर्वस्य
              anuvṛtti:   11049: षष्ठी
  Source #2 — Kāśikā 1.1.55 udāharaṇa:
                — भविता
                भवितुम्
                भवितव्यम्
  Gloss (sa) — अनेकेषु अच्-हल्-वर्णेषु शिति प्रत्यये सर्वेषु विधिः भवति।
  Cross-check — surface pinned by: tests/regression/test_rADA_strilinga_gold.py, tests/unit/test_IDe_lit_indh.py, tests/unit/test_anekAlSit_sarvasya_paribhasha.py
  Reference record: sutra_ref_out/1_1_55.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("anekal_shit_recipe")) and not state.paribhasha_gates.get("1.1.55")


def act(state: State) -> State:
    state.paribhasha_gates["1.1.55"] = True
    state.meta["anekal_shit_recipe"] = False
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

