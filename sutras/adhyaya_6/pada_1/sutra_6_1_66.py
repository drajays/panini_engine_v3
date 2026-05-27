"""
6.1.66  हल्ङ्याब्भ्यो दीर्घात् सुतिपृक्तं हल्  —  VIDHI

Five operational paths — all arm-free, phonemic/tag-based:
  1. Original narrow path: elide apṛkta s after long-vowel upadhā tṛc stem.
  2. vidhi-liṅ y-lopa: Term tagged "yasut_agama" ends in 'y' before HAL.
  3. āśīr-liṅ 2sg sip-derived s lopa: single 's' tiṅ-ādeśa after yasut_agama term.
  4. luṅ vuk v-lopa: Term with meta["vuk_6_4_88"] ends in 'v' before HAL.
  5. karmani vidhi-liṅ sīyuṭ y-lopa: Term tagged "ling_sIyuw" ends in 'y' before HAL.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL
from phonology.pratyahara import is_dirgha


def _find_tfc_aprkta(state: State):
    """Original tṛc-stem + apṛkta-s lopa."""
    if len(state.terms) < 2:
        return None
    ang = state.terms[0]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return None
    if ang.meta.get("apṛkta_hal_lopa_6_1_66_done"):
        return None
    vs = ang.varnas
    if len(vs) < 3:
        return None
    if vs[-1].slp1 != "n":
        return None
    if not is_dirgha(vs[-2].slp1):
        return None
    if len(sup.varnas) != 1:
        return None
    if sup.varnas[0].slp1 != "s":
        return None
    if sup.varnas[0].slp1 not in HAL:
        return None
    return "tfc"


def _find_yasut_y(state: State):
    """liG: yāsuṭ remnant [i,y] with 'y' before HAL-initial next term."""
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if t.meta.get("6_1_66_yasut_y_lopa_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "y":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        if nxt.varnas[0].slp1 not in HAL:
            continue
        return i
    return None


def _find_ashir_sip_s(state: State):
    """āśīr-liṅ 2sg: single apṛkta 's' term after yāsuṭ term."""
    for i, t in enumerate(state.terms):
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("6_1_66_ashir_sip_done"):
            continue
        if len(t.varnas) != 1 or t.varnas[0].slp1 != "s":
            continue
        if i == 0:
            continue
        prev = state.terms[i - 1]
        if "yasut_agama" not in prev.tags:
            continue
        return i
    return None


def _find_vuk_v(state: State):
    """luṅ: vuk term (single 'v' after it-lopa) before HAL-initial next term."""
    for i, t in enumerate(state.terms):
        if not t.meta.get("vuk_6_4_88"):
            continue
        if t.meta.get("6_1_66_vuk_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "v":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        if nxt.varnas[0].slp1 not in HAL:
            continue
        return i
    return None


def _find_karmani_iy(state: State):
    """karmani: drop y from iy within tiṅ ādeśa (after 7.2.81: Ate→iyte).
    Finds the 'y' at varnas[1] of a pratyaya starting with i+y, before a HAL."""
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if t.meta.get("6_1_66_karmani_iy_done"):
            continue
        vs = t.varnas
        if len(vs) < 3:
            continue
        if vs[0].slp1 != "i" or vs[1].slp1 != "y":
            continue
        if vs[2].slp1 not in HAL:
            continue
        return i
    return None


def _find_siyuw_y(state: State):
    """karmani vidhi-liṅ: drop y from sīyuṭ-remnant [I,y] (ling_sIyuw term)
    before HAL-initial next term."""
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("6_1_66_siyuw_y_lopa_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "y":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if not nxt.varnas:
            continue
        if nxt.varnas[0].slp1 not in HAL:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return (
        _find_tfc_aprkta(state) is not None
        or _find_yasut_y(state) is not None
        or _find_ashir_sip_s(state) is not None
        or _find_vuk_v(state) is not None
        or _find_karmani_iy(state) is not None
        or _find_siyuw_y(state) is not None
    )


def act(state: State) -> State:
    if _find_tfc_aprkta(state) is not None:
        state.terms.pop()
        state.meta["apṛkta_hal_lopa_6_1_66_done"] = True
        state.meta["pratyaya_lopa_nimitta"] = True
        return state

    idx = _find_yasut_y(state)
    if idx is not None:
        t = state.terms[idx]
        if t.varnas and t.varnas[-1].slp1 == "y":
            del t.varnas[-1]
        t.meta["6_1_66_yasut_y_lopa_done"] = True
        state.samjna_registry["6.1.66_yasut_y_lopa"] = True
        return state

    idx = _find_ashir_sip_s(state)
    if idx is not None:
        state.terms[idx].meta["6_1_66_ashir_sip_done"] = True
        state.terms.pop(idx)
        state.samjna_registry["6.1.66_ashir_sip_s_lopa"] = True
        return state

    idx = _find_vuk_v(state)
    if idx is not None:
        state.terms[idx].meta["6_1_66_vuk_done"] = True
        state.terms.pop(idx)
        state.samjna_registry["6.1.66_vuk_v_lopa"] = True
        return state

    idx = _find_karmani_iy(state)
    if idx is not None:
        t = state.terms[idx]
        del t.varnas[1]  # drop y at position 1 (i-y-hal → i-hal)
        t.meta["6_1_66_karmani_iy_done"] = True
        t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
        state.samjna_registry["6.1.66_karmani_iy_lopa"] = True
        return state

    idx = _find_siyuw_y(state)
    if idx is not None:
        t = state.terms[idx]
        del t.varnas[-1]  # drop final y from [I,y]
        t.meta["6_1_66_siyuw_y_lopa_done"] = True
        state.samjna_registry["6.1.66_siyuw_y_lopa"] = True
        return state

    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.66",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "halNyAByo dIrGAt suti pfktam hal",
    text_dev       = "हल्ङ्याब्भ्यो दीर्घात् सुतिपृक्तं हल्",
    padaccheda_dev = "हल्-ङि-आप्-भ्यः दीर्घात् सुति पृक्तं हल्",
    why_dev        = (
        "तृच्-पथ: दीर्घात् परस्य अपृक्त हल्-लोपः (सु→स्)। "
        "विधि-लिङ्-पथ: यासुट्-अवशेष [i,y] में य्-लोपः हल्-पूर्वे। "
        "आशीर्-लिङ्-पथ (२मध्यम-एक): यासुट्-पश्चात् सिप्-जन्य-स्-लोपः। "
        "कर्मणि-पथ: ७.२.८१-जन्य इय् में य्-लोपः हल्-पूर्वे (इय्ते→इते)। "
        "कर्मणि-विधिलिङ्-पथ: सीयुट्-अवशेष [I,y] में य्-लोपः हल्-पूर्वे।"
    ),
    anuvritti_from = ("6.1.65",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
