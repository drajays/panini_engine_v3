"""
7.2.81  आतो ङितः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=72081 · आतो ङितः
- Kāśikā: "एधेते। एधेथे। अदन्ताद् अङ्गाद् उत्तराभ्याम् आताम्-आथाम्-आदेशाभ्याम् आकारस्य इय् आदेशो भवति।"
  (कर्तरि एध् + शप् + आते → एधेते — not karmaṇi-only)
- Cross-validation: regression sparD lṛṅ dual ātmane अस्पर्धिष्येताम् (1.2.4 → ङित् आताम् → इय्)

*Padaccheda:* *ātaḥ* / *ṅitaḥ*. Anuvṛtti brings *aṅgasya*, *ataḥ*, *sārvadhātuke*.

*Śāstra:* when the aṅga is a-final, the initial *ā* of a *ṅit* sārvadhātuka (*ātām* / *āthām*,
or *āte* / *āthe* after **3.4.79**) becomes *iy*. *Ṅit* may come from **1.2.4** (apit
sārvadhātuka) in *kartari*, or from a *ṅit* vikaraṇa path in *bhāve*/*karmaṇi* — the sūtra
itself is not restricted to karmaṇi/bhāve.

*Engine:* tiṅ ādeśa with initial ``A``; requires ``kngiti`` (1.2.4) **or** ``bhava_karma_usage``;
skips if the tiṅ is already ārdhadhātuka. No ``_arm`` (Art. 13).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _bhava_karma_dhatu(state: State) -> bool:
    return any("dhatu" in t.tags and "bhava_karma_usage" in t.tags for t in state.terms)


def _find_Ate(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if t.meta.get("7_2_81_done"):
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "A":
            continue
        if "ardhadhatuka" in t.tags:
            continue        # सार्वधातुके (anuvṛtti 7.2.76) — luṅ's ātām stays: 7.3.72 क्सस्याचि (para, 1.4.2) first removes ksa's a
        # अतः (7.2.80): the preceding aṅga ends in a — śap (एध + आते) or yak
        # (भूय + आते). Once gated to yak (bhāva/karma) only, which left
        # kartari ātmanepada duals as एधआते for एधेते.
        prev = next((u for u in reversed(state.terms[:ti]) if u.varnas), None)
        if prev is None or prev.varnas[-1].slp1 != "a":
            continue
        # ङितः — ātām/āthām are ṅit through 1.2.4 (sārvadhātukam apit).
        if "kngiti" not in t.tags and not _bhava_karma_dhatu(state):
            continue
        return ti
    return None


def cond(state: State) -> bool:
    return _find_Ate(state) is not None


def act(state: State) -> State:
    ti = _find_Ate(state)
    if ti is None:
        return state
    t = state.terms[ti]
    t.varnas = [_mk("i"), _mk("y")] + list(t.varnas[1:])
    t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
    t.meta["7_2_81_done"] = True
    state.samjna_registry["7.2.81_Ate_iy"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.81",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ato NitaH",
    text_dev="आतो ङितः",
    samagra_slp1="aNgasya AtaH NitaH sArvaDAtuke iyaH ataH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="अङ्गस्य आतः ङितः सार्वधातुके इयः अतः",
    padaccheda_dev="आतः ङितः",
    why_dev=(
        "अदन्ताङ्गात् परस्य ङित्-सार्वधातुकस्य आकारस्य इय्-आदेशः "
        "(आताम्/आथाम्; आते/आथे) — कर्तरि अपि (१.२.४ कङित्); "
        "एधेते, अस्पर्धिष्येताम्।"
    ),
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
