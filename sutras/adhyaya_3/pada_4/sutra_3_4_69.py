"""
3.4.69  लः कर्मणि च भावे चाकर्मकेभ्यः  —  PARIBHASHA

*Padaccheda* (Kāśikā order, teaching layout):

  - *laḥ* (1.1 *prathamā-bahuvacanam* of *laca* / *lakāra*),
  - *karmaṇi* (*saptamī-ekavacanam*), *ca*, *bhāve* (*saptamī*), *ca*,
  - *akarmakebhyaḥ* (*pañcamī-bahuvacanam* from *akarmaka*)

*Anuvṛtti* (baked into *text_slp1* / *text_dev*, not computed at run time):

  From *pratyayādhikāra* **3.1.1** *pratyayaḥ*; **3.1.2** *paraś ca*; **3.1.3** *ādyudāttaś ca*;
  **3.1.91** *dhātoḥ* — so *lakāra* is *para* to the *dhātu*; *sakarmaka* roots get *lac* in
  *kartari* and *karmaṇi*; *akarmaka* roots in *kartari* and *bhāve*.

This file sets **paribhāṣā gates** so later *vidhi* sūtras (e.g. *tíṅ* replacement) can consult
*prayoga* class without reading (*vibhakti*, *puruṣa*, *lakāra*) — CONSTITUTION Art. 2.
The *dhātu*'s *sakarmakatva* / *akarmakatva* must be supplied on ``Term.meta['karmakatva']``
by the input recipe (or lexicon), not by coordinate inspection.

See ``lakara_prayoga_3_4_69.py`` for the gate shape.
Pāṭha: ashtadhyayi.com data.txt row i=34069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


# --- helpers of this sūtra (formerly lakara_prayoga_3_4_69.py; one sūtra, one file) ---
from typing import Any, Dict, List, Optional, Tuple

from engine.state import State, Term

# Stable gate prefix so downstream sūtras can consult without string typos.
GATE_PFX = "prayoga_3_4_69"


def effective_karmakatva_for_lac(term: Term) -> Optional[str]:
    """
    Return an internal label used only to compute paribhāṣā gates:

    - ``sakarmaka`` — *dvy-artha* / *sakarmaka* in full sense → kartari + karmaṇi
    - ``akarmaka`` — *nityākarmaka* / *akarmaka* → kartari + bhāve, not karmaṇi
    - ``sakarmaka_candra`` — *sakarmaka* with *anādarita-karman* (teaching: treat like
      *akarmaka* for prayoga: kartari + bhāve, not karmaṇi locus in the same way)
    """
    if "dhatu" not in term.tags:
        return None
    raw = term.meta.get("karmakatva")
    if raw is None:
        return None
    if raw in ("dvyarma", "dvikarmaka"):          # a dvikarmaka dhātu is sakarmaka (data: ashtadhyayi.com 'D')
        raw = "sakarmaka"
    if raw not in ("sakarmaka", "akarmaka"):
        return None
    if raw == "sakarmaka" and bool(term.meta.get("avivakshita_karma")):
        return "sakarmaka_candra"
    return raw


def dhatu_slp1_snapshot(term: Term) -> str:
    m = (term.meta.get("upadesha_slp1") or "").strip()
    if m:
        return m
    return "".join(v.slp1 for v in term.varnas)


def build_gates(eff: str, dhatu_slp1: str) -> Dict[str, Any]:
    """
    Boolean licences (downstream *prayoga* / *lakāra* logic may read these only).

    For *sakarmaka*: *kartari* + *karmaṇi* (not the *bhāve* distribution of 3.4.69
    in the *akarmaka* half).

    For *akarmaka* and *sakarmaka* with *anādarita-karman*: *kartari* + *bhāve*.
    """
    g: Dict[str, Any] = {
        f"{GATE_PFX}_dhatu_upadesha": dhatu_slp1,
        f"{GATE_PFX}_effective_karmakatva": eff,
    }
    if eff == "sakarmaka":
        g[f"{GATE_PFX}_licenses_kartari"] = True
        g[f"{GATE_PFX}_licenses_karmani"] = True
        g[f"{GATE_PFX}_licenses_bhave"] = False
    elif eff in ("akarmaka", "sakarmaka_candra"):
        g[f"{GATE_PFX}_licenses_kartari"] = True
        g[f"{GATE_PFX}_licenses_karmani"] = False
        g[f"{GATE_PFX}_licenses_bhave"] = True
    else:
        g[f"{GATE_PFX}_licenses_kartari"] = False
        g[f"{GATE_PFX}_licenses_karmani"] = False
        g[f"{GATE_PFX}_licenses_bhave"] = False
    return g


def find_lac_prayoga_terms(state: State) -> List[Tuple[int, Term]]:
    """(index, term) for terms tagged *dhatu* with usable *karmakatva*."""
    out: list[Tuple[int, Term]] = []
    for i, t in enumerate(state.terms):
        if effective_karmakatva_for_lac(t) is not None:
            out.append((i, t))
    return out




def _strip_old_gates(g: dict) -> None:
    for k in list(g.keys()):
        if k.startswith("prayoga_3_4_69_"):
            del g[k]


def cond(state: State) -> bool:
    return bool(find_lac_prayoga_terms(state))


def act(state: State) -> State:
    pairs = find_lac_prayoga_terms(state)
    _idx, t0 = pairs[0]
    eff = effective_karmakatva_for_lac(t0)
    assert eff is not None
    snap = dhatu_slp1_snapshot(t0)
    new_g = build_gates(eff, snap)
    _strip_old_gates(state.paribhasha_gates)
    state.paribhasha_gates.update(new_g)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.69",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'laH karmaRi ca BAve cAkarmakeByaH',
    text_dev       = 'लः कर्मणि च भावे चाकर्मकेभ्यः',
    samagra_slp1   = "laH kartari karmaRi ca BAve kartari ca akarmakeByaH DAtoH paraSca",
    samagra_dev    = "लः कर्तरि कर्मणि च, भावे कर्तरि  च अकर्मकेभ्यः धातोः परश्च",
    padaccheda_dev = (
        "लः (प्रथमा-बहुवचनम्) · कर्मणि (सप्तमी) · च · भावे (सप्तमी) · च · "
        "अकर्मकेभ्यः (पञ्चमी-बहुवचनम्) · (अन्वितम्) कर्तरि (सप्तमी) — धातोः · परः"
    ),
    why_dev        = (
        "सकर्मकानां धातूनां लकारे कर्तरि कर्मणि च, अकर्मकानां कर्तरि भावे च — "
        "अतः paribhAṣA-dvArAH (Term.meta karmakatva)।"
    ),
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
