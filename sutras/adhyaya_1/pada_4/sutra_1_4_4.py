"""
1.4.4  नेयङुवङ्स्थानावस्त्री  —  NIYAMA

**Pāṭha:** The substitutions *iyaṅ* (*iy*) and *uvaṅ* (*uv*) — or a
non-feminine nominal — do NOT receive the *nadī* saṃjñā from 1.4.3.

v3: removes the *nadi* tag from any Term that already has it but is either
tagged *iyaN_sub*, *uvaN_sub*, or lacks *stri*, and records a done-marker
in ``term.meta`` to prevent re-firing.
Pāṭha: ashtadhyayi.com data.txt row i=14004 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# The pipelines tag a feminine stem "strīliṅga"; these sūtras were written
# against a bare "stri". Accept either, so the नदी / ह्रस्व saṃjñās can fire on
# the tape the subanta pipeline actually builds.
FEMININE_TAGS: frozenset = frozenset({"stri", "strīliṅga"})


def iyanuvan_sthana(t) -> bool:
    """A strī ī/ū-stem that is a dhātu (nī, śrī …) or bhrū: the stems whose ī/ū 6.4.77 turns into iyaṅ/uvaṅ (Kāśikā 1.4.4). Not the word strī (astrī)."""
    from engine.declension import dhatu_aṅga

    return (bool(FEMININE_TAGS & t.tags) and bool(t.varnas) and t.varnas[-1].slp1 in ("I", "U")
            and dhatu_aṅga(t) and (t.meta.get("upadesha_slp1") or "").strip() != "strI")


def _eligible(state: State):
    for t in state.terms:
        if "nadi" in t.tags and not t.meta.get("1_4_4_done") and (iyanuvan_sthana(t) or not (FEMININE_TAGS & t.tags)):
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["nadi_exception_iyaN_uvaN"] = frozenset({"iyaN_sub", "uvaN_sub"})
    for t in _eligible(state):
        t.tags.discard("nadi")
        t.meta["1_4_4_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.4",
    sutra_type             = SutraType.NIYAMA,
    text_slp1              = 'neyaNuvaNsTAnAvastrI',
    text_dev               = 'नेयङुवङ्स्थानावस्त्री',
    samagra_slp1           = "iyaN-uvaNasTAnO yU nadI na  astrI ",
    samagra_dev            = "इयङ्-उवङस्थानौ यू नदी न , अस्त्री ।",
    padaccheda_dev         = "न / इयङ्-उवङ्-स्थानौ / अस्त्री",
    why_dev                = "इयङ्-उवङ्-स्थानभूतस्य अथवा स्त्री-भिन्नस्य नदीसंज्ञा न।",
    apavada_of     = ("1.4.3",),   # अपवाद of 1.4.3 — sutra_ref_out resolver.apavada_of
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
