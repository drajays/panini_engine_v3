"""
3.2.76  क्विप् च  —  VIDHI (narrow *glass-box*)

Śāstra anchor: *kṛt* *kvip* after *upapada* *karman* in *śāstrīya* *prayoga*s such as
*ratnāni dadhāti* → *ratnadhā* (``prakriya_22`` JSON).

Engine (v3):
  When ``state.meta['kvip_recipe']`` is True and the tape already bears a
  *dhātu* ``Term`` without a *kvip* ``Term``, append ``kvip`` as a ``krt`` *pratyaya*
  immediately after that *dhātu*.

Mechanical blindness:
  ``cond`` reads tags + ``state.meta`` only (never *vibhakti* / gold surface).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 32076 · क्विप् च
              padaccheda: क्विँप् च
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ्
  Source #2 — Kāśikā 3.2.76 udāharaṇa:
                उखायाः स्रंसते उखास्रत्
                पर्णध्वत्
                वाहाद् भ्रश्यति वाहाभ्रट्
  Cross-check — surface pinned by: tests/unit/test_agnicit_agni_ci_kvip.py, tests/unit/test_ratnaDAtamam.py
  Reference record: sutra_ref_out/3_2_76.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _already_has_kvip(state: State) -> bool:
    return any(t.meta.get("upadesha_slp1") == "kvip" for t in state.terms)


def cond(state: State) -> bool:
    if not state.meta.get("kvip_recipe"):
        return False
    if _already_has_kvip(state):
        return False
    return _dhatu_index(state) is not None


def act(state: State) -> State:
    if not cond(state):
        return state
    di = _dhatu_index(state)
    if di is None:
        return state
    kvip = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("kvip")),
        tags={"pratyaya", "upadesha", "krt"},
        meta={"upadesha_slp1": "kvip"},
    )
    state.terms.insert(di + 1, kvip)
    state.meta.pop("kvip_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.2.76",
    sutra_type=SutraType.VIDHI,
    text_slp1="kvip ca",
    text_dev="क्विप् च",
    padaccheda_dev="क्विप् / च",
    why_dev="उपपद-कर्मणि धातोः क्विप्-प्रत्ययः (प्रक्रिया-२२, ग्लास-बॉक्स्)।",
    anuvritti_from=("3.2.84",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
