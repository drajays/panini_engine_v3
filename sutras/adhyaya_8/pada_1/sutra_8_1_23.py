"""
8.1.23  त्वामौ द्वितीयायाः  —  VIDHI (narrow *glass-box*)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=81023):** *tvāmau dvitīyāyāḥ* — optional
*ādeśa* of the accusative *padam* ``tvAm`` → ``tvA`` (and, in full *śāstra*,
``mAm`` → ``mA``) when the *prayoga* satisfies *apādādau* (recipe-asserted here
via ``state.meta['prakriya_23_apAda_adau_arm']``).

Engine:
  • ``cond`` requires ``state.meta['prakriya_23_8_1_23_arm']`` and exactly one
    ``prakṛti``/``prātipadika`` ``Term`` whose ``meta['upadesha_slp1']`` is
    ``'tvAm'`` (lexical *pada* label — not *vibhakti* coordinates).
  • ``act`` rewrites varṇas to ``tvA`` and records ``meta['8_1_23_tvA_adesha']``.
  • If ``adhikara_stack`` already bears **8.1.18**, sets
    ``meta['sarva_anudAtta_8_1_18']`` on that ``Term`` (*anudāttaṃ sarvam…*
    *anuvāda* for this *corpus* slice).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State) -> int | None:
    if not state.meta.get("prakriya_23_8_1_23_arm"):
        return None
    if not state.meta.get("prakriya_23_apAda_adau_arm"):
        return None
    if len(state.terms) != 1:
        return None
    t0 = state.terms[0]
    if t0.kind != "prakriti":
        return None
    if t0.meta.get("upadesha_slp1") != "tvAm":
        return None
    if t0.meta.get("8_1_23_tvA_adesha"):
        return None
    return 0


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    j = _site(state)
    if j is None:
        return state
    t = state.terms[j]
    t.varnas = list(parse_slp1_upadesha_sequence("tvA"))
    t.meta["upadesha_slp1"] = "tvA"
    t.meta["8_1_23_tvA_adesha"] = True
    if any(e.get("id") == "8.1.18" for e in state.adhikara_stack):
        t.meta["sarva_anudAtta_8_1_18"] = True
    state.meta.pop("prakriya_23_8_1_23_arm", None)
    state.meta.pop("prakriya_23_apAda_adau_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.23",
    sutra_type=SutraType.VIDHI,
    text_slp1="tvAmau dvitIyAyAH",
    text_dev="त्वामौ द्वितीयायाः",
    padaccheda_dev="त्वामौ / द्वितीयायाः",
    why_dev="अपादादौ त्वाम्-पदस्य त्वा-आदेशः (प्रक्रिया-२३, ग्लास-बॉक्स्)।",
    anuvritti_from=("8.1.17",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
