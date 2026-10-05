"""
6.4.19  च्छ्वोः शूडनुनासिके च  —  VIDHI

For धातु प्रच्छ् (upadeśa praCa~ — a single छ्, no separate च्; the familiar
written "प्रच्छ्" is itself तुक् (6.1.73) + श्चुत्व (8.4.40), already applied),
replace the final छ् — together with any तुक् त् immediately before it — by
श्. Kāśikā: "अन्तरङ्गत्वात् इति तुकि कृते सतुक्कस्य शादेशः" — तुक् (antaraṅga,
so it fires first) inserts त् before छ्; 6.4.19's शादेश then replaces that
whole [त्, छ्] pair (सतुक्कस्य = "of छ् together with its तुक्"), not छ् alone.

Two call sites, two aṅga states:
  - क्त्वा/क्नु (कित्/ङित् affixes; प्रश्नः, पृष्ट्वा/प्रष्ट्वा): called before
    तुक् has been through श्चुत्व, so the dhātu still ends bare-छ् or तुक्+छ्.
  - लृट्/लुट्/लुङ् (स्य/तास्/सिच्, आर्धधातुक — प्रक्ष्यति, प्रष्टा, अप्राक्षीत्):
    same aṅga shape (तुक्+छ् at the end); called from each lakāra's own
    pipeline right before the Tripādī merge, mirroring how 7.3.93 (ब्रुव ईट्)
    is scoped per-lakāra rather than gated by a shared affix tag.
  Not called at all from सार्वधातुक (शप्) lakāras (लट्/लिट्/लोट्/लङ्) — there
  तुक्+छ् survives to 8.4.40 श्चुत्व instead, giving पृच्छति.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64019 · च्छ्वोः शूडनुनासिके च
              padaccheda: च्छ्-वोः श्-ऊठ् अनुनासिके च
              anuvṛtti:   64001: अङ्गस्य | 64015: क्विझलोः क्ङिति
  Source #2 — Kāśikā 6.4.19 udāharaṇa:
                प्रश्नः
                विश्नः
                अन्तरङ्गत्वाच्    इति तुकि कृते सतुक्कस्य शादेशः
  Cross-check — surface pinned by: tests/unit/test_pfzwvA_pracch_ktvA.py;
                dhātu 06.0149 lṛṭ/luṭ/luṅ vs ashtadhyayi.com (प्रक्ष्यति/प्रष्टा/अप्राक्षीत्)
  Reference record: sutra_ref_out/6_4_19.json
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_ROOT_UPADESHAS = frozenset({"praCa", "pfcC"})


_JHAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmSzsh")   # every consonant but the sonorants y r l v


def _liT_not_kvi_jhal_kngiti(state: State) -> bool:
    """क्विझलोः क्ङिति (6.4.15, anuvṛtti): in liṭ the chv-śūṭ stands only before a jhal-initial kit/ṅit ending — not before
    the vowel-initial ṇal/atus/us (पप्रच्छ, पप्रच्छतुः). (The lṛṭ/luṭ/luṅ recipes still call this sūtra for the tuk.)"""
    if len(state.terms) < 2:
        return False
    nxt = state.terms[1]
    if (nxt.meta.get("source_lakara_upadesha") or "").strip() != "liT" or not nxt.varnas:
        return False
    return not ("kngiti" in nxt.tags and nxt.varnas[0].slp1 in _JHAL)


def _site(state: State):
    """(dhātu_term, cut_index) for a trailing [c|t, C] pair on the प्रच्छ् root."""
    if not state.terms:
        return None
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return None
    if (dh.meta.get("upadesha_slp1") or "").strip().rstrip("~") not in _ROOT_UPADESHAS:
        return None
    if dh.meta.get("6_4_19_cch_to_sh_done"):
        return None
    vs = dh.varnas
    if len(vs) < 2 or vs[-1].slp1 != "C" or vs[-2].slp1 not in ("c", "t"):
        return None
    if _liT_not_kvi_jhal_kngiti(state):
        return None
    return dh, len(vs) - 2


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is None:
        return state
    dh, cut = hit
    # Replace the trailing [c|t, C] pair — छ् and any तुक् त् before it — by श्,
    # carrying over छ्'s own dhātु-varṇa tags (else the Tripāḍī tape-scanner
    # in sutras/adhyaya_8/pada_2/_tape.py stops treating this letter as part
    # of the dhātु, per the same convention as that module's substitute()).
    new_S = mk("S")
    old_tags = dh.varnas[-1].tags & {"dhatu_v", "mula_dhatu_v", "dhatu_adesha_v"}
    if old_tags:
        new_S.tags |= old_tags | {"dhatu_adesha_v"}
    dh.varnas = dh.varnas[:cut] + [new_S]
    dh.meta["6_4_19_cch_to_sh_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.19",
    sutra_type=SutraType.VIDHI,
    text_slp1='cCvoH SUqanunAsike ca',
    text_dev='च्छ्वोः शूडनुनासिके च',
    padaccheda_dev="च्छ्वोः / शूड् / अनुनासिके / च",
    why_dev="क्ङिति परे (पृच्छ्) अन्त्य-च्छ् → श् (पृष्ट्वा-पूर्वम्)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

