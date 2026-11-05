# Research papers: what to take, what to skip (2026-10-31, uncommitted)

Method: web search only (search snippets, no full-text reading of the papers). Anything marked [UNVERIFIED] rests on a
snippet, a secondary citation, or my memory. Read the paper before acting on it. Engine modules named below
(engine/resolver, scheduler, dispatcher) are from AGENTS.md; I did not re-read their code.
Laws respected: apply_rule only, no word recipes, Vidyut validator only (T10 floor, never an order to copy), Art. 22/23 authority.

## Papers (8)

1. Kiparsky, "On the Architecture of Pāṇini's Grammar" (2009, LNCS 5402 / SCL).
   https://link.springer.com/chapter/10.1007/978-3-642-00155-0_2
   Proposes: levels of representation, thematic roles, and rule ordering are motivated by compression (lāghava); conflict
   (vipratiṣedha) is resolved by a specificity (apavāda) principle with "param" only for residual cases.
   Verdict: best theory fit to our utsarga/apavāda + tripāḍī design. Take: its framing as the rationale for a
   "specificity before position" ordering in the resolver, and its case list as a conflict test corpus. No code.

2. Joshi & Kiparsky 1979 (Siddha and asiddha in Pāṇinian phonology) and Cardona 1970/1997 (Pāṇini: Structure & rule
   ordering; antaraṅga/nitya/apavāda, siddha/asiddha). [UNVERIFIED: no URL; cited second-hand in 1512.05670 and Rajpopat]
   Verdict: this is the classical source of the paribhāṣā ranking (nityādantaraṅgāpavādānām uttarottaraṃ balīyaḥ;
   Nāgeśa). Take: the ranking as data, each paribhāṣā tied to Art. 23 authority (Pushpa Dixit/Bodas). Likely already
   done in the resolver; audit against it, do not rebuild.

3. Penn & Kiparsky 2012, "On Pāṇini and the Generative Capacity of Contextualized Replacement Systems" (COLING).
   [UNVERIFIED: paper itself not found, only cited in 1512.05670]
   Proposes: Aṣṭādhyāyī rules modelled as contextualised replacement; asks what expressive power conflict resolution needs.
   Verdict: theory only. Take: nothing for code; a possible termination/confluence argument if we ever want a proof
   that apply_rule loops halt. Skip otherwise.

4. Subbanna & Varakhedi 2010, "Asiddhatva Principle in Computational Model of Aṣṭādhyāyī" (SCL 4, LNCS 6465, pp. 231ff).
   https://ui.adsabs.harvard.edu/abs/2010LNCS.6465..231S/abstract
   Proposes: a "filter" that computes what a later-tripāḍī rule may see (visibility), covering all asiddhatva uses.
   Verdict: directly relevant to our asiddha/tripāḍī module. Take: the idea of asiddha as a per-rule visibility
   filter over the derivation history rather than ad hoc checks; compare against our implementation, list gaps.

5. Sohoni & Kulkarni, "A Functional Core for the Computational Aṣṭādhyāyī" (WSC17 vol., 2018) and Goyal/Kulkarni/Behera,
   "Computer Simulation of Aṣṭādhyāyī: Some Insights" / "Simulating the Pāṇinian System" (SCL 2008/2009).
   https://sanskrit.uohyd.ac.in/faculty/amba/PUBLICATIONS/books/WSC17book.pdf
   https://www.sanskritlibrary.org/symposium2/Papers/AmbaSimulation.pdf
   https://link.springer.com/chapter/10.1007/978-3-642-00155-0_4
   Propose: one module per sūtra (as we do), pluggable conflict-resolution, visibility and phase as first-class,
   conflict resolved by utsarga-apavāda plus word-integrity principle.
   Verdict: confirms our architecture; little new. Take: "word integrity" (pada-level scope of an operation) as a
   named conflict test, and their pluggable-resolver test harness idea (run one conflict set under alternate strategies
   to see which rules disagree).

6. Krishna & Goyal, "Towards automating the generation of derivative nouns in Sanskrit by simulating Panini" (2015).
   https://arxiv.org/pdf/1512.05670
   Proposes: separate conflict-resolution module using Nāgeśa's paribhāṣā strength order, falling back to Scharf's
   specificity hierarchy (2010).
   Verdict: a concrete fall-back for the case where utsarga-apavāda does not decide. Take: the fallback order as the
   documented last resort, each use logged in the trace (glass box). Scharf's original paper not read [UNVERIFIED].

