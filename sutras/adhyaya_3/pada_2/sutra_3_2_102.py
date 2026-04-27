"""
3.2.102  निष्ठा  —  VIDHI (narrow: *kta* after *dhātu* in *niṣṭhā* recipes)

**Pāṭha (machine index i=32102):** *niṣṭhā* — *bhūte* *kṛt* **kta** / **ktavatu**…
(adhikāra scope per local ``krit_pratyaya.json`` *vidhana_sutra_range*).

Glass-box v3: when ``state.meta["3_2_102_kta_arm"]`` **or**
``state.meta["3_2_102_ktavatu_arm"]`` is set and ``terms[0]`` is a *dhātu* whose
``meta["upadesha_slp1"]`` matches ``state.meta["3_2_102_target_upadesha_slp1"]``
(recipe-selected *upadeśa* row), append **kta** or **ktavatu~** as a *kṛt* ``Term``
with ``kngiti`` (**1.1.5** *kit* after **1.3.8** drops initial ``k`` *it*;
**ktavatu~** also supplies **1.3.2** *anunāsika* *it* on final ``u`` for *ugit*).

Optional: ``state.meta["3_2_102_bhinn_before_tavat_arm"]`` (``*ktavatu~*`` only)
rewrites ``Bid`` → ``Binn`` on the *dhātu* tape before the *kṛt* is appended
(glass-box *bhid* row; **6.1.111** then drops the *t* onset of *tavat* so *Binn*
+ *avat* merges).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _target_upadesha(state: State) -> str:
    m = (state.meta.get("3_2_102_target_upadesha_slp1") or "").strip()
    if m:
        return m
    # Back-compat: older recipes only used *ciñ* rows.
    return "ciY"


def cond(state: State) -> bool:
    if not (state.meta.get("3_2_102_kta_arm") or state.meta.get("3_2_102_ktavatu_arm")):
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "dhatu" not in t0.tags:
        return False
    if (t0.meta.get("upadesha_slp1") or "").strip() != _target_upadesha(state):
        return False
    if state.samjna_registry.get("3.2.102_krt_attached"):
        return False
    return True


def act(state: State) -> State:
    t0 = state.terms[0]
    if state.meta.get("3_2_102_ktavatu_arm") and state.meta.get("3_2_102_bhinn_before_tavat_arm"):
        if "".join(v.slp1 for v in t0.varnas) == "Bid":
            t0.varnas = parse_slp1_upadesha_sequence("Binn")
        state.meta.pop("3_2_102_bhinn_before_tavat_arm", None)
    if state.meta.get("3_2_102_kta_arm"):
        pr = Term(
            kind="pratyaya",
            varnas=parse_slp1_upadesha_sequence("kta"),
            tags={"krt", "upadesha", "kngiti"},
            meta={"upadesha_slp1": "kta"},
        )
        state.terms.append(pr)
    else:
        pr = Term(
            kind="pratyaya",
            varnas=parse_slp1_upadesha_sequence("ktavatu~"),
            tags={"krt", "upadesha", "kngiti"},
            meta={"upadesha_slp1": "ktavatu~"},
        )
        state.terms.append(pr)
    state.samjna_registry["3.2.102_krt_attached"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.102",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nisthA",
    text_dev       = "निष्ठा",
    padaccheda_dev = "निष्ठा",
    why_dev        = "भूतकालादौ धातोः क्त/क्तवतु-प्रत्ययः (ग्लास-बॉक्स्: चि+क्त → चित; चि+क्तवतु → चितवत्)।",
    anuvritti_from = ("3.1.91",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
