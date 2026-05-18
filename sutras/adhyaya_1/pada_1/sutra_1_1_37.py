"""
1.1.37  स्वरादिनिपातमव्ययम्  —  SAMJNA

Meaning: The svarādi-nipātas are avyaya (indeclinable).

"svarādi" refers to the group of nipāta (particle) words beginning with
"svar" as listed in the nipāta-gaṇa; these are invariably-formed words
that do not take inflectional suffixes (sup-luk by 2.4.82).

Engine (glass-box):
  - A Term whose kind == "nipata" OR whose upadesha_slp1 is in the
    module-level SVARADI_NIPATA_SLP1 frozenset, and which does not yet
    carry the "avyaya" tag, gets tagged "avyaya".
  - Metadata-only change; no surface phoneme altered.

Mechanical blindness (CONSTITUTION Art. 2):
  - cond() reads only Term.kind, Term.meta['upadesha_slp1'], and Term.tags.
  - No vibhakti/vacana/lakāra/gold access.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — traditional svarādi-nipāta list (SLP1 transliteration).
SVARADI_NIPATA_SLP1: frozenset = frozenset({
    "svar",      # the head of the gaṇa
    "antar",     # antara as nipāta-indeclinable
    "prAtar",    # prātar (in the morning)
    "aDas",      # adhas (below)
    "upari",     # upari (above)
    "Avis",      # āvis (manifestly)
    "bahis",     # bahis (outside)
    "agre",      # agre (in front)
    "A",         # ā (up to)
    "i",         # i (particle)
    "u",         # u (particle)
    "RO",        # particle
    "svasti",    # svasti (well-being)
    "alam",      # alam (enough)
    "namas",     # namas (salutation)
    "nanu",      # nanu (is it not)
    "mA",        # mā (prohibitive)
    "mA~",       # mā (with anunāsika marking)
    "mAgra",     # māgra
    "mAGam",     # māgham
    "vi",        # vi (apart)
    "su",        # su (well)
    "dus",       # dus (ill)
    "puras",     # puras (in front)
    "purA",      # purā (formerly)
    "tiras",     # tiras (across/secretly)
    "purA~",     # purā (with anunāsika marking)
    "sad",       # sat
    "saT",       # saṭ
    "sacA",      # sacā (together)
    "sAkam",     # sākam (together)
    "sAkza",     # sākṣa (in person)
    "svayam",    # svayam (by oneself)
    "kintu",     # kintu (but)
    "paramtu",   # paramtu (however)
    "nahi",      # nahi (not at all)
    "nAnu",      # nānu
    "aho",       # aho (exclamation)
    "hanta",     # hanta (alas / well)
    "evam",      # evam (thus)
    "taTā",      # tathā (so)
    "yaTā",      # yathā (as)
    "iti",       # iti (thus / quote-marker)
    "cet",       # cet (if)
    "yadi",      # yadi (if)
    "kim",       # kim (what? — as particle)
    "ku",        # ku (ill / how?)
    "kuvid",     # kuvid (perhaps)
})


def _eligible(state: State):
    for t in state.terms:
        if "avyaya" in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if t.kind == "nipata" or (isinstance(upa, str) and upa in SVARADI_NIPATA_SLP1):
            yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    for t in _eligible(state):
        t.tags.add("avyaya")
    state.samjna_registry["1_1_37_svarAdinipAta"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.1.37",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "svarAdinipatam avyayam",
    text_dev              = "स्वरादिनिपातमव्ययम्",
    padaccheda_dev        = "स्वर-आदि-निपातम् / अव्ययम्",
    why_dev               = (
        "स्वरादि-निपाताः अव्यय-संज्ञकाः; ततो २.४.८२ सुप्-लुक्।"
    ),
    anuvritti_from        = (),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)

__all__ = ["SVARADI_NIPATA_SLP1", "SUTRA"]
