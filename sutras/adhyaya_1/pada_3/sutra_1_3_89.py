"""
1.3.89  न पादम्याङ्यमाङ्यसपरिमुहरुचिनृतिवदवसः  —  VIDHI (blocking/na-sutra)

*Padaccheda:* *na* / *pāt* / *amyāṅ* / *yamāṅ* / *yasa-pari-muha-ruci-nṛti-vada-vasaḥ*.

*Anuvṛtti:* ātmanepada from 1.3.12; akarmaka, cittavat-kartṛ from 1.3.88.

*Content:* Blocking rule (na) — the following roots do NOT take ātmanepada
even when the conditions of 1.3.88 (akarmaka, conscious agent) are met:
pā (to drink), am, yam (with ā prefix), yas, muha, ruc, nṛt, vad, vas.
For example: pibati (not *pibate) — he drinks.

*Engine:* When pada has been set to "Atmanepada" by 1.3.88 and the dhātu is
in the blocked set, this rule reverts it to "Parasmaipada". cond checks
(a) stamp "na_1_3_89" absent, (b) a dhātu whose upadesha_slp1 is in _BLOCKED.
No arm flags (CONSTITUTION Art. 13). r1_form_identity_exempt=True.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
# These roots are blocked from ātmanepada even under 1.3.88
_BLOCKED: frozenset[str] = frozenset({
    "pA",       # pā — to drink
    "am",       # am
    "yam",      # yam (with ā)
    "yama~",
    "yas",      # yas — to strive
    "muha~",    # muh — to be confused
    "muh",
    "ruci~",    # ruc — to shine/please
    "ruc",
    "nftI",     # nṛt — to dance
    "nft",
    "vada~",    # vad — to speak
    "vad",
    "vasa~",    # vas — to dwell
    "vas",
})

_REGISTRY_KEY = "1_3_89_na_blocked_atmanepada"
_STAMP_KEY    = "na_1_3_89"


def _find(state: State):
    if state.meta.get(_STAMP_KEY):
        return None
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _BLOCKED:
            return t
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    t = _find(state)
    if t is None:
        return state
    # Blocking: revert to parasmaipada (na-rule)
    state.meta["pada"]     = "Parasmaipada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.89",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="na pAdamyANyamANyasaparimuhrucinftivadavasaH",
    text_dev="न पादम्याङ्यमाङ्यसपरिमुहरुचिनृतिवदवसः",
    padaccheda_dev="न / पात् / अम्याङ् / यमाङ् / यस-परि-मुह-रुचि-नृति-वद-वसः",
    why_dev=(
        "पा-अम्-यम्-यस्-मुह्-रुच्-नृत्-वद्-वस्-धातूनां आत्मनेपदं न — "
        "pibati, yacchati इत्यादि; "
        "१.३.८८ इत्यस्य अपवादः।"
    ),
    anuvritti_from=("1.3.12", "1.3.88"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
