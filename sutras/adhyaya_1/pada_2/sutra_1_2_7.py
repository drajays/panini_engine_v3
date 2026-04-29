"""
1.2.7  मृडमृदगुधकुषक्लिशवदवसः क्त्वा  —  VIDHI (narrow demo)

Demo slice (मृडित्वा):
  After specific dhātus (mṛḍ etc.), the kṛt suffix `ktvā` is treated as *kit*
  (kṅit-locus), so guṇa is blocked (via 1.1.5 contract) even if the suffix is
  seṭ (took iṭ).

Engine:
  - looks for a dhātu in the narrow demo list and a following kṛt pratyaya whose
    ``upadesha_slp1_original`` is `ktvA` (we model surface as `tvA`).
  - tags that pratyaya with ``kngiti``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


_DHATU_SET = {"mfq", "mfd", "guD", "kuz", "kliz", "vad", "vas"}


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
        if "pratyaya" not in t.tags or "krt" not in t.tags:
            continue
        orig = (t.meta.get("upadesha_slp1_original") or "").strip()
        if orig != "ktvA":
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
    state.samjna_registry["1.2.7_mrdadi_ktva_kngiti"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.7",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="mfqamfdaguDakuZaklizavadvasaH ktvA",
    text_dev="मृडमृदगुधकुषक्लिशवदवसः क्त्वा",
    padaccheda_dev="मृड-मृद-गुध-कुष-क्लिश-वद-वसः / क्त्वा",
    why_dev="एतेभ्यः क्त्वा-प्रत्ययः नित्यं किद्वत् — गुण-निषेध-प्रयोजनम् (मृडित्वा)।",
    anuvritti_from=("1.2.6",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

