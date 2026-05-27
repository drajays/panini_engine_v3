"""
1.3.12  अनुदात्तङित आत्मनेपदम्  —  PARIBHASHA

*Padaccheda:* *anudātta-ṅit* / *ātmanepadam*.

*Śāstra:* *anudāttet* (ekāc) *dhātu* takes *ātmanepada* in *kartari* (**1.3.12**–**77** block;
**1.3.78** *śeṣa* applies only when this block does not license *parasmaipada*).

*Engine:* ``cond`` reads ``ekac_dhatu`` on the primary *dhātu* *Term* (from dhātupāṭha /
``_build_dhatu_term``), not *puruṣa* / *vacana* (Art. 2).  Sets ``kartari_atmanepada_licensed``
so **1.3.78** does not force *parasmaipada*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import ATMANE_LICENSE_META_KEY


def _primary_dhatu(state: State) -> Term | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    if (state.meta.get("pada") or "").strip() == "Atmanepada":
        return False
    d = _primary_dhatu(state)
    if d is None:
        return False
    if d.meta.get(ATMANE_LICENSE_META_KEY):
        return False
    # *anudāttet* = ekāc (ँ) without udātta on the upadeśa (not mere ``ekac`` on भू etc.).
    # Guard: only fire for dhātus the dhātupātha already marks ātmanepada/ubhayapadi.
    # A seṭ parasmaipada dhātu like paWa~ (पठँ) is ekāc+anudātta but its chandrabindu
    # marks iṭ-eligibility (seṭ), NOT ṅit → ātmanepada.
    if not d.meta.get("kartari_atmanepada_licensed"):
        return False
    return bool(d.meta.get("ekac_dhatu")) and not bool(d.meta.get("udatta_dhatu"))


def act(state: State) -> State:
    d = _primary_dhatu(state)
    if d is None:
        return state
    d.meta[ATMANE_LICENSE_META_KEY] = True
    state.meta["pada"] = "Atmanepada"
    state.paribhasha_gates["1.3.12_anudatta_nit_atmanepada"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.3.12",
    sutra_type=SutraType.PARIBHASHA,
    r1_form_identity_exempt=True,
    text_slp1="anudAtta-Nit Atmanepadam",
    text_dev="अनुदात्तङित आत्मनेपदम्",
    padaccheda_dev="अनुदात्त-ङित् / आत्मनेपदम्",
    why_dev="अनुदात्तेत्-धातोः कर्तरि आत्मनेपदम्; १.३.७८-शेष-परस्मैपदं न भवति।",
    anuvritti_from=("1.3.14",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
