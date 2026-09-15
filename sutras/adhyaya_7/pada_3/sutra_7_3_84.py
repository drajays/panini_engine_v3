"""
7.3.84  सार्वधातुकार्धधातुकयोः  —  VIDHI

When the **first** affix **immediately after** the *dhātu* *Term* is *sārvadhātuka*
or *ārdhadhātuka* (``is_sarvadhatuka_upadesha_slp1``, ``sarvadhatuka_3_4_113`` tag,
or ``ardhadhatuka`` / ``sarvadhatuka`` tags — as with *kṛt* **tfc**), replace the
**final ``ik`` vowel** of that *dhātu* with its **guṇa** substitute.

Covers **kṛdanta** ``[dhātu, kṛt]`` and **tin**anta ``[dhātu, śap, tiṅ]`` (trigger
on *Sap* / *tip* *upadeśa*), not only ``terms[-1]`` *kṛt*.

Narrow **P040** (*juhoti*): when ``state.meta['juhoti_guna_recipe']``, *guṇa* targets the
**non-*abhyāsa*** *hu* *dhātu* before ``ti`` (not ``_first_dhatu_index``, which would
hit the *abhyāsa* copy).

ṛ/ṝ → ``a`` with **1.1.51** (उरण् रपरः) completing ``ar`` / ``ar``…

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 73084 · सार्वधातुकार्धधातुकयोः
              padaccheda: सार्वधातुक-आर्धधातुकयोः
              anuvṛtti:   64001: अङ्गस्य | 73082: गुणः | 11003: इकः
  Source #2 — Kāśikā 7.3.84 udāharaṇa:
                तरति
                नयति
                भवति
  Cross-check — surface pinned by: tests/constitutional/test_no_new_duplicates.py, tests/test_bhavati_glassbox.py, tests/unit/test_Bavitavyam_split_prakriyas.py
  Reference record: sutra_ref_out/7_3_84.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import IK, HAL

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import is_sarvadhatuka_upadesha_slp1
from sutras.adhyaya_1.pada_1.sutra_1_1_4 import ik_guna_vriddhi_blocked_by_1_1_4
from sutras.adhyaya_1.pada_1.sutra_1_1_5 import ik_guna_vriddhi_blocked_by_1_1_5
from sutras.adhyaya_1.pada_1.sutra_1_1_6 import dhatu_blocked_by_1_1_6


_IK_GUNA = {
    "i": "e", "I": "e",
    "u": "o", "U": "o",
    "f": "a", "F": "a",
    "x": "a", "X": "a",
}


def _ik_letter(ch: str) -> bool:
    return ch in IK or ch in ("I", "U", "F", "X")


def _first_dhatu_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _last_ik_index(d0) -> int | None:
    """Return the index of the last IK vowel in d0.varnas.

    For vowel-final dhātus (e.g. BU = [B,U]) this is len-1 — same as before.
    For consonant-final dhātus with an IK penultimate vowel (e.g. cit = [c,i,t])
    this returns the index of that vowel so guṇa targets it correctly.
    """
    for j in range(len(d0.varnas) - 1, -1, -1):
        if _ik_letter(d0.varnas[j].slp1):
            return j
    return None


def _p040_non_abhyasa_hu_dhatu_index(state: State) -> int | None:
    """**P040** *juhoti*: *guṇa* on the second *hu* (non-*abhyāsa*), not the first."""
    if not state.meta.get("juhoti_guna_recipe"):
        return None
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "hu":
            continue
        return i
    return None


def _sarvadhatuka_or_ardhadhatuka_following_dhatu(state: State, di: int) -> bool:
    """True iff ``terms[di+1]`` is the *pare* *sārvadhātuka* / *ārdhadhātuka* trigger."""
    if di + 1 >= len(state.terms):
        return False
    nxt = state.terms[di + 1]
    up = (nxt.meta.get("upadesha_slp1") or "").strip()
    if is_sarvadhatuka_upadesha_slp1(up):
        return True
    if "ardhadhatuka" in nxt.tags or "sarvadhatuka" in nxt.tags:
        return True
    if "sarvadhatuka_3_4_113" in nxt.tags:
        return True
    return False


def _tanadi_vikarana_ik_eligible(state: State, di: int) -> bool:
    """True when next term is the tanādi u-vikaraṇa (upadesha='u') and no kṅit follows.

    Narrower than _vikarana_ik_eligible: requires upadesha_slp1 == 'u' so iṭ, sya,
    or other vikaraṇas are excluded.

    Returns False for vidhiliṅ (liG_yasut_expected): yāsuṭ (3.4.103) is ṅit
    and will be inserted after vikaraṇa, blocking guṇa. We pre-block here to
    avoid guṇa before yāsuṭ arrives. Flag is set around _apply_vikarana call
    in _derive_liG and cleared after 3.4.103 inserts yāsuṭ.
    """
    if state.meta.get("liG_yasut_expected"):
        return False
    if di + 1 >= len(state.terms):
        return False
    vik = state.terms[di + 1]
    if "vikarana" not in vik.tags:
        return False
    if (vik.meta.get("upadesha_slp1") or "").strip() != "u":
        return False
    if vik.meta.get("anga_guna_7_3_84"):
        return False
    if not vik.varnas or vik.varnas[0].slp1 != "u":
        return False
    if not _sarvadhatuka_or_ardhadhatuka_following_dhatu(state, di + 1):
        return False
    for j in range(di + 2, len(state.terms)):
        if "kngiti" in state.terms[j].tags:
            return False
    return True


def _vikarana_ik_eligible(state: State, di: int) -> bool:
    """True when the vikaraṇa term at di+1 has an IK vowel before sārvadhatuka,
    AND no kṅit term follows beyond the vikaraṇa.

    Second 7.3.84 firing (karoti trace):
      कर् + उ + ति [७.३.८४] → कर् + ओ + ति   (tiP is pit → NOT kṅit → fire)
    Blocked for weak forms (kurutaḥ trace):
      कर् + उ + तस् [१.१.५]                    (taS is kṅit → 1.1.5 blocks)
    """
    if di + 1 >= len(state.terms):
        return False
    vik = state.terms[di + 1]
    if "vikarana" not in vik.tags:
        return False
    if vik.meta.get("anga_guna_7_3_84"):
        return False
    if not vik.varnas:
        return False
    if not _sarvadhatuka_or_ardhadhatuka_following_dhatu(state, di + 1):
        return False
    # Block when any term AFTER the vikaraṇa is kṅit tagged (1.2.4 marks apit tiṅ).
    # For tiP (pit, strong): 1.2.4 does NOT add kngiti → second 7.3.84 fires → u→o (karoti)
    # For taS (apit, weak): 1.2.4 adds kngiti → blocked → 6.4.110 fires → a→u (kurutaḥ)
    for j in range(di + 2, len(state.terms)):
        if "kngiti" in state.terms[j].tags:
            return False
    return _last_ik_index(vik) is not None


def _p040_eligible(state: State) -> bool:
    di = _p040_non_abhyasa_hu_dhatu_index(state)
    if di is None:
        return False
    d0 = state.terms[di]
    if dhatu_blocked_by_1_1_6(d0.meta.get("upadesha_slp1")):
        return False
    if not _sarvadhatuka_or_ardhadhatuka_following_dhatu(state, di):
        return False
    if d0.meta.get("anga_guna_7_3_84"):
        return False
    if not d0.varnas:
        return False
    return _last_ik_index(d0) is not None


def _liT_strong_eligible(state: State) -> bool:
    """liṭ strong arm: guṇa of IK-upadha root (e.g. cit→cet) when 7.2.116 left it unchanged."""
    if not state.meta.get("liT_strong_recipe"):
        return False
    # Find the NON-abhyāsa dhātu term
    d0 = None
    for t in state.terms:
        if "dhatu" in t.tags and "abhyasa" not in t.tags:
            d0 = t
            break
    if d0 is None:
        return False
    if d0.meta.get("anga_guna_7_3_84") or d0.meta.get("upadha_vrddhi_done"):
        return False  # 7.2.116 already applied vṛddhi (a-upadha case)
    if not d0.varnas:
        return False
    last = d0.varnas[-1].slp1
    # Consonant-final: guṇa targets internal IK vowel (e.g. cit → c-i-t → cet).
    # ṛ/ḷ-final (e.g. kṛ = k-ṛ): guṇa targets the ṛ/ḷ itself (ṛ → ar).
    # Other vowel-final (U, u, I, i, a): vuk (6.4.88) intervenes → block guṇa.
    if last not in HAL and last not in ("f", "F", "x", "X"):
        return False
    return _last_ik_index(d0) is not None


def cond(state: State) -> bool:
    if ik_guna_vriddhi_blocked_by_1_1_4(state):
        return False
    if ik_guna_vriddhi_blocked_by_1_1_5(state):
        return False
    if state.meta.get("juhoti_guna_recipe"):
        return _p040_eligible(state)
    if state.meta.get("liT_strong_recipe"):
        return _liT_strong_eligible(state)
    di = _first_dhatu_index(state)
    if di is None:
        return False
    d0 = state.terms[di]
    if "dhatu" not in d0.tags:
        return False
    if dhatu_blocked_by_1_1_6(d0.meta.get("upadesha_slp1")):
        return False
    if not _sarvadhatuka_or_ardhadhatuka_following_dhatu(state, di):
        return False
    if d0.meta.get("anga_guna_7_3_84"):
        # Dhātu already guṇified — second firing: check vikaraṇa IK (e.g. u→o in karoti)
        return _vikarana_ik_eligible(state, di)
    if not d0.varnas:
        return False
    if _last_ik_index(d0) is not None:
        return True
    # No IK in dhātu (consonant-final tanādi like van, tan): fire on vikaraṇa u.
    # Guard: only the tanādi u-vikaraṇa (upadesha 'u', sarvadhatuka+vikarana tags).
    return _tanadi_vikarana_ik_eligible(state, di)


def _apply_guna_to_dhatu(d0) -> None:
    ik_i = _last_ik_index(d0)
    assert ik_i is not None
    last = d0.varnas[ik_i].slp1
    rep = _IK_GUNA.get(last, last)
    d0.varnas[ik_i] = mk(rep)
    d0.meta["anga_guna_7_3_84"] = True
    if last in ("f", "F"):
        d0.meta["urN_rapara_pending"] = "r"
    elif last in ("x", "X"):
        d0.meta["urN_rapara_pending"] = "l"


def act(state: State) -> State:
    if state.meta.get("liT_strong_recipe") and _liT_strong_eligible(state):
        d0 = next(t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags)
        _apply_guna_to_dhatu(d0)
        return state
    if state.meta.get("juhoti_guna_recipe") and _p040_eligible(state):
        di = _p040_non_abhyasa_hu_dhatu_index(state)
        assert di is not None
        d0 = state.terms[di]
        _apply_guna_to_dhatu(d0)
        state.meta.pop("juhoti_guna_recipe", None)
        return state
    di = _first_dhatu_index(state)
    assert di is not None
    d0 = state.terms[di]
    if d0.meta.get("anga_guna_7_3_84") and _vikarana_ik_eligible(state, di):
        # Second firing: guṇa on the vikaraṇa IK (e.g. u→o before sārvadhatuka tiṅ)
        _apply_guna_to_dhatu(state.terms[di + 1])
        return state
    if _last_ik_index(d0) is None:
        # No IK in dhātu (e.g. van, tan): fire on tanādi u-vikaraṇa directly
        if _tanadi_vikarana_ik_eligible(state, di):
            _apply_guna_to_dhatu(state.terms[di + 1])
        return state
    _apply_guna_to_dhatu(d0)
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.84",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sArvaDAtukArDaDAtukayoH",
    text_dev       = "सार्वधातुकार्धधातुकयोः",
    padaccheda_dev = "सार्वधातुक-आर्धधातुकयोः",
    why_dev        = (
        "अङ्गान्तिकः गुणः — धातोः परतरं सार्वधातुके वा आर्धधातुके वा "
        "(तिङ्-शित्-सूची, तृच्-आदि)।"
    ),
    anuvritti_from = ("7.3.83",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
