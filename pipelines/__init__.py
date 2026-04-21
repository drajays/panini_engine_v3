from pipelines.krdanta import derive_pAcakaH, derive_pAcaka_pratipadika
"""
pipelines — end-to-end derivations (subanta, tinanta, ...).

A pipeline orchestrates apply_rule() calls in Aṣṭādhyāyī order.  It is
NOT part of the engine core and its presence or absence does not
affect correctness of any sūtra.  Pipelines exist so that test suites
can exercise the engine on realistic derivations.
"""
