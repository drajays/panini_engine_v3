"""
7.1.81  शप्श्यनोर्नित्यम्  —  VIDHI

Padaccheda: शप्-श्यनोः नित्यम्

शप्श्यनोर्नित्यम् (7.1.81)
Pāṭha: ashtadhyayi.com data.txt row i=71081 (Art. 14).
"""

from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk
from phonology.varna import AC_DEV


def num_site(state: State, *vikaranas: str):
    """The Śatṛ-anta aṅga whose vikaraṇa is one of ``vikaranas`` and which a nadī (the ṅīp of 4.1.6) follows; not abhyasta (7.1.78)."""
    if not adhikara_in_effect("7.1.81", state, "6.4.1"):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if (origin.last_pratyaya(t) == "Satf~" and origin.has_vikarana(t, *vikaranas) and not origin.is_abhyasta(t)
                and "nadi" in state.terms[i + 1].tags and not t.meta.get("7_1_80_num_done") and t.varnas):
            return t
    return None


def _site(state: State):
    return num_site(state, "Sap", "Syan")


def cond(state: State) -> bool:
    return _site(state) is not None


def put_num(anga) -> None:
    j = max((k for k, v in enumerate(anga.varnas) if v.slp1 in AC_DEV), default=None)
    if j is None:
        return
    n = mk("n")
    n.tags.add("mit")
    anga.varnas.insert(j + 1, n)                 # mit: after the last ac (1.1.47)
    anga.meta["7_1_80_num_done"] = True


def act(state: State) -> State:
    anga = _site(state)
    if anga is not None:
        put_num(anga)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SapSyanornityam",
    text_dev              = "शप्श्यनोर्नित्यम्",
    samagra_slp1          = "aNgasya Sap-SyanoH nityam num SatuH SI-nadyoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य शप्-श्यनोः नित्यम् नुम् शतुः शी-नद्योः",
    padaccheda_dev        = "शप्-श्यनोः नित्यम्",
    why_dev               = "(सूत्रम् 7.1.81) शप्श्यनोर्नित्यम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
