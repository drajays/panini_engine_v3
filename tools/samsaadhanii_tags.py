"""
tools/samsaadhanii_tags.py — parse Saṃsādhanī morph tags into engine inputs.
──────────────────────────────────────────────────────────────────────────────

Saṃsādhanī (IIIT-H / UoH, source #17 in the roster) tags every word of its
e-reader texts with a ``morph_in_context`` string. Tiṅanta tags look like

    कृ3{कर्तरि;लङ्;प्र;बहु;आत्मनेपदी;डुकृञ्;तनादिः}
    अभि_हन्1{कर्मणि;लङ्;प्र;बहु;आत्मनेपदी;अभि_हनँ;अदादिः}
    मृ{णिच्;कर्तरि;लट्;उ;एक;परस्मैपदी;मृङ्;तुदादिः}
    अस्2{कर्तरि;लट्;प्र;एक;परस्मैपदी;अदादिः}          (no upadeśa field)

This module turns one such tag into the arguments of
``pipelines.tinanta.derive`` — dhātupāṭha id, lakāra, prayoga, puruṣa,
vacana, pada, upasargas, sanādi — or into an explicit *unresolved* reason.
It is a tools-layer reader (CONSTITUTION Art. 6): nothing in ``engine/``,
``sutras/`` or ``pipelines/`` may import it.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from functools import lru_cache

from core.transliterate import dev_to_slp1

LAKARA = {
    "लट्": "laT", "लिट्": "liT", "लुट्": "luT", "लृट्": "lRT", "लोट्": "loT",
    "लङ्": "laG", "विधिलिङ्": "liG", "आशीर्लिङ्": "AsIrliG", "लुङ्": "luG", "लृङ्": "lRG",
}
PRAYOGA = {"कर्तरि": "kartari", "कर्मणि": "karmani", "भावे": "bhave"}
PURUSHA = {"प्र": 3, "म": 2, "उ": 1}
VACANA = {"एक": 1, "द्वि": 2, "बहु": 3}
PADA = {"परस्मैपदी": "parasmai", "आत्मनेपदी": "atmane"}
GANA = {
    "भ्वादिः": 1, "अदादिः": 2, "जुहोत्यादिः": 3, "दिवादिः": 4, "स्वादिः": 5,
    "तुदादिः": 6, "रुधादिः": 7, "तनादिः": 8, "क्र्यादिः": 9, "चुरादिः": 10,
}
SANADI = {"णिच्": "nic", "णिजन्त": "nic", "सन्": "san", "सनन्त": "san"}

# The 22 prādayaḥ (1.4.58) in the upadeśa shape ``_attach_upasargas`` expects.
_UPASARGA = {
    "pra", "parA", "apa", "sam", "anu", "ava", "nis", "dus", "vi", "A", "ni",
    "aDi", "api", "ati", "su", "ud", "aBi", "prati", "pari", "upa",
}
_UPASARGA_ALIAS = {"nir": "nis", "dur": "dus", "ut": "ud", "saM": "sam", "AN": "A"}

_TAG = re.compile(r"^(?P<head>[^{}]+)\{(?P<fields>[^{}]*)\}$")


@dataclass
class TinantaCell:
    tag: str
    dhatu_id: str | None = None
    dhatu_upadesha_slp1: str | None = None
    gana: int | None = None
    lakara: str | None = None
    prayoga: str | None = None
    purusha: int | None = None
    vacana: int | None = None
    pada: str | None = None
    upasargas: list[str] = field(default_factory=list)
    sanadi: str | None = None
    unresolved: str | None = None

    def key(self) -> str:
        return "|".join([
            self.dhatu_id or "?", "+".join(self.upasargas), self.sanadi or "",
            self.prayoga or "?", self.lakara or "?", self.pada or "",
            f"{self.purusha}{self.vacana}",
        ])

    def derive_kwargs(self) -> dict:
        """Arguments for ``pipelines.tinanta.derive``; pada is forced only in
        kartari, where Saṃsādhanī reads it from context (ubhayapadī roots)."""
        kw: dict = {"upasargas": self.upasargas or None}
        if self.prayoga == "kartari":
            kw["pada"] = self.pada
        if self.sanadi == "nic":
            kw["nic_recipe"] = True
        elif self.sanadi == "san":
            kw["san_recipe"] = True
        return kw

    def as_dict(self) -> dict:
        return asdict(self)


def _upasarga(dev: str) -> str | None:
    s = dev_to_slp1(dev)
    s = _UPASARGA_ALIAS.get(s, s)
    return s if s in _UPASARGA else None


@lru_cache(maxsize=1)
def _dhatu_index() -> tuple[dict, dict]:
    from pipelines.dhatupatha import iter_dhatu_entries

    by_upadesha: dict[tuple[str, int], list[dict]] = {}
    by_raw: dict[tuple[str, int], list[dict]] = {}
    for e in iter_dhatu_entries():
        if not e.get("id"):
            continue
        g = e.get("gana_number") or e.get("gana")
        by_upadesha.setdefault((e.get("upadesha_dev", ""), g), []).append(e)
        by_raw.setdefault((e.get("raw_dhatu_after_it_lopa_dev", ""), g), []).append(e)
    return by_upadesha, by_raw


def _derivationally_same(hits: list[dict]) -> bool:
    """Homonyms (जि जये / जि अभिभवे) and duplicate rows derive alike when
    upadeśa, iṭ-class and pada agree — artha does not enter the prakriyā."""
    def sig(e: dict) -> tuple:
        f = e.get("flags") or {}
        return (e.get("upadesha_slp1"), f.get("set"), f.get("anit"), f.get("vet"),
                e.get("pada_label_dev"))
    return len({sig(e) for e in hits}) == 1


def _pick(hits: list[dict]) -> dict:
    from pipelines.dhatupatha import resolve_dhatu_identifier

    try:
        default = resolve_dhatu_identifier(hits[0]["upadesha_slp1"]).get("id")
    except KeyError:
        default = None
    return next((e for e in hits if e["id"] == default), hits[0])


def _resolve_dhatu(upadesha_dev: str | None, stem_dev: str, gana: int) -> tuple[dict | None, str | None]:
    by_upadesha, by_raw = _dhatu_index()
    hits = by_upadesha.get((upadesha_dev, gana), []) if upadesha_dev else []
    if not hits:
        hits = by_raw.get((stem_dev, gana), [])
    if not hits:
        return None, f"no dhātupāṭha row for {upadesha_dev or stem_dev} in gaṇa {gana}"
    if len(hits) == 1 or _derivationally_same(hits):
        return _pick(hits), None
    return None, f"ambiguous dhātu {upadesha_dev or stem_dev} in gaṇa {gana} ({len(hits)} rows)"


def tinanta_alternative(morph: str) -> str | None:
    """The first tiṅanta reading in a (possibly ``/``-joined) morph string."""
    for alt in morph.strip().strip("()").split("/"):
        m = _TAG.match(alt.strip())
        if m and any(f in LAKARA for f in m.group("fields").split(";")):
            return alt.strip()
    return None


def parse_tinanta_tag(tag: str) -> TinantaCell:
    cell = TinantaCell(tag=tag)
    m = _TAG.match(tag)
    if not m:
        cell.unresolved = "not a tiṅanta tag"
        return cell
    fields = m.group("fields").split(";")
    if fields and fields[0] in SANADI:
        cell.sanadi = SANADI[fields.pop(0)]
    if len(fields) not in (6, 7):
        cell.unresolved = f"unexpected field count {len(fields)}"
        return cell
    prayoga, lakara, purusha, vacana, pada = fields[:5]
    upadesha_field = fields[5] if len(fields) == 7 else None
    gana_label = fields[-1].lstrip(":")

    cell.prayoga = PRAYOGA.get(prayoga)
    cell.lakara = LAKARA.get(lakara)
    cell.purusha = PURUSHA.get(purusha)
    cell.vacana = VACANA.get(vacana)
    cell.pada = PADA.get(pada)
    cell.gana = GANA.get(gana_label)
    missing = [n for n, v in (("prayoga", cell.prayoga), ("lakāra", cell.lakara),
               ("puruṣa", cell.purusha), ("vacana", cell.vacana), ("gaṇa", cell.gana)) if v is None]
    if missing:
        cell.unresolved = "unknown " + ", ".join(missing)
        return cell

    # Head (कृ3, अभि_हन्1, वि_दॄ2_णिच्) and upadeśa (अभि_हनँ, वि_दॄ_णिच्) share
    # the same ``_``-joined layout: upasargas, dhātu, sanādi.
    def split(s: str) -> tuple[list[str], str, list[str]]:
        ups, dhatu, extra = [], "", []
        for tok in s.split("_"):
            tok = re.sub(r"\d+$", "", tok)
            if not dhatu and _upasarga(tok):
                ups.append(_upasarga(tok))
            elif tok in SANADI:
                extra.append(SANADI[tok])
            elif not dhatu:
                dhatu = tok
            else:
                extra.append(tok)
        return ups, dhatu, extra

    head_ups, stem_dev, head_extra = split(m.group("head"))
    ups, upadesha_dev, extra = split(upadesha_field) if upadesha_field else (head_ups, None, head_extra)
    ups = ups or head_ups
    extra = extra or head_extra
    unknown = [x for x in extra if x not in ("nic", "san")]
    if unknown:
        cell.unresolved = f"unhandled derivative {'+'.join(unknown)}"
        return cell
    if extra:
        if cell.sanadi and cell.sanadi != extra[0]:
            cell.unresolved = "conflicting sanādi markers"
            return cell
        cell.sanadi = extra[0]
    if len(set(x for x in extra)) > 1:
        cell.unresolved = "stacked sanādi (ṇic + san)"
        return cell
    cell.upasargas = ups

    row, why = _resolve_dhatu(upadesha_dev, stem_dev, cell.gana)
    if row is None:
        cell.unresolved = why
        return cell
    cell.dhatu_id = row["id"]
    cell.dhatu_upadesha_slp1 = row.get("upadesha_slp1")
    return cell
