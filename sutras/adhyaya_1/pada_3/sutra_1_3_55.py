"""
1.3.55  दाणश्च सा चेच्चतुर्थ्यर्थे  —  VIDHI

*Padaccheda:* *dāṇaḥ* (षष्ठी-एकवचन) / *ca* / *sā* / *cet* / *caturthyarthe*
(सप्तमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* The root dāṇ (√dā, to give — specifically the dāṇ variety noted
in the Dhātupāṭha) also takes ātmanepada endings if (and only if) the
meaning/purpose expressed is that of a caturthī (dative — i.e., when giving
is for the benefit of someone). The word "ca" pulls in the earlier context
(ātmanepada in the sense of tṛtīyā-yukta from 1.3.54 is also continued here).
For example: devadutte dadāte — he gives for Devadatta's benefit.

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) idempotency
stamp "Atmanepada_1_3_55" is absent, (c) a dhātu Term whose upadesha_slp1 is
in _DAN_ROOTS carries the tag "caturTyarTa_usage". No arm flags
(CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
# dāṇ: SLP1 upadesha is "dAN" or the general dA root
_DAN_ROOTS: frozenset[str] = frozenset({"dAN", "dA", "qf"})

_REGISTRY_KEY = "1_3_55_dAN_caturTyarTa"
_STAMP_KEY    = "Atmanepada_1_3_55"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    if state.meta.get("pada") == "Atmanepada":
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _DAN_ROOTS and "caturTyarTa_usage" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    if t is None:
        return state
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.55",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="dARaSca sA ceccaturTyarTe",
    text_dev="दाणश्च सा चेच्चतुर्थ्यर्थे",
    padaccheda_dev="दाणः (षष्ठी-एकवचन) / च / सा / चेत् / चतुर्थ्यर्थे (सप्तमी-एकवचन)",
    why_dev=(
        "दाण्-धातोः चतुर्थ्यर्थ-प्रयोगे आत्मनेपदम् — "
        "devadutte dadAte इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
