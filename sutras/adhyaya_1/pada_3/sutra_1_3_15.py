"""
1.3.15  न गतिहिंसार्थेभ्यः  —  NIYAMA

*Padaccheda:* *na* / *gati-hiṃsā-arthebhyaḥ* (पञ्चमी-बहुवचन).

*Anuvṛtti:* ātmanepada from 1.3.12, 1.3.13.

*Content:* Roots whose meaning is gati (motion) or hiṃsā (harm/violence) do NOT take
ātmanepada — they remain parasmaipada — notwithstanding the preceding rules 1.3.13–14.

*Engine:* GATI_HIMSA_ROOTS (module-level frozenset, SLP1) lists common gati/hiṃsā roots.
cond checks (a) pada is already "Atmanepada", (b) at least one dhātu Term whose
upadesha_slp1 is in GATI_HIMSA_ROOTS, and (c) the blocking tag is not already applied.
act reverts pada to "parasmaipada" and stamps each matching term with the blocking tag.
No arm flags (CONSTITUTION Art. 13).
r1_form_identity_exempt=True because no surface phonological change occurs.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — common gati (motion) and hiṃsā (harm/violence) roots in SLP1.
GATI_HIMSA_ROOTS: frozenset[str] = frozenset({
    # gati (motion) roots
    "gam",   # go
    "gAN",   # go (class 1, forms like gacchati)
    "yA",    # go, travel
    "vraj",  # walk, wander
    "car",   # move, roam
    "iz",    # go, seek
    "ej",    # stir, move
    "cal",   # move, shake
    # hiṃsā (harm/violence) roots
    "han",   # strike, kill
    "hiMs",  # harm, injure
    "vadh",  # slay
    "mard",  # crush, grind
    "piS",   # crush, grind
})

_BLOCK_TAG = "na_gati_himsa_1_3_15"
_REGISTRY_KEY = "1_3_15_na_gati_hiMsA"


def _matching_dhatu_terms(state: State):
    """Return dhātu Terms whose upadesha_slp1 is in GATI_HIMSA_ROOTS
    and that have not yet received the blocking tag."""
    result = []
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        upadesha = (t.meta.get("upadesha_slp1") or "").strip()
        if upadesha in GATI_HIMSA_ROOTS and _BLOCK_TAG not in t.meta:
            result.append(t)
    return result


def cond(state: State) -> bool:
    if state.meta.get("pada") != "Atmanepada":
        return False
    return bool(_matching_dhatu_terms(state))


def act(state: State) -> State:
    state.meta["pada"] = "parasmaipada"
    for t in _matching_dhatu_terms(state):
        t.meta[_BLOCK_TAG] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.15",
    sutra_type=SutraType.NIYAMA,
    text_slp1="na gati-hiMsArTeByaH",
    text_dev="न गतिहिंसार्थेभ्यः",
    padaccheda_dev="न / गति-हिंसा-अर्थेभ्यः (पञ्चमी-बहुवचन)",
    why_dev=(
        "गति-हिंसा-अर्थकेभ्यो धातुभ्यः आत्मनेपदं न भवति; "
        "ते परस्मैपद-विषया एव — १.३.१३–१४ इत्यतः प्रतिषेधः।"
    ),
    anuvritti_from=("1.3.12", "1.3.13"),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
