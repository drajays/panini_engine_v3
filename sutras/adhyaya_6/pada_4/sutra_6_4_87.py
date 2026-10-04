"""
6.4.87  हुश्नुवोः सार्वधातुके  —  VIDHI

Padaccheda: हु-श्नुवोः सार्वधातुके

हुश्नुवोः सार्वधातुके (6.4.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_AC = frozenset("aAiIuUfFxXeEoO")


def _weak_after(ts, k: int) -> bool:
    """The affix right after the vikaraṇa (an āgama such as āṭ belongs to it) is not pit: weak (cinvanti), whether or not
    1.2.4 has already tagged it. A pit one (tip, mip, loṭ ni…) takes guṇa first: cinoti, cinavAni, acinavam."""
    from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import sthanin_was_pit
    j = k + 1
    while j + 1 < len(ts) and "agama" in ts[j].tags:
        j += 1
    t = ts[j]
    if "kngiti" in t.tags or t.meta.get("is_apit") or "kngiti" in ts[k + 1].tags:
        return True
    up = (t.meta.get("upadesha_slp1") or "").strip()
    loT_uttama = (t.meta.get("source_lakara_upadesha") or "").strip() == "loT" and up in {"mip", "vas", "mas", "ni", "va", "ma"}
    return not (up.endswith(("p", "P")) or sthanin_was_pit(t) or loT_uttama or t.meta.get("pit"))


def _site(state: State):
    """हुश्नुवोः सार्वधातुके (असंयोगपूर्वस्य, 6.4.82): the उ of श्नु (and of हु) not after a
    conjunct becomes व् before a vowel-initial sārvadhātuka — सुनु+अन्ति → सुन्वन्ति;
    after a conjunct 6.4.77 uvaṅ stays (आप्नुवन्ति)."""
    ts = state.terms
    for k in range(1, len(ts) - 1):
        nu, nxt = ts[k], ts[k + 1]
        if (nu.meta.get("upadesha_slp1") or "").strip() != "Snu" or [v.slp1 for v in nu.varnas] != ["n", "u"]:
            continue
        if not nxt.varnas or nxt.varnas[0].slp1 not in _AC:
            continue
        # only before a weak (kṅit) ending: cinvanti — but cinavAni / acinavam (pit: guṇa, then av) keep the u
        if not _weak_after(ts, k):
            continue
        # सार्वधातुके: a tiṅ is sārvadhātuka by 3.4.113 even when its ādeśa lost the tag
        if not (any(t.startswith("sarvadhatuka") for t in nxt.tags) or "tin_adesha_3_4_78" in nxt.tags):
            continue
        prev = ts[k - 1].varnas
        if prev and prev[-1].slp1 in _AC:           # न् is the only consonant before उ
            return nu
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    nu = _site(state)
    nu.varnas[-1] = mk("v")
    nu.tags.discard("upadesha")          # the v is not an upadeśa-final: 1.3.3 must not take it for a halantyam it
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.87",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "huSnuvoH sArvaDAtuke",
    text_dev              = "हुश्नुवोः सार्वधातुके",
    padaccheda_dev        = "हु-श्नुवोः सार्वधातुके",
    why_dev               = "असंयोगपूर्वस्य श्नुप्रत्ययस्य उकारस्य यण् अजादौ सार्वधातुके (सुन्वन्ति, चिन्वन्ति)।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
