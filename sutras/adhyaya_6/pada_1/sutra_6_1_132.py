"""
6.1.132  एतत्तदोः सुलोपोऽकोरनञ्समासे हलि  —  VIDHI

Padaccheda: एतद्-तदोः सु-लोपः अ-कोः अ-नञ्-समासे हलि

एतत्तदोः सुलोपोऽकोरनञ्समासे हलि (6.1.132)
Pāṭha: ashtadhyayi.com data.txt row i=61132 (Art. 14).
Kāśikā 6.1.132: eṣa dadāti, sa dadāti; Laghukaumudī: eṣa viṣṇuḥ, sa śambhuḥ; eṣako, asaḥ and eṣo'tra are outside.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

from phonology.pratyahara import HAL

_SU = frozenset({"s~", "su", "su~", "s"})
META = "sulopa_6_1_132"


def _find(state: State):
    for i in range(len(state.terms) - 2):
        stem, sup, nxt = state.terms[i], state.terms[i + 1], state.terms[i + 2]
        if "sup" not in sup.tags or sup.meta.get(META) or not sup.varnas or not nxt.varnas:
            continue
        if (sup.meta.get("upadesha_slp1") or "").strip() not in _SU:
            continue
        name = (stem.meta.get("upadesha_slp1") or "").strip()
        flat = "".join(v.slp1 for v in stem.varnas)
        if not (name in ("etad", "tad") or flat in ("etad", "tad", "eza", "sa")):      # akac stems (eSaka, saka) are not these words
            continue
        if "lex:nanjsamAsa" in stem.tags:                                              # anañsamāse: caller tag (S76)
            continue
        if nxt.varnas[0].slp1 in HAL:
            return i + 1
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    j = _find(state)
    if j is None:
        return state
    sup = state.terms[j]
    sup.varnas = []                                    # lopa of su
    sup.meta[META] = True
    state.meta["__why_now_dev__"] = "एतद्-तदोः सुशब्दस्य हलि परे संहितायां लोपः (६.१.१३२)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'etattadoH sulopokoranaYsamAse hali',
    text_dev              = 'एतत्तदोः सुलोपोऽकोरनञ्समासे हलि',
    samagra_slp1          = "anaYsamAse - akoH etad-tadoH hali su~lopaH",
    samagra_dev           = "अनञ्समासे - अकोः एतद्-तदोः हलि सुँलोपः",
    padaccheda_dev        = "एतद्-तदोः सु-लोपः अ-कोः अ-नञ्-समासे हलि",
    why_dev               = "काशिका ६.१.१३२ — ककाररहितयोः एतद्-तदोः यः सुः तस्य हलि परे संहितायां लोपः, नञ्समासे न (एष ददाति, स ददाति)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
