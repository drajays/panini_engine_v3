"""
4.1.92  तस्यापत्यम्  —  ADHIKARA (artha-nirdeśa with forward adhikāra force)

Sources consulted:
- ashtadhyayi.com data.txt row i=41092 (type ``AD`` "प्राग्दीव्यतीयः शेषाधिकारः",
  end 43120 — site taxonomy; superseded on scope by the vṛttis below, see
  docs/SOURCE_CONFLICTS.md SC-001)
- Kāśikā: "अर्थनिर्देशोऽयम्, पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते। तस्येति
  षष्ठीसमर्थादपत्यमित्येतस्मिन्नर्थे यथाविहितं प्रत्ययो भवति। … उपगोरपत्यमौपगवः।
  आश्वपतः। दैत्यः। औत्सः। स्त्रैणः। पौंस्नः।"
- Nyāsa: "पूर्वैस्तावदणादिभिः सम्बध्यते; असंयुक्तविधानात्। … उत्तरैरप्यभिसम्बध्यते;
  तेष्वस्य स्वरितत्वात्।"  Padamañjarī: "उतरैरपि सम्बध्यते;
  स्वरितत्वात्साकांक्षत्वाच्च तेषाम्।"  Mahābhāṣya: "अवश्यमुत्तरार्थमर्थनिर्देशः कर्तव्यः।"
- Bhaṭṭoji's Kaumudī, cross-reference only (Art. 3): "षष्ठ्यन्तात्कृतसन्धेः समर्थादपत्येऽर्थे
  उक्ता वक्ष्यमाणाश्च प्रत्यया वा स्युः।"
- Cross-validation: regression tests tests/unit/test_dASaraThi_apatya_iY.py
  (दाशरथिः, 4.1.95 under this frame) and the औपगवः recipe
  (pipelines/aupagu_apatya_aupAgava.py, 4.1.83 aṇ in the apatya sense).

Not a pure adhikāra: it assigns the meaning *apatya* (with ṣaṣṭhī-samartha
prakṛti) to the affixes already taught (pūrvaiḥ — aṇ etc. of 4.1.83–4.1.91,
shown by the separate yoga, else Pāṇini would read "तस्यापत्यमत इञ्") **and**,
being svarita (1.3.11), to those taught after it (uttaraiḥ — 4.1.95 ff.).
Ruling (Ajay, 2026-10-01; Constitution Art. 20): an ``ArthaNirdesha`` on an
ADHIKARA record. The frame it opens covers 4.1.83 (aṇ, the first pūrva affix —
Nyāsa "अणादिभिः") through 4.1.178 (end of the apatya section) and carries the
meaning ``apatya``; recipes apply 4.1.92 before attaching the affix.

cond: the frame is not already open. act: push the 4.1.92 frame.
"""
from __future__ import annotations

from engine       import ArthaNirdesha, SutraType, SutraRecord, register_sutra
from engine.state import State

ARTHA = ArthaNirdesha(
    artha      = "apatya",
    artha_dev  = "अपत्यम्",
    purva_from = "4.1.83",
    source     = "अर्थनिर्देशोऽयम्, पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते।",
)
SCOPE_END = "4.1.178"


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.92" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"          : "4.1.92",
        "scope_start" : ARTHA.purva_from,
        "scope_end"   : SCOPE_END,
        "artha"       : ARTHA.artha,
        "text_dev"    : 'तस्यापत्यम्',
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.92",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = 'tasyApatyam',
    text_dev       = 'तस्यापत्यम्',
    samagra_slp1   = "tasya apatyam iti samarTAnAm praTamAt paraH aR pratyayaH",
    samagra_dev    = "'तस्य अपत्यम्' (इति) समर्थानाम् प्रथमात् परः अण् प्रत्ययः",
    padaccheda_dev = "तस्य / अपत्यम्",
    why_dev        = "अर्थनिर्देशः — पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते; स्वरितत्वादपत्याधिकारः ४.१.९२ तः ४.१.१७८ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.92", SCOPE_END),
    artha_nirdesha = ARTHA,
)

register_sutra(SUTRA)
