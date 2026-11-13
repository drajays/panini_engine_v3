"""engine/tape_init/samasa.py — the start state of a samāsa derivation: the speaker's vākya, each member a prātipadika + the sup it stands in
(rājñaḥ puruṣaḥ = rājan + Nas, puruṣa + s~), none of it yet a compound (the 2.1.x / 2.2.x sūtras make it one).

The sup's vibhakti is the speaker's sentence (as ``vibhakti`` is for derive_nama_dhatu): it is turned into the sup's upadeśa and its saṃjñā name
here, once; every sūtra after reads the name (``vib:dvitIyA``) or the upadeśa, never the number."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from engine.state import State, Term
from engine.vivaksha import set_vivaksha
from phonology.varna import parse_slp1_upadesha_sequence

_SUP = Path(__file__).resolve().parents[2] / "data" / "inputs" / "sup_upadesha.json"
VIB_NAME = {1: "prathamA", 2: "dvitIyA", 3: "tftIyA", 4: "caturTI", 5: "paYcamI", 6: "zazWI", 7: "saptamI", 8: "sambuddhi"}


@lru_cache(maxsize=1)
def _sups() -> dict:
    return json.loads(_SUP.read_text(encoding="utf-8"))


def build_samasa_state(members: list[tuple], **vivaksha: str) -> State:
    """``members``: (stem_slp1, vibhakti, vacana[, tags[, linga]]) in the order the vākya speaks them."""
    terms: list[Term] = []
    for m in members:
        stem, vib, vac = m[0], m[1], m[2]
        tags = set(m[3]) if len(m) > 3 and m[3] else set()
        linga = m[4] if len(m) > 4 else None
        up = _sups()[f"{vib}-{vac}"]
        terms.append(Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence(stem)),
                          tags={"prātipadika", "samasa_cand"} | tags | {linga or "pulliṅga"}, meta={"upadesha_slp1": stem}))
        terms.append(Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence(up)),
                          tags={"pratyaya", "sup", "upadesha", f"vib:{VIB_NAME[vib]}"}, meta={"upadesha_slp1": up}))
    state = State(terms=terms, meta={"adhikara_frames": "samasa"}, trace=[])
    set_vivaksha(state, **vivaksha)
    return state
