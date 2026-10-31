"""Taddhita-prakriyā deck 3 (owner's teaching deck: sopāna of a taddhita derivation, aṅga/bha/pada, aṅgakārya (ādivarṇa, ṭi, antimavarṇa),
then the prāgdīvyatīya senses: tasyāpatyam 4.1.92, rakta 4.2.1-2, nakṣatrayukta kāla 4.2.3-6, dṛṣṭaṃ sāma 4.2.7-9, parivṛta ratha 4.2.10-12,
udhṛta 4.2.14). Passing cases pin what the loop does by rule; strict xfails are gaps / wrong surfaces, with the cause. See docs/TADDHITA_3_CHECK.md.
Stems are the loop's stem before the tripāḍī (m->n, s->z come later); caller tags (lex:rAga, lex:nakzatra) are Lexicon facts."""
import pytest

from tests.regression.test_taddhita_2 import derive

E = frozenset()
RAGA = frozenset({"lex:rAga"})
NAKS = frozenset({"lex:nakzatra"})


def chain_stem(stem, artha, strI_first=True):
    from pipelines import chain
    s = chain.Stem(stem)
    return chain.taddhita(chain.strI(s) if strI_first else s, taddhitArtha=artha).slp1


# --- passing: by rule, the deck's surface is what the loop gives ----------------------------------------------------------------------
OK = [   # (stem, artha, tags, form)
    ("raGu", "apatya", E, "rAGava"), ("diti", "apatya", E, "dEtya"), ("aditi", "apatya", E, "Aditya"), ("daSaraTa", "apatya", E, "dASaraTi"),
    ("pfTivI", "apatya", E, "pArTiva"), ("suBadrA", "apatya", E, "sOBadra"), ("somadatta", "apatya", E, "sOmadatti"), ("Siva", "apatya", E, "SEva"),
    ("deva", "apatya", E, "dEva"), ("aSvapati", "apatya", E, "ASvapata"), ("SuBra", "apatya", E, "SOBreya"),
    ("SiSu", "apatya", E, "SESava"), ("rUru", "apatya", E, "rOrava"), ("pfTA", "apatya", E, "pArTa"),             # 6.4.146 ogunaH; 6.4.148 + 7.2.117
    ("madrarAjan", "samAsAnta", frozenset({"lex:samAsa"}), "madrarAja"),                                          # 5.4.91 ṭac, 6.4.144 an-lopa
    ("UrRA", "astyasya", E, "UrRAyu"),                                                                            # 5.2.123 yus (sit: pada)
    ("kazAya", "rakta", RAGA, "kAzAya"), ("maYjizWa", "rakta", RAGA, "mAYjizWa"), ("kusumBa", "rakta", RAGA, "kOsumBa"),
    ("Sukla", "rakta", RAGA, "SOkla"), ("kfzRa", "rakta", RAGA, "kArzRa"),                                        # 4.2.1 aṇ
    ("lAkzA", "rakta", RAGA, "lAkzika"), ("rocanA", "rakta", RAGA, "rOcanika"), ("Sakala", "rakta", RAGA, "SAkalika"),
    ("kardama", "rakta", RAGA, "kArdamika"),                                                                      # 4.2.2 ṭhak
    ("pIta", "rakta", RAGA, "pItaka"), ("nIlI", "rakta", RAGA, "nIla"), ("Sakala", "rakta", RAGA, "SAkala"),      # 4.2.2 vārttikas v1-v3
    ("haridrA", "rakta", RAGA, "hAridra"), ("mahArajana", "rakta", RAGA, "mAhArajana"),                           # vā. añ
    ("maGA", "yukta", NAKS, "mAGa"),                                                                              # 4.2.3 aṇ
    ("vasizWa", "dfzwa", E, "vAsizWa"), ("viSvAmitra", "dfzwa", E, "vESvAmitra"), ("kruYca", "dfzwa", E, "krOYca"),   # 4.2.7
    ("kali", "dfzwa", E, "kAleya"), ("vAmadeva", "dfzwa", E, "vAmadevya"), ("uSanas", "dfzwa", E, "OSanasa"),     # 4.2.8, 4.2.9
    ("vastra", "parivfta", E, "vAstra"), ("pARqukambala", "parivfta", E, "pARqukambalin"),                         # 4.2.10, 4.2.11
    ("dvEpa", "parivfta", E, "dvEpa"), ("vEyAGra", "parivfta", E, "vEyAGra"),                                      # 4.2.12 añ
    ("SarAva", "udDfta", E, "SArAva"), ("mallikA", "udDfta", E, "mAllika"), ("karpara", "udDfta", E, "kArpara"),   # 4.2.14
    ("carman", "parivfta", E, "cArmana"),   # Kāśikā 4.2.10 gives cārmaṇaḥ; the deck's cārma is a source conflict (Art. 22): the engine follows the Kāśikā
]


@pytest.mark.parametrize("stem,artha,og,want", OK, ids=[f"{o[0]}-{o[3]}" for o in OK])
def test_by_rule(stem, artha, og, want):
    assert want in derive(stem, artha, og), sorted(derive(stem, artha, og))


@pytest.mark.parametrize("stem,artha,want", [("gaNga", "apatya", "gANgeya"), ("kadru", "apatya", "kAdraveya"), ("kOSalya", "apatya", "kOSalyeya")])
def test_dhak_after_strI(stem, artha, want):          # 4.1.120 strībhyo ḍhak; 6.4.147 keeps the u of kadrū, 6.4.148 drops the ā / ī-final's last varṇa
    assert chain_stem(stem, artha) == want


