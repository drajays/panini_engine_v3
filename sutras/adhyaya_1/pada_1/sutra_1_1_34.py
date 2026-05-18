"""
1.1.34  pūrvaparāvaradakṣiṇottarāparādharāṇi vyavasthāyām asaṃjñāyām  —  NIYAMA

*Anuvṛtti*: sarvanāma from **1.1.27**.

**Pāṭha:** The seven directional words — pūrva, para, avara, dakṣiṇa, uttara,
apara, adhara — [get] *sarvanāma*-saṃjñā ONLY in positional/directional usage
(*vyavasthāyām*) and NOT when used as a proper name (*asaṃjñāyām*).

These words are in the *sarvādi* gaṇa-pāṭha (**1.1.27**) and therefore
ordinarily receive *sarvanāma*-saṃjñā.  This *niyama* restricts that: when a
Term carries ``samjna_proper_name`` (i.e. it is functioning as a proper name /
*saṃjñā* word), the *sarvanāma*-saṃjñā is removed.

v3:
  - Module-level frozenset ``DAISIKA_SLP1`` contains the seven SLP1 forms.
  - ``cond``: any Term in the set that has both ``sarvanama`` AND
    ``samjna_proper_name`` tags (i.e. it is a proper name and must not be a
    sarvanāma).
  - ``act``: ``discard`` ``sarvanama`` tag; set a done-marker in ``meta`` to
    prevent re-application; record in ``samjna_registry``.
  - ``r1_form_identity_exempt=True`` — no surface change.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only ``Term.meta['upadesha_slp1']`` and Term.tags.
  - No paradigm coordinates, no Devanāgarī strings.
"""
from __future__ import annotations

from typing import FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# SLP1 prātipadika forms of the daiśika (directional) words restricted by 1.1.34.
DAISIKA_SLP1: FrozenSet[str] = frozenset({
    "pUrva",     # पूर्व
    "para",      # पर
    "avara",     # अवर
    "dakziRa",   # दक्षिण
    "uttara",    # उत्तर
    "apara",     # अपर
    "aDara",     # अधर
})

# Meta key used as a done-marker to prevent re-application.
META_1_1_34_DONE: str = "1_1_34_daisika_proper_name_sarvanama_removed"

# Registry key for this rule.
REGISTRY_KEY: str = "1_1_34_vyavasTA_asaMjJAyAm"


def _eligible(state: State):
    """
    Yield Terms that:
      - have upadesha_slp1 in the daiśika set
      - currently carry 'sarvanama' (set by 1.1.27)
      - carry 'samjna_proper_name' (they are being used as a proper name)
      - have not already been processed by this rule
    """
    for t in state.terms:
        if t.meta.get(META_1_1_34_DONE):
            continue
        upa = t.meta.get("upadesha_slp1")
        if not isinstance(upa, str):
            continue
        if upa not in DAISIKA_SLP1:
            continue
        if "sarvanama" not in t.tags:
            continue
        if "samjna_proper_name" not in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.discard("sarvanama")
        t.meta[META_1_1_34_DONE] = True
    state.samjna_registry[REGISTRY_KEY] = DAISIKA_SLP1
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.34",
    sutra_type     = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1      = "pUrvaparAvaradakziRottarAparADarARi vyavasTA yaM asaMjJAyAm",
    text_dev       = "पूर्वपरावरदक्षिणोत्तरापराधराणि व्यवस्थायामसंज्ञायाम्",
    padaccheda_dev = "पूर्व-पर-अवर-दक्षिण-उत्तर-अपर-अधराणि / व्यवस्थायाम् / असंज्ञायाम्",
    why_dev        = "दिशावाचि-शब्दानाम् (पूर्वादि-सप्तानाम्) सर्वनाम-संज्ञा व्यवस्थायाम् एव, "
                     "न तु संज्ञा-शब्देषु (नियमः)।",
    anuvritti_from = ("1.1.27",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

__all__ = ["DAISIKA_SLP1", "META_1_1_34_DONE", "REGISTRY_KEY", "SUTRA"]
