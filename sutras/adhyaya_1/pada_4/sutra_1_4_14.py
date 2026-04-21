"""
1.4.14  सुप्तिङन्तं पदम्  —  SAMJNA

A nominal or verbal form ending in a *sup* or *tiṅ* affix is called *pada*
(when the technical conditions for *pada* operations apply in the śāstra).

Engine: registers the *pada*‑śāstra node for Tripāḍī / sandhi scope (trace).
Actual *pada* tagging of merged Terms is done structurally in ``subanta._pada_merge``.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    return state.samjna_registry.get("1.4.14_suptinganta_pada_samjna") is None


def act(state: State) -> State:
    state.samjna_registry["1.4.14_suptinganta_pada_samjna"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.14",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "suptiNantam padam",
    text_dev       = "सुप्तिङन्तं पदम्",
    padaccheda_dev = "सुप्-तिङ्-अन्तं पदम्",
    why_dev        = "सुप्-अन्तः तिङ्-अन्तः वा शब्दः पद-संज्ञकः (अष्टाध्यायी)।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