7. Scharf, "Rule selection in the Aṣṭādhyāyī, or Is Pāṇini's grammar mechanistic?" (WSC14, 2009) and Scharf 2010
   specificity hierarchy. [UNVERIFIED: full text not found; known via citations]
   Proposes: ordering competing rules by how specific their conditions are (most concrete first).
   Verdict: gives a measurable definition of "apavāda" from the rule's own cond features, instead of hand-tagging.
   Take: a lint (not a runtime rule) that flags pairs where our hand-assigned bādhaka disagrees with specificity.
   Cheap way to find bad apavāda tags.

8. Rajpopat, "In Pāṇini We Trust" (Cambridge PhD, 2022) vs Kiparsky's reply.
   https://www.cam.ac.uk/system/files/rajpopat_phd_thesis_15_dec_2022.pdf
   Proposes: 1.4.2 means "of rules applying to left vs right parts, the right-side one wins", not "later in the text".
   Contested: Kiparsky (listed as 2026 on ResearchGate, abstract only [UNVERIFIED]) says it gives wrong results in a large
   class of cases; Scharf, Samskrita Bharati also object (via partisan secondary press, low reliability).
   Verdict: do not adopt. It contradicts Art. 23 authority (tradition + Pushpa Dixit) unless the owner rules otherwise.
   Take only: as a hypothesis test (see idea 6), never as engine behaviour.

Also seen, no action: Mishra 2007 PaSSim; Petersen & Soubusta 2013 is a digital-edition paper, not rule interaction
(my premise in the brief was wrong) [UNVERIFIED beyond a citation]; Rama Nath Sharma, "Rule Interaction, Blocking and
Derivation in Pāṇini" (SCL 4 vol.) is the likely intended one, not read.
Vidyut: Prasad, "A fast prakriyā generator" https://aclanthology.org/2024.iscls-1.7.pdf (ISCLS 2024): Rust, ~2000 rules,
~600x faster than SanskritVerb. Our use stays validator-only. Take: nothing on ordering. Perf ideas are moot (our cost
is suite/agent time, not derivation speed).
Not found: Patel & Katuri (no hit), Bhate & Kak (not searched), Hellwig (not searched), Petersen rule interaction (see above).

## Plan (adopt? how)

| # | Idea | Adopt | Maps to | Cost | Risk | Proof |
|---|------|-------|---------|------|------|-------|
| 1 | Specificity lint: compare each hand-set bādhaka/apavāda pair with Scharf-style cond specificity; report disagreements only | YES | tools/ (new audit script) + docs/CONFLICT_CELLS.md | M | Low (read-only; heuristic produces false positives, each disagreement needs a human verdict with authority) | Run on existing conflict cells; known-good pairs agree, list disagreements; at least one triaged into a real fix or a documented non-issue |
| 2 | Audit our tripāḍī/asiddha implementation against Subbanna-Varakhedi's visibility filter: enumerate every asiddha case (8.2.1 scope, 6.1.86 etc.) and check each has a test | YES | asiddha module, docs/ADHIKARA_CROSSCHECK.md style table | S | Low | Table of asiddha cases vs tests; any missing case becomes a strict xfail |
| 3 | Log which fall-back (utsarga-apavāda / paribhāṣā rank / param) decided each conflict in the trace | YES if not already there | engine/resolver (coordinator-only hotspot) | S-M | Med (hotspot, needs COORDINATOR=1) | Trace for 3 known conflicts names the deciding principle; no output form changes; full suite green |
| 4 | "Word integrity" (pada-scope) as an explicit conflict check | MAYBE, only if the 81 surface FAILs in sig/exercise_audit.json show a cluster it explains | resolver | M | Med | Cluster triage first; skip if none |
| 5 | Pluggable alternate strategies to measure disagreement (Sohoni/Kulkarni) | NO for runtime; fold into idea 1 | n/a | L | Violates "one mechanism" | n/a |
| 6 | Rajpopat 1.4.2 right-side rule as a hypothesis experiment: offline script, count conflicts where it differs from our resolver | OPTIONAL, low priority | scratch only, no engine change | S | None if never wired | Differences listed; owner decides. Any adoption needs Art. 22/23 ruling |
| 7 | Penn-Kiparsky termination/confluence formalism | NO | n/a | L | No payoff for coverage | n/a |
| 8 | Copy Vidyut ordering / port Vidyut speed ideas | NO | Constitution (validator only); no perf problem | n/a | Law breach | n/a |

Recommendation: do 2 and 1 (in that order), then 3. They are cheap, read-only or trace-only, and target the open
"surface differs" bugs in docs/STATE.md (some may be wrong apavāda/asiddha tags). Skip 5, 7, 8. 6 only if the owner is curious.
The literature mostly confirms the current architecture; no paper offers a shortcut to the 321 unexercised sūtras
(that gap is data and per-sūtra audit, not conflict theory).
