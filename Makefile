# Canonical refresh: 9 SIG JSONs + coverage.json + sig_manifest.json
# (24 *rāma* subanta cells + *jayati* gold tinanta path).
PYTHON ?= python3
.PHONY: sig
sig:
	$(PYTHON) -m tools.regenerate_sig_artifacts
