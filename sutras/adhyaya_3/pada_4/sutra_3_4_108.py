"""
3.4.108  झेर्जुस्  —  VIDHI

Two operational paths:
  1. Legacy arm ``3_4_108_arm``: gate-setter (krt_kind = 3.4.108).
  2. Phonological path: liṅ/āśīr-liṅ, or seṭ-luṅ 3pl — substitute the jhi
     tiṅ ādeśa with jus residue [u,s].  jus upadeśa = j+u+s; j is cuṭu-it
     (1.3.7) and drops, leaving [u,s].  Discriminated by lakāra key on state.

cond (phonological path): state.meta["lakara"] ∈ {"liG","AsIrliG"} OR
  (lakāra=="luG" AND dhātu is seṭ, i.e. not anit_dhatu) — AND jhi ādeśa
  tagged tin_adesha_3_4_78 is on the tape.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 34108 · झेर्जुस्
              padaccheda: झेः जुस्
              anuvṛtti:   34102: लिङः
  Source #2 — Kāśikā 3.4.108 udāharaṇa:
                लिङादेशस्य झेर्जुसादेशो भवति
                झोऽन्तापवादः
                पचेयुः
  Cross-check — surface pinned by: tests/unit/test_tinanta_bhavet_ling.py, tests/unit/test_tinanta_bhuyat_ashirling.py
  Reference record: sutra_ref_out/3_4_108.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk



def _dhatu_is_anit(state: State) -> bool:
    for t in state.terms:
        if "dhatu" in t.tags and "abhyasa" not in t.tags:
            return bool(t.meta.get("anit_dhatu"))
    return False


def _find_jhi_tin(state: State) -> int | None:
    """The jhi tiṅ ādeśa of a liṅ (vidhi or āśīr) — and of a luṅ that has sic (3.4.109 सिजभ्यस्तविदिभ्यश्च,
    अपठिषुः) — read from the affix's own provenance, not from the derivation's lakāra (Art. 2)."""
    has_sic = any((t.meta.get("upadesha_slp1") or "").strip() == "sic" for t in state.terms)
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags or t.meta.get("3_4_108_liG_done"):
            continue
        source = (t.meta.get("source_lakara_upadesha") or "").strip()
        if source != "liG" and not (source == "luG" and has_sic):
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() == "Ji" and "".join(v.slp1 for v in t.varnas) in {"Ji", "J"}:
            return i
    return None


def cond(state: State) -> bool:
    return _find_jhi_tin(state) is not None


def act(state: State) -> State:
    j = _find_jhi_tin(state)
    if j is None:
        return state
    t = state.terms[j]
    # जुस् = ज्+उ+स्: the ज् is it (1.3.7 चुटू) and goes; [u, s] stands in place of the whole झि (1.1.55).
    t.varnas = [mk("u"), mk("s")]
    t.meta["upadesha_slp1"] = "jus"
    t.meta["3_4_108_liG_done"] = True
    t.tags.discard("upadesha")
    state.samjna_registry["3.4.108_jhi_jus"] = True
    state.meta["__why_now_dev__"] = (
        "लिङः झि-आदेशस्य स्थाने जुस् (झोऽन्तस्य अपवादः) — भवेयुः, भूयासुः; सिचि लुङ्यपि (अपठिषुः)। (३.४.१०८)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.108",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "Jerjus",
    text_dev              = "झेर्जुस्",
    padaccheda_dev        = "झेः जुस्",
    why_dev               = (
        "विधि-लिङि झि-आदेशस्य स्थाने जुस् (j-cuṭु-it → लोपः → [u,s])।"
    ),
    anuvritti_from        = ('3.4.102',),
    apavada_of            = ("7.1.3",),   # झोऽन्तापवादः — Kāśikā 3.4.108 (cited above)
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
