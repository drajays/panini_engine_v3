"""
1.4.60  गतिश्च  (gatiś ca)  —  SAMJNA

The upasargas (enumerated in 1.4.58 prādayaḥ) also get the gati-saṃjñā
(in addition to being nipātas). The word "ca" includes other kriyā-viśeṣaṇas
(adverbial modifiers of verbs) that qualify as gati.

v3: registers samjna_registry["gati_set"] with the upasarga list plus the
    word "gati" tag, enabling downstream rules (e.g., 2.2.18, 6.2.49) to
    identify gati members.
"""
from __future__ import annotations

from engine import SutraRecord, SutraType, register_sutra
from engine.state import State

# Gati set = upasargas (from 1.4.58) + additional kriyā-viśeṣaṇas recognized
# as gati by the tradition.  The upasargas are duplicated here so this rule
# can stand alone when 1.4.58's registry entry is absent.
_GATI_SET: frozenset[str] = frozenset({
    # Twenty upasargas
    "pra", "parA", "apa", "sam", "anu", "ava",
    "nis", "nir", "dus", "dur", "vi", "A",
    "ni", "aDi", "api", "ati", "su", "ut", "ud",
    # Additional gatis recognised by the tradition
    "alam", "tiras", "punar", "asTam", "antar",
})


def cond(state: State) -> bool:
    return state.samjna_registry.get("gati_set") is None


def act(state: State) -> State:
    state.samjna_registry["gati_set"] = _GATI_SET
    return state


SUTRA = SutraRecord(
    sutra_id="1.4.60",
    sutra_type=SutraType.SAMJNA,
    text_slp1="gatiS ca",
    text_dev="गतिश्च",
    padaccheda_dev="गतिः / च",
    why_dev="उपसर्गाश्च गति-संज्ञकाः — गति-सूचिः संज्ञारजिस्ट्रीयां स्थाप्यते।",
    anuvritti_from=("1.4.58", "1.4.59"),
    r1_form_identity_exempt=True,
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
