"""
tools/dcs_reader.py — DCS word analyses, Pāṇinian verification.
───────────────────────────────────────────────────────────────

Reads the CoNLL-U snapshot written by ``tools.fetch_dcs`` (source #20, DCS,
CC BY 4.0). Each tagged word is a **hypothesis**; the engine is the judge
(Art. 17): the word is *derived* only if the sūtra chain regenerates the
attested pada-pāṭha form (``Unsandhied``).

* subanta — lemma + Case / Gender / Number → ``pipelines.subanta.derive``.
* tiṅanta — DCS gives the lemma, tense / mood, person, number and voice but
  not the lakāra, gaṇa or pada. Its lexicon (``dictionary.csv``) gives gaṇa,
  pada and preverbs. Every lakāra the tense / mood can name (Past → liṭ or
  luṅ, Fut → lṛṭ or luṭ) × every dhātupāṭha row of the root × every pada the
  row allows is proposed; a reading is accepted only when its derivation
  reaches the attested form.
* compound members, indeclinables and kṛdantas are counted, not attempted.

Tools-layer (Art. 6): reads ``data/reference/``; nothing under ``engine/``,
``sutras/`` or ``pipelines/`` imports it.
"""
from __future__ import annotations

import collections
import csv
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

from tools.fetch_dcs import RAW
from tools.samsaadhanii_tags import _UPASARGA, _UPASARGA_ALIAS, TinantaCell

ATTRIBUTION = "Word analyses: Digital Corpus of Sanskrit (Oliver Hellwig), CC BY 4.0. Each ✓ is re-derived by the engine."

CASE = {"Nom": 1, "Acc": 2, "Ins": 3, "Dat": 4, "Abl": 5, "Gen": 6, "Loc": 7, "Voc": 8}
NUMBER = {"Sing": 1, "Dual": 2, "Plur": 3}
GENDER = {"Masc": "pulliṅga", "Fem": "strīliṅga", "Neut": "napuṃsaka"}
# Tense / Mood → the lakāras that can carry it (UD for DCS: Impf = laṅ; Past = liṭ or luṅ;
# Jus = augmentless luṅ with mā, 6.4.74; Fut = lṛṭ or the periphrastic luṭ).
LAKARAS = {
    ("Pres", "Ind"): ("laT",), ("Pres", "Imp"): ("loT",), ("Pres", "Opt"): ("liG",),
    ("Impf", "Ind"): ("laG",), ("Past", "Ind"): ("liT", "luG"), ("Past", "Prec"): ("AsIrliG",),
    ("Fut", "Ind"): ("lRT", "luT"), ("Fut", "Cond"): ("lRG",),
}
# DCS lemma conventions → engine stems (``enad`` is the anvādeśa form of idam / etad, 2.4.32–34).
PRONOUN_STEM = {"mad": "asmad", "tvad": "yuzmad", "aham": "asmad", "tvam": "yuzmad", "ka": "kim"}
ANVADESHA_STEMS = {"enad": ("etad", "idam")}
INDEFINITE = ("cit", "cana", "api")  # kaścit = kim + cit: two padas, not one subanta
# DCS tokenises the bhāva taddhitas apart from their base (guru-tvāt, guru-tā). -tā declines as any ā-stem,
# but a bare ``tva`` is the sarvādi pronoun (1.1.27), so the split -tva cannot be judged on its own.
TADDHITA_SPLIT = {"tva": "5.1.119 tasya bhāvas tvatalau"}
AVYAYA_POS = {"ADV", "PART", "CONJ", "CCONJ", "SCONJ", "ADP", "INTJ"}
_PADA = {"P": "parasmai", "Ā": "atmane"}


def iast_to_slp1(s: str) -> str:
    from indic_transliteration import sanscript

    # DCS writes vocalic ḷ as U+FFB1 (kḷp) and ṝ as U+FFDE (kṝ, pṝ, jṝ)
    s = unicodedata.normalize("NFC", s or "").replace("\uffb1", "ḷ").replace("\uffde", "ṝ")
    return sanscript.transliterate(s, sanscript.IAST, sanscript.SLP1)


# ── Snapshot access ────────────────────────────────────────────────────────

def available() -> bool:
    return (RAW / "dictionary.csv").is_file()


def texts() -> list[str]:
    return sorted(p.name for p in RAW.iterdir() if p.is_dir()) if RAW.is_dir() else []


def chapters(text: str) -> list[Path]:
    return sorted((RAW / text).glob("*.conllu"))


