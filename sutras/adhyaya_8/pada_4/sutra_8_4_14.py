"""
8.4.14  उपसर्गादसमासेऽपि णोपदेशस्य  —  VIDHI

Padaccheda: उपसर्गात् अ-समासे अपि ण-उपदेशस्य

Sources consulted:
- ashtadhyayi.com data.txt row i=84014 (samagra: पूर्वपदात् उपसर्गात् रषाभ्याम् ण-उपदेशस्य नः णः, असमासेऽपि)
- Kāśikā: "णोपदेशस्य धातोर्यो नकारः तस्य उपसर्गस्थाद् निमित्तादुत्तरस्य णकारादेशो भवत्यसमासेऽपि समासेऽपि। प्रणमति। परिणमति।
  प्रणायकः। परिणायकः।"
  pratyudāharaṇa: "उपसर्गादिति किम्? … प्रनायको देशः। … णोपदेशस्येति किम्? प्रनर्दति। प्रनर्दकः॥"
- Cross-validation: LK cases tests/fixtures/lk_cases/a8.json (8.4.14: praRamati, pariRamati; negative namati).

The n of a dhātu taught with ṇ in the dhātupāṭha (its aupadeśika form begins with R: Rama~, RIY) becomes ṇ when an r / ṣ of an
upasarga precedes it, across the vyavāya 8.4.2 allows. The upasarga | dhātu seam is not samānapada, so 8.4.1 / 8.4.2 stop at it;
a dhātu taught with n (nard → प्रनर्दति) keeps its n.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.natva import dhatu_upadesha, flat, upasarga_nimitta_before
from engine.state import State
from phonology    import mk


def _site(state: State):
    if not state.tripadi_zone or not dhatu_upadesha(state).startswith("R"):
        return None
    tape = flat(state)
    for k, (t, i, v) in enumerate(tape):
        if "dhatu_v" in v.tags and "abhyasa_v" not in v.tags:      # the dhātu's first varṇa
            if v.slp1 == "n" and "natva_done" not in v.tags and upasarga_nimitta_before(tape, k):
                return t, i
            return None
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, i = _site(state)
    new = mk("R")
    new.tags |= t.varnas[i].tags | {"natva_done"}
    t.varnas[i] = new
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.14",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'upasargAdasamAsepi RopadeSasya',
    text_dev              = 'उपसर्गादसमासेऽपि णोपदेशस्य',
    samagra_slp1          = "pUrvapadAt upasargAt razAByAm Ra-upadeSasya naH RaH asamAsepi",
    samagra_dev           = "पूर्वपदात् उपसर्गात् रषाभ्याम् ण-उपदेशस्य नः णः, असमासेऽपि",
    padaccheda_dev        = "उपसर्गात् अ-समासे अपि ण-उपदेशस्य",
    why_dev               = "(सूत्रम् 8.4.14) उपसर्गस्थाद् निमित्तात् णोपदेशस्य धातोः नस्य णः — प्रणमति, परिणमति।",
    anuvritti_from        = ('8.4.1', '8.4.2', '8.4.3'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
