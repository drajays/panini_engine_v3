"""
3.1.68  कर्तरि शप्  —  VIDHI

*Padaccheda:* *kartari* (saptamī), *śap* (prathamā); *sārvadhātake* **3.1.67** *anuvṛtti*.

*Anuvṛtti:* *pratyayaḥ* **3.1.1**; *paraś ca* **3.1.2**; *ādyudāttaś ca* **3.1.3**; *dhātoḥ* **3.1.91** *adhikāra*.

*Śāstra:* *śap* *vikaraṇa* between *dhātu* and a following *sārvadhātuka* affix in *kartari* (*it* **1.3.3**/**1.3.8**;
*lopa* **1.3.9**; *guṇa* **6.1.97** — separate rules).

*Engine:* inserts a ``Sap`` *pratyaya* ``Term`` immediately after the *dhātu* when ``vikarana_sap_3_1_68`` says so;
requires **3.1.91** on ``adhikara_stack`` (*dhātoḥ*) and *kartari* licence (**3.4.69** or recipe meta).
Does **not** implement *divādi*
*apavāda* (*śyan* etc.).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 31068 · कर्तरि शप्
              padaccheda: कर्तरि शप्
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31022: धातोः | 31067: सार्वधातुके
  Source #2 — Kāśikā 3.1.68 udāharaṇa:
                पकारः स्वरार्थः, शकारः सार्वधातुकसंज्ञार्थः
                भवति
                पचति
  Cross-check — surface pinned by: tests/test_bhavati_glassbox.py, tests/unit/test_aBavatAm_split_prakriyas.py, tests/unit/test_autonomous_vs_recipe.py
  Reference record: sutra_ref_out/3_1_68.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


# --- helpers of this sūtra (formerly vikarana_sap_3_1_68.py; one sūtra, one file) ---
from typing import Final

from engine.state import State

from sutras.adhyaya_3.pada_4.sutra_3_4_69 import GATE_PFX
from sutras.adhyaya_3.pada_4.sutra_3_4_113 import (
    SIT_KRT_SARVADHATUKA_SLP1,
    SIT_VIK_SARVADHATUKA_SLP1,
    is_sarvadhatuka_upadesha_slp1,
)
from sutras.adhyaya_1.pada_4.sutra_1_4_104 import TIN_SURFACE_AADESHA_SLP1_EXTRA
from sutras.adhyaya_3.pada_4.sutra_3_4_78 import TIN_ADESHA_SET

# Recipe-only: when **3.4.69** has not run, allow *kartari* for unit tests / narrow demos.
KARTARI_RECIPE_META_KEY: Final[str] = "3_1_68_kartari_recipe"

SAP_INSERT_TAG: Final[str] = "3_1_68_sap"


def _norm_upadesha(up: str) -> str:
    t = up.strip()
    if t.endswith("~"):
        return t[:-1]
    return t


def _sap_trigger_next_pratyaya(up: str) -> bool:
    """
    *Śap* is inserted only before *tiṅ* *ādeśa* or *kṛt* *śit* (e.g. *śatṛ*), not before another
    *vikaraṇa* (*śyan* …) which is an *apavāda* to **3.1.68**.
    """
    k = _norm_upadesha(up)
    if k == "Sap":
        return False
    if k in SIT_VIK_SARVADHATUKA_SLP1:
        return False
    from sutras.adhyaya_3.pada_4.sutra_3_4_113 import TIN_3_4_79_ADESHA
    return (
        k in TIN_ADESHA_SET
        or k in TIN_SURFACE_AADESHA_SLP1_EXTRA
        or k in TIN_3_4_79_ADESHA        # te/Ate/se/… stay tiṅ by 1.1.56 (एधताम्)
        or k in SIT_KRT_SARVADHATUKA_SLP1
    )


def _kartari_ok(state: State) -> bool:
    gate_key = f"{GATE_PFX}_licenses_kartari"
    # If 3.4.69 ran and explicitly licensed kartari, honour it.
    if state.paribhasha_gates.get(gate_key) is True:
        return True
    # If 3.4.69 ran and explicitly denied kartari (karmani/bhāve), respect that.
    if gate_key in state.paribhasha_gates:
        return False
    # 3.4.69 has not run: kartari is the unmarked (default) prayoga.
    return True


def _dhato_adhikara_3_1_91_open(state: State) -> bool:
    """**3.1.91** on stack ⇒ *kṛt* / *tiṅ* attach to *dhātu*; **3.1.68** is before **3.1.91** in the book."""
    return any(e.get("id") == "3.1.91" for e in state.adhikara_stack)


def find_sap_insertion_dhatu_index(state: State) -> int | None:
    if not _dhato_adhikara_3_1_91_open(state):
        return None
    if not _kartari_ok(state):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("3_1_78_snam_done"):      # śnam (rudhādi) is an infix of the dhātu, not a Term: it displaced śap (apavāda)
            continue
        if t.meta.get("3_1_68_sap_given"):      # śap was introduced (and a luk, 2.4.72/75, may have removed it): once
            continue
        if i + 1 >= len(state.terms):
            continue
        j = i + 1
        # Skip *liṅ* *sīyuṭ* residue (**3.4.102**) so *śap* targets the first *tiṅ*
        # *ādeśa* (e.g. **P038** *vidhi-liṅ* → ``ran``).
        # (and the āṭ of 3.4.92 आडुत्तमस्य: an āgama is part of the affix it stands before, 1.1.46 —
        # वनं… भवा+नि: śap goes between the dhātu and the whole 'ā+ni')
        while j < len(state.terms) and ({"ling_sIyuw", "aTa_agama", "yasut_agama"} & state.terms[j].tags):
            j += 1
        if j >= len(state.terms):
            continue
        nxt = state.terms[j]
        if nxt.kind != "pratyaya":
            continue
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up == "Sap":
            continue
        if SAP_INSERT_TAG in nxt.tags:
            continue
        if nxt.meta.get("3_1_83_done"):         # śānac stands in śnā's place (3.1.83 hau): the vikaraṇa slot is taken
            continue
        if nxt.meta.get("vikarana_chosen"):     # cli/sic already took the slot (and may have been luk'd, 2.4.77)
            continue
        # A tiṅ stays a tiṅ — and sārvadhātuka — after an ādeśa replaces it (1.1.56 sthānivat; tas → tām
        # is still the tiṅ 3.4.113 named), so the tags decide first; the upadeśa inventory is the
        # fallback for affixes that never went through 3.4.78/3.4.113.
        if "ardhadhatuka" in nxt.tags:          # सार्वधातुके: āśīr-liṅ's tiṅ is ārdhadhātuka (3.4.116)
            continue
        tin_sarva = "tin_adesha_3_4_78" in nxt.tags and (
            "sarvadhatuka_3_4_113" in nxt.tags       # 3.4.113 may not have run yet: the sthānī lakāra says the same (3.4.113 / 3.4.114–116)
            or ((nxt.meta.get("source_lakara_upadesha") or "").strip() in ("laT", "loT", "laG", "liG")
                and "ashir_liG" not in nxt.tags))
        if not (tin_sarva or is_sarvadhatuka_upadesha_slp1(up)):
            continue
        if not (tin_sarva or _sap_trigger_next_pratyaya(up)):
            continue
        return i
    return None


def sarvadhatuka_lakara_context(state: State) -> bool:
    """A vikaraṇa (śap, śnu, śa, śnam, u, śnā…) stands only before a *sārvadhātuka* ending: the tiṅ of laṭ, loṭ, laṅ,
    vidhi-liṅ. Not before liṭ, luṭ, lṛṭ, luṅ, lṛṅ or āśīr-liṅ, whose affixes are ārdhadhātuka (3.4.114–116). With no
    tiṅ on the tape yet (a recipe's lakāra placeholder), the question is open and the answer is yes. A kṛdanta has no
    tiṅ: its kṛt decides — only a śit kṛt (śatṛ, śānac) is sārvadhātuka (3.4.113), ktvā, tṛc, kta … are not. With no
    affix at all after the dhātu there is nothing for the vikaraṇa to stand before."""
    for t in state.terms:
        if "tin_adesha_3_4_78" in t.tags:
            src = (t.meta.get("source_lakara_upadesha") or "").strip()
            if "ashir_liG" in t.tags or "ardhadhatuka" in t.tags:
                return False
            return src in ("", "laT", "loT", "laG", "liG")
    affixes = [t for t in state.terms if t.kind == "pratyaya" or "pratyaya" in t.tags]
    if not affixes:
        return False
    krt = [t for t in affixes if "krt" in t.tags]
    if krt:
        return any("sarvadhatuka_3_4_113" in t.tags
                   or is_sarvadhatuka_upadesha_slp1(t.meta.get("upadesha_slp1_original") or t.meta.get("upadesha_slp1") or "")
                   for t in krt)
    return True




def cond(state: State) -> bool:
    return find_sap_insertion_dhatu_index(state) is not None


def act(state: State) -> State:
    i = find_sap_insertion_dhatu_index(state)
    assert i is not None
    sap = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sap"),
        tags={"pratyaya", "vikarana", "upadesha", SAP_INSERT_TAG},
        meta={"upadesha_slp1": "Sap"},
    )
    state.terms.insert(i + 1, sap)
    state.terms[i].meta["3_1_68_sap_given"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.68",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = (
        'kartari Sap'
    ),
    text_dev       = 'कर्तरि शप्',
    samagra_slp1   = "sArvaDAtuke kartari DAtoH Sap",
    samagra_dev    = "सार्वधातुके कर्तरि धातोः शप्",
    padaccheda_dev = "सार्वधातुके (३.१.६७) / कर्तरि / धातोः / शप्",
    why_dev        = (
        "कर्तरि सार्वधातुके परे विकरण-शप्-आगमः; अपवादाः ३.१.६९ इत्यादौ पृथक्।"
    ),
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.67", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

