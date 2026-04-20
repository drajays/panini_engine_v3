"""
phonology — pure phoneme-level machinery.

Nothing in this package references engine.* at module load time — these
are leaf utilities.  Sūtra files import mk/AC/HAL/IK/... from here.
"""
from phonology.varna      import Varna, mk, AC_DEV, HAL_DEV, AC_MATRA, HAL_BASE
from phonology.pratyahara import (
    AC, HAL, IK, EC, JHAL, KHAR, YAN, TUSMA, CUTU, KU_VARGA, NI_TU_DU,
    is_hrasva, is_dirgha,
)
from phonology.savarna    import is_savarna, dirgha_of
from phonology.joiner     import slp1_to_devanagari

__all__ = [
    "Varna", "mk",
    "AC", "HAL", "IK", "EC", "JHAL", "KHAR", "YAN",
    "TUSMA", "CUTU", "KU_VARGA", "NI_TU_DU",
    "AC_DEV", "HAL_DEV", "AC_MATRA", "HAL_BASE",
    "is_hrasva", "is_dirgha",
    "is_savarna", "dirgha_of",
    "slp1_to_devanagari",
]
