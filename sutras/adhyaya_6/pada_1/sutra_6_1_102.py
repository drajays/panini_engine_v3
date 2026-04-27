"""
6.1.102  प्रथमयोः पूर्वसवर्णः  —  VIDHI

"At the boundary of the prathamā and dvitīyā (nominative / accusative)
 pratyayas, when a + ac occurs, the pūrva-savarṇa (the long vowel
 matching the pūrva letter) replaces both."

Operational narrow reading for rāma paradigm:
  cell 1-3 / 8-3: rAma + jas → rAmAs (a + ja is consumed:
                  the 'j' is absorbed under the prathamā-plural
                  pūrvasavarṇa rule — stem-final 'a' + pratyaya 'j a'
                  → 'ā + s').  Then tripāḍī 8.2.66 s→ru, 8.3.15 ru→H
                  → rAmAH.

We detect this narrowly: when state.terms[-1] is a sup pratyaya whose
upadeśa is 'jas' AND the preceding aṅga ends in 'a', perform the
combined substitution:
  - delete the stem-final 'a'
  - replace pratyaya 'j a s' → 'A s'

This collapses the 'ja' portion under the pūrva's lengthening.

Applies only to prathamā-plural (1-3) and sambuddhi-plural (8-3)
— both use the 'jas' upadeśa.  Dvitīyā-plural uses 'Sas' which is
handled by the sister rule 6.1.102b (our sutra_6_1_102_sas.py, or
treated here with target upadesha 'Sas' → 'An' variant).
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TAG_REFRESH_ARM_META


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pratyaya.tags:
        return False
    up = pratyaya.meta.get("upadesha_slp1")
    if up == "jas":
        if pratyaya.meta.get("jas_purvasavarna_done"):
            return False
        if not anga.varnas:
            return False
        return anga.varnas[-1].slp1 == "a"
    if up in {"O", "Ow"}:
        # v3.4 extension: i-stem dual (hari + au → harī) under the same
        # pūrva-savarṇa idea (prathamā/dvitīyā dual boundary).
        if pratyaya.meta.get("au_purvasavarna_done"):
            return False
        if not anga.varnas or not pratyaya.varnas:
            return False
        if anga.varnas[-1].slp1 == "i" and pratyaya.varnas[0].slp1 == "O":
            return True
        # u-stem dual (vāyu + au → vāyū) — same *pūrva-savarṇa* pattern as *hari* + *au*.
        return anga.varnas[-1].slp1 == "u" and pratyaya.varnas[0].slp1 == "O"
    return False


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    up = pratyaya.meta.get("upadesha_slp1")
    if up == "jas":
        # Delete the stem-final 'a'.
        del anga.varnas[-1]
        # Replace pratyaya 'j a s' → 'A s' (the pūrva-savarṇa lengthens
        # the combined a+a → ā; the 'j' vanishes under this merger).
        pratyaya.varnas = [mk("A"), mk("s")]
        pratyaya.meta["jas_purvasavarna_done"] = True
        pratyaya.meta["upadesha_slp1_original"] = "jas"
        pratyaya.meta["upadesha_slp1"] = "As"
        return state
    if up in {"O", "Ow"}:
        # i + au → ī (hari + au → harī); u + au → ū (vāyu + au → vāyū)
        last = anga.varnas[-1].slp1
        anga.varnas[-1] = mk("I" if last == "i" else "U")
        # Drop the pratyaya entirely; the long vowel is the combined result.
        pratyaya.varnas = []
        pratyaya.meta["au_purvasavarna_done"] = True
        # Stem-final *ī/ū* is now *pragṛhya*-eligible; **1.1.11** runs again in P13.
        state.meta[PRAGHYA_TAG_REFRESH_ARM_META] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.102",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "prathamayoH pUrvasavarRaH",
    text_dev       = "प्रथमयोः पूर्वसवर्णः",
    padaccheda_dev = "प्रथमयोः पूर्व-सवर्णः",
    why_dev        = "प्रथमा/द्वितीया-बहुवचन-सीमायां अ+अच्-योः पूर्व-सवर्ण-दीर्घः "
                     "(जस्-प्रत्यये परे 'ज'-वर्णोऽपि पूर्वयोगेन अन्तर्भवति)।",
    anuvritti_from = ("6.1.84", "6.1.101"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
