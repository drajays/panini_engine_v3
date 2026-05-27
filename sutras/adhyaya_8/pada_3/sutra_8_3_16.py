"""
8.3.16  रोः सुपि  —  ANUVADA (trace marker)

"A ru (intermediate r from 8.2.66) before a sup retains visarga."

Engine role: 8.3.15 (khara-avasānayoḥ) already converts ru → visarga before
khar-initial sup (e.g. 'su' of saptamī bahu: s is khar).  Before voiced-initial
sup (e.g. bhyām: B is voiced, not khar) the ru stays as 'r' — 8.3.15 does not
fire, and 8.3.16 does not create a new visarga either (classical form dhanurbhyām,
not dhanuḥbhyām).

This sūtra is recorded as ANUVADA: it fires as a trace event to mark the
"roḥ supi" śāstra context for downstream rules (8.3.17+), but does not itself
mutate any varṇa.  All structural work is done by 8.3.15 and 8.3.59.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    # Structural conversion already handled by 8.3.15; this rule is a trace only.
    return False


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.16",
    sutra_type            = SutraType.ANUVADA,
    r1_form_identity_exempt = True,
    text_slp1             = "roH supi",
    text_dev              = "रोः सुपि",
    padaccheda_dev        = "रोः सुपि",
    why_dev               = "सुपि-पूर्वस्य रु-विसर्गः (८.३.१५ एव कार्यम्; अनुवादः)।",
    anuvritti_from        = ("8.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
