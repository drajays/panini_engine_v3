"""
6.1.103  तस्माच्छसो नः पुंसि  —  VIDHI

"For a masculine a-stem (puṃsi), after the substitution of 6.1.102
 pūrva-savarṇa applies, the 's' of Sas (accusative plural) is replaced
 by 'n'."

Operational meaning:
  cell 2-3: rAma + Sas (acc pl)
            → by the preceding 6.1.102-family pūrva-savarṇa, stem-final
              'a' absorbs pratyaya-initial 'Sa' → 'A' + 's'
            → then 6.1.103 (masc-a-stem specific) replaces 's' by 'n'
            → rAmAn → रामान्

We implement as a single-step VIDHI: when the pratyaya upadesha is
'Sas' and the aṅga ends in 'a' AND the liṅga is pulliṅga, perform
the combined substitution directly:
  - delete stem's final 'a'
  - replace pratyaya 'S a s' → 'A n'

Liṅga is a state.meta field, readable by act() (but NOT by cond()).
For cond, we require the pratyaya tag 'sup' + upadesha 'Sas' + stem
final 'a'.  The masc/neut/fem split is performed in act().
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pratyaya.tags:
        return False
    if pratyaya.meta.get("upadesha_slp1") != "Sas":
        return False
    if pratyaya.meta.get("sas_substitution_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    # Delete stem's final 'a' — absorbed by the lengthening.
    del anga.varnas[-1]
    # Choose pratyaya replacement based on liṅga.
    linga = state.meta.get("linga", "pulliṅga")
    if linga == "pulliṅga":
        # Sas → An for masculine a-stems.
        pratyaya.varnas = [mk("A"), mk("n")]
        new_upa = "An"
    else:
        # Neuter / feminine: standard pūrva-savarṇa → As.
        pratyaya.varnas = [mk("A"), mk("s")]
        new_upa = "As"
    pratyaya.meta["sas_substitution_done"] = True
    pratyaya.meta["upadesha_slp1_original"] = "Sas"
    pratyaya.meta["upadesha_slp1"] = new_upa
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.103",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tasmAc CasaH naH puMsi",
    text_dev       = "तस्माच्छसो नः पुंसि",
    padaccheda_dev = "तस्मात् शसः नः पुंसि",
    why_dev        = "पुंलिङ्ग-अदन्त-प्रातिपदिकात् परस्य 'शस्'-प्रत्ययस्य "
                     "पूर्वसवर्ण-दीर्घानन्तरं स-कारस्य न-कारादेशः।",
    anuvritti_from = ("6.1.84", "6.1.102"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
