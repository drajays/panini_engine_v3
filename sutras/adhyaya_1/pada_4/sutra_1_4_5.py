"""
1.4.5  वाऽऽमि  —  VIBHASHA

**Pāṭha:** Optionally (*vā*) [the prātipadika is treated as *nadī*] before
the suffix *āmi* (*āmi* — genitive plural marker).

v3: optionally adds the *nadi* tag to eligible prātipadika–stri Terms that
appear in an *āmi* context and have not yet been processed by this sūtra.
The default choice is to apply (``vibhasha_default=True``).
Pāṭha: ashtadhyayi.com data.txt row i=14005 (Art. 14).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# The pipelines tag a feminine stem "strīliṅga"; these sūtras were written
# against a bare "stri". Accept either, so the नदी / ह्रस्व saṃjñās can fire on
# the tape the subanta pipeline actually builds.
FEMININE_TAGS: frozenset = frozenset({"stri", "strīliṅga"})


def _eligible(state: State):
    """An iyaṅuvaṅsthāna yU stem (1.4.4 took its nadī-saṃjñā away) directly before the sup Ām: śriyām / śrīṇām (Kāśikā 1.4.5)."""
    from sutras.adhyaya_1.pada_4.sutra_1_4_4 import iyanuvan_sthana

    for i, t in enumerate(state.terms[:-1]):
        nxt = state.terms[i + 1]
        if ("nadi" not in t.tags and t.meta.get("1_4_4_done") and iyanuvan_sthana(t) and "sup" in nxt.tags
                and (nxt.meta.get("upadesha_slp1") or "") == "Am" and not t.meta.get("1_4_5_done")):
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["nadi_vA_Ami"] = frozenset({"optional_nadi_before_Ami"})
    for t in _eligible(state):
        t.tags.add("nadi")
        t.meta["1_4_5_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.5",
    sutra_type             = SutraType.VIBHASHA,
    text_slp1              = 'vAmi',
    text_dev               = 'वाऽऽमि',
    samagra_slp1           = "iyaN-uvaN-sTAnO yU stryAKyO Ami nadI vA astrI",
    samagra_dev            = "इयङ्-उवङ्-स्थानौ यू स्त्र्याख्यौ आमि नदी वा, अस्त्री",
    padaccheda_dev         = "वा / आमि",
    why_dev                = "आमि परे स्त्री-प्रातिपदिकस्य वा नदीसंज्ञा।",
    apavada_of     = ("1.4.4",),   # अपवाद of 1.4.4 — sutra_ref_out resolver.apavada_of
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    vibhasha_default       = True,
    vibhasha_scope         = lambda state: next(_eligible(state), None) is not None,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
