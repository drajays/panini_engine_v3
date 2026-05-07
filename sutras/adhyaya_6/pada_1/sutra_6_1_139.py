"""
6.1.139  उपात्प्रतियत्नवैकृतवाक्याध्याहारेषु  —  VIDHI (narrow)

*Pāṭha (teaching source:* `ashtadhyayi.github.io` *6.1 section; cross-check*
``ashtadhyayi-com/data`` *``data.txt`` i-key)*.

Under **6.1.135** *suṭ kāt pūrvaḥ*, *suṭ*-style augment before **कृ** after the
*upasarga* **उप** in the bundle sense slice (**``corrected_prakriyas_v2``** row
**P011-B**).

**CONSTITUTION Art. 2:** ``cond`` does not read prayoga semantics (*pratiyatna*
etc.); the recipe arms ``state.meta['corrected_v2_P011_B_6_1_139_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _upa_before_kf(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        up = (t.meta.get("upadesha_slp1") or "").strip().replace("~", "")
        if up != "upa":
            continue
        if "upasarga" not in t.tags:
            continue
        nxt = state.terms[i + 1]
        if "dhatu" not in nxt.tags:
            continue
        dh_up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if dh_up not in {"kf", "qukfY"}:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("corrected_v2_P011_B_6_1_139_arm"):
        return False
    i = _upa_before_kf(state)
    if i is None:
        return False
    ins = i + 1
    if ins < len(state.terms):
        mid = state.terms[ins]
        if (mid.meta.get("upadesha_slp1") or "").strip() in {"suw", "suT"}:
            return False
    return True


def act(state: State) -> State:
    i = _upa_before_kf(state)
    if i is None:
        return state
    su = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("suT")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "suT"},
    )
    state.terms.insert(i + 1, su)
    state.meta["corrected_v2_P011_B_6_1_139_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.139",
    sutra_type=SutraType.VIDHI,
    text_slp1="upAt pratiyatnavaikftavAkyAdhyAhArezu",
    text_dev="उपात्प्रतियत्नवैकृतवाक्याध्याहारेषु",
    padaccheda_dev="उपात् / प्रतियत्न-वैकृत-वाक्याध्याहारेषु",
    why_dev="उप-पूर्वक-कृञि सुट्-आगमः (डेमो: उपस्कुरुते) — षष्ठ्यर्थानुवृत्तौ।",
    anuvritti_from=("6.1.135",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
