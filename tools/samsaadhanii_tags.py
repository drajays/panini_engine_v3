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

import json
import re
from dataclasses import asdict, dataclass, field
from functools import lru_cache
from pathlib import Path

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


_PADA_LABEL = {"parasmai": "परस्मैपदी", "atmane": "आत्मनेपदी"}


def _narrow(hits: list[dict], pada: str | None) -> list[dict]:
    """Disambiguate homonym rows: the tag's pada, then the numbered dhātupāṭha row over a curated duplicate."""
    by_pada = [e for e in hits if e.get("pada_label_dev") in (_PADA_LABEL.get(pada or ""), "उभयपदी")]
    hits = by_pada or hits
    numbered = [e for e in hits if re.search(r"_\d\d_\d{4}$", e["id"])]
    return numbered if numbered and len({e["upadesha_slp1"].replace("~", "") for e in hits}) == 1 else hits


def _resolve_dhatu(upadesha_dev: str | None, stem_dev: str, gana: int,
                   pada: str | None = None) -> tuple[dict | None, str | None]:
    by_upadesha, by_raw = _dhatu_index()
    hits = by_upadesha.get((upadesha_dev, gana), []) if upadesha_dev else []
    if not hits:
        hits = by_raw.get((stem_dev, gana), [])
    if not hits:
        return None, f"no dhātupāṭha row for {upadesha_dev or stem_dev} in gaṇa {gana}"
    if len(hits) > 1:
        hits = _narrow(hits, pada)
    if len(hits) == 1 or _derivationally_same(hits):
        return _pick(hits), None
    return None, f"ambiguous dhātu {upadesha_dev or stem_dev} in gaṇa {gana} ({len(hits)} rows)"


LINGA = {"पुं": "pulliṅga", "स्त्री": "strīliṅga", "नपुं": "napuṃsaka"}


@dataclass
class SubantaCell:
    tag: str
    stem_dev: str = ""
    stem_slp1: str = ""
    linga: str | None = None
    vibhakti: int | None = None
    vacana: int | None = None
    unresolved: str | None = None

    def key(self) -> str:
        return f"{self.stem_slp1}|{self.linga}|{self.vibhakti}{self.vacana}"

    def as_dict(self) -> dict:
        return asdict(self)


def parse_subanta_tag(tag: str) -> SubantaCell:
    """``क्षेत्र{नपुं;7;एक}`` · ``एतद्{स्त्री}{2;एक}`` · ``युष्मद्{6;एक}`` ·
    ``भवत्{सर्वनाम;पुं;1;एक}`` · ``(अस्मद्{1;एक})`` (adhyāhṛta). Pronouns
    without a liṅga (yuṣmad/asmad) take pulliṅga — their paradigm does not
    vary by liṅga."""
    cell = SubantaCell(tag=tag)
    raw = (tag or "").strip()
    if raw.startswith("(") and raw.endswith(")") and raw.count("(") == 1:
        raw = raw[1:-1].strip()
    head = raw.split("{", 1)[0]
    groups = re.findall(r"\{([^{}]*)\}", raw)
    if "(" in raw or not groups:
        cell.unresolved = "kṛdanta/taddhita stem" if "(" in raw else "no sup tag"
        return cell
    fields = [f.strip() for g in groups for f in g.split(";")]
    if any(f.startswith("कृत्_प्रत्ययः") for f in fields):
        cell.unresolved = "kṛdanta stem"
        return cell
    if any(f in ("मतुप्", "तद्धित") or f.startswith("तद्धित") for f in fields):
        cell.unresolved = "taddhita stem"
        return cell
    cell.stem_dev = re.sub(r"\d+$", "", head.strip())
    cell.stem_slp1 = dev_to_slp1(cell.stem_dev)
    for f in fields:
        if f in LINGA:
            cell.linga = LINGA[f]
        elif f.isdigit() and 1 <= int(f) <= 8:
            cell.vibhakti = int(f)
        elif f in VACANA:
            cell.vacana = VACANA[f]
    if cell.vibhakti is None or cell.vacana is None:
        cell.unresolved = "no vibhakti/vacana"
        return cell
    cell.linga = cell.linga or "pulliṅga"
    return cell


def align_subanta_linga(cell: SubantaCell, word_slp1: str) -> SubantaCell:
    """Repair SCL liṅga when the attested pada is unambiguously napuṃsaka.

    Gītā 15.3–4: पदम् / तत् tagged पुं, which yields पदः / सः.
    """
    w = (word_slp1 or "").strip()
    if cell.unresolved or cell.vibhakti != 1 or cell.vacana != 1:
        return cell
    if cell.stem_slp1 == "pada" and w in {"padam", "padaM"}:
        cell.linga = "napuṃsaka"
    if cell.stem_slp1 == "tad" and w == "tat":
        cell.linga = "napuṃsaka"
    return cell


@dataclass
class KrdantaCell:
    """Indeclinable kṛt (क्त्वा, ल्यप्, तुमुन्, …) — sūtra from ``krit_pratyaya.json``."""
    tag: str
    krt_dev: str = ""
    krt_slp1: str = ""
    vidhana_sutra: str | None = None
    unresolved: str | None = None

    def as_dict(self) -> dict:
        return asdict(self)


@lru_cache(maxsize=1)
def _krt_index() -> dict[str, dict]:
    path = Path(__file__).resolve().parent.parent / "data" / "inputs" / "krit_pratyaya.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for key, v in data.items():
        if not isinstance(v, dict) or "upadesha_devanagari" not in v:
            continue
        out[v["upadesha_devanagari"]] = v
        out[key] = v
    return out


def parse_krdanta_tag(tag: str) -> KrdantaCell:
    cell = KrdantaCell(tag=tag)
    m = re.search(r"कृत्_प्रत्ययः:([^;}]+)", tag)
    if not m:
        cell.unresolved = "no kṛt pratyaya field"
        return cell
    cell.krt_dev = m.group(1).strip()
    row = _krt_index().get(cell.krt_dev)
    if not row:
        cell.unresolved = f"kṛt {cell.krt_dev} not in krit_pratyaya.json"
        return cell
    cell.krt_slp1 = row.get("upadesha_slp1") or ""
    cell.vidhana_sutra = row.get("vidhana_sutra")
    return cell


def classify_morph(morph: str) -> tuple[str, str]:
    """(kind, tag) for the first reading: tinanta · subanta · avyaya · krdanta ·
    samasa_member (bare pūrvapada stem) · none."""
    m = (morph or "").strip()
    if m in ("", "-"):
        return "none", m
    tin = tinanta_alternative(m)
    if tin:
        return "tinanta", tin
    first = m.strip("()").split("/")[0].strip()
    if "{अव्य}" in first:
        return "avyaya", first
    if "{" not in first:
        return ("krdanta" if "(" in first else "samasa_member"), first
    if "कृत्_प्रत्ययः" in first or "(" in first:
        return "krdanta", first
    return "subanta", first


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

    row, why = _resolve_dhatu(upadesha_dev, stem_dev, cell.gana, cell.pada)
    if row is None:
        cell.unresolved = why
        return cell
    cell.dhatu_id = row["id"]
    cell.dhatu_upadesha_slp1 = row.get("upadesha_slp1")
    return cell
