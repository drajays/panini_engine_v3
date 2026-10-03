"""
6.1.97  अतो गुणे  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=60197
- Kāśikā: अतो गुणे — गुणे पररूपम् (एकादेशः) यत्र अकारो द्विर्वर्तते।
- Cross-validation: regression tests/unit/test_corrected_prakriyas_v2_bundle.py
  (P013 SuSrUzate, P017 pawapawAyati); pipelines/asmad_subanta.py paradigm cells.

Operational role (v3.6): one structural rule, no paradigm coordinates.

A short ``a`` that is **not padānta** (the Term is not tagged ``pada``, or the
``a`` is not its last varṇa) followed immediately by a guṇa vowel (``a`` ``e``
``o``) is deleted — the following guṇa vowel stands alone (pararūpa).  The
scan is over the flat varṇa stream, so it covers a pair inside one Term
(merged pada ``pacatha``, asmad/tyadādi stems) and across a Term boundary
(vikaraṇa/dhātu ``a`` + tiṅ ``anti``/``ete``).  Terms emptied by lopa are
invisible (1.1.60).

At a *sup* junction a para sup-ādeśa / ekādeśa rule wins (1.4.2 vipratiṣedha:
anya+jas → 7.1.17, rāma+jas → 6.1.102, rāma+ṅas → 7.1.12), so there the rule only
fires for asmad/yuṣmad stems (``_sup_junction_is_ours``).  The fixed
subanta lists do not run the scheduler's resolver, hence this explicit guard.
The one non-phonemic helper kept is P017's ``pawat+pawat+qAc`` merge.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

_GUNA = frozenset("aeo")


_ASMAD_DONE_TAGS = frozenset({
    "7_2_94_done", "7_2_92_done", "7_2_93_done", "7_2_95_done", "7_2_96_done",
})


def _sup_junction_is_ours(left: Term) -> bool:
    """
    At a *sup* junction a para sup-ādeśa / ekādeśa rule (7.1.12-17, 6.1.102-110)
    normally wins (1.4.2), so 6.1.97 only takes it for asmad/yuṣmad stems whose own
    aṅga-ādeśa (7.2.9x) is done and where no sup-ādeśa competes.
    """
    if "anga" not in left.tags:
        return False
    return bool(left.tags & _ASMAD_DONE_TAGS) or bool(left.tags & {"asmad_stem", "yuzmad_stem"})


def _find_p017_pararupa(state: State) -> bool:
    """P017: ``pawat`` + ``pawat`` + ``qAc`` → ``pawapawat`` before *it* lopa."""
    if len(state.terms) != 3:
        return False
    t0, t1, t2 = state.terms
    if t0.meta.get("p017_pararupa_done"):
        return False
    if "".join(v.slp1 for v in t0.varnas) != "pawat" or "".join(v.slp1 for v in t1.varnas) != "pawat":
        return False
    return (t2.meta.get("upadesha_slp1") or "").strip() == "qAc"


def _find_pair(state: State) -> tuple[int, int] | None:
    """(term_i, varna_i) of an apadānta short ``a`` directly before a guṇa vowel."""
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for n, ti in enumerate(live):
        t = state.terms[ti]
        vs = t.varnas
        for k in range(len(vs) - 1):  # inside one Term
            if vs[k].slp1 == "a" and vs[k + 1].slp1 in _GUNA:
                return ti, k
        if n + 1 < len(live) and "pada" not in t.tags and vs[-1].slp1 == "a":
            nxt = state.terms[live[n + 1]]
            if nxt.varnas[0].slp1 in _GUNA and ("sup" not in nxt.tags or _sup_junction_is_ours(t)):
                return ti, len(vs) - 1
    return None


def cond(state: State) -> bool:
    if _find_p017_pararupa(state):
        return True
    return _find_pair(state) is not None


def act(state: State) -> State:
    if _find_p017_pararupa(state):
        t0, t1, t2 = state.terms
        merged = Term(
            kind="prakriti",
            varnas=list(t0.varnas[:-1]) + list(t1.varnas),
            tags=set(t0.tags) | {"anga", "prātipadika"},
            meta=dict(t0.meta),
        )
        merged.meta["p017_pararupa_done"] = True
        state.terms = [merged, t2]
    else:
        hit = _find_pair(state)
        if hit is None:
            return state
        ti, vi = hit
        del state.terms[ti].varnas[vi]
    state.meta["__why_now_dev__"] = (
        "अपदान्त-ह्रस्व-अकारात् गुण-स्वरे (अ/ए/ओ) परे पररूप-एकादेशः — पूर्व-अकारस्य लोपः। (६.१.९७)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.97",
    sutra_type=SutraType.VIDHI,
    text_slp1='ato guRe',
    text_dev='अतो गुणे',
    padaccheda_dev="अतः गुणे",
    why_dev="अपदान्त-ह्रस्व-अकारात् गुणे परे पररूप-एकादेशः।",
    apavada_of     = ("6.1.101",),
    anuvritti_from=("6.1.84",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
