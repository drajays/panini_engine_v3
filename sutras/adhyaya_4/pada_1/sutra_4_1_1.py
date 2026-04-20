"""
4.1.1  ङ्याप्प्रातिपदिकात्  —  ANUVADA

"(The following sūtras operate) from a prātipadika that ends in
 ङी or आप् (the feminine-stem-formers) — OR from a prātipadika as
 such."

Pure anuvāda: it does no operation.  It simply re-states the
inheritance scope for subsequent sup-attachment rules
(4.1.2 'svaujasamauṭchaṣṭā ...').  Trace reflects the fact.

Per CONSTITUTION.md Article 4, the anuvṛtti is baked into downstream
sūtras' text_slp1 already — this file exists so the trace shows the
classical reader what-carries-over at this point.
"""
from engine        import SutraType, SutraRecord, register_sutra


SUTRA = SutraRecord(
    sutra_id       = "4.1.1",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "NyAp prAtipadikAt",
    text_dev       = "ङ्याप्-प्रातिपदिकात्",
    padaccheda_dev = "ङी-आप्-प्रातिपदिकात्",
    why_dev        = "ङी/आप्-अन्त-प्रातिपदिकात् अथवा प्रातिपदिकात् — "
                     "इति अनुवादः; अग्रिम-सूत्राणां स्कोप-निर्देशः।",
    anuvritti_from = (),
    cond           = None,
    act            = None,
)

register_sutra(SUTRA)
