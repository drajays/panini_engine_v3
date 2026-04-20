"""
1.2.1  गाङ्कुटादिभ्योऽञ्णिन्ङित्  —  ATIDESHA

"After the dhātus गाङ् (= gāN, meaning 'to go') and those of the
 kuṭādi-gaṇa, the pratyayas which are not listed as ñit or ṇit
 behave AS-IF they were ṅit (i.e. kit-like, blocking guṇa/vṛddhi)."

ATIDESHA: transfers the property 'ṅit-ness' from a fictive source
to real pratyayas in a given context.  It writes to
state.atidesha_map[(source, dest)] = target_property, which subsequent
guṇa/vṛddhi VIDHIs consult.

For this representative file we do the minimal: if ANY Term has
upadesha_slp1 == 'gAN' or tag 'kuṭādi', install the atideśa.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    for t in state.terms:
        if t.meta.get("upadesha_slp1") == "gAN":
            return True
        if "kuṭādi" in t.tags:
            return True
    return False


def act(state: State) -> State:
    state.atidesha_map[("pratyaya_after_gaN_or_kutAdi", "pratyaya")] = "ṅit"
    return state


SUTRA = SutraRecord(
    sutra_id         = "1.2.1",
    sutra_type       = SutraType.ATIDESHA,
    text_slp1        = "gANkuwAdibhyo aY-Rin-Nit",
    text_dev         = "गाङ्कुटादिभ्योऽञ्णिन्ङित्",
    padaccheda_dev   = "गाङ्-कुटादिभ्यः अञ्-णित्-ङित्",
    why_dev          = "गाङ्/कुटादि धातोः परस्य प्रत्ययस्य (अञ्-णित्-भिन्नस्य) "
                       "ङित्वम् अतिदिश्यते।",
    anuvritti_from   = (),
    cond             = cond,
    act              = act,
    atidesha_target  = "ṅit",
    atidesha_source  = "pratyaya_after_gaN_or_kutAdi",
    atidesha_dest    = "pratyaya",
)

register_sutra(SUTRA)
