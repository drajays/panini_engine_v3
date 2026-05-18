"""
1.3.36  सम्माननोत्सञ्जनाचार्यकरणज्ञानभृतिविगणनव्ययेषु नियः  —  VIDHI

*Padaccheda:* *sammānana-utsañjana-ācārya-karaṇa-jñāna-bhṛti-vigaṇana-vyayeṣu*
(सप्तमी-बहुवचन) / *niyaḥ* (षष्ठी-एकवचन).

*Anuvṛtti:* ātmanepada from 1.3.12.

*Content:* [Ātmanepada] for ni + yam (niyam = to regulate/control) in the
contexts of: sammānana (honouring), utsañjana (giving up / releasing),
ācārya-karaṇa (causing one to be teacher), jñāna (knowledge),
bhṛti (wages / livelihood), vigaṇana (calculation / reckoning),
and vyaya (expenditure / expense).

*Engine:* cond checks (a) pada is not already "Atmanepada", (b) at least
one dhātu Term has upadesha_slp1 in _NIYAM_ROOTS and carries the tag
"ni_prefix", and also carries at least one tag from _NIYAM_USAGES, and
(c) the idempotency stamp "Atmanepada_1_3_36" is absent from state.meta.
No arm flags (CONSTITUTION Art. 13).  r1_form_identity_exempt=True because
no surface phonological change occurs here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets (CONSTITUTION Art. 13.3)
_NIYAM_ROOTS: frozenset[str] = frozenset({"yam", "niyam"})
_NIYAM_USAGES: frozenset[str] = frozenset({
    "sammAnana_usage",
    "utsaYjana_usage",
    "AcArya_karaRa_usage",
    "jYAna_usage",
    "Bfti_usage",
    "vigaNana_usage",
    "vyaya_usage",
})

_REGISTRY_KEY = "1_3_36_ni_yam_usages"
_STAMP_KEY    = "Atmanepada_1_3_36"


def cond(state: State) -> bool:
    if state.meta.get("pada") == "Atmanepada":
        return False
    if state.meta.get(_STAMP_KEY):
        return False
    return any(
        "dhatu" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _NIYAM_ROOTS
        and "ni_prefix" in t.tags
        and not _NIYAM_USAGES.isdisjoint(t.tags)
        for t in state.terms
    )


def act(state: State) -> State:
    state.meta["pada"]     = "Atmanepada"
    state.meta[_STAMP_KEY] = True
    state.samjna_registry[_REGISTRY_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.36",
    sutra_type=SutraType.VIDHI,
    text_slp1="sammAnanotsaYjanAcAryakaraRajYAnaBftivigaNanavyayezu niyaH",
    text_dev="सम्माननोत्सञ्जनाचार्यकरणज्ञानभृतिविगणनव्ययेषु नियः",
    padaccheda_dev=(
        "सम्मानन-उत्सञ्जन-आचार्यकरण-ज्ञान-भृति-विगणन-व्ययेषु (सप्तमी-बहुवचन) "
        "/ नियः (षष्ठी-एकवचन)"
    ),
    why_dev=(
        "सम्मानन-उत्सञ्जन-आचार्यकरण-ज्ञान-भृति-विगणन-व्यय-अर्थेषु "
        "नि-पूर्वस्य यम्-धातोः प्रयोगे आत्मनेपदम् — "
        "niyamate इत्यादि; "
        "१.३.१२ इत्यतः आत्मनेपदम् अनुवर्तते।"
    ),
    anuvritti_from=("1.3.12",),
    cond=cond,
    act=act,
    r1_form_identity_exempt=True,
)

register_sutra(SUTRA)
