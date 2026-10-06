"""
1.2.3  विभाषोर्णोः  —  VIBHASHA

Anuvṛtti: iḍādi pratyaya, ṅit-vat (from 1.2.1 गाङ्कुटादिभ्योऽञ्णिन्ङित्).

Meaning: after the dhātu ऊर्णु (upadeśa ऊर्णुञ्, "to cover"; already सेट् in
the dhātupātha — this sūtra does not grant seṭ-ness), an iṭ-ādi ārdhadhātuka
pratyaya is OPTIONALLY ṅit-vat (1.1.5 क्ङिति च blocks guṇa/vṛddhi of the
aṅga on that branch). Kāśikā: "ऊर्णुञ् आच्छादने, अस्मात् परः इडादिः
प्रत्ययो विभाषा ङित्वद् भवति। प्रोर्णुविता। प्रोर्णविता।" — same mechanism
as 1.2.1/1.2.2 (tag the following iṭ-ādi pratyaya ``kngiti``; read by 1.1.5
and by 6.4.77's uvaṅ), but वा: the declined branch keeps ordinary guṇa.

  - ṅit branch  (kngiti tagged): no guṇa → 6.4.77 uvaṅ → ऊर्णु+व्+इता  → ūrṇuvitā
  - declined    (no tag)       : guṇa उ→ओ, othen o+i sandhi → अव्      → ūrṇavitā

Engine: finds the iṭ-ādi pratyaya (its first varna tagged "it_agama" by the
iṭ-augment sūtras, e.g. 7.2.35) immediately after a dhātu Term whose
upadesha_slp1 == "UrRuY" (data/inputs/dhatupatha_upadesha.json id
Adadi_02_0034; post-it-lopa citation_dhatu_slp1 == "UrRu"), not already
kngiti. act() (vibhasha_default=True) tags it "kngiti"; the exec_vibhasha
fork records the declined (guṇa) branch for engine.vikalpa.explore().
r1_form_identity_exempt=True: no surface string changes in this step itself.
Pāṭha: ashtadhyayi.com data.txt row i=12003 (Art. 14).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_URNNU_UPADESHA: frozenset = frozenset({"UrRuY"})


def _find_target(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _URNNU_UPADESHA:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if (nxt is not None and "pratyaya" in nxt.tags and "kngiti" not in nxt.tags
                and "it_agama" in nxt.varnas[0].tags):
            return nxt
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    nxt = _find_target(state)
    if nxt is None:
        return state
    nxt.tags.add("kngiti")
    state.samjna_registry["1_2_3_UrRu_kngiti_vibhASA"] = True
    return state


def apply_at_it_insertion(state: State, it_term) -> None:
    """Hook called by 7.2.35 (आर्धधातुकस्येड् वलादेः) right after it inserts the
    iṭ varna onto ``it_term``: the scheduler does not revisit Adhyāya 1.2 once
    Adhyāya 7 has run in this derivation (same structural reason 7.2.35 already
    carries ``_vij_kit`` for 1.2.2), so 1.2.3 decides and records itself here —
    mutates via the sūtra's own ``act()``, in-scope cond/predicate owned by this
    file, not by 7.2.35. Idempotent: a no-op if ``it_term`` is not the match, or
    if some other pass already tagged it.
    """
    from engine.vikalpa import policy_choice
    from engine.trace   import make_applied_step, make_blocked_step, GATE_VIBHASHA

    if _find_target(state) is not it_term:
        return
    choice = policy_choice("1.2.3", True)
    form = state.flat_slp1()
    if choice:
        act(state)
        step = make_applied_step("1.2.3", "VIBHASHA", "विभाषा", form, state.flat_slp1(), SUTRA.why_dev)
    else:
        step = make_blocked_step("1.2.3", "VIBHASHA", "विभाषा", form, SUTRA.why_dev, GATE_VIBHASHA)
    state.trace.append(step)


SUTRA = SutraRecord(
    sutra_id              = "1.2.3",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    vibhasha_default      = True,
    text_slp1             = 'viBAzorRoH',
    text_dev              = 'विभाषोर्णोः',
    samagra_slp1          = "viBAzA UrRoH Nit iw",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "विभाषा ऊर्णोः ङित् इट्",
    padaccheda_dev        = "विभाषा / ऊर्णोः",
    why_dev               = "ऊर्णु-धातोः परः इडादिः प्रत्ययः विकल्पेन ङित्वत् (गुणवृद्धि-निषेधः) — प्रोर्णुविता/प्रोर्णविता।",
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
