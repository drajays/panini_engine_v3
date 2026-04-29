"""
2.1.13  लक्षणेनाभिप्रती आभिमुख्ये  —  VIDHI (narrow v3 demo slice)

Used in the user's *pratyagni* derivation: agnim prati → pratyagni (avyayībhāva).

Engine approach (glass-box):
  - Pipeline arms ``meta['2_1_13_prati_abhimukhya_arm']=True``.
  - If an avyaya member with ``upadesha_slp1 == 'prati'`` is present, mark the
    samāsa members as ``avyayibhava`` so downstream 1.2.43 / 2.2.30 / 1.1.41 fire.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_2.pada_1.sutra_2_1_6 import TAG_AVYAYIBHAVA


def _has_prati(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") == "prati" and ("avyaya" in t.tags or t.kind == "nipata")) for t in state.terms)


def cond(state: State) -> bool:
    if not state.meta.get("2_1_13_prati_abhimukhya_arm"):
        return False
    if state.samjna_registry.get("2_1_13_prati_abhimukhya"):
        return False
    return _has_prati(state)


def act(state: State) -> State:
    for t in state.terms:
        if "samasa_member" in t.tags or "anga" in t.tags:
            t.tags.add(TAG_AVYAYIBHAVA)
    state.samjna_registry["2_1_13_prati_abhimukhya"] = True
    state.meta["avyayibhava_kind"] = "2.1.13"
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.1.13",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1      = "lakzaNenABhipratI ABimuKye",
    text_dev       = "लक्षणेनाभिप्रती आभिमुख्ये",
    padaccheda_dev = "लक्षणेन / अभिप्रती / आभिमुख्ये",
    why_dev        = "प्रति-प्रत्यय-योगे आभिमुख्ये अव्ययीभावः (demo arm meta).",
    anuvritti_from = ("2.1.5",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

