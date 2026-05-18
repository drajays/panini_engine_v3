"""
1.3.49  अनोरकर्मकात्  —  NIYAMA

*Padaccheda:* *anoḥ* (पञ्चमी-एकवचन) / *akarmakāt* (पञ्चमी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* Except from (anoḥ = not after anu) an akarmaka root. That is,
ātmanepada does NOT apply when the prefix anu precedes an akarmaka root.
This is a NIYAMA (restriction) on the prior rule 1.3.45 (akarmakāc ca):
the anu-prefix environment is carved out — anu + akarmaka → parasmaipada only.

*Engine:* This NIYAMA fires when a dhātu Term carries both "anu_prefix" and
"akarmaka" — the rule removes any Atmanepada assignment made by 1.3.45.
cond checks (a) pada is currently "Atmanepada", (b) the stamp
"Atmanepada_1_3_45" is present (meaning 1.3.45 applied), (c) the
idempotency stamp "Niyama_1_3_49" is absent, and (d) a dhātu Term carries
both "anu_prefix" and "akarmaka" tags.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=False because
this rule reverts a prior state change (NIYAMA contract).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_REGISTRY_KEY = "1_3_49_anor_akarmaka_niyama"
_STAMP_KEY    = "Niyama_1_3_49"


def cond(state: State) -> bool:
    if state.meta.get(_STAMP_KEY):
        return False
    # Only restricts if 1.3.45 (akarmaka rule) applied and set Atmanepada
    if state.meta.get("pada") != "Atmanepada":
        return False
    if not state.meta.get("Atmanepada_1_3_45"):
        return False
    # Fire only when anu_prefix + akarmaka present
    return any(
        "dhatu" in t.tags
        and "anu_prefix" in t.tags
        and "akarmaka" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    # Remove the ātmanepada assigned by 1.3.45
    state.meta["pada"] = "Parasmaipada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.49",
    sutra_type=SutraType.NIYAMA,
    r1_form_identity_exempt=True,
    text_slp1="anorAkarmakAt",
    text_dev="अनोरकर्मकात्",
    padaccheda_dev="अनोः (पञ्चमी-एकवचन) / अकर्मकात् (पञ्चमी-एकवचन)",
    why_dev=(
        "अनु-पूर्वकस्य अकर्मक-धातोः प्रयोगे आत्मनेपदं न — "
        "अनुव्रजति इत्यादि परस्मैपदम् एव; "
        "१.३.४५ इत्यस्य अयं नियमः; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12", "1.3.45"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
