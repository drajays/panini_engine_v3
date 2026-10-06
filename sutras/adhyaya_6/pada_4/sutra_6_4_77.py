"""
6.4.77  अचि श्नुधातुभ्रुवां य्वोरियङुवङौ  —  VIDHI 

Glass-box scope for `loluv`:
  When a dhātu ends in ū (U) and an a-initial pratyaya follows, replace that U
  with the sequence "uv" (u + v).
Pāṭha: ashtadhyayi.com data.txt row i=64077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_AC = frozenset("aAiIuUfFxXeEoO")
_IYUV = {"i": "iy", "I": "iy", "u": "uv", "U": "uv"}


def _find(state: State):
    """A dhātu ending in इ/उ-varṇa before a vowel-initial pratyaya: इयङ्/उवङ्
    (नु+अ → नुव, प्रि+अ → प्रिय, लू+उस् …). 6.4.81 इणो यण् (the root इ) is excepted."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("6_4_77_uvang_done"):
            continue
        pr = state.terms[i + 1]
        if pr.kind != "pratyaya" or not pr.varnas or pr.varnas[0].slp1 not in _AC:
            continue
        if not dh.varnas or dh.varnas[-1].slp1 not in _IYUV:
            continue
        j = i + 1
        while j + 1 < len(state.terms) and "agama" in state.terms[j].tags:
            j += 1
        tin = state.terms[j]
        if ("tin_adesha_3_4_78" in tin.tags and "kngiti" not in tin.tags and not tin.meta.get("is_apit")
                and "ardhadhatuka" not in tin.tags and any(t.startswith("sarvadhatuka") for t in tin.tags)):
            continue                                   # a pit sārvadhātuka (āni, ni…) takes guṇa first: biBayAni, not *biBeyAni
        if len(dh.varnas) == 1 and dh.varnas[0].slp1 == "i":
            continue                                   # 6.4.81 इणो यण्
        if (not any("abhyasa" in u.tags for u in state.terms)
                and (any((u.meta.get("source_lakara_upadesha") or "").strip() == "liT" for u in state.terms)
                     or dh.meta.get("slu_replaced_sap"))):
            continue                                   # dvitva (6.1.8 / 6.1.10) comes first: jiGyatuH, not *jiGiyatuH
        # 6.4.82 एरनेकाचोऽसंयोगपूर्वस्य: an अनेकाच् aṅga (here: after its abhyāsa)
        # ending in इ-varṇa not after a conjunct takes yaṇ (निन्युः, निन्यिरे)
        if dh.varnas[-1].slp1 in "iI" and i > 0 and "abhyasa" in state.terms[i - 1].tags \
                and not (len(dh.varnas) >= 3 and dh.varnas[-2].slp1 not in _AC
                         and dh.varnas[-3].slp1 not in _AC):
            continue
        return i
    return None


def _snu_samyogapurva(state: State):
    """śnu after a conjunct (the root ends in a consonant: Sak+nu, āp+nu): uvaṅ, not yaṇ — Saknuvanti, āpnuvanti."""
    ts = state.terms
    for k in range(1, len(ts) - 1):
        nu, nxt = ts[k], ts[k + 1]
        if (nu.meta.get("upadesha_slp1") or "").strip() != "Snu" or [v.slp1 for v in nu.varnas] != ["n", "u"]:
            continue
        if nu.meta.get("6_4_77_uvang_done") or not nxt.varnas or nxt.varnas[0].slp1 not in _AC:
            continue
        j = k + 1
        while j + 1 < len(ts) and "agama" in ts[j].tags:
            j += 1
        if not ("kngiti" in ts[j].tags or ts[j].meta.get("is_apit")):      # Apnuvanti — but ApnavAni (pit): guṇa first
            continue
        prev = ts[k - 1].varnas
        if prev and prev[-1].slp1 not in _AC:            # a consonant before n: saṃyogapūrva
            return k
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _snu_samyogapurva(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        k = _snu_samyogapurva(state)
        if k is not None:
            state.terms[k].varnas.append(mk("v"))
            state.terms[k].meta["6_4_77_uvang_done"] = True
            state.terms[k].tags.discard("upadesha")
        return state
    dh = state.terms[i]
    a, b = _IYUV[dh.varnas[-1].slp1]
    dh.varnas[-1] = mk(a)
    dh.varnas.append(mk(b))
    dh.meta["6_4_77_uvang_done"] = True
    dh.tags.discard("upadesha")          # the new final v/y is no upadeśa-final (1.3.3 must not strip it)
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.77",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'aci SnuDAtuBruvAM yvoriyaNuvaNO',
    text_dev       = 'अचि श्नुधातुभ्रुवां य्वोरियङुवङौ',
    samagra_slp1   = "aci Snu-DAtu-BruvAm yvoH aNgasya iyaN uvaNO",
    samagra_dev    = "अचि श्नु-धातु-भ्रुवाम् य्वोः अङ्गस्य इयङ् उवङौ",
    padaccheda_dev = "अचि / श्नु-धातु-भ्रुवाम् / य्वोः / इयु-वङौ",
    why_dev        = "धातोः इवर्ण-उवर्णयोः अचि परे इयङ्-उवङौ (नुवति, म्रियते)।",
    anuvritti_from = ("6.4.1",),
    apavada_of            = ("6.1.77",),      # iyaṅ/uvaṅ for i/u-final aṅgas — the specific over iko yaṇ aci
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