@lru_cache(maxsize=1)
def lexicon() -> dict[str, dict]:
    """LemmaId → {word, grammar, preverbs} from DCS ``dictionary.csv``."""
    with (RAW / "dictionary.csv").open(encoding="utf-8", newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)}


def _feats(s: str) -> dict[str, str]:
    return dict(kv.split("=", 1) for kv in s.split("|") if "=" in kv) if s not in ("", "_") else {}


def parse(text: str) -> list[dict]:
    """CoNLL-U → sentences ``{sent_id, text, tokens}``; multiword ranges are skipped (their parts are words)."""
    out, cur, span = [], None, None
    for line in text.splitlines():
        c = line.split("\t")
        if len(c) == 10 and re.fullmatch(r"\d+-\d+", c[0]):
            a, b = map(int, c[0].split("-"))
            span = (a, b, c[1])
            continue
        if line.startswith(("# text =", "# sent_id")) and (cur is None or cur["tokens"]):
            cur = {"sent_id": "", "text": "", "tokens": []}
            out.append(cur)
        if line.startswith("# text ="):
            cur["text"] = line.split("=", 1)[1].strip()
        elif line.startswith("# sent_id"):
            cur["sent_id"] = line.split("=", 1)[1].strip()
        elif line and not line.startswith("#") and cur is not None:
            if len(c) != 10 or not c[0].isdigit():
                continue
            i = int(c[0])
            tok = {"id": i, "form": c[1], "lemma": c[2], "upos": c[3], "feats": _feats(c[5]), "misc": _feats(c[9])}
            if span and span[0] <= i <= span[1]:
                tok["span_surface"] = span[2] if i == span[1] else None  # only the last word ends the written string
            cur["tokens"].append(tok)
    return [s for s in out if s["tokens"]]


# ── Classification and engine requests ─────────────────────────────────────

def classify(tok: dict) -> str:
    """tinanta · subanta · krdanta · samasa_member · avyaya · none."""
    f, pos = tok["feats"], tok["upos"]
    if f.get("Case") == "Cpd":
        return "samasa_member"
    if "VerbForm" in f:
        return "krdanta"
    if pos == "VERB" and "Person" in f:
        return "tinanta"
    if f.get("Case") in CASE:
        return "subanta"
    if pos in AVYAYA_POS:
        return "avyaya"
    return "none"


def attested_slp1(tok: dict) -> str:
    return attested_forms(tok)[0] if attested_forms(tok) else ""


def attested_forms(tok: dict) -> list[str]:
    """Pada-pāṭha form first, then FORM: DCS reconstructs ``Unsandhied`` by machine and it can be wrong
    (Megh. वोक॰ ``jalada`` reconstructed as ``jaladaiḥ``), while FORM of a stand-alone word is the text."""
    out = []
    for s in (tok["misc"].get("Unsandhied"), tok["form"]):
        w = iast_to_slp1(s) if s and s != "_" else ""
        if w and w not in out:
            out.append(w)
    return out


def subanta_requests(tok: dict) -> tuple[list[dict], str | None]:
    """Readings the tag names; an untagged liṅga proposes all three (the attested form decides)."""
    f = tok["feats"]
    lemma = iast_to_slp1(tok["lemma"])
    v, vac = CASE.get(f.get("Case", "")), NUMBER.get(f.get("Number", ""))
    if None in (v, vac):
        return [], "no case/number"
    if tok["upos"] == "PRON" and lemma.endswith(INDEFINITE) and lemma != "api":
        return [], f"{tok['lemma']} = kim + particle (two padas)"
    if lemma in TADDHITA_SPLIT and tok["upos"] != "PRON":
        return [], f"taddhita -{tok['lemma']} split from its base by DCS ({TADDHITA_SPLIT[lemma]})"
    stems = [(s, True) for s in ANVADESHA_STEMS.get(lemma, ())] or [(PRONOUN_STEM.get(lemma, lemma), False)]
    linga = GENDER.get(f.get("Gender", ""))
    if linga:
        lingas = (linga,)
    elif stems[0][0] in ("asmad", "yuzmad"):
        lingas = ("pulliṅga",)  # their paradigm does not vary by liṅga
    else:
        lingas = tuple(GENDER.values())
    return [{"kind": "subanta", "stem_slp1": s, "vibhakti": v, "vacana": vac, "linga": lg,
             **({"anvadesha": True} if anv else {}), **({} if linga or len(lingas) == 1 else {"linga_proposed": True})}
            for s, anv in stems for lg in lingas], None


