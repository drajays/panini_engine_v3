"""
4.3.138  त्रपुजतुनोः षुक्  —  VIDHI

Glass-box demo slice (from note `त्रापुषम् .md`):
  For the stems `trapu` and `jatu` in the "vikāra" taddhita demo, attach:
    - the taddhita pratyaya `aR` (ṇit via halantyam on final R),
    - and insert the augment `zuk` (kit) after the aṅga per 1.1.46.

We model this as an explicit recipe-armed constructor:
  - expects a frame: [anga(prātipadika), sup(Nas)]
  - inserts: [anga, zuk, sup(Nas), aR]

The subsequent it-prakaraṇa (1.3.2/3/8/9) will delete `u~` and `k` of `zuk`,
leaving `z` (ष्), and delete `R` of `aR` while recording `R` as it-marker,
so 7.2.117 can apply vṛddhi (ṇit taddhita).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _matches(state: State) -> bool:
    if not state.meta.get("4_3_138_arm"):
        return False
    if len(state.terms) < 2:
        return False
    t0 = state.terms[0]
    t1 = state.terms[1]
    if "anga" not in t0.tags or "prātipadika" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") not in {"trapu", "jatu"}:
        return False
    if "sup" not in t1.tags or t1.meta.get("upadesha_slp1") != "Nas":
        return False
    # Do not refire if already expanded.
    if any(t.meta.get("upadesha_slp1") == "aR" and "taddhita" in t.tags for t in state.terms):
        return False
    if any(t.meta.get("upadesha_slp1") == "zuk" and "upadesha" in t.tags for t in state.terms):
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state

    zuk = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("zu~k")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "zuk"},
    )
    aR = Term(
        kind="pratyaya",
        # NOTE: our pratyāhāra HAL set includes 'N' (ण) but not 'R';
        # using 'aN' here allows 1.3.3 halantyam to mark the final hal as it,
        # while we keep the classical label 'aR' in metadata for this demo.
        varnas=list(parse_slp1_upadesha_sequence("aN")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "aR"},
    )
    # Frame: [anga, Nas] -> [anga, zuk, Nas, aR]
    state.terms = [state.terms[0], zuk, state.terms[1], aR] + state.terms[2:]
    state.meta["4_3_138_trapu_jatu_zuk_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="4.3.138",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="trapu-jatunoH zuk",
    text_dev="त्रपुजतुनोः षुक्",
    padaccheda_dev="त्रपु-जतु-नोः षुक्",
    why_dev="त्रपु/जतु-शब्दयोः तद्धिते षुक्-आगमः (विकार-अर्थे, अण्-सह)।",
    anuvritti_from=("4.3.134",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

