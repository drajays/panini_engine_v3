"""generator for T14a (5.3.1-60): wraps each stub like T12 (legacy halves kept, new attach block, SutraRecord flags). Run: python3 scratch/gen_t14a.py <ids...>"""
import pathlib
import sys

D = pathlib.Path("sutras/adhyaya_5/pada_3")
SARVA = ("sarva", "viSva", "uBa", "uBaya", "qatara", "qatama", "anya", "anyatara", "itara", "tvat", "tva", "nema", "sama", "sima", "pUrva", "para", "avara",
         "dakziRa", "uttara", "apara", "aDara", "sva", "antara", "tyad", "tad", "yad", "etad", "idam", "adas", "eka", "kim", "bahu")   # 5.3.2: sarvādi up to eka (not dvyādi), kim, bahu
AVY = "state.terms[-1].meta[META_ASARVA_VIBHAKTI_TADDHITA] = True      # a vibhakti pratyaya (5.3.1) does not take every case: 1.1.38 makes the word an avyaya\n    state.terms[-1].tags.add(TAG_5_3_1_VIBHAKTI)      # 5.3.1 prāg diśo vibhaktiḥ: its scope's pratyayas are vibhakti (1.3.4 keeps the final m of dānīm)"


def att(sid, ok_lines, rules, vibhakti=True, note=""):
    """rules: ((stems, pratyaya-or-readings), ...); a reading "-" stands aside (the vā)."""
    rules = "(\n" + "".join(f"    ({(dict(stems=sorted(s)) if isinstance(s, (set, frozenset)) else s)!r}, {up!r}),\n" for s, up in rules) + ")"
    imp = "\nfrom sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA\nfrom sutras.adhyaya_1.pada_3.sutra_1_3_4 import TAG_5_3_1_VIBHAKTI" if vibhakti else ""
    tail = f"    {AVY}\n" if vibhakti else ""
    return f'''from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita{imp}

_RULES = {rules}      # (the stems the sūtra names, the pratyaya or its readings){note}


def _attach(state: State):
{ok_lines}
    if not ok:
        return None
    for kw, up in _RULES:
        if taddhita_site(state, None, ok=True, **{{k: (frozenset(v) if k == "stems" else v) for k, v in kw.items()}}) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:{sid}")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "{sid}", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:{sid}"] = True
        return state
    state = attach_taddhita(state, up)
{tail}    return state
'''


def wrap(n, block, apav=None, also=False):
    p = D / f"sutra_5_3_{n}.py"
    s = p.read_text()
    assert "_legacy_cond" not in s, n
    s = s.replace("\ndef cond(", "\ndef _legacy_cond(").replace("\ndef act(", "\ndef _legacy_act(")
    s = s.replace("\n\nSUTRA = SutraRecord(", "\n\n" + block + "\n\nSUTRA = SutraRecord(", 1)
    extra = ""
    if apav:
        extra += f"    apavada_of     = {apav!r},\n"
    if also:
        extra += "    also_vidhi     = True,          # the loop opens this sense-frame from the speaker's taddhitArtha\n"
    s = s.replace("    cond                  = cond,", extra + "    cond                  = cond,", 1)
    p.write_text(s)


def ok(*pairs):
    return "    ok = " + " and ".join(f'vivaksita(state, "{k}", "{v}")' for k, v in pairs)


S = set(SARVA)
PA, SA, KALE, PRAKARA, ANADYA = ("taddhitArtha", "paYcamIvib"), ("taddhitArtha", "saptamIvib"), ("taddhitArtha", "kAle"), ("taddhitArtha", "prakAravacana"), ("arthaViSeSa", "anadyatana")