_PREVERB_ALIAS = {**_UPASARGA_ALIAS, "niH": "nis", "duH": "dus"}
# Vowel sandhi at the preverb–root seam: the root-initial vowels a junction can hide.
# 6.1.101 akaḥ savarṇe dīrghaḥ, 6.1.87 ādguṇaḥ, 6.1.88 vṛddhir eci; ar = a + ṛ (6.1.87 with 1.1.51).
_SEAM = {"A": ("a", "A"), "e": ("i", "I"), "o": ("u", "U"), "E": ("e", "E"), "O": ("o", "O"), "ar": ("f",)}
_VOWELS = set("aAiIuUfFxXeEoO")


def split_preverbs(s: str) -> list[str] | None:
    """DCS writes stacked preverbs in sandhi (``samā``, ``vyā``, ``abhisam``) → the prādi upadeśas (1.4.58)."""
    if not s:
        return []
    for u in sorted(_UPASARGA | set(_PREVERB_ALIAS), key=len, reverse=True):
        name = _PREVERB_ALIAS.get(u, u)
        heads = [(u, s[len(u):])] if s.startswith(u) else []
        if u.endswith("i") and s.startswith(u[:-1] + "y"):  # yaṇ 6.1.77: vi + ā → vyā
            heads.append((u, s[len(u):]))
        if u.endswith("a") and s.startswith(u[:-1] + "A"):  # savarṇa-dīrgha 6.1.101: upa + ā → upā
            heads += [(u, "A" + s[len(u):]), (u, "a" + s[len(u):])]
        for _, rest in heads:
            tail = split_preverbs(rest)
            if tail is not None:
                return [name] + tail
    return None


@lru_cache(maxsize=1)
def _dhatu_rows() -> dict[str, list[dict]]:
    from pipelines.dhatupatha import iter_dhatu_entries

    by: dict[str, list[dict]] = {}
    for e in iter_dhatu_entries():
        if not e.get("id"):
            continue
        for k in ("raw_dhatu_after_it_lopa_slp1", "citation_dhatu_slp1"):
            v = (e.get(k) or "").replace("~", "")
            # 6.1.45 ādeca upadeśe 'śiti: DCS cites ec-final roots in their ā shape (dhyai → dhyā)
            for key in {v, v[:-1] + "A" if v[-1:] in ("e", "E", "o", "O") else v}:
                if key and e not in by.get(key, []):
                    by.setdefault(key, []).append(e)
    return by


def _roots(lemma: str, pv: str) -> list[str]:
    """Root candidates once the preverb string is taken off the lemma (prekṣ = pra + īkṣ)."""
    if lemma.startswith(pv):
        return [lemma[len(pv):]]
    out = []
    if pv[-1:] not in _VOWELS and lemma.startswith(pv[:-1]) and lemma[len(pv) - 1:len(pv)] not in _VOWELS:
        # consonant seam: niḥ + viś → nirviś (8.2.66), niḥ + pat → niṣpat (8.3.41), sam + lakṣ → saṃlakṣ (8.3.23)
        out.append(lemma[len(pv):])
    if pv[-1:] in ("a", "A") and lemma.startswith(pv[:-1]):
        rest = lemma[len(pv) - 1:]
        for seam, firsts in _SEAM.items():
            if rest.startswith(seam):
                out += [f + rest[len(seam):] for f in firsts]
    if pv[-1:] in ("i", "u") and lemma.startswith(pv[:-1] + {"i": "y", "u": "v"}[pv[-1]]):  # 6.1.77 iko yaṇ aci
        rest = lemma[len(pv):]
        out += [rest] if rest[:1] in _VOWELS else []
    if pv[-1:] in ("i", "u") and lemma.startswith(pv[:-1] + {"i": "I", "u": "U"}[pv[-1]]):  # 6.1.101
        out.append(pv[-1] + lemma[len(pv):])
        out.append({"i": "I", "u": "U"}[pv[-1]] + lemma[len(pv):])
    return out


def _row_padas(e: dict) -> tuple[str | None, ...]:
    """The engine's own pada choice (1.3.12 ff., incl. upasarga-conditioned 1.3.19–) first, then each pada the row allows."""
    lab = e.get("pada_label_dev") or ""
    return (None,) + {"परस्मैपदी": ("parasmai",), "आत्मनेपदी": ("atmane",)}.get(lab, ("parasmai", "atmane"))


