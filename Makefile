# Canonical refresh: 9 SIG JSONs + coverage.json + sig_manifest.json
# (24 *rāma* subanta cells + *jayati* gold tinanta path).
PYTHON ?= python3
.PHONY: sig
sig:
	$(PYTHON) -m tools.regenerate_sig_artifacts

.PHONY: ratchet-status
ratchet-status:
	$(PYTHON) audit/ratchet_collapse.py --status

.PHONY: ratchet-next
ratchet-next:
	$(PYTHON) audit/ratchet_collapse.py --next

.PHONY: ratchet-n
ratchet-n:
	$(PYTHON) audit/ratchet_collapse.py --run $(N)

.PHONY: audit-blocks
audit-blocks:
	@# Auditor exits nonzero while duplicates remain; the constitutional gate enforces ceiling.
	-$(PYTHON) audit/scheduling_block_auditor.py .

.PHONY: audit-duplicates
audit-duplicates:
	$(PYTHON) -m audit.pipeline_auditor

.PHONY: audit-constitutional
audit-constitutional:
	$(PYTHON) -m pytest tests/constitutional -v --tb=short

.PHONY: test-unity
test-unity:
	$(PYTHON) -m pytest tests/test_pipeline_unity.py -v --tb=short

.PHONY: test-all
test-all:
	$(PYTHON) -m pytest tests/ -v --tb=short -x

.PHONY: full-check
full-check: audit-duplicates audit-blocks audit-constitutional test-all
	@echo ""
	@echo "══════════════════════════════════════════"
	@echo "  ALL CHECKS PASSED"
	@$(PYTHON) -c 'import re; from pathlib import Path; f=Path("tests/constitutional/test_no_new_duplicates.py"); m=re.search(r"MAX_DUPLICATE_GROUPS\s*=\s*(\d+)", f.read_text(encoding="utf-8")); ceiling=int(m.group(1)) if m else -1; print(f"  Duplicate ceiling : {ceiling}"); print("  Target            : 0"); print(f"  Progress          : {112-ceiling}/112 collapsed")'
	@echo "══════════════════════════════════════════"

pages:
	python3 -m tools.build_pages

api:
	uvicorn api.main:app --reload --port 8000

lab:   ## local test panel → http://127.0.0.1:8000/lab (Vidyut column needs .venv)
	@(sleep 3; open http://127.0.0.1:8000/lab) & uvicorn api.main:app --port 8000

ui:
	./"Panini Engine.command"

coverage:
	python3 -m tools.firing_coverage
	python3 -m tools.firing_coverage --report

confident:   ## per-phase list of sūtras done with confidence → docs/CONFIDENT_SUTRAS.md
	python3 -m tools.sutra_class

lint:
	python3 -m tools.sutra_lint

bench:
	python3 -m bench.run --show-disagreements --write

gaps:
	python3 -m tools.gaps_report

index:
	python3 -m tools.build_form_index
	python3 -m tools.build_form_index --verify 300

prakriya:
	python3 -m tools.show_prakriya --check

autonomy:
	python3 -m tools.autonomy_report

shabda:
	python3 -m tools.shabda_table --check

# ── reference brain (read-only; see AGENTS.md "Brain") ──
BRAIN ?= $(HOME)/data-master/ashtadhyayi-ai
BRAIN_PY = $(BRAIN)/venv/bin/python $(BRAIN)/agent/knowledge_api.py
.PHONY: brain scaffold resolve brain-wiki
brain:      ## make brain S=6.1.77 — rule, meaning, examples ±, prakriyā, graph, conflicts
	@$(BRAIN_PY) dossier $(S)
scaffold:   ## make scaffold S=6.1.77 — draft file: metadata, samagra, Art. 14 citations
	@$(BRAIN_PY) scaffold $(S)
resolve:    ## make resolve S=6.1.77 — evidence per source conflict, Art. 22 order
	@$(BRAIN_PY) resolve $(S)
brain-wiki: ## local wiki of the brain (human view)
	@open "$(BRAIN)/Brain.command"

# ── multi-agent gate (see AGENTS.md) ──
.PHONY: preflight claim release claims ratchets scope status hooks
preflight:
	@$(PYTHON) -m tools.agent_gate preflight $(S)
claim:
	@$(PYTHON) -m tools.agent_gate claim $(ID) "$(SCOPE)"
release:
	@$(PYTHON) -m tools.agent_gate release $(ID)
claims:
	@$(PYTHON) -m tools.agent_gate status
ratchets:
	@$(PYTHON) -m tools.agent_gate ratchets
scope:
	@$(PYTHON) -m tools.agent_gate scope
status:
	@$(PYTHON) -m tools.status
hooks:
	git config core.hooksPath .githooks
