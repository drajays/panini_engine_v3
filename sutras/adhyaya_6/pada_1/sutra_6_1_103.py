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
    # पुंसि — the sūtra's own restriction, read off the aṅga's liṅga tag
    # (structural, not a paradigm coordinate). Feminine and neuter stems keep
    # whatever 6.1.102 gave them: नदी + अस् → नदीस् → नदीः, and the old
    # unconditional As-substitution here overwrote exactly that.
    return bool({"pulliṅga", "pum"} & anga.tags)


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if True:
        if anga.varnas and anga.varnas[-1].slp1 == "a":
            # a-stem: delete stem's final 'a' — absorbed by the lengthening.
            del anga.varnas[-1]
            pratyaya.varnas = [mk("A"), mk("n")]
            new_upa = "An"
        elif anga.varnas and anga.varnas[-1].slp1 == "i":
            # i-stem: i + śas → īn (hari → harīn)
            anga.varnas[-1] = mk("I")
            pratyaya.varnas = [mk("n")]
            new_upa = "n"
        elif anga.varnas and anga.varnas[-1].slp1 == "u":
            # u-stem: u + śas → ūn (śambhu → śambhūn) via pūrva-savarṇa dīrgha
            anga.varnas[-1] = mk("U")
            pratyaya.varnas = [mk("n")]
            new_upa = "n"
        else:
            # Fallback: keep existing behaviour (no-op would violate R1),
            # so treat like the a-stem An substitution without stem deletion.
            pratyaya.varnas = [mk("A"), mk("n")]
            new_upa = "An"
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
