"""
1.2.8  रुदविदमुषग्रहिस्वपिप्रच्छः सँश्च  —  VIDHI (narrow demo)

Demo slice (पृष्ट्वा):
  For the listed dhātus, the suffix `ktvā` is treated as *kitvat* (kṅit-locus),
  which licenses samprasāraṇa / cch→ś and blocks guṇa where applicable.

Engine:
  - detects a dhātu in the narrow list and a following kṛt pratyaya whose
    ``upadesha_slp1_original`` is `ktvA`, and tags that pratyaya with ``kngiti``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


_DHATU_SET = {"rud", "vid", "muz", "grah", "svap", "pfcC", "ci"}


def _find(state: State) -> int | None:
    if len(state.terms) < 2:
        return None
    d0 = state.terms[0]
    if "dhatu" not in d0.tags:
        return None
    up = (d0.meta.get("upadesha_slp1") or "").strip()
    if up not in _DHATU_SET:
        return None
    for i in range(1, len(state.terms)):
        t = state.terms[i]
        if "pratyaya" not in t.tags:
            continue
        # ktvā-branch (old)
        orig = (t.meta.get("upadesha_slp1_original") or "").strip()
        up = (t.meta.get("upadesha_slp1") or "").strip()
        is_ktva = ("krt" in t.tags) and orig == "ktvA"
        # san-branch (desiderative): treat `san`/`is` as kitvat too.
        is_san = ("sanadi" in t.tags) and (up in {"san", "is"})
        if not (is_ktva or is_san):
            continue
        if "kngiti" in t.tags:
            return None
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("kngiti")
    state.samjna_registry["1.2.8_rudadi_ktva_kngiti"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.8",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="rudavidamuza-grahisvapi-pfcCaH saMzca",
    text_dev="रुदविदमुषग्रहिस्वपिप्रच्छः सँश्च",
    padaccheda_dev="रुद-विद-मुष-ग्रहि-स्वपि-प्रच्छः / सन् च",
    why_dev="एतेभ्यः क्त्वा-प्रत्ययः किद्वत् (सम्प्रसारणादि-प्रसङ्गः) — पृष्ट्वा।",
    anuvritti_from=("1.2.7",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

