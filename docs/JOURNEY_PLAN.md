# यात्रा · Śabda journey — status (UI: `webui/static/journey.js`, hidden panel, ◆ teaching aid)

Reads the engine's own trace only. Authority: Kāśikā 1.2.45, 1.2.46, 1.2.64, 2.4.71, 3.1.8, 4.1.1, 4.1.82, 8.4.56.
Rule: a stem + its sup is what enters samāsa / nāmadhātu / taddhita (sup dropped by 2.4.71); only kṛt enters at the very start. Ekaśeṣa (1.2.64) is a vṛtti merging subantas, not a stem source. Strī-pratyaya is a loop at the stem stage (4.1.1).

| Branch | Status | Next |
|---|---|---|
| अव्युत्पन्न (1.2.45) | ✔ | — |
| कृदन्त ← धातु+कृत् | ◐ tṛc/ṇvul pipelines | link journey to `pipelines/krdanta.py`; per-stem origin record |
| तद्धितान्त | ◐ example pipelines | per-stem origin record |
| समास | ◐ dvandva/bahuvrīhi examples | members as sub-journeys |
| नामधातु / सनाद्यन्त | ◐ san/ṇic examples | nāmadhātu (3.1.8) |
| स्त्री-प्रत्यय loop | ⌛ | link 4.1.4/4.1.5 pipelines |
| एकशेष | ⌛ | after samāsa members |
| end forks (vā/vibhāṣā) | shown; other branch not run to its end | replay `State.fork` |

Open: per-stem origin classification (9,007 stems) — hand/corpus-tag, never guessed. Engine fork record names 8.4.47 for rāmāt/rāmād; the UI shows the applied VIBHASHA row (8.4.56) instead — check the record.
