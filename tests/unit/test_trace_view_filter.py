from streamlit_app.trace_view import filter_steps_surface_changed


def test_filter_keeps_only_changed():
    trace = [
        {"sutra_id": "1.1.1", "form_before": "a", "form_after": "a"},
        {"sutra_id": "4.1.2", "form_before": "ab", "form_after": "ac"},
    ]
    f = filter_steps_surface_changed(trace)
    assert len(f) == 1
    assert f[0]["sutra_id"] == "4.1.2"


def test_filter_missing_keys_treated_equal():
    trace = [{"sutra_id": "x", "form_before": None, "form_after": None}]
    assert filter_steps_surface_changed(trace) == []
