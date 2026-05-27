"""
ट्रेस दृश्य — पूर्ण बनाम केवल सतह-परिवर्तन (Streamlit UI मात्र)।
"""
from __future__ import annotations

from typing import Any, Dict, List


def filter_steps_surface_changed(trace: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    केवल वे चरण जहाँ ``form_before`` और ``form_after`` (SLP1 ``render()``) भिन्न हैं।

    संज्ञा / अनुवाद जैसे चरण अक्सर रूप नहीं बदलते — वे इस सूची में नहीं आते।
    """
    out: List[Dict[str, Any]] = []
    for step in trace:
        if step.get("form_before") != step.get("form_after"):
            out.append(step)
    return out
