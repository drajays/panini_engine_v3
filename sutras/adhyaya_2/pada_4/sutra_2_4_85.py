"""
2.4.85  लुटः प्रथमस्य डारौरसः  —  VIDHI

When ``luT_prathama_recipe`` is set and the *tiṅ* residue is the *prathama*
*parasmaipada* shape (after *halantyam*-lopa on *tip*/*tas*/*jhi*), replace it
with the adesha given by ``state.meta['luT_adesha_form']``:
  - ``ti``  (from *tip*)  → ``qA``  (ḍā)
  - ``tas`` (from *tas*)  → ``rO``  (rau)
  - ``jhi`` (from *jhi*)  → ``ras`` (ras)

The *recipe* commits the target adesha in ``state.meta['luT_adesha_form']``
so ``cond`` remains blind to *puruṣa* / *vacana* coordinates (CONSTITUTION Art. 2).

For backward-compat, when ``luT_adesha_form`` is absent, defaults to *ti* → *qA*
(the legacy single-cell path).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 24085 · लुटः प्रथमस्य डारौरसः
              padaccheda: लुटः प्रथमस्य डा-रौ-रसः
  Source #2 — Kāśikā 2.4.85 udāharaṇa:
                कर्ता
                आत्मनेपदस्य — अध्येता
                प्रथमस्येति किम्? श्वः कर्तासि
  Cross-check — surface pinned by: tests/unit/test_tinanta_ad_lut_kartari.py
  Reference record: sutra_ref_out/2_4_85.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk
from phonology.varna import parse_slp1_upadesha_sequence

# Map: (expected current varnas of tiṅ residue, upadesha) → adesha SLP1
_PRATHAMA_MAP: dict[str, tuple[str, ...]] = {
    "qA" : ("ti", "ta"),         # tip→ti (parasmai) / ta (ātmanepada) → qA (ḍā)
    "rO" : ("tas", "AtAm"),      # tas (parasmai) / AtAm (ātmanepada) → rO (rau)
    "ras": ("Ji", "Ja", "tas"),   # झि/झ (3pl) or tas (3du peric. fut. clip)
}


def _find_tin_residue(state: State, expected_varnas: tuple[str, ...]) -> int | None:
    """Find the rightmost pratyaya term whose varnas match expected_varnas (SLP1 sequence)."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if "pratyaya" not in t.tags:
            continue
        vs = tuple(v.slp1 for v in t.varnas)
        if vs == expected_varnas:
            return i
        # Also accept tuple prefix for jhi (may still have h if 1.3.9 not yet fired)
        # but in our pipeline 1.3.3/1.3.9 fired before 2.4.85 for jhi
    return None


# लुटः प्रथमस्य डारौरसः: the prathama-puruṣa tiṅ of luṭ — tip · tas · jhi — become ḍā · rau · ras (यथासंख्यम्, 1.3.10).
_PRATHAMA_ADESHA = {"tip": "qA", "tas": "rO", "Ji": "ras"}
_PRATHAMA_ADESHA_ATMANE = {"ta": "qA", "AtAm": "rO", "Ja": "ras"}      # ātmanepada prathama: ta, ātām, jha (adhyetā)


def _adesha_of(t) -> str | None:
    """यथासंख्यम्: the ḍā/rau/ras that replaces this prathama tiṅ — parasmaipada or ātmanepada (3.4.78)."""
    up = (t.meta.get("upadesha_slp1") or "").strip()
    return (_PRATHAMA_ADESHA if "parasmaipada" in t.tags else _PRATHAMA_ADESHA_ATMANE).get(up)


def _structural_site(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "tin_adesha_3_4_78" not in t.tags or t.meta.get("2_4_85_lut_prathama_done"):
            continue
        if (t.meta.get("source_lakara_upadesha") or "").strip() == "luT" and _adesha_of(t):
            return i
    return None


def cond(state: State) -> bool:
    if _structural_site(state) is not None:
        return True
    if not state.meta.get("luT_prathama_recipe"):
        return False
    if state.meta.get("2_4_85_lut_prathama_done"):
        return False
    adesha = (state.meta.get("luT_adesha_form") or "qA").strip()
    expected_list = _PRATHAMA_MAP.get(adesha)
    if expected_list is None:
        return False
    for exp in expected_list:
        if _find_tin_residue(state, tuple(exp)) is not None:
            return True
    return False


def act(state: State) -> State:
    i = _structural_site(state)
    if i is not None:
        from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas

        t = state.terms[i]
        adesha = _adesha_of(t)
        adesha_substitute_varnas(t, adesha, state, sutra_id="2.4.85", gunadharmas=frozenset({TING_PRATYAYATVA}))
        t.tags.add("tin_adesha_2_4_85")        # the ḍ of ḍā is its it (→ 6.4.143 ṭi-lopa); rau and ras have none
        t.meta["2_4_85_lut_prathama_done"] = True
        state.meta["__why_now_dev__"] = (
            f"लुटः प्रथमपुरुषस्य तिप्-तस्-झि इत्येतेषां यथासंख्यं डा-रौ-रस् — {adesha}। (२.४.८५)"
        )
        return state
    adesha = (state.meta.get("luT_adesha_form") or "qA").strip()
    expected_list = _PRATHAMA_MAP.get(adesha)
    if not expected_list:
        return state
    j = None
    for exp in expected_list:
        j = _find_tin_residue(state, tuple(exp))
        if j is not None:
            break
    if j is None:
        return state
    t = state.terms[j]
    t.varnas = list(parse_slp1_upadesha_sequence(adesha))
    t.meta["upadesha_slp1"] = adesha
    t.tags.add("tin_adesha_2_4_85")
    state.meta["2_4_85_lut_prathama_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.85",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'luwaH praTamasya qArOrasaH',
    text_dev       = 'लुटः प्रथमस्य डारौरसः',
    padaccheda_dev = "लुटः प्रथमस्य डा-रौ-रसः",
    why_dev        = "लुट्-लकारे प्रथम-पुरुष-परस्मैपदानां डा-रौ-रस्-आदेशः।",
    anuvritti_from = (),
    apavada_of            = ("3.4.79",),   # luṭ-prathama's ḍā/rau/ras is the special case of ṭita ṭer e (adhyetā, not *adhyete)
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
