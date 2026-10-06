"""
3.4.107  सुट् तिथोः  —  VIDHI (āśīr-liṅ: full 9-cell)

Insert the augment **suṭ** (surface ``s``) immediately before a tiṅ ādeśa
that begins with dental **t** or **tha** (= SLP1 't' or 'T') in āśīr-liṅ.

This fires for: 3sg (t), 3du (tāṃ), 2du (tam), 2pl (ta) — all t-initial.
Does NOT fire for: 3pl (us), 2sg (s), 1sg (am), 1du (va), 1pl (ma).
Ātmanepada: त, थास् take सुट् before them (सीष्ट, सीष्ठाः); in आताम्, आथाम्
the सुट् goes before the inner त/थ (सीयास्ताम्, सीयास्थाम्).

Engine:
  - arm ``state.meta['suw_recipe']`` + ``state.meta['ashir_liG']``.
  - suṭ Term tagged ``suw_agama``.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34107 · सुट् तिथोः
              padaccheda: सुट् ति-थोः
              anuvṛtti:   34102: लिङः
  Source #2 — Kāśikā 3.4.107 udāharaṇa:
                लिङ्संबन्धिनोस्तकारथकारयोः सुडागमो भवति
                तकारथकारावागमिनौ
                सीयुटस्तु लिङेवागमी
  Cross-check — surface pinned by: tests/unit/test_BitzIzwa_ashir_ling.py, tests/unit/test_saGgasIzwa_sam_gam_ashir_ling.py, tests/unit/test_tinanta_bhuyat_ashirling.py
  Reference record: sutra_ref_out/3_4_107.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk


def _find_tin_t_initial(state: State) -> int | None:
    """Find the rightmost tiṅ ādeśa whose first varṇa is dental t or T."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if not t.varnas:
            continue
        if t.varnas[0].slp1 not in ('t', 'T'):
            continue
        # Idempotency: skip if suṭ is already before this tiṅ
        if i > 0 and "suw_agama" in state.terms[i - 1].tags:
            continue
        return i
    return None


def _find_tin_t_medial(state: State) -> tuple[int, int] | None:
    """(term, varṇa) of a non-initial t/T inside an ātmanepada tiṅ (आताम्, आथाम्):
    the सुट् is an āgama of the t/th itself (Kāśikā: तकारथकारावागमिनौ)."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("suw_3_4_107_done"):
            continue
        for j, v in enumerate(t.varnas[1:], start=1):
            if v.slp1 in ("t", "T"):
                return i, j
    return None


def _atmane_liG_site(state: State):
    """ātmanepada liṅ (vidhi or āśīr): ("init", i) before a t/th-initial tiṅ (ta, thās), or ("medial", i, j) inside
    ātām/āthām — read off the tape: sthānī liṅ, no parasmaipada tag, no suṭ yet (3.4.107 सुट् तिथोः)."""
    for i, t in enumerate(state.terms):
        if (t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags or "parasmaipada" in t.tags
                or t.meta.get("suw_3_4_107_done") or (t.meta.get("source_lakara_upadesha") or "").strip() != "liG"
                or not t.varnas):
            continue
        if i > 0 and "suw_agama" in state.terms[i - 1].tags:
            continue
        if not any("ling_sIyuw" in u.tags for u in state.terms[:i]):     # suṭ follows sīyuṭ (3.4.102 first)
            continue
        if t.varnas[0].slp1 in ("t", "T"):
            return ("init", i)
        for j, v in enumerate(t.varnas[1:], start=1):
            if v.slp1 in ("t", "T"):
                return ("medial", i, j)
    return None


def _structural_site(state: State) -> bool:
    idx = _find_tin_t_initial(state)
    return idx is not None and "ashir_liG" in state.terms[idx].tags and "parasmaipada" in state.terms[idx].tags


def cond(state: State) -> bool:
    if _structural_site(state) or _atmane_liG_site(state):
        return True
    if not state.meta.get("suw_recipe"):
        return False
    if not (
        state.meta.get("ashir_liG")
        or state.meta.get("_liG_ad_spine")
    ):
        return False
    if _find_tin_t_initial(state) is not None:
        return True
    return bool(state.meta.get("ashir_liG")) and _find_tin_t_medial(state) is not None


def act(state: State) -> State:
    hit = None if state.meta.get("suw_recipe") else _atmane_liG_site(state)
    if hit is not None:
        if hit[0] == "medial":
            _, i, j = hit
            s_v = mk("s")
            s_v.tags.update({"suw_agama", "suw_s"})
            state.terms[i].varnas.insert(j, s_v)
            state.terms[i].meta["suw_3_4_107_done"] = True
        else:
            s_v = mk("s")
            s_v.tags.add("suw_s")
            state.terms.insert(hit[1], Term(kind="pratyaya", varnas=[s_v], tags={"pratyaya", "suw_agama"},
                                            meta={"upadesha_slp1": "s", "suw_agama": True}))
        state.samjna_registry["3.4.107_suw_inserted"] = True
        return state
    idx = _find_tin_t_initial(state)
    if idx is None:
        hit = _find_tin_t_medial(state)
        if hit is None:
            return state
        i, j = hit
        s_v = mk("s")
        s_v.tags.update({"suw_agama", "suw_s"})
        state.terms[i].varnas.insert(j, s_v)
        state.terms[i].meta["suw_3_4_107_done"] = True
        state.meta["suw_recipe"] = False
        state.samjna_registry["3.4.107_suw_inserted"] = True
        return state
    s_v = mk("s")
    s_v.tags.add("suw_s")            # survives pada_merge, so 8.2.26 (झलो झलि) can find it
    suw = Term(
        kind="pratyaya",
        varnas=[s_v],
        tags={"pratyaya", "suw_agama"},
        meta={"upadesha_slp1": "s", "suw_agama": True},
    )
    state.terms.insert(idx, suw)
    state.meta["__why_now_dev__"] = "आशिषि लिङः त-थ-आदि तिङः पूर्वं सुट्-आगमः — भू + यास् + त् → भू + यास् + स् + त् (भूयात्)। (३.४.१०७)"
    state.meta["suw_recipe"] = False
    state.samjna_registry["3.4.107_suw_inserted"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.107",
    sutra_type=SutraType.VIDHI,
    text_slp1="suw tiToH",
    text_dev="सुट् तिथोः",
    samagra_slp1="liNaH tiToH suw",
    samagra_dev="लिङः तिथोः सुट्",
    padaccheda_dev="सुट् / तिथोः",
    why_dev=(
        "आशीर्-लिङि त-थ-प्रारम्भ-तिङ्-आदेशात् पूर्वं सुट्-आगमः — "
        "३सग (त्), ३द्वि (ताम्), २द्वि (तम्), २बहु (त)।"
    ),
    anuvritti_from=("3.4.77",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
