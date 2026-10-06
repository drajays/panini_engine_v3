"""
7.2.13  कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि  —  VIDHI

Padaccheda: कृ-सृ-भृ-वृ-स्तु-द्रु-स्रु-श्रुवः लिटि

Special iṭ-agama privilege for the kṛsṛ… dhātus in liṭ context.
The "liṭi" context is structurally detected via the "abhyasa" tag: after
6.1.8 dvitva (liṭ-specific), an abhyāsa-tagged Term is on the tape.
The dhātu is checked by its post-lopa upadesha_slp1 root.
Pāṭha: ashtadhyayi.com data.txt row i=72013 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_13_kfsfBfvfst_13"

_KRSRBHR_ROOTS = frozenset({
    "kf", "sf", "Bf", "vf", "stu", "dru", "sru", "Sru",
    # (घस् was listed here, but the sūtra names only कृ सृ भृ वृ स्तु द्रु स्रु श्रु;
    #  घस् takes iṭ in liṭ — जघसिथ, जक्षिव. Harmless while 7.2.35 ignored this
    #  gate; removed 2026-09-28 when the gate became effective.)
    # normalised forms (after it-lopa):
    "kfN", "sfp", "BfY", "vfṃj",  # fallback raw keys
})


def _dhatu_in_group(state: State) -> bool:
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        raw = (t.meta.get("upadesha_slp1") or "").replace("~", "").strip()
        # strip trailing it-markers (N, Y, R, etc.)
        base = raw.rstrip("NYRzZ")
        if base.startswith(("qu", "wu", "Yi")):   # ādi ñi/ṭu/ḍu (1.3.5): डुकृञ् → kf
            base = base[2:]
        if base in _KRSRBHR_ROOTS or raw.split("~")[0] in _KRSRBHR_ROOTS:
            return True
        # Also check flat form
        flat = "".join(v.slp1 for v in t.varnas)
        if flat in _KRSRBHR_ROOTS:
            return True
    return False


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: liṭ context + dhātu in the kṛ-sṛ-bhṛ… group. (The old legacy
    # arm ``liT_krsrbhr_recipe`` was set by the liṭ spine for *every* root, so
    # this fired vacuously everywhere and blocked nothing.)
    return _lit_sthani(state) and _dhatu_in_group(state)


def _lit_sthani(state: State) -> bool:
    """लिटि — a term whose sthānī upadeśa is liṭ (the lakāra itself, or its
    tiṅ ādeśa through 1.1.56)."""
    return any((t.meta.get("upadesha_slp1") or "").strip() == "liT"
               or (t.meta.get("source_lakara_upadesha") or "").strip() == "liT"
               for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.13",
    sutra_type            = SutraType.PRATISHEDHA,     # a niṣedha of 7.2.35's iṭ: settled before it contends
    r1_form_identity_exempt = True,
    text_slp1             = "kfsfBfvfstudrusruSruvo liwi",
    text_dev              = "कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि",
    samagra_slp1          = "aNgasya kfsfBfvfstudrusruSruvaH liwi na iw",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य कृसृभृवृस्तुद्रुस्रुश्रुवः लिटि न इट्",
    padaccheda_dev        = "कृ-सृ-भृ-वृ-स्तु-द्रु-स्रु-श्रुवः लिटि",
    why_dev               = "(सूत्रम् 7.2.13) कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
    blocks_sutra_ids      = ("7.2.35",),
)

register_sutra(SUTRA)
