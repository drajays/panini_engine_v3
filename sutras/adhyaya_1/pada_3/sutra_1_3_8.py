"""
1.3.8  लशक्वतद्धिते  —  SAMJNA

Sources consulted:
- ashtadhyayi.com data.txt row i=13008
- Kāśikā: "लकार — चयनम्, जयनम् (ल्युट्)। शकार — भवति, पचति (शप्)"
- Cross-validation: regression tests tests/unit/test_it_prakarana.py
  (क्त्वा → त्वा with kit, शप् → अ with śit, ल्युट् → यु, ङीष् → ई; taddhita
  कन् keeps क्)

Śāstra / engine role (CONSTITUTION Arts. 1–2, 4, 7)
──────────────────────────────────────────────────
• **Type:** SAMJNA — the **first sound** (*ādiḥ*, *pratyayasya*) of a pratyaya
  that is **not a taddhita**, if it is ल्, श् or a **ku**-varga consonant
  (क ख ग घ ङ), is *it*.  Never a dhātu, āgama or upasarga
  (``is_pratyaya_upadesha``).

• **Lakāra:** the ल् of an abstract *lakāra* (``lakAra_pratyaya_placeholder``) is
  the sthānin of 3.4.77 *lasya*, so it is not *it* here; its टित् / ङित् marker
  is **1.3.3**'s.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.it_phonetic import IT_LOPA_TAGS
from engine.it_samjna import TAG_LASAKU, is_pratyaya_upadesha, it_lopa_already_done, register_candidate_tag
from engine.state  import State
from phonology      import KU_VARGA

# ल्·श्·कवर्ग (SLP1) — *upadeśa* first letter for **1.3.8** *ataddhite*.
_LASAKU_INITIAL_SLP1 = frozenset({"l", "S"}) | KU_VARGA


def term_candidates(state: State, ti: int) -> list[int]:
    t = state.terms[ti]
    if not t.varnas or "taddhita" in t.tags or "lakAra_pratyaya_placeholder" in t.tags:
        return []
    if not is_pratyaya_upadesha(t) or it_lopa_already_done(t):
        return []
    first = t.varnas[0]
    if first.slp1 not in _LASAKU_INITIAL_SLP1 or first.tags & IT_LOPA_TAGS:
        return []
    return [0]


def cond(state: State) -> bool:
    return any(term_candidates(state, ti) for ti in range(len(state.terms)))


def act(state: State) -> State:
    for ti, t in enumerate(state.terms):
        for j in term_candidates(state, ti):
            t.varnas[j].tags.add("it_candidate_lasaku")
            state.samjna_registry[("it_lasaku", ti)] = frozenset({t.varnas[j].slp1})
    state.meta["__why_now_dev__"] = (
        "अतद्धित-प्रत्ययस्य आदौ ल्/श्/कवर्ग-वर्णः 'इत्'-संज्ञां प्राप्नोति; "
        "अयं वर्णः अनन्तरं १.३.९ इति लुप्यते (यथा शप् → अ, ङी → ई)। (१.३.८)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.8",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'laSakvatadDite',
    text_dev       = 'लशक्वतद्धिते',
    samagra_slp1   = "upadeSe atadDitasya pratyayasya AdiH la-Sa-ku it",
    samagra_dev    = "उपदेशे अतद्धितस्य  प्रत्ययस्य आदिः ल-श-कु इत्",
    padaccheda_dev = "उपदेशे लशकु-अतद्धिते इत्",
    why_dev        = (
        "अतद्धिते प्रत्ययादौ ल्-श्-कु-वर्णानाम् इत्-संज्ञा; लोपः १.३.९। "
        "सुप्-पङ्क्तिषु ङ्-आदिर् अपि (*N* ∈ *ku*)।"
    ),
    apavada_of     = ("1.3.7",),
    anuvritti_from = ("1.3.2", "1.3.5", "1.3.6"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
register_candidate_tag(TAG_LASAKU, SUTRA.sutra_id)
