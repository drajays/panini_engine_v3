"""
1.2.4  सार्वधातुकमपित्  —  SAMJNA (narrow demo)

Demo slice (कुरुतः prakriyā):
  A *sārvadhātuka* tiṅ-pratyaya that is **a-pit** behaves as *kṅit* for the
  purpose of blocking guṇa/vṛddhi under **1.1.5 kṅiti**.

Engine contract:
  - We model this by tagging the qualifying pratyaya Term with ``kngiti`` and
    recording ``samjna_registry['1.2.4_sarvadhatukam_apit'] = True``.
  - This is a narrow glass-box slice: we treat tiṅ-ādeśa `tas` (3rd dual
    parasmaipada) as the qualifying target in the demo.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1


def _find(state: State) -> int | None:
    if state.samjna_registry.get("1.2.4_sarvadhatukam_apit") is True:
        return None
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not is_sarvadhatuka_upadesha_slp1(up):
            continue
        # Narrow demo: treat missing pit marker as a-pit.
        if t.meta.get("pit") is True:
            continue
        if "kngiti" in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.samjna_registry["1.2.4_sarvadhatukam_apit"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.4",
    sutra_type=SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1="sArvaDAtukam apit",
    text_dev="सार्वधातुकमपित्",
    padaccheda_dev="सार्वधातुकम् / अपित्",
    why_dev="अपित्-सार्वधातुकस्य कङित्-व्यवहारः — गुणादि निषेध-प्रसङ्गः (कुरुतः)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