def test_magha_nip():                                 # 4.1.15 ṅīp after aṇ: māghī rātriḥ
    from pipelines import chain
    s = chain.strI(chain.taddhita(chain.Stem("maGA", frozenset({"lex:nakzatra"})), taddhitArtha="yukta"))
    assert s.slp1 == "mAGI"


def test_no_rakta_without_raga():                     # deck: devadattena raktam / kaṣāyena dhūtam: no aṇ (4.2.1 reads rāga-viśeṣa)
    assert "kAzAya" not in derive("kazAya", "rakta", E)


def test_antima_varna_order_kunja():                  # deck: it-lopa 1.3.7 / 1.3.3 / 1.3.9, then 7.1.2, then vṛddhi 7.2.117, then a-lopa 6.4.148
    s = derive("kuYja", "apatya")["kOYjAyana"]
    assert {"1.3.7", "1.3.3"} <= set(s) and s.index("1.3.9") < s.index("7.1.2") < s.index("7.2.117") < s.index("6.4.148")


# --- strict xfail: gaps and wrong surfaces ---------------------------------------------------------------------------------------------
def _x(reason, stem, artha, og, want, **kw):
    return pytest.param(stem, artha, og, want, marks=pytest.mark.xfail(strict=True, reason=reason), id=want)


GAPS = [
    _x("vārttika 'tiṣyapuṣyayor nakṣatrāṇi yalopaḥ' (6.4.149): not written; the loop gives pOzya", "puzya", "yukta", NAKS, "pOza"),
    _x("4.2.4 lup aviśeṣe is a gate-only stub: the aṇ of 4.2.3 is never luped (adya puṣyaḥ)", "puzya", "yukta", NAKS, "puzya"),
    _x("4.2.4 lup (uttarā kālaḥ: the aṇ of 4.2.3 luped, 1.2.51 keeps the prakṛti's liṅga): stub", "uttarA", "yukta", NAKS, "uttarA"),
    _x("4.2.6 dvandvāc cha is a gate-only stub (tiṣyapunarvasavīyam needs a dvandva stem and cha in both viśeṣa / aviśeṣa)", "tizyapunarvasu", "yukta", NAKS, "tizyapunarvasavIya"),
    _x("vārttika 'asminn arthe aṇ ḍid vā vaktavyaḥ' (4.2.8): the ḍit reading (ṭi-lopa 6.4.143: auśanaḥ) is not offered", "uSanas", "dfzwa", E, "OSana"),
    _x("vārttika 'mahiṣāc ca' on 4.2.87: not written; the cāturarthika aṇ gives mAhiza", "mahiza", "asti", E, "mahizmat"),
    _x("vārttika 'pāṇḍor ḍyaṇ' (4.1.166-170 tadrāja group): the janapada-kṣatriya sūtras 4.1.168-178 are gate-only stubs; the loop gives pARqava", "pARqu", "apatya", E, "pARqya"),
    _x("4.1.137 rājaśvaśurād yat does not fire (+ vārttika rājño jātigrahaṇam: rājanya): the loop gives rAja", "rAjan", "apatya", E, "rAjanya"),
    _x("4.1.151 kurvādibhyo ṇyaḥ is a gate-only stub (Kāśikā: kauravyaḥ; the deck's añ via 4.1.86 contradicts the Kāśikā, Art. 22): the loop gives kOrava", "kuru", "apatya", E, "kOravya"),
    _x("4.1.171 vṛddhetkosalājādāñ ñyaṅ is a gate-only stub (Kāśikā: kuntī/kunti -> kauntyaḥ; the deck's ḍhak kaunteya differs): the loop gives kOnta", "kunti", "apatya", E, "kOntya"),
    _x("bāhvādi is an ākṛtigaṇa whose pāṭha has loman, not uḍuloman (Kāśikā 6.4.144 gives it only as an example): the loop gives Oqulomna", "uquloman", "apatya", E, "Oqulomi"),
    _x("4.1.135 catuṣpādbhyo ḍhañ (śītabāhu, jambū, kamaṇḍalu) is a gate-only stub: the loop gives SEtabAhava", "SItabAhu", "apatya", E, "SEtabAheya"),
    _x("5.2.140 ahaṃśubhamor yus is not reached: matup gives ahammat", "aham", "astyasya", E, "ahaMyu"),
    _x("4.2.14 needs the amatra (pātra-vācin) fact: pāṇau udhṛtaḥ odanaḥ must give no aṇ; the sūtra reads only the vivakṣā and fires for any stem", "pARi", "udDfta", E, None),
]


@pytest.mark.parametrize("stem,artha,og,want", GAPS)
def test_gaps(stem, artha, og, want):
    d = derive(stem, artha, og)
    if want is None:
        assert "pARa" not in d, sorted(d)
    else:
        assert want in d, sorted(d)


@pytest.mark.xfail(strict=True, reason="1.2.51 lupi yuktavad vyaktivacane needs 4.2.4 lup first (śravaṇam kālaḥ: neuter prakṛti-liṅga after the aṇ is luped)")
def test_lupi_yuktavat():
    assert "SravaRa" in derive("SravaRa", "yukta", NAKS)
