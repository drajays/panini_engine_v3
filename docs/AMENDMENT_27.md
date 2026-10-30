# AMENDMENT 27 — `taddhitArtha=svArTa`: the svārthika pratyayas (accepted by the owner 2026-10-30)

**Status:** accepted: *"amendment accepted and go ahead"* (owner, 2026-10-30), after the proposal in the session of that date. Source of authority: the Kāśikā, not a sūtra word — see below. Touches Amendment 25's law "a sūtra may ask only for a vivakṣā value whose form occurs in its own samagra".

## Problem
A svārthika sūtra (5.4.7 `azaqakzASitaNgvalaMkarmAlampuruzADyuttarapadAt KaH`, 5.4.8, 13 – 15, 23, 27 – 29, 34, 38, 39; 5.1.58) names no sense; the Kāśikā supplies "svārthe". Under Amendment 25 such a sūtra has no value it may ask for, hence no gate; ungated it would fire in every taddhita derivation and add readings to unrelated words.

## Authority (checked in `ashtadhyayi.db`, table `texts`, source `kashika`)
- Kāśikā 5.3.1: *ataḥ paraṃ svārthikāḥ pratyayāḥ, teṣu samarthādhikāraḥ prathamagrahaṇaṃ ca … nivṛttam; vāvacanaṃ tu vartata eva* — the svārthika pratyayas need no samartha-vibhakti and no prathamāt; the optional `vā` (4.1.82) continues.
- `sutras.adhikara` of these sūtras in the database lists only `tadditāḥ 4.1.76` and `vā 4.1.82` — consistent.
- Kāśikā 5.4.7: *… ādibhyaḥ svārthe khaḥ pratyayo bhavati.*

## Rule
1. One new value `taddhitArtha=svArTa` ("the speaker means the plain word, adding no new sense"). Its schema entry carries `"kashika": "5.3.1"` and, as `sutras`, the allow-list of svārthika sūtras (`SVARTHIKA` in `tools/build_vivaksha_schema.py`).
2. The constitutional test accepts a `vivaksita(state, "taddhitArtha", "svArTa")` call only inside a sūtra on that allow-list, and a listed sūtra asks for no other value; every other sūtra keeps Amendment 25 unchanged. The "named by the sūtras they cite" test skips entries that carry `kashika`.
3. In the loop a svārthika sūtra gates on `svArTa`, applies its own stem condition, needs no samartha-vibhakti and no sense frame, and attaches as a `vā` reading: both branches are explored (the pratyaya, and the plain stem stays).
4. Adding a sūtra to the allow-list needs the Kāśikā line saying "svārthe" (or the 5.3.1 passage) cited in its file; nothing else.

## Not changed
Every non-svārthika sūtra; the closed vocabulary; the rule that the engine never infers a value.
