"""
6.1.78  एचोऽयवायावः  —  VIDHI

Classical rule:
  If an EC vowel (e/E/o/O) is followed by an AC vowel, the EC splits:
    e → ay, E → Ay, o → av, O → Av

v3.1 originally implemented only a narrow 'a + os' helper for रामयोः.
v3.4 extends the rule to its standard eco+aci behaviour, while keeping
the prior narrow helper intact.

v3.5: skip the *ec*+*ac* split when the *aṅga* **Term** carries **1.1.11**
``pragrahya`` (e.g. *māle* + *iti* — **6.1.125** *prakṛti-bhāva*).
"""
from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import iter_anga_to_following_pratyaya_pairs, state_has_sup_luk_ghost
from engine.state import State
from phonology     import mk
from phonology.pratyahara import AC

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


_ECO_SPLIT = {
    "e": ("a", "y"),
    "E": ("A", "y"),
    "o": ("a", "v"),
    "O": ("A", "v"),
}


def _find_eco_aci_boundary(state: State):
    if len(state.terms) < 2:
        return None
    pairs = (
        iter_anga_to_following_pratyaya_pairs(state)
        if state_has_sup_luk_ghost(state)
        else ((i, i + 1) for i in range(len(state.terms) - 1))
    )
    for i, j in pairs:
        anga = state.terms[i]
        nxt = state.terms[j]
        if "anga" not in anga.tags:
            continue
        if not anga.varnas or not nxt.varnas:
            continue
        # Avoid interfering with the dedicated ṅasi/ṅas pūrvarūpa handling (6.1.110).
        if nxt.meta.get("upadesha_slp1") in {"Nasi", "Nas"}:
            continue
        if anga.meta.get("eco_ayavayava_done"):
            continue
        if PRAGHYA_TERM_TAG in anga.tags:
            # Pragṛhya ‖ ac — no *ay/Av* split (6.1.125 *prakṛti-bhāva*; 1.1.11 tag).
            continue
        last = anga.varnas[-1].slp1
        first = nxt.varnas[0].slp1
        if last in _ECO_SPLIT and first in AC:
            return i
    return None


def _find_target(state: State):
    """
    Find a boundary where stem-a meets pratyaya-o of 'os'.  Insert y
    between the stem's final 'a' and the pratyaya's 'o'.
    """
    if len(state.terms) < 2:
        return None
    pairs = (
        iter_anga_to_following_pratyaya_pairs(state)
        if state_has_sup_luk_ghost(state)
        else ((i, i + 1) for i in range(len(state.terms) - 1))
    )
    for i, j in pairs:
        anga = state.terms[i]
        nxt = state.terms[j]
        if not anga.varnas or not nxt.varnas:
            continue
        if "anga" not in anga.tags:
            continue
        if nxt.meta.get("upadesha_slp1") != "os":
            continue
        # Idempotency: skip if already inserted.
        if anga.meta.get("ay_insertion_done"):
            continue
        if anga.varnas[-1].slp1 != "a":
            continue
        if nxt.varnas[0].slp1 != "o":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return (
        _find_eco_aci_boundary(state) is not None
        or _find_target(state) is not None
    )


def act(state: State) -> State:
    i = _find_eco_aci_boundary(state)
    if i is not None:
        anga = state.terms[i]
        last = anga.varnas[-1].slp1
        a, yv = _ECO_SPLIT[last]
        anga.varnas[-1] = mk(a)
        anga.varnas.append(mk(yv))
        anga.meta["eco_ayavayava_done"] = True
        return state

    i = _find_target(state)
    if i is None:
        return state
    anga = state.terms[i]
    # Legacy narrow helper: insert 'y' at the END of the aṅga Term.
    anga.varnas.append(mk("y"))
    anga.meta["ay_insertion_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.78",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "eco ayavAyAvaH",
    text_dev       = "एचोऽयवायावः",
    padaccheda_dev = "एचः अय्-अव्-आय्-आवः",
    why_dev        = "एचः (ए, ऐ, ओ, औ) स्थाने परे अचि "
                     "क्रमेण अय्, अव्, आय्, आव् आदेशः (एचोऽयवायावः) — "
                     "ओस्-विषयकः पूर्वे य्-आगम-वर्णनम् अत्रानुपयुक्तम्। "
                     "अत्र यथा अङ्गान्ते एच्-वर्णः \"e\" (गुणात्) + परे अच् \"a\" (विकरणादादौ) → "
                     "\"e\"+\"a\" → \"a\"+\"y\"+\"a\" (अय्) → je+a+… → jay+a+… → jayati। "
                     "अपरः प्रसङ्गः: अदन्त-अङ्ग + \"ओस्\"-प्रत्यय (a+o) पूर्वे \"य्\"-आगमः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
