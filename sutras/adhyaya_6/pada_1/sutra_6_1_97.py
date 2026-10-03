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

Conflicts are judged inside the rule as Pāṇini does (see ``_para_competitor``):
6.1.97 is the apavāda of 6.1.88 and 6.1.101 only ("purastād apavādā anantarān
vidhīn bādhante nottarān"), so a later rule that also applies at the junction —
6.1.102 for rāma+jas, 7.1.17 for anya+jas, 7.1.12 for rāma+ṅas — is *para* and
wins (1.4.2); a rival that needs the following Term (7.3.101 in paśya+a+mi) is
bahiraṅga and loses; a pending strī ṭāp (4.1.4) is added before saṃhitā.
The one non-phonemic helper kept is P017's ``pawat+pawat+qAc`` merge.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

_GUNA = frozenset("aeo")


_APAVADA_OF = ("6.1.101",)   # bādhita by 6.1.97 (6.1.88 is earlier); keep in sync with SUTRA.apavada_of


def _num(sid: str) -> tuple[int, int, int]:
    a, p, n = (int(x) for x in sid.split("."))
    return a, p, n


def _footprint(state: State, i: int, j: int):
    """What a rule could be competing for at the junction: Term count + the two Terms."""
    def snap(t: Term):
        return ("".join(v.slp1 for v in t.varnas), frozenset(t.tags), t.meta.get("upadesha_slp1"))
    return snap(state.terms[i]), snap(state.terms[j])


def _para_competitor(state: State, i: int, j: int) -> str | None:
    """
    Vipratiṣedha (1.4.2, para wins).  A later vidhi sūtra that is applicable *now*
    and would rewrite the junction ``terms[i] ‖ terms[j]`` is *para* to 6.1.97 and
    takes it (rāma+jas → 6.1.102, anya+jas → 7.1.17, rāma+ṅas → 7.1.12).
    6.1.97's own apavāda-targets (6.1.88, 6.1.101) are earlier/declared, and
    "purastād apavādā anantarān vidhīn bādhante nottarān" keeps 6.1.102 free.
    Tripāḍī rules are asiddha here and never compete.

    Antaraṅga beats bahiraṅga (PŚ 50): a rival that still applies with every Term
    after the junction cut away depends only on the two adjacent Terms (antaraṅga,
    equal to 6.1.97) and is judged by para; one that needs the following Term
    (7.3.101 ato dīrgho yañi: paśya+a+mi) is bahiraṅga and loses.
    A pratyaya-vidhāna (4.1) that would be inserted between the two Terms
    (ṭāp in ena|as) precedes saṃhitā and also takes the junction.
    """
    from engine.phase import is_tripadi_sutra
    from engine.registry import SUTRA_REGISTRY
    cut = state.fork()
    cut.terms = cut.terms[: j + 1]
    if any("strīliṅga" in t.tags for t in cut.terms) and \
            not any(e.get("id") == "4.1.3" for e in cut.adhikara_stack):
        cut.adhikara_stack.append({"id": "4.1.3"})  # strī is already chosen: 4.1.3 striyām governs the rival test
    before = _footprint(cut, i, j)
    for sid, rec in SUTRA_REGISTRY.items():
        n = _num(sid)
        if sid == "6.1.97" or sid in _APAVADA_OF or is_tripadi_sutra(sid):
            continue
        # para (later) rules compete by 1.4.2; earlier ones only if they are pratyaya-vidhāna
        # (4.1: a strī/ṭāp pratyaya is added to the stem before saṃhitā, ena|as → enā|as)
        if n < (6, 1, 97) and n[:2] != (4, 1):
            continue
        if rec.sutra_type not in (SutraType.VIDHI, SutraType.VIBHASHA):
            continue
        if getattr(rec, "r1_form_identity_exempt", False) or rec.cond is None:
            continue
        try:
            if not rec.cond(cut):
                continue
            trial = cut.fork()
            rec.act(trial)
            if _footprint(trial, i, j) != before:
                return sid
        except Exception:
            continue
    return None


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
            if state.terms[live[n + 1]].varnas[0].slp1 in _GUNA:
                return ti, len(vs) - 1
    return None


def cond(state: State) -> bool:
    if _find_p017_pararupa(state):
        return True
    hit = _find_pair(state)
    if hit is None:
        return False
    ti, vi = hit
    from engine.resolver import decides

    if vi == len(state.terms[ti].varnas) - 1 and not decides():  # cross-Term junction: para rule may take it
        j = next(k for k in range(ti + 1, len(state.terms)) if state.terms[k].varnas)
        if _para_competitor(state, ti, j):
            return False
    return True


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
