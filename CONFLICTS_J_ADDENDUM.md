# Addendum to `CONFLICTS_J_RESOLUTION.md`: verified parts of the external dossier

This adds the verified parts of an external dossier, written in another session
(`/home/user/PANINI_ENGINE_V3_CONFLICT_RESOLUTION_2026-10-06.md`). That file is not on this Mac, so only
the claims quoted in its summary could be checked. Every quotation kept here was checked against
`~/data-master` (your local ashtadhyayi.com checkout). Read-only: no repo file was changed.

## 1. What to discard

| claim in the dossier | check | verdict |
|---|---|---|
| "recipe == loop on all 1071 cells; the loop is not a second opinion" | `docs/RECHECK_2026-10-06.txt`: **398 of 761 rows have recipe ≠ loop** | **False for this checkout.** It probably ran an older or different tree. Do not act on it. |
| "अङि नलोपः । अस्रसत् । अस्रंसिष्ट" is **gaṇapāṭha** | found only in **SK** (key 73082, under स्रंसु/ध्वंसु/भ्रंसु) | the quote is genuine but the source label is wrong. Cite it as SK. |
| "PŚ numbering in KV 6.1.102 is off by one" | not checked | harmless. The rule "cite paribhāṣās by text, not number" is good practice anyway. |

## 2. Verified doctrine for ordering (vipratiṣedha). This part is useful.

These quotations are verbatim from `~/data-master`. Together they give the resolver a source for each
of its precedence rules (Art. 21).

| # | principle | source (verbatim) | consequence for the engine |
|---|---|---|---|
| 1 | Paratva applies only between rules of **equal** strength | KV 1.4.2: "तुल्यबलविरोधो विप्रतिषेधः … तस्मिन् विप्रतिषेधे परं कार्यं भवति। **उत्सर्गापवादनित्यानित्यान्तरङ्गबहिरङ्गेषु तुल्यबलता नास्तीति नायमस्य योगस्य विषयः।** बलवतैव तत्र भवितव्यम्" | Check apavāda, nitya and antaraṅga **first**. Use para only when none of them decides. Example: 7.3.72 over 7.2.81 in अधुक्षाताम् is a para decision because neither is apavāda of the other. |
| 2 | A rule set aside once stays set aside… | KV 6.4.101: "परत्वात् तातङि कृते **<<सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितमेव>>** इति पुनर्धिभावो न भवति" (also PŚ 40) | `blocked_sutras` must record *which conflict* blocked the rule, keyed to its nimitta. |
| 3 | …unless the conflict itself has gone | same KV: "भिन्द्धकि छिन्द्धकीत्यत्र परत्वाद् धिभावे कृते **<<पुनः प्रसङ्गविज्ञानाद्>>** अकच् क्रियते" | A blocked rule must be **releasable** when the blocking nimitta disappears. It must not be a permanent flag. |
| 4 | Apavāda status comes from **lack of scope** | Bhāṣya 7.4.55: "**अनवकाशा हि विधयो बाधका भवन्ति**" | Compute apavāda from the rules' own conditions (no room left for the special rule ⇒ it blocks). Do not hard-code it per pair. |
| 5 | Abhyāsa changes: the apavāda does not block the general rules | KV 7.4.66: "नर्नर्ति, नरिनर्ति, नरीनर्ति इत्येवमादौ **अभ्यासविकारेषु अपवादो न उत्सर्गान् विधीन् बाधते**" | Inside the abhyāsa block, let उरत् etc. run together with the general rules. This bears on the recipe's abhyāsa errors (स्मस्मर्थ, बद्ग्भ्रज्जे). |

## 3. Verified extra resolutions (not in the main file)

| cells | resolution | source (verbatim) |
|---|---|---|
| **द्युतँ luṅ parasmai** (Vidyut अद्योतीत्) | 1.3.91 द्युद्भ्यो लुङि makes parasmaipada optional in luṅ. In the parasmai branch 3.1.55 gives aṅ, so the form is **व्यद्युतत् / अद्युतत्** (engine right). The ātmane branch has sic: **अद्योतिष्ट**. | KV 1.3.91: "द्युतादिभ्यो लुङि वा परस्मैपदं भवति। **व्यद्युतत्, व्यद्योतिष्ट।**" |
| **मीञ् (9) / डुमिञ् (5)** liṭ, luṅ | 6.1.50: ā before an ej-producing ārdhadhātuka, so ममौ, ममिथ/ममाथ, अमासीत्, अमासिष्टाम् (Vidyut right; engine मिमाय, अमैष्टाम् wrong) | SK 3.1.81: "मीनातिमिनोति इत्येज्विषये आत्वम् । **ममौ । मिम्यतुः । ममिथ । ममाथ । मिम्ये । माता । मास्यति । मीयात् । मासीष्ट । अमासीत् । अमासिष्टाम् । अमास्त ।**" |
| **स्रंसु-type luṅ** | aṅ (द्युतादि, 3.1.55): the nasal is lost; with sic it is kept | SK 73082: "अङि नलोपः । **अस्रसत् । अस्रंसिष्ट ।** नास्रसत्करिणां ग्रैवमिति रघुकाव्ये" |
| **स्रन्भुँ liṭ ātmane** (loop सस्रभे) | not covered by the dossier. Same reason as रञ्ज् in the main file: a saṃयोग-final root's liṭ is not kit (1.2.5), so there is no 6.4.24. **सस्रम्भे** (Vidyut, recipe right) | KV 1.2.5: "असंयोगादिति किम्? **सस्रंसे। दध्वंसे।**" |
| **अद् liṭ** | 2.4.40 लिट्यन्यतरस्याम्: घसॢ optional, so **जघास / आद** | SK 2.4.40: "अदो घसॢ वा स्याल्लिटि । **जघास** … जक्षतुः … **आद । आदतुः**" |
| **कृष् luṅ** | vārttika: sic optional, so **अक्राक्षीत् / अकार्क्षीत् / अकृक्षत्** | KV 3.1.44 vārt.: "स्पृशमृशकृषतृपदृपां सिज् वा वक्तव्यः॥ अस्प्राक्षीत्, अस्पार्क्षीत्, अस्पृक्षत्"; SK 6.4.47 lists अक्राक्षीत् । अकार्क्षीत् । अकृक्षत् |

The last two belong in the vibhāṣā table (§8e) of the main file. With them, the engine should
return the set of forms, not one form.

## 4. Kept deliberately open (agree with the dossier)

- **शॄ (9) शीर्णाति (Vidyut):** the form occurs nowhere in KV, SK, Bālamanoramā or Bhāṣya in
  `~/data-master`. SK 7.4.12 has शृणीहि. **Do not patch toward Vidyut.**
- **भस् extra alternant अभासीत्:** the only hit is Bālamanoramā (key 73087). Leave open until the
  passage is read in full.

## 5. Bottom line

Use §2 as the resolver doctrine and §3 as extra fixed cells. The dossier's "recipe == loop" finding
does not match the current recheck, so do not plan around it.
