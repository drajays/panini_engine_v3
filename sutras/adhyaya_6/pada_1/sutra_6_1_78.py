"""
6.1.78  एचोऽयवायावः  —  VIDHI

Classical rule:
  If an EC vowel (e/E/o/O) is followed by an AC vowel, the EC splits:
    e → ay, E → Ay, o → av, O → Av

Universal: fires on any ec‖ac, inside a Term or across Terms (no aṅga-tag gate).
रामयोः is derived honestly: 7.3.104 ओसि च (a → e) then this rule (e → ay).

v3.5: skip the *ec*+*ac* split when the *aṅga* **Term** carries **1.1.11**
``pragrahya`` (e.g. *māle* + *iti* — **6.1.125** *prakṛti-bhāva*).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61078 · एचोऽयवायावः
              padaccheda: एचः अय्-अव्-आय्-आवः
              anuvṛtti:   61072: संहितायाम् | 61077: अचि
              adhikāra:   6.1.72
  Source #2 — Kāśikā 6.1.78 udāharaṇa:
                चयनम्
                लवनम्
                चायकः
  Gloss (sa) — संहितायाम् अचि परतः एचः स्थाने अय्/अव्/आय्/आव् आदेशाः यथासङ्ख्यं भवन्ति।
  Cross-check — surface pinned by: tests/forward/test_forward_krdanta_nayaka.py, tests/forward/test_forward_krdanta_pacaka.py, tests/regression/test_anya_pullinga_gold.py
  Reference record: sutra_ref_out/6_1_78.json
"""
from engine import SutraType, SutraRecord, register_sutra
from engine.lopa_ghost import iter_anga_to_following_pratyaya_pairs, state_has_sup_luk_ghost
from engine.state import State
from phonology     import mk
from phonology.pratyahara import AC

# AC pratyāhāra in the engine stores only short vowels (savarṇa via savarna.py).
# 6.1.78 fires before ANY ac — both short and long — so extend the check set.
_AC_ALL = AC | frozenset({"A", "I", "U", "F", "X"})

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


_ECO_SPLIT = {
    "e": ("a", "y"),
    "E": ("A", "y"),
    "o": ("a", "v"),
    "O": ("A", "v"),
}


def _live_pairs(state: State):
    """Adjacent terms *as heard*: a term emptied by lopa (1.1.60 अदर्शनम्, e.g. the
    vikaraṇa a after 6.1.97) is invisible, so ec meets the next audible term."""
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    return zip(live, live[1:])


def _find_eco_aci_boundary(state: State) -> tuple[int, int] | None:
    """
    Flat scan: ``(term_i, varna_i)`` of an EC vowel immediately followed by an
    AC vowel — inside one Term, or across a Term boundary (left Term not
    pragṛhya, not already split; ṅasi/ṅas left to 6.1.110).
    """
    for i, left in enumerate(state.terms):
        vs = left.varnas
        for k in range(len(vs) - 1):  # intra-term
            if vs[k].slp1 in _ECO_SPLIT and vs[k + 1].slp1 in _AC_ALL:
                return i, k
    pairs = (
        iter_anga_to_following_pratyaya_pairs(state)
        if state_has_sup_luk_ghost(state)
        else _live_pairs(state)
    )
    for i, j in pairs:
        left, nxt = state.terms[i], state.terms[j]
        if left.meta.get("eco_ayavayava_done") or PRAGHYA_TERM_TAG in left.tags:
            continue  # pragṛhya ‖ ac: 6.1.125 prakṛti-bhāva
        # ṅasi/ṅas pūrvarūpa is 6.1.110's business.
        if nxt.meta.get("upadesha_slp1") in {"Nasi", "Nas"}:
            continue
        if left.varnas[-1].slp1 in _ECO_SPLIT and nxt.varnas[0].slp1 in _AC_ALL:
            return i, len(left.varnas) - 1
    return None


def cond(state: State) -> bool:
    return _find_eco_aci_boundary(state) is not None


_WHY_NOW = (
    "अच्-वर्णे परे एच्-वर्णस्य (ए/ऐ/ओ/औ) क्रमेण अय्/आय्/अव्/आव् इति आदेशः; "
    "यथा ए+अ → अय् (जे+अ → जय → जयति)। (६.१.७८)"
)


def act(state: State) -> State:
    hit = _find_eco_aci_boundary(state)
    if hit is None:
        return state
    i, k = hit
    left = state.terms[i]
    a, yv = _ECO_SPLIT[left.varnas[k].slp1]
    left.varnas[k] = mk(a)
    left.varnas.insert(k + 1, mk(yv))
    left.meta["eco_ayavayava_done"] = True
    state.meta["__why_now_dev__"] = _WHY_NOW
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.78",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'ecoyavAyAvaH',
    text_dev       = 'एचोऽयवायावः',
    padaccheda_dev = "एचः अय्-अव्-आय्-आवः",
    why_dev        = "एचः (ए, ऐ, ओ, औ) स्थाने परे अचि "
                     "क्रमेण अय्, अव्, आय्, आव् आदेशः (एचोऽयवायावः) — "
                     "अत्र यथा अङ्गान्ते एच्-वर्णः \"e\" (गुणात्) + परे अच् \"a\" (विकरणादादौ) → "
                     "\"e\"+\"a\" → \"a\"+\"y\"+\"a\" (अय्) → je+a+… → jay+a+… → jayati।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
