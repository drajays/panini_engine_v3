"""tools/build_vivaksha_schema.py — AMENDMENT 25: the closed vivakṣā vocabulary, taken from the Aṣṭādhyāyī's own words.

    python3 -m tools.build_vivaksha_schema        # writes data/inputs/vivaksha_schema.json

A value is admitted only if one of its word forms occurs as a word of some sūtra's samagra text (ashtadhyayi.com,
Art. 4); the file lists those sūtras as its citation. Nothing is invented: a value with no occurrence is refused.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
OUT = _ROOT / "data" / "inputs" / "vivaksha_schema.json"

# key -> value (SLP1 stem) -> the inflected forms in which Pāṇini states that meaning in a sūtra
VOCABULARY = {
    "artha": {
        "kartf": ["kartari"], "karman": ["karmaRi"], "BAva": ["BAve", "BAvakaraRayoH"], "karaRa": ["karaRe", "karaRam", "karaRADikaraRayoH", "BAvakaraRayoH"],
        "aDikaraRa": ["aDikaraRe", "karaRADikaraRayoH"], "sampradAna": ["sampradAne"], "apAdAna": ["apAdAne"],
        # the meanings the kṛtya sūtras 3.1.103, 115, 116, 121, 125 name in their own words
        "svAmivESya": ["vESyayoH"], "nada": ["nade"], "nakzatra": ["nakzatre"], "patra": ["patre"], "AvaSyaka": ["AvaSyake"],
    },
    "kala": {"BUta": ["BUte"], "vartamAna": ["vartamAne"], "Bavizyat": ["Bavizyati"], "pUrvakAla": ["pUrvakAle"]},
    "kartrabhiprAya": {"kartraBiprAya": ["kartraBiprAye"]},
    # AMENDMENT 25 addendum (2026-10-24, owner: "update if as per the sūtra"): the kṛt families the Aṣṭādhyāyī itself sets side by side
    # as adhikāra-level choices — कृत्याः (3.1.95), ण्वुल्तृचौ (3.1.133) — and the kriyārthā sense of 3.3.10. The word is the sūtra's own.
    "krt": {"kftya": ["kftyAH"], "Rvultfc": ["tfcO"]},
    "kriyArTA": {"kriyArTA": ["kriyArTAyAm"]},
    # 3.2.124: śatṛ-śānac replace laṭ when the word agrees with a noun that is not in the first case (pacantaṃ caitram paśya)
    "samAnADikaraRa": {"apraTamA": ["apraTamAsamAnADikaraRe"]},
    # 3.2.125–133: the meanings that place śatṛ / śānac / śānan / cānaś in laṭ's stead (each word is the sūtra's own)
    "sambodhana": {"sambodhana": ["samboDane"]},
    "lakzaRahetu": {"lakzaRa": ["lakzaRahetvoH"], "hetu": ["lakzaRahetvoH"]},
    "tAcCIlyAdi": {"tAcCIlya": ["tAcCIlya"], "vayovacana": ["vayovacana"], "Sakti": ["Saktizu"]},
    "akfcCra": {"akfcCra": ["akfcCriRi"]}, "amitra": {"amitra": ["amitre"]},
    "yajYasaMyoga": {"yajYasaMyoga": ["yajYasaMyoge"]}, "praSaMsA": {"praSaMsA": ["praSaMsAyAm"]},
    # 3.2.20 (kṛñ + ṭa) and 3.2.78 (ṇini), 3.2.83 (khaś / ṇini)
    "hetutAcCIlyAnulomya": {"hetu": ["hetu"], "tAcCIlya": ["tAcCIlya"], "Anulomya": ["anulomyezu"]},
    # the gender a bhāve kṛt is taught for (3.3.94 striyām ktin, 3.3.115 napuṃsake lyuṭ, 3.3.121 puṃsi)
    "linga": {"strI": ["striyAm"], "napuMsaka": ["napuMsake"], "puM": ["puMsi"]},
    # taddhita: the sense a pratyaya is taught in (the frame an ADHIKARA opens: 4.1.92 tasyāpatyam …) and, for apatya, which descendant (4.1.162 gotra, 4.1.163 yuvan)
    "taddhitArtha": {"apatya": ["apatyam"], "rakta": ["raktaM", "rakte"], "yukta": ["yuktaH"], "dfzwa": ["dfzwaM"], "parivfta": ["parivfto"], "udDfta": ["udDftamamatreByaH"], "saMskfta": ["saMskftaM"], "devatA": ["devatA"], "samUha": ["samUhaH"], "asti": ["astIti"], "nirvfta": ["nirvfttam"], "nivAsa": ["nivAsaH"], "adUraBava": ["adUraBavaH"], "Seza": ["Seze"], "prAyaBava": ["prAya"], "praBavati": ["praBavati"], "granTa": ["granTe"], "idam": ["idam"], "vikAra": ["vikAraH"], "jAta": ["jAtaH"], "Bava": ["BavaH"], "Agata": ["AgataH"],
        # 4.3.85 / 86 / 135: the senses that name their own word
        "gacCatiPaTiDUta": ["paTidUtayoH"], "abhinizkrAmati": ["aBinizkrAmati"], "avayava": ["avayave"],
        # 4.4.2 – 74 (ṭhak): the senses each sūtra names in its own words
        "dIvyati": ["dIvyati"], "Kanati": ["Kanati"], "jayati": ["jayati"], "jita": ["jitam"], "tenasaMskfta": ["saMskftam"], "tenanirvfta": ["nirvftte"], "tarati": ["tarati"],
        "carati": ["carati"], "jIvati": ["jIvati"], "harati": ["harati"], "saMsfzwa": ["saMsfzwe"], "upasikta": ["upasikte"], "vartate": ["vartate"],
        "prayacCati": ["prayacCati"], "uYCati": ["uYCati"], "rakzati": ["rakzati"], "karoti": ["karoti"], "hanti": ["hanti"], "tizWati": ["tizWati"],
        "DAvati": ["DAvati"], "gfhRAti": ["gfhRAti"], "eti": ["eti"], "samavEti": ["samavEti"], "paSyati": ["paSyati"], "Darmya": ["Darmyam"],
        "avakraya": ["avakrayaH"], "paRya": ["paRyam"], "Silpa": ["Silpam"], "praharaRa": ["praharaRam"], "mati": ["matiH"], "SIla": ["SIlam"],
        "vftta": ["vfttam"], "hita": ["hitam"], "dIyate": ["dIyate"], "niyukta": ["niyuktaH"], "aDyAyin": ["aDyAyini"], "vyavaharati": ["vyavaharati"],
        "vasati": ["vasati"],
        # 4.4.76 – 109 (yat)
        "vahati": ["vahati"], "viDyati": ["viDyati"], "labDA": ["labDA"], "gata": ["gataH"], "dfSya": ["dfSyamasmin"], "Abarhi": ["Abarhi"],
        "saMyukta": ["saMyukte"], "tArya": ["tArya"], "tulya": ["tulya"], "prApya": ["prApya"], "vaDya": ["vaDya"], "AnAmya": ["AnAmya"],
        "sama": ["sama"], "samita": ["samita"], "sammita": ["sammitezu"], "anapeta": ["saMjYAyAmanapete"], "nirmita": ["nirmite", "nirmitaH"],
        "priya": ["priyaH"], "sADu": ["sADuH"], "vAsI": ["vAsI"], "Sayita": ["SayitaH"],
        # 5.1.5 – 17 (cha)
        "tasmEhita": ["hitam"], "prakfti": ["prakftO"], "syAt": ["syAt"],
        # 5.1.37
        "krIta": ["krItam"],
        # 5.1.38 – 63 (the other senses of the ārhīya group)
        "nimitta": ["nimittam", "nimittaM"], "Izvara": ["ISvaraH"], "vidita": ["viditaH"], "vApa": ["vApaH"], "vfdDyAdi": ["upadAH"],
        "bhArahAra": ["Avahati"], "samBavati": ["samBavati"], "avaharati": ["avaharati"], "pacati": ["pacati"],
        "aMSavasnaBfti": ["aMSa", "vasna", "BftayaH"], "tadasyaparimARam": ["parimARam"], "arhati": ["arhati"],
        # 5.1.72 – 94 (the ṭhañ group: what he does, where he goes, and the kāla senses)
        "vartayati": ["vartayati"], "saMSayApanna": ["saMSayamApannaH"], "yojanagacCati": ["yojanam"], "gacCati": ["gacCati"], "uttarapaTa": ["Ahftam"],
        "kAlanirvftta": ["nirvfttam"], "kAlAdhIzwa": ["tamaDIzwaH"], "kAlaBfta": ["BftaH"], "kAlaBUta": ["BUtaH"], "kAlaBAvI": ["BAvI"],
        "kAlaparijayya": ["parijayya"], "kAlalaBya": ["laBya"], "kAlakArya": ["kArya"], "kAlasukara": ["sukaram"], "kAlabrahmacarya": ["brahmacaryam"],
        # 5.1.95 – 112 (dakṣiṇā, bhava-vat, sampādin, prabhavati, prāpta, prayojana)
        "dakziRA": ["dakziRA"], "kAladIyate": ["dIyate"], "kAlatatrakArya": ["kAryam"], "tenadIyate": ["dIyate"], "tenakArya": ["kAryam"],
        "sampAdin": ["sampAdini"], "tasmaiPraBavati": ["praBavati"], "prApta": ["prAptam"], "prakfzwa": ["prakfzwe"], "prayojana": ["prayojanam"],
        # 5.2.1 – 45 (agent A)
        "kzetra": ["kzetre"], "sarvacarmakfta": ["kftaH"], "darSana": ["darSanaH"], "vyApnoti": ["vyApnoti"], "prApnoti": ["prApnoti"],
        "baddhA": ["badDA"], "Bakzayati": ["Bakzayati"], "neya": ["neyezu"], "anuBavati": ["putrapOtramanuBavati"], "gAmI": ["gAmI"], "alaMgAmI": ["alaNgAmI"],
        "BUtapUrva": ["BUtapUrve"], "ekAhagama": ["ekAhagamaH"], "vrAtajIvati": ["jIvati"], "pAka": ["pAka"], "mUla": ["mUle"], "vitta": ["vittaH"],
        "karmaGawa": ["GawaH"], "saMjAta": ["saMjAtam"], "pramANa": ["pramARe"], "parimARa": ["parimARe"], "saMKyAparimARa": ["saNKyAparimARe"],
        "saMKyAvayava": ["avayave"], "aDika": ["aDikam"],
        # 5.2.46 – 88 (agent B)
        "tadasminnaDika": ["aDikam"], "guRanimAna": ["nimAne"], "tasyapUraRa": ["pUraRe"], "matvartha": ["matvarTayoH", "matau", "matO"], "kuSala": ["kuSalaH"],
        "kAma": ["kAme"], "prasita": ["prasite"], "parijAta": ["parijAtaH"], "aMSaMhArI": ["hArI"], "acirApahfta": ["apahfte"], "kAriRi": ["kAriRi"],
        "anvicCati": ["anvicCati", "daRqAjinAByAmanvicCati"], "grahaRa": ["grahaRam"], "grAmaRI": ["grAmaRIH"], "bandhana": ["banDanamasya"],
        "annaprAya": ["prAye"], "SrAddhaBukta": ["Buktam"], "anena": ["anena"],
        # 5.4.68: the samāsānta frame (the speaker forms a compound)
        "samAsAnta": ["samAsAntAH"],
        # 5.2.94 – 140 (agent C)
        "astyasya": ["astIti"],
        # 5.4.3 – 67 (agent G)
        "prakAravacana": ["prakAravacane"], "anatyantagati": ["anatyantagatO"], "AcCAdana": ["AcCAdane"], "banDu": ["banDuni"], "sasTAna": ["sasTAnena"],
        "matsya": ["matsye"], "kriyAaByAvftti": ["aByAvfttigaRane"], "prakfta": ["prakftavacane"], "tAdarTya": ["tAdarTye", "tAdaraTye"], "maRi": ["maRO"],
        "varRa": ["varRe"], "vyAhftArTA": ["arTAyAm"], "dvitIyAsaptamI": ["saptamyoH"], "kfzi": ["kfzO"],
        "yApanA": ["yApanAyAm"], "ativyaTana": ["ativyaTane"], "nizkozaRa": ["nizkozaRe"], "Anulomya": ["Anulomye"], "prAtilomya": ["prAtilomye"],
        "pAkaviSaya": ["pAke"], "aSapaTa": ["aSapaTe"], "parivApaRa": ["parivApaRe"],
        # 5.3.1 – 60 (agent E)
        "paYcamIvib": ["paYcamyAH"], "saptamIvib": ["saptamyAH"], "kAle": ["kAle"],
        "viDArTa": ["viDArTe"], "aDikaraRavicAla": ["aDikaraRavicAle"], "yApya": ["yApye"], "BAga": ["BAge"], "asahAya": ["asahAye"], "atiSAyana": ["atiSAyane"], "dik": ["dig"],
        # 5.3.61 – 110 (agent F)
        "praSaMsA": ["praSaMsAyAm"], "IzadasamApti": ["asamAptO"], "prakAra": ["prakAravacane"], "ajYAta": ["ajYAte"], "kutsita": ["kutsite"],
        "anukampA": ["anukampAyAm"], "nIti": ["nItO"], "alpa": ["alpe"], "hrasva": ["hrasve"], "nirDAraRadvaya": ["dvayoH"], "nirDAraRabahu": ["bahUnAm"],
        "avakzepaRa": ["avakzepaRe"], "iva": ["ive"],
        # 5.4.68 ff (agent H)
        "samAsAnta": ["samAsAntAH"]},
    "arthaViSeSa": {"aviSeza": ["aviSeze"], "garhya": ["garhyam", "garhyAt"], "saMjYA": ["saMjYAyAm", "asaMjYAyAm", "saMjYA", "saMjYAyAM", "saMjYayoH"], "brAhmaRasaMjYA": ["brAhmaRe"], "vayas": ["vayasi"], "avayas": ["avayasi"], "cittavat": ["cittavati"],
                      "manTa": ["manTa"], "daRqa": ["daRqayoH", "daRqa"], "anadyatana": ["anadyatane"], "dvivacanavibhajya": ["upapade"],
                      # 5.2 (agents B, C)
                      "sUkta": ["sUktasAmnoH"], "sAman": ["sUktasAmnoH"], "aDyAya": ["aDyAya"], "anuvAka": ["anuvAkayoH"], "AdyUna": ["Adyune"], "karaBa": ["karaBe"],
                      "kAma": ["kAma"], "bala": ["bale"], "deSa": ["deSe"], "unnata": ["unnataH"], "Ahata": ["Ahata"], "praSaMsA": ["praSaMsayoH", "praSaMsAyAm"],
                      "bahuBAzin": ["bahuBAziRi"], "dvandva": ["dvandva"], "upatApa": ["upatApa"], "jAti": ["jAtO", "jAti"], "brahmacAri": ["brahmacAriRi"],
                      # 5.4.104 – 157 (agent H)
                      "samavAya": ["samavAye"], "lavana": ["lavane"], "hiMsA": ["hiMsAyAm"],
                      "jAnapadAKyA": ["jAnapadAKyAyAm"], "dAru": ["dAruRi"], "karmavyatihAra": ["karmavyatihAre"], "vandita": ["vandite"],
                      "aviprakfzwakAla": ["aviprakfzwakAle"], "anitya": ["anitye"], "ajAti": ["ajAtO"], "vIpsA": ["vIpsAyAm"], "vyavasarga": ["vyavasargayoH"],
                      "tanutva": ["tanutve"], "prAcAm": ["prAcAm"], "jAtiparipraSna": ["jAtiparipraSne"], "pratikfti": ["pratikftO"]},
    # 5.3.98 – 99: who or what is meant when the kan is taken away (lup)
    "abhiDeya": {"manuzya": ["manuzye"], "apaRya": ["apaRye"]},
    # 4.1.65 – 66: the stem names a human tribe / class (manuzya-jAteH): ūṅ after u-final (kuru → kurūḥ)
    "jAtiBeda": {"manuzyajAti": ["jAteH"]},
    # 1.1.35: sva as a kinsman or wealth is not a sarvanāma (svam ajñātidhanākhyāyām) · 1.1.36: antara of an outside / an inner garment is
    "svaBeda": {"jYAti": ["svamajYAtiDanAKyAyAmasaMjYAyAm"], "Dana": ["svamajYAtiDanAKyAyAmasaMjYAyAm"]},       # the samagra of 1.1.35 is one run-together word
    "antaraBeda": {"bahiryoga": ["bahiryoga"], "upasaMvyAna": ["upasaMvyAnayoH"]},
    # 1.4.24 / 42 / 49 / 51: the role the speaker gives the noun in the sentence (kārakāṇi vivakṣātaḥ): the fixed point of a separation,
    # the most effective means, what the agent most wishes to reach, what is not otherwise said
    "kArakaArTa": {"apAya": ["apAye"], "sADakatama": ["sADakatamam"], "Ipsitatama": ["Ipsitatamam"], "akaTita": ["akaTitam"]},
    "jIvikArTa": {"jIvikArTa": ["jIvikArTe"]},
    # 5.1.64 / 5.1.89: the pratyaya for what is always so (niyatam, nityam)
    "nityatA": {"nitya": ["nityam", "nityamarhati"]},
    # 7.3.16: the sense is not the future (bhāvī): the speaker says so
    "bhavizyat": {"aBavizyat": ["aBavizyati"]},
    # 4.3.3: the yuṣmad / asmad that speaks of one person
    "ekavacana": {"ekavacana": ["ekavacane"]},
    # inside the vikāra group (4.3.134 – 168): which vikāra the speaker means
    "vikAraBeda": {"purIza": ["purIze"], "saMjYA": ["saMjYAyAm"], "puroqASa": ["puroqASe"], "parimARa": ["parimARe"], "mAna": ["mAne"], "Pala": ["Pale"]},
    "apatyaBeda": {"gotra": ["gotre", "gotrApatye"], "yuvan": ["yuni"]},
    "tAcCIlya": {"tAcCIlya": ["tAcCIlye"]}, "AtmamAna": {"AtmamAna": ["AtmamAne"]},
    # ashtadhyayi.com spells the 3.4.21 pada कर्त्तृ (samAnakarttfkayoH); 3.1.7 and 3.3.158 have one t
    "samAnakartfka": {"samAnakartfka": ["samAnakarttfkayoH", "samAnakartfkezu", "samAnakartfkAt"]},
    # the sanādi senses: 3.1.7 san / 3.1.8 kyac / 3.1.9 kāmyac — the wish (icCAyAm); 3.1.26 ṇic — the prompting agent (hetumati)
    "icCA": {"icCA": ["icCAyAM"]}, "hetumat": {"hetumat": ["hetumati"]},
    # AMENDMENT 30 pilot, the pada sūtras 1.3.47 – 50, 1.3.66 (each word is the sūtra's own; Kāśikā 1.3.47 – 50, 66 glosses them)
    # 1.3.47: the six senses in which vad takes ātmanepada
    "vadArTa": {"BAsana": ["BAsana"], "upasamBAzA": ["upasamBAzA"], "jYAna": ["jYAna"], "yatna": ["yatna"], "vimati": ["vimati"],
                "upamantraRa": ["upamantraRezu"]},
    # 1.3.48 – 50: facts of the sentence (context): the speakers are articulate-voiced beings, they speak together, they contradict one another
    "vyaktavAk": {"vyaktavAc": ["vyaktavAcAm", "vyaktavAcAM"]},
    "samuccAraRa": {"samuccAraRa": ["samuccAraRe"]},
    "vipralApa": {"vipralApa": ["vipralApe"]},
    # 1.3.49 akarmakāt: the verb is used with no object meant
    "karmakatva": {"akarmaka": ["akarmakAt"]},
    # 1.3.66: Buj of the rudhādi class in a sense other than protecting (the tudādi Buj, kauṭilya, is another root, told apart by its dhātu id)
    "BujArTa": {"anavana": ["anavane"]},
}

# AMENDMENT 30 rule 4: what each key is. kind: intent (the speaker's choice, explored or fixed) | context (a fact of the sentence or of the stem:
# supplied by the caller, never explored). default None = the unmarked value: the key is not set. applies_to: the entry points that may use it.
# requires: what the derivation must contain for the key to mean anything (informational). Glosses in Sanskrit and English.
_I, _C = "intent", "context"
KEY_META: dict[str, tuple] = {
    # key: (kind, applies_to, requires, gloss_dev, gloss_en)
    "artha": (_I, ["tinanta", "krdanta"], [], "कर्तृकर्मभावादिः प्रत्ययार्थः", "the sense a pratyaya is taught in: agent, object, action, instrument, locus"),
    "kala": (_I, ["tinanta", "krdanta"], [], "कालः (भूतः, वर्तमानः, भविष्यन्, पूर्वकालः)", "the time meant"),
    "kartrabhiprAya": (_I, ["tinanta"], ["Yit root (1.3.72) or Nic Term (1.3.74)"], "क्रियाफलं कर्तारं गच्छति", "the fruit of the act goes to the agent"),
    "krt": (_I, ["krdanta"], [], "कृत्य-ण्वुल्तृचोः विकल्पः", "which kṛt family (kṛtya, ṇvul/tṛc) the speaker takes"),
    "kriyArTA": (_I, ["krdanta"], [], "क्रियार्था क्रिया", "the act is for the sake of another act"),
    "samAnADikaraRa": (_C, ["krdanta"], [], "अप्रथमासमानाधिकरणम्", "the participle agrees with a noun not in the first case"),
    "sambodhana": (_I, ["krdanta"], [], "सम्बोधनम्", "address (vocative sense)"),
    "lakzaRahetu": (_I, ["krdanta"], [], "लक्षणं हेतुश्च", "mark or cause as the sense of śatṛ/śānac"),
    "tAcCIlyAdi": (_I, ["krdanta"], [], "ताच्छील्यवयोवचनशक्तिषु", "habit, age, capability"),
    "akfcCra": (_I, ["krdanta"], [], "अकृच्छ्रम्", "without difficulty"),
    "amitra": (_I, ["krdanta"], [], "अमित्रम्", "enemy as object"),
    "yajYasaMyoga": (_I, ["krdanta"], [], "यज्ञसंयोगः", "connection with a sacrifice"),
    "praSaMsA": (_I, ["krdanta", "taddhita"], [], "प्रशंसा", "praise"),
    "hetutAcCIlyAnulomya": (_I, ["krdanta"], [], "हेतुताच्छील्यानुलोम्यानि", "cause, habit, compliance"),
    "linga": (_C, ["krdanta", "subanta"], [], "लिङ्गम्", "the gender of the word"),
    "taddhitArtha": (_I, ["taddhita"], [], "तद्धितार्थः", "the sense a taddhita pratyaya is taught in"),
    "arthaViSeSa": (_I, ["taddhita"], [], "अर्थविशेषः", "a particular sense inside a taddhita frame"),
    "abhiDeya": (_C, ["taddhita"], [], "अभिधेयम्", "what the word names (human, not-for-sale)"),
    "jAtiBeda": (_C, ["subanta"], [], "मनुष्यजातिः", "the stem names a human tribe"),
    "svaBeda": (_C, ["subanta"], [], "स्वशब्दस्य ज्ञातिधनार्थत्वम्", "sva as kinsman or wealth"),
    "antaraBeda": (_C, ["subanta"], [], "अन्तरशब्दस्य बहिर्योगोपसंव्यानार्थत्वम्", "antara as outside or inner garment"),
    "kArakaArTa": (_I, ["subanta", "samasa"], [], "कारकविवक्षा", "the role the speaker gives the noun"),
    "jIvikArTa": (_I, ["taddhita"], [], "जीविकार्थः", "livelihood sense"),
    "nityatA": (_I, ["taddhita"], [], "नित्यत्वम्", "what is always so"),
    "bhavizyat": (_C, ["taddhita"], [], "अभविष्यत्", "the sense is not the future"),
    "ekavacana": (_C, ["taddhita"], [], "एकवचनम्", "yuṣmad/asmad speaks of one person"),
    "vikAraBeda": (_I, ["taddhita"], [], "विकारविशेषः", "which modification the speaker means"),
    "apatyaBeda": (_I, ["taddhita"], [], "गोत्रं युवा वा", "descendant: gotra or yuvan"),
    "tAcCIlya": (_I, ["krdanta"], [], "ताच्छील्यम्", "habitual agent"),
    "AtmamAna": (_C, ["krdanta"], [], "आत्ममानः", "the agent is self-regarded"),
    "samAnakartfka": (_C, ["krdanta"], [], "समानकर्तृकत्वम्", "the two acts share one agent"),
    "icCA": (_I, ["tinanta", "krdanta"], [], "इच्छा", "wish (san)"),
    "hetumat": (_I, ["tinanta", "krdanta"], [], "हेतुमान्", "the prompting agent (ṇic)"),
    "vadArTa": (_I, ["tinanta", "krdanta"], ["dhātu vad"], "भासनादिषु वदः", "the sense of vad: shining, addressing, knowing, effort, dissent, inviting"),
    "vyaktavAk": (_C, ["tinanta"], ["dhātu vad"], "व्यक्तवाचः कर्तारः", "the speakers have articulate speech"),
    "samuccAraRa": (_C, ["tinanta"], ["dhātu vad"], "सहोच्चारणम्", "they speak together"),
    "vipralApa": (_C, ["tinanta"], ["dhātu vad"], "विप्रलापः", "they speak contradicting one another"),
    "karmakatva": (_C, ["tinanta"], ["dhātu vad", "upasarga anu"], "अकर्मकत्वम्", "the verb is used with no object meant"),
    "BujArTa": (_I, ["tinanta"], ["dhātu Buj of the rudhādi class (07.0017)"], "भुजोऽनवने", "Buj in a sense other than protecting"),
}
# AMENDMENT 27 allow-list: sūtras that may ask taddhitArtha=svArTa (Kāśikā: "svārthe"); extend only with the Kāśikā line cited in the sūtra's file
SVARTHIKA = ["5.1.58", "5.4.7", "5.4.8", "5.4.13", "5.4.14", "5.4.15", "5.4.23", "5.4.27", "5.4.28", "5.4.29", "5.4.34", "5.4.38", "5.4.39"]
_SPLIT = re.compile(r"[\s\-,.;:|।॥()'\"]+")


def build() -> dict:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    words = {sid: set(_SPLIT.split(getattr(rec, "samagra_slp1", "") or "")) for sid, rec in SUTRA_REGISTRY.items()}
    order = lambda s: tuple(map(int, s.split(".")))
    schema: dict = {"_doc": __doc__.strip().splitlines()[0], "source": "samagra_slp1 of the sūtra records (ashtadhyayi.com)",
                    "keys": {}}
    for key, values in VOCABULARY.items():
        schema["keys"][key] = {}
        for value, forms in values.items():
            cited = sorted((sid for sid, w in words.items() if w & set(forms)), key=order)
            if not cited:
                raise SystemExit(f"{key}={value}: none of {forms} occurs in any samagra — refused")
            schema["keys"][key][value] = {"forms": forms, "sutras": cited}
    # AMENDMENT 27: the svārthika sūtras name no sense; the Kāśikā (5.3.1, "svārthe") supplies it. One value, an explicit allow-list, a Kāśikā citation.
    schema["keys"].setdefault("taddhitArtha", {})["svArTa"] = {"forms": ["svArTe"], "sutras": sorted(SVARTHIKA, key=order), "kashika": "5.3.1"}
    missing = set(schema["keys"]) - set(KEY_META)
    if missing:
        raise SystemExit(f"keys without KEY_META: {sorted(missing)}")
    schema["meta"] = {k: {"kind": kind, "default": None, "applies_to": applies, "requires": requires, "gloss_dev": gd, "gloss_en": ge}
                      for k, (kind, applies, requires, gd, ge) in KEY_META.items() if k in schema["keys"]}
    return schema


def main() -> int:
    schema = build()
    OUT.write_text(json.dumps(schema, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for key, values in schema["keys"].items():
        print(key, {v: len(d["sutras"]) for v, d in values.items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