T = {   # id: (block, apavada_of)
    "7": (att("5.3.7", ok(PA), [(S, "tasi~l")]), None),
    "10": (att("5.3.10", ok(SA), [(S, "tral")]), None),
    "11": (att("5.3.11", ok(SA), [({"idam"}, "ha")]), ("5.3.10",)),
    "12": (att("5.3.12", ok(SA), [({"kim"}, ("at", "-"))]), ("5.3.10",)),
    "15": (att("5.3.15", ok(KALE), [({"sarva", "eka", "anya", "kim", "yad", "tad"}, "dA")]), None),
    "16": (att("5.3.16", ok(KALE), [({"idam"}, "rhil")]), None),
    "18": (att("5.3.18", ok(KALE), [({"idam"}, "dAnIm")]), None),
    "19": (att("5.3.19", ok(KALE), [({"tad"}, ("dA", "dAnIm"))]), ("5.3.15",)),
    "21": (att("5.3.21", ok(KALE, ANADYA), [(S - {"idam"}, ("rhil", "-"))]), ("5.3.15",)),
    "23": (att("5.3.23", ok(PRAKARA), [(S, "TAl")]), None),
    "24": (att("5.3.24", ok(PRAKARA), [({"idam"}, "Tamu~")]), ("5.3.23",)),
    "25": (att("5.3.25", ok(PRAKARA), [({"kim"}, "Tamu~")]), ("5.3.23",)),
}



def adesha(sid, stems_rules, prs=(), vikalpa=False):
    """rules: ((initial letter of the pratyaya or None for any, replacement as a tuple of SLP1 letters), ...): the stem is replaced whole (sarvādeśa) before a vibhakti pratyaya of 5.3.2 ff.; vikalpa: the vā"""
    return f'''from engine.vikalpa import policy_pick
from phonology import mk
from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA

_RULES = {stems_rules!r}      # {{the sthānin: ((the first letter of the pratyaya or None, the ādeśa), ...)}}
_PRATYAYAS = {tuple(prs)!r}      # the pratyayas the ādeśa is taught before (empty: any vibhakti pratyaya of 5.3.2 ff.)


def _site(state: State):
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if t.meta.get("upadesha_slp1") not in _RULES or t.meta.get("adesha_done:{sid}") or t.meta.get("adesha_of_stem"):
            continue
        if _PRATYAYAS and pr.meta.get("upadesha_slp1") not in _PRATYAYAS:
            continue
        if "taddhita" not in pr.tags or not pr.meta.get(META_ASARVA_VIBHAKTI_TADDHITA) or not pr.varnas:
            continue
        for first, new in _RULES[t.meta["upadesha_slp1"]]:
            if first is None or pr.varnas[0].slp1 == first:
                return t, new
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None and not state.meta.get("declined:{sid}")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    site = _site(state) if _new_cond(state) else None
    if site is None:
        return _legacy_act(state)
    t, new = site
{"    if policy_pick(state, " + repr(sid) + ", 2) == 1:                      # the vā: the stem stays" + chr(10) + "        t.meta[" + repr('adesha_done:' + sid) + "] = True" + chr(10) + "        t.meta['adesha_of_stem'] = " + repr(sid) + chr(10) + "        state.meta[" + repr('declined:' + sid) + "] = True" + chr(10) + "        return state" + chr(10) if vikalpa else ""}    t.varnas = [mk(c) for c in new]
    t.meta["adesha_sthani"] = t.meta["upadesha_slp1"]
    t.meta["upadesha_slp1"] = "".join(new)      # the ādeśa is the word now (not a tyadādi member: 1.2.72 / 7.2.102 leave it)
    t.tags.discard("tyadadi")
    t.meta["adesha_of_stem"] = "{sid}"
    t.meta["adesha_done:{sid}"] = True
    return state
'''

T["3"] = (adesha("5.3.3", {"idam": [(None, ("i",))]}), None)
T["4"] = (adesha("5.3.4", {"idam": [("r", ("e", "t", "a")), ("T", ("i", "t"))]}), ("5.3.3",))
T["5"] = (adesha("5.3.5", {"etad": [(None, ("a",))]}), None)
T["6"] = (adesha("5.3.6", {"sarva": [("d", ("s", "a"))]}, vikalpa=True), None)



