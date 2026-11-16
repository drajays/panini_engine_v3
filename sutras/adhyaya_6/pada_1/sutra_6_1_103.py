"""
6.1.103  तस्माच्छसो नः पुंसि  —  VIDHI

"For masculine (puṃsi), the śas-ending (Sas) yields final 'n'."

Operational meaning (v3.4 scope):
  - Keep the existing a-stem handling for रामा́न्.
  - Extend to i-stem masculine like हरि + Sas → हरीन्.

We implement as a single-step VIDHI: when the pratyaya upadesha is
'Sas' and the aṅga ends in 'a' AND the liṅga is pulliṅga, perform
the combined substitution directly:
  - delete stem's final 'a'
  - replace pratyaya 'S a s' → 'A n'

पुंसि is the sūtra's own restriction and is now part of ``cond``, read from
the aṅga's liṅga tag. A feminine or neuter stem does not reach this rule at
all: it keeps the pūrvasavarṇa 6.1.102 gave it (नदी + अस् → नदीस् → नदीः).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 61103 · तस्माच्छसो नः पुंसि
              padaccheda: तस्मात् शसः नः पुंसि
              anuvṛtti:   61072: संहितायाम् | 61102: पूर्वसवर्णः
  Source #2 — Kāśikā 6.1.103 udāharaṇa:
                वृक्षान्
                अग्नीन्
                वायून्
  Cross-check — surface pinned by: tests/unit/test_SamBu_subanta.py
  Reference record: sutra_ref_out/6_1_103.json
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
    # तस्मात्: only after 6.1.102 has made the pūrvasavarṇa dīrgha on this śas (the ekādeśa is 6.1.102's work, not this sūtra's)
    if not pratyaya.meta.get("Sas_purvasavarna_done"):
        return False
    # पुंसि — the sūtra's own restriction, read off the aṅga's liṅga tag
    # (structural, not a paradigm coordinate). Feminine and neuter stems keep
    # whatever 6.1.102 gave them: नदी + अस् → नदीस् → नदीः, and the old
    # unconditional As-substitution here overwrote exactly that.
    # तस्मात्: after the 6.1.102 pūrvasavarṇa dīrgha — an ak-final aṅga (राम, हरि, गुरु,
    # पितृ); a hal-final one (राजन्) keeps शस् as अस् (राज्ञः)
    if not pratyaya.varnas or pratyaya.varnas[-1].slp1 != "s":
        return False
    return bool({"pulliṅga", "pum"} & anga.tags)


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pratyaya = state.terms[-1]
    # only the s of the śas becomes n; 6.1.102 already made the dīrgha (a-stem: the suffix is A+s; other ak-stems: lengthened aṅga + s)
    pratyaya.varnas[-1] = mk("n")
    pratyaya.meta["sas_substitution_done"] = True
    pratyaya.meta["upadesha_slp1_original"] = "Sas"
    pratyaya.meta["upadesha_slp1"] = "".join(v.slp1 for v in pratyaya.varnas)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.103",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'tasmAcCaso naH puMsi',
    text_dev       = 'तस्माच्छसो नः पुंसि',
    samagra_slp1   = "praTamayoH pUrvasavarRaH tasmAt pu~si SasaH naH",
    samagra_dev    = "प्रथमयोः पूर्वसवर्णः तस्मात् पुँसि शसः नः",
    padaccheda_dev = "तस्मात् शसः नः पुंसि",
    why_dev        = "पुंलिङ्ग-अदन्त-प्रातिपदिकात् परस्य 'शस्'-प्रत्ययस्य "
                     "पूर्वसवर्ण-दीर्घानन्तरं स-कारस्य न-कारादेशः।",
    anuvritti_from = ("6.1.84", "6.1.102"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
