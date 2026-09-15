"""
engine/paribhasha.py — the resolver's rule set, cited.

A conflict between two sūtras is not settled by engineering taste. It is
settled by the paribhāṣās, and the collection that states them is Nāgeśa's
**परिभाषेन्दुशेखर**. This module loads the slice vendored in
``data/inputs/paribhasha_shekhara.json`` (provenance in the file) so that
every layer of :mod:`engine.resolver` can name the paribhāṣā it implements —
and so that no sūtra id is typed into engine code by hand (Art. 14).

The strength ladder the resolver follows is PŚ 38::

    पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः

Five terms, ascending: *pūrva* < *para* < *nitya* < *antaraṅga* < *apavāda*.
Two of them execute today (*apavāda*, *para*); *nitya* and *antaraṅga* are
declared ``not_modelled`` in the data, which is what lets a report say so
instead of the engine pretending otherwise.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

_DATA = Path(__file__).resolve().parent.parent / "data" / "inputs" / "paribhasha_shekhara.json"


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
        source = f"परिभाषेन्दुशेखर {self.ps_num}"
        if self.sutra_id:
            source += f" · अष्टाध्यायी {self.sutra_id}"
        return f"{self.label_dev} ({source}): {self.paribhasha_dev}"


@lru_cache(maxsize=1)
def _payload() -> dict[str, Any]:
    return json.loads(_DATA.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def layers() -> dict[str, Layer]:
    payload = _payload()
    texts = {entry["num"]: entry["paribhasha"] for entry in payload["entries"]}
    return {
        key: Layer(
            key=key,
            label_dev=spec["label_dev"],
            ps_num=spec["ps_num"],
            paribhasha_dev=texts.get(spec["ps_num"], ""),
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
    raise KeyError(f"paribhāṣā {num} is not in the vendored slice")


def not_modelled() -> list[Layer]:
    """The layers a conflict may need that the engine does not yet weigh."""
    return [value for value in layers().values() if not value.modelled]
