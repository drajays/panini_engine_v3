"""
1.2.1  गाङ्कुटादिभ्योऽञ्णिन्ङित्  —  ATIDESHA

"After the dhātus गाङ् (= gāN, meaning 'to go') and those of the
 kuṭādi-gaṇa, the pratyayas which are not listed as ñit or ṇit
 behave AS-IF they were ṅit (i.e. kit-like, blocking guṇa/vṛddhi)."

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 12001 · गाङ्कुटादिभ्योऽञ्णिन्ङित्
              padaccheda: गाङ्-कुटादिभ्यः अञ्णित् ङित्
  Source #2 — Kāśikā 1.2.1 udāharaṇa:
                अध्यगीष्ट, कुटिता, कुटितुम्, कुटितव्यम्
                pratyudāharaṇa: उत्कोटयति (ṇic, ṇit), चुकोट (ṇal), उत्कोटः (ghañ, ñit)
  Cross-check — ashtadhyayi.com gold कुटिता / चुकुटिथ / चुकोट (bench/ashtadhyayi_gold.py);
                tests/unit/test_kutadi_1_2_1.py; pipelines/adhyagIzwa_luN.py (अध्यगीष्ट)

Membership: the dhātu's upadeśa is गाङ् (``gAN``), or its dhātupāṭha antargaṇa
is कुटादिः (``meta["antarganas"]`` — lexical, like the gaṇa). By 1.1.67
तस्मादित्युत्तरस्य the atideśa reaches the pratyaya immediately after the dhātu;
unless that pratyaya is ñit / ṇit (its it-markers hold ``Y`` / ``R``), it is
tagged ``kngiti`` — the same mark 1.2.5 gives, read by 1.1.5 क्ङिति च. The
registry entry 6.4.66 reads for गाङ् is kept.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

_KUTADI = "कुटादिः"


def _member(t) -> bool:
    if "dhatu" not in t.tags or "abhyasa" in t.tags:
        return False
    return t.meta.get("upadesha_slp1") == "gAN" or _KUTADI in (t.meta.get("antarganas") or ())


def _nyit_or_nit(p) -> bool:
    marks = p.meta.get("it_markers") or set()
    if "Y" in marks or "R" in marks:
        return True
    up = (p.meta.get("upadesha_slp1") or "").strip()
    return bool(up) and (up[0] in "YR" or up[-1] in "YR")


def _target(state: State):
    for i, t in enumerate(state.terms):
        if not _member(t):
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if (nxt is not None and "pratyaya" in nxt.tags and "kngiti" not in nxt.tags
                and not _nyit_or_nit(nxt)):
            return nxt
    return None


def _gaN(state: State) -> bool:
    return any(t.meta.get("upadesha_slp1") == "gAN" for t in state.terms)


def cond(state: State) -> bool:
    key = ("pratyaya_after_gaN_or_kutAdi", "pratyaya")
    return _target(state) is not None or (_gaN(state) and key not in state.atidesha_map)


def act(state: State) -> State:
    if _gaN(state):
        state.atidesha_map[("pratyaya_after_gaN_or_kutAdi", "pratyaya")] = "ṅit"
    nxt = _target(state)
    if nxt is not None:
        nxt.tags.add("kngiti")
    return state


SUTRA = SutraRecord(
    sutra_id         = "1.2.1",
    sutra_type       = SutraType.ATIDESHA,
    text_slp1        = 'gANkuwAdiByoYRinNit',
    text_dev         = 'गाङ्कुटादिभ्योऽञ्णिन्ङित्',
    padaccheda_dev   = "गाङ्-कुटादिभ्यः अञ्-णित्-ङित्",
    why_dev          = "गाङ्/कुटादि धातोः परस्य प्रत्ययस्य (अञ्-णित्-भिन्नस्य) "
                       "ङित्वम् अतिदिश्यते — कुटिता।",
    anuvritti_from   = (),
    cond             = cond,
    act              = act,
    atidesha_target  = "ṅit",
    atidesha_source  = "pratyaya_after_gaN_or_kutAdi",
    atidesha_dest    = "pratyaya",
)

register_sutra(SUTRA)
