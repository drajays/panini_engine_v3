"""
5.3.71  अव्ययसर्वनाम्नामकच् प्राक् टेः  —  VIDHI

*Śāstrīya* target (v3 *corpus*): a-stem *sarvanāma* in the *sarvādi* list, when the
derivation is *armed* (``5_3_71_akac_arm`` in *state*.*meta* — *not* a *siddha*
reading of (vibhakti, vacana); *CONSTITUTION* Art. 2), receives the *taddhita*
*upadeśa* *akac* (śeṣa *ak* after **1.3.3** *c* = *it*, **1.3.9** *lopa* — one *vidhi*
inserō here as *a* + *k* *varṇa*s *prāk* the final *ac* (*ṭi* zone per **1.1.64**
*prayoga*; the engine does not materialise a separate **1.1.64** *śabda* here).

*Prāk ṭeḥ* = immediately before the last *ac* of a single *aṅga* *Term* whose *upadeśa* is
a-*anta*; output base shape ``…aka`` (e.g. *sarva* → ``sarvaka``).

*Cross-check* *pāṭha* / machine row: *ashtadhyayi-com* *sutraani* ``i=53071`` if needed.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from engine.it_phonetic import term_phonetic_slp1
from phonology     import mk

META_5_3_71_AKAC_ARM: str = "5_3_71_akac_arm"
"""Set by *recipe* (``pipelines.sarvaka_subanta``) before **5.3.71** — not *siddha* *vivakṣā*."""

_META_VYUTPANNA: str = "5_3_71_akac_vyutpanna"


def _open_5_3_70(state: State) -> bool:
    return any(
        (e.get("id") == "5.3.70")
        and (e.get("scope_end") == "5.3.95")
        for e in state.adhikara_stack
    )


def _site_akac_infix(state: State) -> int | None:
    if not state.meta.get(META_5_3_71_AKAC_ARM):
        return None
    if not _open_5_3_70(state):
        return None
    if len(state.terms) != 1:
        return None
    t = state.terms[0]
    if "anga" not in t.tags or "prātipadika" not in t.tags:
        return None
    if "sarvanama" not in t.tags:
        return None
    if not t.varnas or t.varnas[-1].slp1 != "a":
        return None
    if t.meta.get(_META_VYUTPANNA):
        return None
    return 0


def cond(state: State) -> bool:
    return _site_akac_infix(state) is not None


def act(state: State) -> State:
    idx = _site_akac_infix(state)
    if idx is None:
        return state
    t = state.terms[idx]
    v = t.varnas
    # *akac* — *c* = *it*; śeṣa *ak* *prāk ṭeḥ* (final *a*).
    t.varnas = v[:-1] + [mk("a"), mk("k"), v[-1]]
    t.tags.discard("sarvanama")
    t.meta["upadesha_slp1"] = term_phonetic_slp1(t)
    t.meta[_META_VYUTPANNA] = True
    state.meta.pop(META_5_3_71_AKAC_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id         = "5.3.71",
    sutra_type       = SutraType.VIDHI,
    text_slp1        = "avyaya-sarvanAmanAm kac prAk deH",
    text_dev         = "अव्ययसर्वनाम्नामकच् प्राक् टेः",
    padaccheda_dev   = "अव्यय-सर्वनाम्नाम् / कच् / प्राक् / टेः",
    why_dev          = (
        "सर्वनाम-अव्यय-विषये *अकच्* प्रत्ययः (च्-इत्संज्ञकलोपे *क्* शिष्यते) "
        "टि-वर्णात् (अन्त्याच्) ठञ्-नुरादौ प्राक्, अदन्त-अङ्गे — यथा *सर्व* → *सर्वक* (पश्चात् *sup*)।"
    ),
    anuvritti_from   = ("5.3.70",),
    cond             = cond,
    act              = act,
)

register_sutra(SUTRA)

__all__ = ["META_5_3_71_AKAC_ARM", "SUTRA"]