# DCS lemmatises some substitutes as roots: 7.3.78 pāghrā-… (paśyati → paś), 8.2.18 kṛpo ro laḥ (kḷp).
_ADESHA_ROOT = {"paS": "dfS", "pib": "pA", "jiGr": "GrA", "tizW": "sTA", "yacC": "dA", "sId": "sad", "kxp": "kfp",
                "TA": "sTA", "Tamb": "stamB"}  # 8.4.61 udaḥ sthāstambhoḥ pūrvasya: ut + sthā → utthā


def _nic_bases(stem: str) -> list[str]:
    """Roots a ṇic stem (``Xay``, 3.1.25–26) can come from, undoing the changes ṇic conditions:
    7.2.116 upadhā a → ā, 7.2.115 final vowel vṛddhi (+ 6.1.78 āy / āv), 7.3.86 laghūpadha guṇa,
    6.4.92 mit hrasva (no change to undo), 7.3.36 puk after ā, 6.4.48 ato lopaḥ (adanta curādi gaṇa → gaṇay)."""
    b = stem[:-2]
    out = {b, b + "a"}
    for done, roots in (("Ay", ("i", "I")), ("Av", ("u", "U")), ("Ar", ("f",))):
        if b.endswith(done):
            out.update(b[:-2] + r for r in roots)
    m = re.search(r"(A|e|o|ar|al)([^aAiIuUfFxeEoO]*)$", b)
    if m:
        for r in {"A": ("a",), "e": ("i", "I"), "o": ("u", "U"), "ar": ("f",), "al": ("x",)}[m.group(1)]:
            out.add(b[:m.start()] + r + m.group(2))
    if b.endswith(("Ap", "ap")):
        out.add(b[:-2] + "A")
    out.update(_ADESHA_ROOT[r] for r in list(out) if r in _ADESHA_ROOT)
    out.update(r[:-1] + "F" for r in list(out) if r.endswith("f"))
    return sorted(out)


def _dcs_ganas(grammar: str) -> set[int]:
    return {int(m) for m in re.findall(r"(\d+)\.\s*[PĀ]", grammar or "")}


def tinanta_requests(tok: dict) -> tuple[list[dict], str | None]:
    """Every reading the tag can name, DCS-listed gaṇas first; or ``([], reason)``."""
    f = tok["feats"]
    lak = LAKARAS.get((f.get("Tense"), f.get("Mood")))
    if f.get("Mood") == "Jus":
        return [], "injunctive (augmentless luṅ, māṅ-yoga 6.4.74) not modelled"
    if not lak:
        return [], f"tense/mood {f.get('Tense')}/{f.get('Mood')} not mapped"
    person, number = f.get("Person"), NUMBER.get(f.get("Number", ""))
    if person not in ("1", "2", "3") or number is None:
        return [], "no person/number"
    lex = lexicon().get(tok["misc"].get("LemmaId", ""), {})
    grammar = lex.get("grammar") or ""
    if re.search(r"Denom|Caus|Desid|Intens", grammar):
        return [], f"derived root ({grammar.split()[0]})"
    pv_iast = lex.get("preverbs") or ""
    ups = split_preverbs(iast_to_slp1(pv_iast))
    if ups is None:
        return [], f"preverbs {pv_iast} not split"
    lemma = iast_to_slp1(tok["lemma"])
    pv = iast_to_slp1(pv_iast)
    roots = _roots(lemma, pv) if pv else [lemma]
    if not roots:
        return [], f"root not separable from preverb {pv_iast} in {tok['lemma']}"
    roots += [_ADESHA_ROOT[r] for r in roots if r in _ADESHA_ROOT]
    roots += [r[:-1] + "F" for r in roots if r.endswith("f")]  # DCS cites ṝ-final roots with ṛ (tṝ → tṛ, śṝ → śṛ)
    rows = [(e, False) for r in roots for e in _dhatu_rows().get(r, [])]
    if not rows:  # a ṇic stem: curādi rows carry ṇic themselves (3.1.25); others take hetumati ṇic (3.1.26)
        rows = [(e, e.get("gana_number") != 10) for r in roots if r.endswith("ay")
                for b in _nic_bases(r) for e in _dhatu_rows().get(b, [])]
    if not rows:
        return [], f"no dhātupāṭha row for {'/'.join(roots)}"
    ganas = _dcs_ganas(grammar)
    rows = sorted(rows, key=lambda x: (x[0].get("gana_number") not in ganas, x[1], x[0]["id"]))
    prayoga = "karmani" if f.get("Voice") == "Pass" else "kartari"
    out = []
    for e, nic in rows:
        for lk in lak:
            padas = (None, "parasmai", "atmane") if nic else _row_padas(e)  # 1.3.74 ṇicaś ca: ṇijanta is ubhayapadī
            for pada in (padas if prayoga == "kartari" else (None,)):
                out.append({"kind": "tinanta", "dhatu_id": e["id"], "dhatu_upadesha_slp1": e.get("upadesha_slp1"),
                            "gana": e.get("gana_number"), "lakara": lk, "prayoga": prayoga,
                            "purusha": int(person), "vacana": number, "pada": pada, "upasargas": ups,
                            "sanadi": "nic" if nic else None})
    return out, None


