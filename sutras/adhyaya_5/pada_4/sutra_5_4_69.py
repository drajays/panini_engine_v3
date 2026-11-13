"""
5.4.69  न पूजनात्  —  PRATISHEDHA

Padaccheda: न पूजनात्

न पूजनात् (5.4.69)
Pāṭha: ashtadhyayi.com data.txt row i=54069 (Art. 14).
Kāśikā 5.4.69: "यान् शब्दानुपादाय समासान्ता विधीयन्ते राजाहःसखिभ्यष्टच् इत्येवमादीन्, यदा ते पूजनात् पूजनवचनात् परे भवन्ति तदा
समासान्तो न भवति। सुराजा। अतिराजा। सुगौः। अतिगौः॥ पूजायां स्वतिग्रहणं कर्तव्यम्॥ … प्राग्बहुव्रीहिग्रहणं च कर्तव्यम्॥"

The samāsa is read off the tape: a pūrvapada Term (``samasa_purvapada``, in a ``tatpurusha``) that is su or ati in the sense of
honour (``lex:pUjana``, a vivakṣā of the speaker, as ``lex:pUjArTa`` in 6.4.30), with its uttarapada Term after it. The samāsānta
sūtras before the bahuvrīhi ones (5.4.70 – 5.4.112, *prāg bahuvrīheḥ*) are blocked.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.registry import SUTRA_REGISTRY
from engine.state import State

_SU_ATI = frozenset({"su", "ati"})      # vārttika: pūjāyāṃ svatigrahaṇam


def _blocked_ids() -> tuple[str, ...]:
    return tuple(f"5.4.{n}" for n in range(70, 113) if f"5.4.{n}" in SUTRA_REGISTRY)


def cond(state: State) -> bool:
    if not adhikara_in_effect("5.4.69", state, "5.4.68"):
        return False
    for t in state.terms[:-1]:
        if {"samasa_purvapada", "tatpurusha", "lex:pUjana"} <= t.tags and "".join(v.slp1 for v in t.varnas) in _SU_ATI:
            return not set(_blocked_ids()) <= state.blocked_sutras
    return False


def act(state: State) -> State:
    state.blocked_sutras |= set(_blocked_ids())
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.69",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na pUjanAt",
    text_dev              = "न पूजनात्",
    samagra_slp1          = "samAsAntAH pUjanAt na",
    samagra_dev           = "समासान्ताः पूजनात् न",
    padaccheda_dev        = "न पूजनात्",
    why_dev               = "न पूजनात् — पूजनार्थात् परेभ्यः समासान्ताः न (सुराजा, अतिराजा)।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
