"""
3.4.69  लः कर्तरि कर्मणि च, भावे कर्तरि च अकर्मकेभ्यः धातोः परश्च  —  PARIBHASHA

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
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_3.pada_4.lakara_prayoga_3_4_69 import (
    build_gates,
    dhatu_slp1_snapshot,
    effective_karmakatva_for_lac,
    find_lac_prayoga_terms,
)


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
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "laH kartrA karmaRi ca BAve kartrA ca akarmakAByaH DAtoH paraH",
    text_dev       = "लः कर्तरि कर्मणि च, भावे कर्तरि च अकर्मकेभ्यः धातोः परः",
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