VIDHA, ADHIK, YAPYA, BHAGA, ASAHAYA, BHUTAPURVA = ("taddhitArtha", "viDArTa"), ("taddhitArtha", "aDikaraRavicAla"), ("taddhitArtha", "yApya"), ("taddhitArtha", "BAga"), ("taddhitArtha", "asahAya"), ("taddhitArtha", "BUtapUrva")
SAMKHYA = dict(tag="saMKyA")      # SHORTCUT S53: the saṃkhyā words are a lexical tag from the caller (1.1.23 names bahu, gaṇa, vatu, ḍati; the numerals are laukika)
T.update({
    "42": (att("5.3.42", ok(VIDHA), [(SAMKHYA, "DA")]), None),
    "43": (att("5.3.43", ok(ADHIK), [(SAMKHYA, "DA")]), None),
    "44": (att("5.3.44", "    ok = vivaksita(state, \"taddhitArtha\", \"viDArTa\") or vivaksita(state, \"taddhitArtha\", \"aDikaraRavicAla\")", [({"eka"}, ("Dyamu~Y", "-"))]), ("5.3.42", "5.3.43")),
    "45": (att("5.3.45", "    ok = vivaksita(state, \"taddhitArtha\", \"viDArTa\") or vivaksita(state, \"taddhitArtha\", \"aDikaraRavicAla\")", [({"dvi", "tri"}, ("Damu~Y", "-"))]), ("5.3.42", "5.3.43")),
    "46": (att("5.3.46", "    ok = vivaksita(state, \"taddhitArtha\", \"viDArTa\") or vivaksita(state, \"taddhitArtha\", \"aDikaraRavicAla\")", [({"dvi", "tri"}, ("eDAc", "-"))]), ("5.3.42", "5.3.43")),
    "47": (att("5.3.47", ok(YAPYA), [({}, "pASap")], vibhakti=False), None),
    "48": (att("5.3.48", ok(BHAGA), [({"dvitIya", "tftIya"}, "an")], vibhakti=False), None),
    "49": (att("5.3.49", ok(BHAGA), [({"caturTa", "paYcama", "zazWa", "saptama", "azwama", "navama", "daSama"}, "an")], vibhakti=False), None),
    "50": (att("5.3.50", ok(BHAGA), [({"zazWa", "azwama"}, ("Ya", "-"))], vibhakti=False), ("5.3.49",)),
    "52": (att("5.3.52", ok(ASAHAYA), [({"eka"}, ("Akinic", "kan"))], vibhakti=False), None),
    "53": (att("5.3.53", ok(BHUTAPURVA), [({}, "caraw")], vibhakti=False), None),
})

DIK = ("taddhitArtha", "dik")
DIKSHABDA = dict(tag="dikSabda")      # SHORTCUT S53: the dik-śabda are a lexical tag from the caller
T.update({
    "27": (att("5.3.27", ok(DIK), [(DIKSHABDA, "astAti~")]), None),
})
T.update({
    "28": (att("5.3.28", ok(DIK), [({"dakziRa", "uttara"}, "atasu~c")]), ("5.3.27",)),
    "29": (att("5.3.29", ok(DIK), [({"para", "avara"}, ("atasu~c", "-"))]), ("5.3.27",)),
    "40": (adesha("5.3.40", {"pUrva": [(None, ("p", "u", "r"))], "aDara": [(None, ("a", "D"))], "avara": [(None, ("a", "v"))]}, prs=("astAti~",)), None),
    "41": (adesha("5.3.41", {"avara": [(None, ("a", "v"))]}, prs=("astAti~",), vikalpa=True), ("5.3.40",)),
})
ATISH = ("taddhitArtha", "atiSAyana")
# SHORTCUT S54: only the tamap / tarap readings of 5.3.55 / 5.3.57 are generated; iṣṭhan / īyasun (guṇavacana only, 5.3.58) wait for 6.4.154 – 159 (ṭi-lopa, prakṛtibhāva): they give paṭaviṣṭha for paṭiṣṭha
T.update({
    "55": (att("5.3.55", ok(ATISH), [({}, "tamap")], vibhakti=False), None),
    "57": (att("5.3.57", ok(ATISH, ("arthaViSeSa", "dvivacanavibhajya")), [({}, "tarap")], vibhakti=False), ("5.3.55",)),
})
if __name__ == "__main__":
    for n in sys.argv[1:]:
        wrap(n, *T[n])
