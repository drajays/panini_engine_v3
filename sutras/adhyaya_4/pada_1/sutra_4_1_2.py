"""
4.1.2  स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाम्ङ्योस्सुप्  — ADHIKARA

Lists the 21 sup upadeśas in a fixed order (the 24 cells collapse
to 21 distinct pratyayas).  Acts as:
  (a) the LOCUS where the inventory enters the engine (via
      data/inputs/sup_upadesha.json);
  (b) the ADHIKARA whose scope covers 4.1.2 through 5.4.160.

This sūtra's act() does BOTH things:
  • pushes an adhikāra scope entry;
  • attaches the correct sup pratyaya Term to state.terms when the
    recipe signals a (vibhakti, vacana) in step['vibhakti_vacana'].

NOTE: The ONLY place (vibhakti, vacana) may be read is inside THIS
sūtra's act().  This is the single exception granted by the
Constitution because the sup-attachment is itself the rule that maps
paradigm-coordinates to upadeśa.  Downstream cond()s never see them.
"""
import json
from pathlib import Path
from typing  import Any, Dict, Optional

from engine            import SutraType, SutraRecord, register_sutra
from engine.state      import State, Term
from phonology.varna   import parse_slp1_upadesha_sequence


_INVENTORY: Optional[Dict[str, str]] = None
_META     : Optional[Dict[str, Any]] = None


def _load_inventory() -> None:
    global _INVENTORY, _META
    if _INVENTORY is not None:
        return
    path = Path(__file__).parents[3] / "data" / "inputs" / "sup_upadesha.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _INVENTORY = {k: v for k, v in data.items() if not k.startswith("_")}
    _META      = data.get("_meta", {})


def _inventory() -> Dict[str, str]:
    _load_inventory()
    return _INVENTORY  # type: ignore


def _meta() -> Dict[str, Any]:
    _load_inventory()
    return _META or {}


def _upadesha_to_varnas(slp1_seq: str):
    """
    Raw sup upadeśa SLP1 (see ``data/inputs/sup_upadesha.json``).
    ``~`` and Devanagari candrabindu both denote the same ``anunasika`` tag;
    see ``phonology.varna.parse_slp1_upadesha_sequence``.
    """
    return parse_slp1_upadesha_sequence(slp1_seq)


def cond(state: State) -> bool:
    """
    Fire if ANY term is tagged 'prātipadika' and no sup pratyaya Term
    has been attached yet.
    """
    has_prat = any("prātipadika" in t.tags for t in state.terms)
    has_sup  = any(t.kind == "pratyaya" and "sup" in t.tags for t in state.terms)
    return has_prat and not has_sup


def act(state: State) -> State:
    """
    Reads state.meta['vibhakti_vacana'] (e.g. '6-3').  Builds the
    corresponding sup Term and appends it to state.terms.
    """
    # Scope push.
    state.adhikara_stack.append({
        "id"        : "4.1.2",
        "scope_end" : "5.4.160",
        "text_dev"  : "स्वौजसमौट्छष्टा...सुप्",
    })

    vv = state.meta.get("vibhakti_vacana")
    if not vv:
        # No coordinate supplied — ADHIKARA push alone is the effect.
        return state

    upadesha = _inventory().get(vv)
    if upadesha is None:
        raise ValueError(f"4.1.2: no sup upadeśa for {vv!r}")

    # 'sup' varṇas (WITH it-markers preserved; 1.3.* will remove them)
    varnas = _upadesha_to_varnas(upadesha)

    # Pratyaya tags.  v3.1 addition: tag sambuddhi-ekavacana (8-1) so
    # 6.1.69 (su-lopa at sambuddhi) can fire without reading
    # (vibhakti, vacana) in its cond().  This is the ONE place where
    # these paradigm coordinates may be read (Constitution Art. 2
    # exception granted to the sup-attacher).
    tags = {"sup", "upadesha", "pratyaya"}
    if vv == "8-1":
        tags.add("sambuddhi")

    # v3.1: tag pratyaya with it-candidate hints derived from _meta in
    # sup_upadesha.json.  These tags are read by the 1.3.x prakaraṇa.
    meta_tags = _meta()
    if vv in meta_tags.get("has_halant_it", []):
        tags.add("has_halant_it")
    if vv in meta_tags.get("has_initial_n_it", []):
        tags.add("has_initial_n_it")

    pratyaya = Term(
        kind   = "pratyaya",
        varnas = varnas,
        tags   = tags,
        meta   = {"upadesha_slp1": upadesha},
    )
    state.terms.append(pratyaya)
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.2",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "svaujasamauTchazwABhyAmBhisNeByAmByas-NasiByAmByasNasosAmNyossuP",
    text_dev       = "स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्"
                     "भ्यस्ङसोसाम्ङ्योस्सुप्",
    padaccheda_dev = "सु-औ-जस्, अम्-औट्-शस्, टा-भ्याम्-भिस्, ङे-भ्याम्-भ्यस्, "
                     "ङसि-भ्याम्-भ्यस्, ङस्-ओस्-आम्, ङि-ओस्-सुप्",
    why_dev        = "एकविंशति सुप्-प्रत्ययाः क्रमेण प्रातिपदिकात् विधीयन्ते; "
                     "अधिकारः ४.१.२ तः ५.४.१६० पर्यन्तम्।",
    anuvritti_from = ("4.1.1",),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.2", "5.4.160"),
)

register_sutra(SUTRA)
