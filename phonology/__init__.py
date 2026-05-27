"""
phonology — pure phoneme-level machinery.

Nothing in this package references engine.* at module load time — these
are leaf utilities.  Sūtra files import mk/AC/HAL/IK/... from here.
"""
from phonology.varna      import Varna, mk, parse_slp1_upadesha_sequence, AC_DEV, HAL_DEV, AC_MATRA, HAL_BASE
from phonology.pratyahara import (
    AC, HAL, IK, EC, JHAL, KHAR, YAN, TUSMA, CUTU, KU_VARGA, NI_TU_DU,
    is_hrasva, is_dirgha,
)
from phonology.pratyaya_pratyahara import (
    build_pratyaya_pratyahara,
    SUP, SUT, TAP, TIN, TAN, TRN, SAN, PARASMAI,
    is_sup_upadesha, is_tin_upadesha, is_atmanepada_tin,
    is_parasmaipada_tin, is_tap_upadesha,
)
from phonology.savarna    import is_savarna, dirgha_of
from phonology.joiner     import slp1_to_devanagari

__all__ = [
    "Varna", "mk",
    "AC", "HAL", "IK", "EC", "JHAL", "KHAR", "YAN",
    "TUSMA", "CUTU", "KU_VARGA", "NI_TU_DU",
    "AC_DEV", "HAL_DEV", "AC_MATRA", "HAL_BASE",
    "parse_slp1_upadesha_sequence",
    "is_hrasva", "is_dirgha",
    "is_savarna", "dirgha_of",
    "slp1_to_devanagari",
    # Pratyaya pratyāhāras (1.1.71)
    "build_pratyaya_pratyahara",
    "SUP", "SUT", "TAP", "TIN", "TAN", "TRN", "SAN", "PARASMAI",
    "is_sup_upadesha", "is_tin_upadesha", "is_atmanepada_tin",
    "is_parasmaipada_tin", "is_tap_upadesha",
]
