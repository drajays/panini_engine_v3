"""
7.2.43  ऋतश्च संयोगादेः  —  VIDHI

Padaccheda: ऋतः च संयोग-आदेः

ऋतश्च संयोगादेः (7.2.43)
Pāṭha: ashtadhyayi.com data.txt row i=72043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_BLOCKS = ("7.2.35",)      # a seṭ dhātu (vṛ, tṝ): the iṭ-less branch


def _site(state: State):
    """A short-ṛ-final dhātu that begins with a conjunct, before the ātmanepada liṅ / sic: the iṭ is optional (smṛṣīṣṭa / smariṣīṣṭa; Kāśikā 7.2.43)."""
    if not any("atmanepada" in t.tags or ("tin_adesha_3_4_78" in t.tags and "parasmaipada" not in t.tags) for t in state.terms):
        return None      # the loop never tags atmanepada: a tiṅ that is not parasmaipada is it (as in engine/ling_sic_kit)
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags or not t.varnas:
            continue
        if not (t.varnas[-1].slp1 == "f" and len(t.varnas) > 2 and t.varnas[0].slp1 not in "aAiIuUfFxXeEoO" and t.varnas[1].slp1 not in "aAiIuUfFxXeEoO"):
            continue
        rest = state.terms[i + 1:]
        if any((u.meta.get("source_lakara_upadesha") or "").strip() == "liG" for u in rest) \
                or any((u.meta.get("upadesha_slp1") or "").strip() == "sic" for u in rest):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if "7.2.35" in state.blocked_sutras:      # an aniṭ dhātu (smṛ, 7.2.10): this branch gives the iṭ back
        state.blocked_sutras.discard("7.2.35")
    else:
        state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.43",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "ftaSca saMyogAdeH",
    text_dev              = "ऋतश्च संयोगादेः",
    samagra_slp1          = "aNgasya ftaH ca saMyogAdeH valAdeH iw ArDaDAtukasya vA liNsicoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऋतः च संयोगादेः वलादेः इट् आर्धधातुकस्य वा लिङ्सिचोः",
    padaccheda_dev        = "ऋतः च संयोग-आदेः",
    why_dev               = "(सूत्रम् 7.2.43) ऋतश्च संयोगादेः।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the iṭ is the default reading; choose({"7.2.43": True}) / explore() give the other branch (iṭ-less for a seṭ dhātu, iṭ for an aniṭ one)
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
