"""
8.2.108  तयोर्य्वावचि संहितायाम्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=82108):** *tayor yvāv aci saṃhitāyām* —
*saṃhitādhikāraḥ (tṛtīyaḥ)* (scope through **8.4.68** अ अ).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.2.108" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.2.108",
        "scope_end" : "8.4.68",
        "text_dev"  : "तयोर्य्वावचि संहितायाम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.108",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "tayor yvAv aci saMhitAyAm",
    text_dev       = "तयोर्य्वावचि संहितायाम्",
    padaccheda_dev = "तयोः / य्वौ / अचि / संहितायाम्",
    why_dev        = "संहिताधिकारः (तृतीयः) — ८.२.१०८ तः ८.४.६८ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.2.108", "8.4.68"),
)

register_sutra(SUTRA)