# ── Verdicts ──────────────────────────────────────────────────────────────
# DCS's pada-pāṭha form is reconstructed from the text, so it can keep a choice the
# śāstra leaves open. Each equivalence below is one such vibhāṣā or sandhi, named.

_JAS_CAR = str.maketrans("gqdb", "kwtp")
_NASAL = {**dict.fromkeys("kKgGN", "N"), **dict.fromkeys("cCjJY", "Y"), **dict.fromkeys("wWqQR", "R"),
          **dict.fromkeys("tTdDn", "n"), **dict.fromkeys("pPbBm", "m")}


def _fold_nasal(s: str) -> str:
    """8.4.59 vā padāntasya: anusvāra before a stop ≡ the stop's nasal (saṃdeśa / sandeśa)."""
    return re.sub(r"M(?=([kKgGNcCjJYwWqQRtTdDnpPbBm]))", lambda m: _NASAL[m.group(1)], s)


def _match(produced: str, word: str) -> str | None:
    if produced == word:
        return "derived"
    if produced[:-1] == word[:-1] and produced[-1:].translate(_JAS_CAR) == word[-1:].translate(_JAS_CAR):
        return "derived_8_4_56"  # vāvasāne: pausal jaś or car (kaścid / kaścit)
    if _fold_nasal(produced) == _fold_nasal(word):
        return "derived_8_4_59"
    if produced.endswith("H") and produced[:-1] == word and produced[-2:-1] in ("a", "A"):
        return "derived_8_3_22"  # bho-bhago-agho-a-pūrvasya yo 'śi (8.3.17) + lopa (8.3.19 / 8.3.22) before the next word
    return None


def _tinanta_cell(req: dict) -> tuple[str, str]:
    c = TinantaCell(tag="dcs", **{k: req[k] for k in ("dhatu_id", "dhatu_upadesha_slp1", "gana", "lakara",
                                                      "prayoga", "purusha", "vacana", "pada", "upasargas",
                                                      "sanadi")})
    return c.key(), json.dumps(c.as_dict(), ensure_ascii=False, sort_keys=True)


def _match_any(produced: str, forms: list[str], surface: str | None = None) -> str | None:
    m = next((m for w in forms if (m := _match(produced, w))), None)
    if m is None and surface and len(produced) >= 3 and surface.endswith(produced):
        # the written string ends in the engine's form; DCS's reconstruction of the last word disagrees with the text
        # (MBh guṇāṃstāta: FORM and Unsandhied both "tātaiḥ", the vocative tāta is written)
        return "derived_surface"
    return m


def _enclitic_context(prev: list[dict], nxt: dict | None) -> dict:
    """Neighbours in the DCS sentence; DCS marks no pāda, so the context is approximate (8.1.18 apādādau)."""
    from core.transliterate import slp1_to_dev
    from tools.reader_enclitic import PARTICLES

    before = [{"slp1": attested_slp1(t), "vibhakti": CASE.get(t["feats"].get("Case", ""))}
              for t in prev if classify(t) != "samasa_member"]
    after = []
    if nxt is not None:
        w = attested_slp1(nxt)
        after = [{"slp1": w, "lexeme": PARTICLES.get(slp1_to_dev(w))}]
    return {"before": before, "after": after, "approx": True}


