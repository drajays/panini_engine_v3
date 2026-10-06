"""
3.4.84  ब्रुवः पञ्चानामादित आहो ब्रुवः  —  VIBHASHA

After ब्रू, the first five of the nine parasmaipada laṭ endings (tip tas jhi sip thas) are optionally replaced by the
first five of the ṇalādi set (ṇal atus us thal aṭhus), and ब्रू itself becomes आह्:
  आह  आहतुः  आहुः  आत्थ  आहथुः      (the other branch: ब्रवीति ब्रूतः ब्रुवन्ति ब्रवीषि ब्रूथः)
The remaining four (tha, mip, vas, mas) are untouched: ब्रूथ ब्रवीमि ब्रूवः ब्रूमः.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com sūtra 3.4.84 (padaccheda: ब्रुवः पञ्चानाम् आदितः आहः ब्रुवः)
  Source #2 — ashtadhyayi.com dhātu table, ब्रूञ् (adādi) laṭ parasmaipada: आह,ब्रवीति ; आहतुः,ब्रूतः ; आहुः,ब्रुवन्ति ;
              आत्थ,ब्रवीषि ; आहथुः,ब्रूथः ; ब्रूथ ; ब्रवीमि ; ब्रूवः ; ब्रूमः.  Gītā 10.12–13 आह; 10.2 प्राहुः.

Engine: ``cond`` reads the root's lexical identity (ब्रूञ् = upadeśa ``brUY``) and the tiṅ Terms' sthānin tag. The ādeśa
for brū is sarvādeśa (1.1.55), keeps dhātutva and aṅgatva by 1.1.56, and is tagged ``ah_adesha`` for 8.2.35.
Pāṭha: ashtadhyayi.com data.txt row i=34084 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import ANGATVA, DHATUTVA, adesha_substitute_varnas
from sutras.adhyaya_3.pada_4.nal_adi_common import FIRST_FIVE, lat_parasmai_tin, replace_tin

_ROOT = "brUY"


def _brU(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == _ROOT
                 and not t.meta.get("3_4_84_done")), None)


def _targets(state: State) -> list[int]:
    return lat_parasmai_tin(state, FIRST_FIVE) if _brU(state) is not None else []


def cond(state: State) -> bool:
    return bool(_targets(state))


def act(state: State) -> State:
    root = _brU(state)
    idx = _targets(state)
    if root is None or not idx:
        return state
    for i in idx:
        replace_tin(state, i, "3.4.84")
    adesha_substitute_varnas(root, "Ah", state, sutra_id="3.4.84", gunadharmas=frozenset({DHATUTVA, ANGATVA}))
    root.tags.add("ah_adesha")
    root.meta["3_4_84_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.84",
    sutra_type=SutraType.VIBHASHA,
    text_slp1="bruvaH paYcAnAmAdita Aho bruvaH",
    text_dev="ब्रुवः पञ्चानामादित आहो ब्रुवः",
    samagra_slp1="bruvaH lawaH lasya parasmEpadAnAmAditaH paYcAnAm Ral-atus-us-Tal-aTus  bruvaH AhaH ",
    samagra_dev="ब्रुवः लटः लस्य परस्मैपदानामादितः पञ्चानाम् णल्-अतुस्-उस्-थल्-अथुस् , ब्रुवः आहः ।",
    padaccheda_dev="ब्रुवः पञ्चानाम् आदितः आहः ब्रुवः",
    why_dev="ब्रू से परे लट् के आदि पाँच परस्मैपद तिङ् विकल्प से णल्-आदि हों और ब्रू को आह् आदेश (आह, आहतुः, आहुः, आत्थ, आहथुः)।",
    anuvritti_from=("3.4.82", "3.4.83"),
    vibhasha_default=False,
    vibhasha_scope=cond,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
