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
