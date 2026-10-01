"""
engine/paribhasha.py — the resolver's rule set, cited.

A conflict between two sūtras is not settled by engineering taste. It is
settled by the paribhāṣās, and the collection that states them is Nāgeśa's
**परिभाषेन्दुशेखर**. This module loads the slice vendored in
``data/inputs/paribhasha_shekhara.json`` — the full 133-paribhāṣā pāṭha from
ashtadhyayi-com/data, plus the resolver-layer table — so that every layer of
:mod:`engine.resolver` can name the paribhāṣā it implements, and so that no
sūtra id is typed into engine code by hand (Art. 14).

The strength ladder the resolver follows is PŚ 38::

    पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः

Five terms, ascending: *pūrva* < *para* < *nitya* < *antaraṅga* < *apavāda*.
Antaraṅga's *wording* is PŚ 50 (असिद्धं बहिरङ्गमन्तरङ्गे); it is still
``not_modelled`` as a decision procedure (Art. 21). SOI is not a layer.

Ārthika granthas (वाक्यपदीय, भूषणसार, परमलघुमञ्जूषा) are catalogued in
``data/inputs/grantha_catalog.json`` and **never** pick a runtime winner.
Laghuśabdenduśekhara is T5 (design-time); excerpts the resolver names live
under ``laghu_excerpts``.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

_DIR = Path(__file__).resolve().parent.parent / "data" / "inputs"
_DATA = _DIR / "paribhasha_shekhara.json"
_CATALOG = _DIR / "grantha_catalog.json"


@dataclass(frozen=True)
class Layer:
    """One resolver layer and the paribhāṣā that authorises it."""

    key: str
    label_dev: str
    ps_num: str
    paribhasha_dev: str
    sutra_id: str | None
    status: str
    note: str

    @property
    def modelled(self) -> bool:
        return self.status == "modelled"

    def citation(self) -> str:
        bits = []
        if self.ps_num:
            bits.append(f"परिभाषेन्दुशेखर {self.ps_num}")
        if self.sutra_id:
            bits.append(f"अष्टाध्यायी {self.sutra_id}")
        source = " · ".join(bits) if bits else "Art. 21"
        text = self.paribhasha_dev or self.note
        return f"{self.label_dev} ({source}): {text}"


@lru_cache(maxsize=1)
def _payload() -> dict[str, Any]:
    return json.loads(_DATA.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def grantha_catalog() -> dict[str, Any]:
    return json.loads(_CATALOG.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def layers() -> dict[str, Layer]:
    payload = _payload()
    texts = {entry["num"]: entry["paribhasha"] for entry in payload["entries"]}
    return {
        key: Layer(
            key=key,
            label_dev=spec["label_dev"],
            ps_num=spec["ps_num"],
            paribhasha_dev=(
                (texts.get(spec["ps_num"], "") if spec.get("ps_num") else "")
                or spec.get("text_dev")
                or ""
            ),
            sutra_id=spec.get("astadhyayi_sutra"),
            status=spec["status"],
            note=spec["note"],
        )
        for key, spec in payload["resolver_layers"].items()
    }


def layer(key: str) -> Layer:
    return layers()[key]


def paribhasha(num: str) -> str:
    """The text of one vendored paribhāṣā, by its Śekhara number."""
    for entry in _payload()["entries"]:
        if entry["num"] == num:
            return entry["paribhasha"]
    raise KeyError(f"paribhāṣā {num} is not in the vendored pāṭha")


def all_paribhashas() -> dict[str, str]:
    return {entry["num"]: entry["paribhasha"] for entry in _payload()["entries"]}


def laghu_excerpt(sutra_id: str) -> str:
    """Design-time LŚ excerpt the resolver is allowed to quote (Art. 22 T5)."""
    return _payload()["laghu_excerpts"][sutra_id]["excerpt"]


def runtime_granthas() -> list[str]:
    """Granthas that may decide a runtime conflict — PŚ only."""
    return [g["id"] for g in grantha_catalog()["paribhasha_granthas"] if g.get("runtime")]


def not_modelled() -> list[Layer]:
    """The layers a conflict may need that the engine does not yet weigh."""
    return [value for value in layers().values() if not value.modelled]