def _verify_subanta(tok: dict, out: dict, prev: list[dict], nxt: dict | None) -> dict:
    from tools.samsaadhanii_reader import _derive_subanta

    reqs, why = subanta_requests(tok)
    if why:
        return {**out, "status": "unresolved", "note": why}
    forms, produced, err = out["forms"], [], None
    for req in reqs:
        st, slp, dev = _derive_subanta(req["stem_slp1"], req["vibhakti"], req["vacana"], req["linga"],
                                       bool(req.get("anvadesha")))
        if st == "error":
            err = err or dev
            continue
        m = _match_any(slp, forms, out.get("surface"))
        if m:
            return {**out, "status": m, "produced": slp, "request": req}
        produced.append((slp, req))
    if reqs[0]["stem_slp1"] in ("asmad", "yuzmad") and 1 <= reqs[0]["vibhakti"] <= 7:
        from tools.reader_enclitic import judge

        ctx = _enclitic_context(prev, nxt)
        v = next((v for w in forms if (v := judge(reqs[0], w, [ctx])) and v["status"] == "derived"), None)
        if v:
            return {**out, "status": "derived_8_1_20", "produced": v["produced_slp1"], "request": {**reqs[0], "context": ctx},
                    "note": "8.1.20–26 in sentence context (pāda boundary approximate)"}
    if not produced:
        return {**out, "status": "error", "note": err}
    return {**out, "status": "differs", "produced": produced[0][0] if len(produced) == 1 else sorted({p for p, _ in produced}),
            "request": produced[0][1]}


def _verify_tinanta(tok: dict, out: dict) -> dict:
    from tools.samsaadhanii_reader import _derive_tinanta, _tinanta_readings

    reqs, why = tinanta_requests(tok)
    if why:
        return {**out, "status": "unresolved", "note": why}
    forms, produced, errors = out["forms"], [], []
    for req in reqs:
        st, slp, dev = _derive_tinanta(*_tinanta_cell(req))
        if st == "error":
            errors.append(dev)
            continue
        m = _match_any(slp, forms, out.get("surface"))
        if m:
            return {**out, "status": m, "produced": slp, "request": req}
        produced.append(slp)
    for req in reqs:  # a vibhāṣā the first reading did not take (engine.vikalpa.explore)
        for s2, _d2, choices in _tinanta_readings(*_tinanta_cell(req)):
            m = _match_any(s2, forms, out.get("surface"))
            if m:
                return {**out, "status": m, "produced": s2, "request": req,
                        "note": "vibhāṣā " + ", ".join(sid for sid, ch in choices if ch)}
    if not produced:
        return {**out, "status": "error", "note": errors[0] if errors else "no reading"}
    return {**out, "status": "differs", "produced": sorted(set(produced)), "readings_tried": len(reqs)}


def verify(tok: dict, prev: list[dict] = (), nxt: dict | None = None) -> dict:
    """Engine verdict for one DCS word; ``prev`` / ``nxt`` are its sentence neighbours."""
    kind = classify(tok)
    forms = attested_forms(tok)
    out = {"kind": kind, "word": forms[0] if forms else "", "forms": forms, "lemma": tok["lemma"], "feats": tok["feats"]}
    if tok.get("span_surface"):
        out["surface"] = iast_to_slp1(tok["span_surface"])
    if kind in ("subanta", "tinanta") and not forms:
        return {**out, "status": "unresolved", "note": "no attested form"}
    if kind == "subanta":
        return _verify_subanta(tok, out, list(prev), nxt)
    if kind == "tinanta":
        return _verify_tinanta(tok, out)
    return {**out, "status": "not_attempted"}


DERIVED = ("derived", "derived_8_4_56", "derived_8_4_59", "derived_8_3_22", "derived_8_1_20", "derived_surface")
GAP = ("differs", "error", "unresolved")


def coverage(text: str, limit: int | None = None, every: int = 1) -> dict:
    """Verdict counts ``{kind: {status: n}}`` and the non-derived words for one DCS text.
    ``every`` samples every k-th chapter across the whole text; ``limit`` then caps sentences."""
    counts: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    gaps, n = [], 0
    for path in chapters(text)[::max(every, 1)]:
        for s in parse(path.read_text(encoding="utf-8")):
            if limit is not None and n >= limit:
                return {"text": text, "counts": {k: dict(v) for k, v in counts.items()}, "gaps": gaps}
            n += 1
            toks = s["tokens"]
            for i, tok in enumerate(toks):
                v = verify(tok, toks[:i], toks[i + 1] if i + 1 < len(toks) else None)
                counts[v["kind"]][v["status"]] += 1
                if v["status"] in GAP:
                    gaps.append({**v, "sent_id": s["sent_id"], "chapter": path.stem})
    return {"text": text, "counts": {k: dict(v) for k, v in counts.items()}, "gaps": gaps}


