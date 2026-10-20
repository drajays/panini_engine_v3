"""
tools/practice_sentences.py — sentence practice from Saṃsādhanī's "1000 Sentences", checked without AI.
──────────────────────────────────────────────────────────────────────────────────────────────────────────

Each sentence comes with Saṃsādhanī's word analysis (morph tag, kāraka relation, Hindi gloss) and the
engine's verdict on every word (samsaadhanii_reader.verify — the form is re-derived from its tag). A client
(Subhastini's अभ्यास) builds its drills from this record and checks answers by exact match:

* a blank is offered only for a word the engine *derives*, so its expected form is engine-confirmed;
* the grammar hint is the tag itself, written out (क्रीड् · लोट् · मध्यमपुरुष · एकवचन);
* a kāraka question carries the sūtras that name the relation (1.4.x / 2.3.x).

The glosses are Saṃsādhanī's word-by-word Hindi, not a translation. Tools layer (CONSTITUTION Art. 6).
"""
from __future__ import annotations

import re

from tools import samsaadhanii_reader as rd
from tools.library_providers import READER

UNIT = "1000_Sentences"
_VIB = {"1": "प्रथमा", "2": "द्वितीया", "3": "तृतीया", "4": "चतुर्थी", "5": "पञ्चमी", "6": "षष्ठी", "7": "सप्तमी",
        "8": "सम्बोधनम्"}
_FIELD = {"प्र": "प्रथमपुरुषः", "म": "मध्यमपुरुषः", "उ": "उत्तमपुरुषः", "एक": "एकवचनम्", "द्वि": "द्विवचनम्",
          "बहु": "बहुवचनम्", "पुं": "पुंलिङ्गम्", "स्त्री": "स्त्रीलिङ्गम्", "नपुं": "नपुंसकलिङ्गम्", "अव्य": "अव्ययम्",
          "परस्मैपदी": "परस्मैपदम्", "आत्मनेपदी": "आत्मनेपदम्", **_VIB}
# The relations a learner is asked to recognise (kārakas 1.4.23 ff., śeṣa 2.3.50, sambodhana, and a few
# Saṃsādhanī labels that recur in simple sentences). Other labels are shown in the analysis, not quizzed.
ROLES = ["कर्ता", "कर्म", "करणम्", "सम्प्रदानम्", "अपादानम्", "अधिकरणम्", "कालाधिकरणम्", "देशाधिकरणम्",
         "षष्ठीसम्बन्धः", "सम्बोध्यः", "हेतुः", "विशेषणम्", "प्रतिषेधः"]


def hint(tag: str) -> str:
    """``क्रीड्1{कर्तरि;लोट्;म;एक;परस्मैपदी;भ्वादिः}`` → ``क्रीड् · कर्तरि · लोट् · मध्यमपुरुषः · एकवचनम् · परस्मैपदम् · भ्वादिः``."""
    m = re.match(r"^\(?([^{}()]+)((?:\{[^{}]*\})+)\)?$", (tag or "").strip())
    if not m:
        return (tag or "").strip()
    head = re.sub(r"\d+", "", m[1]).replace("_", "-")
    fields = [f.strip() for g in re.findall(r"\{([^{}]*)\}", m[2]) for f in g.split(";") if f.strip()]
    return " · ".join([head] + [_FIELD.get(f, f) for f in fields if f != "सर्वनाम"])


def sets() -> list[dict]:
    if not rd.available():
        return []
    return [{"id": ch, "count": len(rd.verses(UNIT, ch))} for ch in rd.chapters(UNIT)]


def sentences(set_id: str) -> list[dict]:
    if set_id not in rd.chapters(UNIT):
        raise KeyError(set_id)
    return [{"id": v["sloka"], "text": " ".join(v["text"])} for v in rd.verses(UNIT, set_id)]


def sentence(set_id: str, sid: str) -> dict:
    v = rd.verse(UNIT, set_id, sid)
    words = []
    for s in v["sentences"]:
        by = {w["anvaya_no"]: w for w in s["words"]}
        for w in s["anvaya"]:
            rel, e = w.get("relation"), w["engine"]
            head = by.get((rel or {}).get("target"))
            words.append({
                "n": w["anvaya_no"], "form": w["word_dev"], "surface": w.get("sandhied_word") or "",
                "implied": (w.get("word") or "").startswith("("), "kind": w["kind"], "tag": w["morph"],
                "hint": hint(w["morph"]), "gloss": (w.get("hindi") or "").replace("_", " "),
                "role": rel and rel["label"].replace("_", ""), "head": head and head["word_dev"],
                "role_sutras": [{"id": x["id"], "text": x["text_dev"]} for x in (rel or {}).get("sutras", [])],
                "vibhakti_check": w.get("vibhakti_check"),
                "engine": {"status": e["status"], "produced": e.get("produced_dev"), "note": e.get("note"),
                           "request": e.get("request")},
            })
    return {"set": set_id, "id": sid, "text": " ".join(v["text"]), "words": words, "counts": v["counts"],
            "source": "Saṃsādhanī e-reader “1000 Sentences” (University of Hyderabad, GPL-2.0)",
            "analysis_url": f"{READER}#{UNIT}/{set_id}/{sid}"}
