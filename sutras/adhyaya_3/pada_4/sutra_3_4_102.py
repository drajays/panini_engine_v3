"""
3.4.102  लिङस्सीयुट्  —  VIDHI (narrow demo)

Demo slice (भित्सीष्ट / BitzIzwa):
  For āśīr-liṅ, insert the augment **sīyut** before the *tiṅ* ādeśa.

**P038** (*vidhi-liṅ*, *paceran*): when ``vidhi_liG`` is set, insert full ``sIyuw``
before the ``liG`` *lakāra* placeholder (then **3.4.78** replaces ``liG``).

*Āśīr* path: the augment is सीय् (``sIy``; ṭ and उ removed as anubandhas),
ārdhadhātuka by 3.4.116. 6.1.66 लोपो व्योर्वलि drops its य् before a val
(एधिषीष्ट, एधिषीरन्) and keeps it before a vowel (एधिषीयास्ताम्, एधिषीय).

Engine:
  - recipe arms via ``state.meta['sIyuw_recipe']``.
  - inserts a pratyaya Term tagged ``ling_sIyuw`` immediately before the final
    *tiṅ* term (``ashir_liG``) **or** before ``liG`` (``vidhi_liG``).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34102 · लिङस्सीयुट्
              padaccheda: लिङः सीयुट्
  Source #2 — Kāśikā 3.4.102 udāharaṇa:
                टकारो देशविध्यर्थः
                उकार उच्चारणार्थः
                पचेत
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_paceran_vidhi_liG_pac_Ja.py, tests/unit/test_saGgasIzwa_sam_gam_ashir_ling.py
  Reference record: sutra_ref_out/3_4_102.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_tin_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" in t.tags:
            return i
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG"}:
            return i
    return None


def _find_liG_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "liG":
            continue
        if "lakAra_pratyaya_placeholder" not in t.tags:
            continue
        return i
    return None


_ATMANE = frozenset({"ta", "AtAm", "Ja", "TAs", "ATAm", "Dvam", "iw", "vahi", "mahiG", "ran"})   # the nine (3.4.78, ātmanepada) and 3.4.105's ran


def _structural_idx(state: State) -> int | None:
    """liṅaḥ sīyuṭ read off the tape (no recipe flag): an ātmanepada tiṅ ādeśa whose sthānī is liṅ, not yet augmented."""
    if any("ling_sIyuw" in t.tags for t in state.terms):
        return None
    for i, t in enumerate(state.terms):
        if ("tin_adesha_3_4_78" in t.tags and "parasmaipada" not in t.tags    # sīyuṭ is ātmanepada's; parasmaipada has yāsuṭ
                and (t.meta.get("source_lakara_upadesha") or "").strip() == "liG"
                and ("atmanepada" in t.tags or t.meta.get("3_4_106_done")           # iṭ→a (3.4.106) is ātmanepada's
                     or (t.meta.get("upadesha_slp1") or "").strip() in _ATMANE)):
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("sIyuw_recipe"):
        return _structural_idx(state) is not None
    if any("ling_sIyuw" in t.tags for t in state.terms):
        return False
    if state.meta.get("ashir_liG"):
        return _find_tin_index(state) is not None
    if state.meta.get("vidhi_liG"):
        # karmani vidhi-liG: tiṅ ādeśa already installed (no liG placeholder)
        if state.meta.get("karmani_liG_recipe"):
            return _find_tin_index(state) is not None
        return _find_liG_index(state) is not None
    return False


def act(state: State) -> State:
    if not state.meta.get("sIyuw_recipe") and (idx := _structural_idx(state)) is not None:
        ashir = "ashir_liG" in state.terms[idx].tags        # āśiṣi liṅ (3.3.173) marks its tiṅ; then ārdhadhātuka (3.4.116)
        sI = Term(kind="pratyaya", varnas=parse_slp1_upadesha_sequence("sIy"),
                  tags={"pratyaya", "ling_sIyuw"}, meta={"upadesha_slp1": "sIy"})
        if "kngiti" in state.terms[idx].tags and not ashir:   # āśīr-liṅ is ārdhadhātuka (3.4.116): 1.2.4 does not make it ṅit
            sI.tags.add("kngiti")
        if ashir:
            sI.tags.add("ardhadhatuka")
            for v in sI.varnas:                   # 8.3.78 ṣīdhvam: the sīyuṭ of āśīr-liṅ stays findable after the merge
                v.tags.add("ashir_sIy_v")
        state.terms.insert(idx, sI)
        return state
    if state.meta.get("ashir_liG"):
        idx = _find_tin_index(state)
        slp = "sIy"
    elif state.meta.get("vidhi_liG"):
        if state.meta.get("karmani_liG_recipe"):
            idx = _find_tin_index(state)
        else:
            idx = _find_liG_index(state)
        slp = "sIy"   # sīy after IT-lopa of ṭ (halantyam); uccharaṇārtha u also elided
    else:
        return state
    if idx is None:
        return state
    sI = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(slp),
        tags={"pratyaya", "ling_sIyuw"},
        meta={"upadesha_slp1": slp},
    )
    if "kngiti" in state.terms[idx].tags:      # ṭit āgama: part of the (ṅit) tiṅ, 1.1.46
        sI.tags.add("kngiti")
    if state.meta.get("ashir_liG"):            # 3.4.116 लिङाशिषि: ārdhadhātuka
        sI.tags.add("ardhadhatuka")
    state.terms.insert(idx, sI)
    state.meta["sIyuw_recipe"] = False
    state.meta.pop("karmani_liG_recipe", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.102",
    sutra_type=SutraType.VIDHI,
    text_slp1='liNassIyuw',
    text_dev='लिङस्सीयुट्',
    samagra_slp1="liNaH sIyuw",
    samagra_dev="लिङः सीयुट्",
    padaccheda_dev="लिङः / सीयुट्",
    why_dev="लिङि सीयुट्-आगमः — आशीर्लिङ् (भित्सीष्ट) अथवा विधि-लिङ् (P038)।",
    anuvritti_from=("3.4.77", "3.4.78"),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

