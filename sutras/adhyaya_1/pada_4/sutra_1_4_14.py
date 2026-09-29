"""
1.4.14  सुप्तिङन्तं पदम्  —  SAMJNA

A nominal or verbal form ending in a *sup* or *tiṅ* affix is called *pada*
(when the technical conditions for *pada* operations apply in the śāstra).

Engine: registers the *pada*‑śāstra node for Tripāḍī / sandhi scope (trace).
Actual *pada* tagging of merged Terms is done structurally in ``subanta._pada_merge``.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _ends(state: State):
    """The sup/tiṅ that closes a pada (सुप्तिङन्तम्)."""
    return [t for t in state.terms
            if "sup" in t.tags or "tin_adesha_3_4_78" in t.tags or "tin" in t.tags]


def cond(state: State) -> bool:
    return state.samjna_registry.get("1.4.14_suptinganta_pada_samjna") is None and bool(_ends(state))


def act(state: State) -> State:
    state.samjna_registry["1.4.14_suptinganta_pada_samjna"] = True
    for t in _ends(state):
        t.tags.add("suptinanta_pada")      # the pada ends here
    state.meta["__why_now_dev__"] = (
        "सुप्-अन्तः तिङ्-अन्तः वा शब्दः पद-संज्ञकः; अनेन पद-कार्याणि "
        "(त्रिपादी-सन्धि-आदि) प्रसजन्ति। (१.४.१४)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.14",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'suptiNantaM padam',
    text_dev       = 'सुप्तिङन्तं पदम्',
    padaccheda_dev = "सुप्-तिङ्-अन्तं पदम्",
    why_dev        = "सुप्-अन्तः तिङ्-अन्तः वा शब्दः पद-संज्ञकः (अष्टाध्यायी)।",
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
