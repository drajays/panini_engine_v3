"""
3.3.161  विधिनिमन्त्रणामन्त्रणाधीष्टसम्प्रश्नप्रार्थनेषु लिङ्  —  VIDHI (narrow: *vidhi-liṅ*)

Teaching **P038** (*paceran*): in *vidhi* / *nimantraṇa* / … senses, introduce the
*lakāra* placeholder ``liG`` (*liṅ*).

Engine:
  - recipe arms ``state.meta['P038_3_3_161_vidhi_liG_arm']``.
  - appends ``liG`` like **3.3.173**, but sets ``vidhi_liG`` (not ``ashir_liG``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("P038_3_3_161_vidhi_liG_arm"):
        return False
    return not any((t.meta.get("upadesha_slp1") or "").strip() == "liG" for t in state.terms)


def act(state: State) -> State:
    if not cond(state):
        return state
    liG = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("liG"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "liG"},
    )
    state.terms.append(liG)
    state.meta["vidhi_liG"] = True
    state.meta.pop("P038_3_3_161_vidhi_liG_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.161",
    sutra_type=SutraType.VIDHI,
    text_slp1="vidhinimantraRAmantraRAxISwasampraSnaprArTanezu liG",
    text_dev="विधिनिमन्त्रणामन्त्रणाधीष्टसम्प्रश्नप्रार्थनेषु लिङ्",
    padaccheda_dev="विधि-निमन्त्रणा-मन्त्रणा-अधीष्ट-सम्प्रश्न-प्रार्थनेषु लिङ्",
    why_dev="विधि-मन्त्रणादिषु लिङ्-लकारः (ग्लास-बॉक्स्: P038)।",
    anuvritti_from=("3.3.157",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
