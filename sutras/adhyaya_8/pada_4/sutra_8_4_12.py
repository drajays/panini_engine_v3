"""
8.4.12  एकाजुत्तरपदे णः  —  VIDHI

Padaccheda: एक-अच्-उत्तरपदे णः

एकाजुत्तरपदे णः (8.4.12)
Pāṭha: ashtadhyayi.com data.txt row i=84012 (Art. 14).
Kāśikā 8.4.12: "एकाजुत्तरपदं यस्य स एकाजुत्तरपदः, तस्मिन् … प्रातिपदिकान्तनुम्विभक्तिषु पूर्वपदस्थाद् निमित्तादुत्तरस्य
नकारस्य णकार आदेशो भवति। वृत्रहणौ, वृत्रहणः।"

Reads the samāsa seam off the varṇas (``samasa_purva_v`` / ``samasa_uttara_v``, set by the pada merge from the Terms'
``samasa_purvapada`` / ``samasa_uttarapada`` tags). Slice: the pratipadika-final n (vṛtrahaṇau); the num and vibhakti n
(kṣīrapāṇi, kṣīrapeṇa) are not yet read.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_4.sutra_8_4_2 import _BLOCKERS

_NIMITTA = frozenset({"r", "z", "f", "F"})
_VOWELS = "aAiIuUfFxXeEoO"


def _target(state: State):
    """(term_idx, varna_idx) of the pratipadika-final n of an ekāc uttarapada, after an r / ṣ / ṛ of the pūrvapada with only
    non-blockers between (aṭkupvāṅnumvyavāye'pi, as 8.4.2)."""
    if not state.tripadi_zone:
        return None
    for ti, t in enumerate(state.terms):
        if sum(v.slp1 in _VOWELS for v in t.varnas if "samasa_uttara_v" in v.tags) != 1:     # ekāc
            continue
        for vi, v in enumerate(t.varnas):
            if v.slp1 != "n" or "samasa_uttara_v" not in v.tags or "natva_done" in v.tags or "pratipadika_anta_v" not in v.tags:
                continue
            for u in reversed(t.varnas[:vi]):
                if u.slp1 in _NIMITTA:
                    if "samasa_purva_v" in u.tags:
                        return (ti, vi)
                    break
                if u.slp1 in _BLOCKERS:
                    break
    return None


def cond(state: State) -> bool:
    return _target(state) is not None


def act(state: State) -> State:
    ti, vi = _target(state)
    t = state.terms[ti]
    before = "".join(v.slp1 for v in t.varnas)
    r = mk("R")
    r.tags |= {"natva_done", "samasa_uttara_v"}
    t.varnas[vi] = r
    state.meta["__why_now_dev__"] = (
        f"एकाच् उत्तरपद (काशिका ८।४।१२): पूर्वपदस्थ निमित्त से उत्तरपद का प्रातिपदिकान्त न → ण; {before} → {''.join(v.slp1 for v in t.varnas)}।")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAjuttarapade RaH",
    text_dev              = "एकाजुत्तरपदे णः",
    samagra_slp1          = "pUrvapadAt razAByAM prAtipadikAnta-num-viBaktizu ekAc-uttarapade naH RaH  awkupvANnumvyavAye api",
    samagra_dev           = "पूर्वपदात् रषाभ्यां प्रातिपदिकान्त-नुम्-विभक्तिषु एकाच्-उत्तरपदे नः णः , अट्कुप्वाङ्नुम्व्यवाये अपि",
    padaccheda_dev        = "एक-अच्-उत्तरपदे णः",
    why_dev               = "(सूत्रम् 8.4.12) एकाजुत्तरपदे णः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
