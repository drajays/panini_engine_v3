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


def _find(state: State) -> int | None:
    """Return index of non-abhyāsa dhātu where 6.4.120 applies, or None."""
    # liṭ context: check lakara meta or presence of abhyāsa term
    if state.meta.get("lakara") != "liT":
        if not any("abhyasa" in t.tags for t in state.terms):
            return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if t.meta.get("upadha_vrddhi_done"):
            continue  # strong arm: 7.2.116 already fired
        if t.meta.get("anga_guna_7_3_84"):
            continue  # 'a' is from ādeśa (guṇa of ṛ→ar): anādehādeḥ violated
        if t.meta.get("6_4_120_done"):
            continue
        # Scope: tanādi (gana 8) roots — consonant-final CVC roots like tan, van, san
        # Other ganas (pac, etc.) do not use 6.4.120 in their liṭ weak forms.
        if t.meta.get("gana") != 8:
            continue
        vs = t.varnas
        # Find 'a' between single consonants (ekahalmadhye)
        for j in range(1, len(vs) - 1):
            if vs[j].slp1 != "a":
                continue
            before = vs[j - 1].slp1
            after  = vs[j + 1].slp1
            if before not in HAL or after not in HAL:
                continue
            # Check ekahalmadhye: no adjacent consonant clusters
            # Simple check: positions immediately before (j-1) and after (j+1) are single hals
            # For CVC roots like tan: j=1, before=t, after=n ✓
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
    # Find the 'a' between single consonants and change to 'e'
    for j in range(1, len(vs) - 1):
        if vs[j].slp1 != "a":
            continue
        before = vs[j - 1].slp1
        after  = vs[j + 1].slp1
        if before not in HAL or after not in HAL:
            continue
        vs[j] = mk("e")
        break
    t.meta["6_4_120_done"] = True
    # Remove the abhyāsa term: in the traditional derivation, the anga after
    # 6.4.120 is the dhātu CeC alone (e.g. ten), not ta+ten.  The abhyāsa's
    # initial consonant coalesces with the dhātu's identical initial consonant.
    for i, term in enumerate(state.terms):
        if "abhyasa" in term.tags:
            del state.terms[i]
            break
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
