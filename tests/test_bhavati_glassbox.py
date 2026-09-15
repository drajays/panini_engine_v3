"""
tests/test_bhavati_glassbox.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Glass-box prakriyā tests for भवति (bhū + laṭ + kartari + 3sg).

Tests verify:
  1. Final surface form is correct (Bavati / भवति).
  2. Each critical sūtra fired in correct order.
  3. Each form-changing step produced the expected phonemic state.
  4. No forbidden reads (CONSTITUTION Art. 2) — structural check.
"""
import pytest

import sutras  # noqa: F401

from pipelines.tinanta import derive, derive_bhavati


# ─────────────────────────────────────────────────────────────────────────────
# FIXTURES
# ─────────────────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def bhavati_state():
    return derive_bhavati()


# ─────────────────────────────────────────────────────────────────────────────
# SURFACE FORM
# ─────────────────────────────────────────────────────────────────────────────

def test_surface_slp1(bhavati_state):
    assert bhavati_state.flat_slp1() == "Bavati"


def test_surface_dev(bhavati_state):
    assert bhavati_state.flat_dev() == "भवति"


# ─────────────────────────────────────────────────────────────────────────────
# SUTRA FIRING ORDER
# ─────────────────────────────────────────────────────────────────────────────

def _fired_sutra_ids(state) -> list[str]:
    return [t["sutra_id"] for t in state.trace]


def test_sutra_1_3_1_fires(bhavati_state):
    """1.3.1 bhūvādayo dhātavaḥ must fire early to establish dhātu-saṃjñā.

    P01_samjna_dhatu_class (1.1.20, 1.1.5) now fires before 1.3.1 in the
    tinanta pipeline (audit P2 §4.3).  1.3.1 must still precede 1.3.78.
    """
    ids = _fired_sutra_ids(bhavati_state)
    assert "1.3.1" in ids
    assert ids.index("1.3.1") < ids.index("1.3.78")


def test_sutra_1_3_78_fires_before_tin(bhavati_state):
    """1.3.78 parasmaipada gate must be set before tiṅ selection (3.4.78)."""
    ids = _fired_sutra_ids(bhavati_state)
    assert "1.3.78" in ids and "3.4.78" in ids
    assert ids.index("1.3.78") < ids.index("3.4.78")


def test_sutra_3_4_78_fires(bhavati_state):
    """3.4.78 must substitute laṭ → tip."""
    fa = _applied_form_after(bhavati_state, "3.4.78")
    assert fa is not None, "3.4.78 should change the form"
    assert "tip" in fa


def test_sutra_3_1_68_fires_after_tin(bhavati_state):
    """3.1.68 kartari śap must fire after tiṅ selection."""
    ids = _fired_sutra_ids(bhavati_state)
    assert "3.1.68" in ids and "3.4.78" in ids
    assert ids.index("3.1.68") > ids.index("3.4.78")


def test_sutra_3_4_113_fires_after_sap(bhavati_state):
    """3.4.113 must mark śap as sārvadhatuka before guṇa."""
    ids = _fired_sutra_ids(bhavati_state)
    assert "3.4.113" in ids and "7.3.84" in ids
    assert ids.index("3.4.113") < ids.index("7.3.84")


def test_sutra_7_3_84_fires(bhavati_state):
    """7.3.84 must apply guṇa: u → o in bhū → bho."""
    fa = _applied_form_after(bhavati_state, "7.3.84")
    assert fa is not None, "7.3.84 must change the form"
    assert "Bo" in fa


def test_sutra_6_1_78_fires(bhavati_state):
    """6.1.78 eco'yavāyāvaḥ must split o+a → av: bho+a → bhav."""
    fa = _applied_form_after(bhavati_state, "6.1.78")
    assert fa is not None, "6.1.78 must change the form"
    assert "Bav" in fa


# ─────────────────────────────────────────────────────────────────────────────
# FORM SEQUENCE (phonemic transitions)
# ─────────────────────────────────────────────────────────────────────────────

def _applied_form_after(state, sutra_id: str) -> str | None:
    """Return form_after for the first trace entry of sutra_id that changed the form."""
    for t in state.trace:
        if t["sutra_id"] != sutra_id:
            continue
        fb = t.get("form_before", "")
        fa = t.get("form_after", "")
        if fb != fa:
            return fa
    return None


def test_tip_substitution(bhavati_state):
    """After 3.4.78: form contains 'tip'."""
    fa = _applied_form_after(bhavati_state, "3.4.78")
    assert fa is not None and "tip" in fa


def test_sap_insertion(bhavati_state):
    """After 3.1.68: form contains 'Sap' (śap vikaraṇa inserted)."""
    fa = _applied_form_after(bhavati_state, "3.1.68")
    assert fa is not None and "Sap" in fa


def test_guna_bho(bhavati_state):
    """After 7.3.84: dhātu's 'U' → 'o' (guṇa)."""
    fa = _applied_form_after(bhavati_state, "7.3.84")
    assert fa is not None and "Bo" in fa


def test_ec_split(bhavati_state):
    """After 6.1.78: 'o' splits to 'av', yielding 'Bav'."""
    fa = _applied_form_after(bhavati_state, "6.1.78")
    assert fa is not None and "Bavati" in fa


# ─────────────────────────────────────────────────────────────────────────────
# PARIBHĀṢĀ GATE — 1.3.78 parasmaipada
# ─────────────────────────────────────────────────────────────────────────────

def test_parasmaipada_gate_set(bhavati_state):
    """1.3.78 must set the parasmaipada gate active."""
    gate = bhavati_state.paribhasha_gates.get(
        "prayoga_1_3_78_seza_kartari_parasmaipada", {}
    )
    assert isinstance(gate, dict)
    assert gate.get("active") is True


# ─────────────────────────────────────────────────────────────────────────────
# DERIVE() GENERIC API — other cells
# ─────────────────────────────────────────────────────────────────────────────

def test_derive_accepts_BU_upadesha():
    """derive() must accept raw upadeśa 'BU' (not just dhātupātha id)."""
    s = derive("BU", "laT", "kartari", 3, 1)
    assert s.flat_dev() == "भवति"


def test_derive_accepts_dhatupatha_id():
    """derive() must accept dhātupātha canonical id 'BvAdi_01_0001'."""
    s = derive("BvAdi_01_0001", "laT", "kartari", 3, 1)
    assert s.flat_dev() == "भवति"


def test_derive_accepts_alias():
    """derive() must accept alias 'BvAdi_BU'."""
    s = derive("BvAdi_BU", "laT", "kartari", 3, 1)
    assert s.flat_dev() == "भवति"


# ─────────────────────────────────────────────────────────────────────────────
# TRACE SANITY
# ─────────────────────────────────────────────────────────────────────────────

def test_trace_non_empty(bhavati_state):
    assert len(bhavati_state.trace) >= 20


def test_trace_contains_merge(bhavati_state):
    """Trace must contain a __MERGE__ step (pipeline ends with tripāḍī now)."""
    ids = [s["sutra_id"] for s in bhavati_state.trace]
    assert "__MERGE__" in ids
    # After merge, the tripāḍī section closes the pipeline.
    assert bhavati_state.trace[-1]["sutra_id"] in ("8.2.1", "8.2.66", "8.3.15")


def test_no_vibhakti_in_sutra_ids(bhavati_state):
    """No sūtra may have a 'vibhakti' string in its trace entry — Constitution Art.2."""
    for step in bhavati_state.trace:
        assert "vibhakti" not in str(step.get("why_dev", "")).lower() or \
               step["sutra_id"] in ("1.4.13",), \
               f"Suspicious vibhakti reference in {step['sutra_id']}"
