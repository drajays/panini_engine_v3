"""
1.1.37  स्वरादिनिपातमव्ययम्  —  SAMJNA

Meaning: The svarādi-nipātas are avyaya (indeclinable).

"svarādi" refers to the group of nipāta (particle) words beginning with
"svar" as listed in the nipāta-gaṇa; these are invariably-formed words
that do not take inflectional suffixes (sup-luk by 2.4.82).

Engine (glass-box):
  - A Term whose kind == "nipata" OR whose upadesha_slp1 is in the
    module-level SVARADI_NIPATA_SLP1 frozenset, and which does not yet
    carry the "avyaya" tag, gets tagged "avyaya".
  - Metadata-only change; no surface phoneme altered.

Mechanical blindness (CONSTITUTION Art. 2):
  - cond() reads only Term.kind, Term.meta['upadesha_slp1'], and Term.tags.
  - No vibhakti/vacana/lakāra/gold access.
Pāṭha: ashtadhyayi.com data.txt row i=11037 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra, gana
from engine.state import State

# The nipātas of the Gaṇapāṭha: the svarādi, ca-ādi (1.4.57) and pra-ādi (1.4.58) gaṇas (engine/gana.py)
_NIPATA_GANAS = ("svarAdiH", "cAdiH", "prAdiH")


def _eligible(state: State):
    for t in state.terms:
        if "avyaya" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if t.kind == "nipata" or (isinstance(upa, str) and any(gana.in_gana(g, upa) for g in _NIPATA_GANAS)):
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("avyaya")
    state.samjna_registry["1_1_37_svarAdinipAta"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.1.37",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = 'svarAdinipAtamavyayam',
    text_dev              = 'स्वरादिनिपातमव्ययम्',
    samagra_slp1          = "svarAdinipAtamavyayam",
    samagra_dev           = "स्वरादिनिपातमव्ययम्",
    padaccheda_dev        = "स्वर-आदि-निपातम् / अव्ययम्",
    why_dev               = (
        "स्वरादि-निपाताः अव्यय-संज्ञकाः; ततो २.४.८२ सुप्-लुक्।"
    ),
    anuvritti_from        = (),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
