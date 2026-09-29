"""
6.4.120  अत एकहल्मध्येऽनादेशादेर्लिटि  —  VIDHI

Padaccheda: अतः एक-हल्-मध्ये अन्-आदेश-आदेः लिटि

In liṭ (perfect), for the non-abhyāsa dhātu term where:
  1. The vowel is 'a' (atah)
  2. Exactly one consonant on each side (ekahalmadhye)
  3. The dhātu's initial is original, not an ādeśa (anādehādeḥ)
  4. 7.2.116 (vṛddhi) has NOT already applied (= weak form)

Replace 'a' with 'e'.

  tan → ten  (3du: t + ten + atuḥ → tenatuh → तेनतुः)
  tan → ten  (3pl: t + ten + uḥ → tenuh → तेनुः)

Does NOT fire for:
  - kṛ → kar (anga_guna_7_3_84=True: 'a' is from ṛ→ar substitution)
  - Strong forms (upadha_vrddhi_done=True: 7.2.116 already gives ā)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import HAL


_VOWELS = frozenset("aAiIuUfFxXeEoO")
_ASPIRATE = frozenset("KGCJWQTDPB")          # 8.4.54 re-makes their abhyāsa: an ādeśa
# 6.4.122 तॄफलभजत्रपश्च — e/abhyāsa-lopa despite ādeśādi (फल्, भज्) or saṃyoga (त्रप्)
_6_4_122 = frozenset({"Pal", "Baj", "trap"})
# 6.4.126 न शसददवादिगुणानाम्
_6_4_126 = frozenset({"Sas", "dad"})


def _ending_licenses(t) -> bool:
    """kit liṭ ending (1.2.5), or 6.4.121 थलि च सेटि: thal with iṭ (पेचिथ)."""
    if "kngiti" in t.tags:
        return True
    up = (t.meta.get("upadesha_slp1") or "").strip()
    return up in ("Tal", "Ta") and bool(t.varnas) and "it_agama" in t.varnas[0].tags


def _find(state: State) -> int | None:
    """Index of the liṭ dhātu (after its abhyāsa) where a → e and the abhyāsa drops."""
    for i in range(1, len(state.terms) - 1):
        ab, t, nxt = state.terms[i - 1], state.terms[i], state.terms[i + 1]
        if "abhyasa" not in ab.tags or "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if t.meta.get("6_4_120_done") or t.meta.get("upadha_vrddhi_done") or t.meta.get("anga_guna_7_3_84"):
            continue          # the a must be the root's own (6.4.126 …गुणानाम्)
        if not _ending_licenses(nxt):
            continue
        vs = [v.slp1 for v in t.varnas]
        if "".join(vs) in _6_4_122:
            return i
        if len(vs) != 3 or vs[1] != "a" or vs[0] in _VOWELS or vs[2] in _VOWELS:
            continue          # एकहल्मध्ये: a between single consonants
        if "".join(vs) in _6_4_126 or vs[0] == "v":
            continue
        if vs[0] in _ASPIRATE or not ab.varnas or ab.varnas[0].slp1 != vs[0]:
            continue          # अनादेशादेः: the abhyāsa keeps the root's initial (चकणे: no)
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    idx = _find(state)
    if idx is None:
        return state
    t = state.terms[idx]
    vs = t.varnas
    j = next(j for j, v in enumerate(vs) if v.slp1 == "a")
    vs[j] = mk("e")
    t.meta["6_4_120_done"] = True
    # Remove the abhyāsa term: in the traditional derivation, the anga after
    # 6.4.120 is the dhātu CeC alone (e.g. ten), not ta+ten.  The abhyāsa's
    # initial consonant coalesces with the dhātu's identical initial consonant.
    del state.terms[idx - 1]
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ata ekahalmaDye'nAdeSAderliwi",
    text_dev              = "अत एकहल्मध्येऽनादेशादेर्लिटि",
    padaccheda_dev        = "अतः एक-हल्-मध्ये अन्-आदेश-आदेः लिटि",
    why_dev               = (
        "लिटि अनाभ्यास-धातोः एकहल्मध्यस्थ 'अ' → 'ए' — "
        "तन् → तेन् (तेनतुः, तेनुः); "
        "न कृ/कर् (आदेश-जन्य-अकार) नापि उपधा-वृद्धि-कृतेषु।"
    ),
    anuvritti_from        = ("6.4.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
