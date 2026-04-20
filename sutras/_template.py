"""
sutras/_template.py — THE CANONICAL SHAPE OF EVERY SŪTRA FILE.
───────────────────────────────────────────────────────────────

READ THIS FIRST.

Every file under `sutras/adhyaya_X/pada_Y/sutra_X_Y_Z.py` must follow this
exact shape:

    from engine import SutraType, SutraRecord, register_sutra
    from engine.state     import State
    from phonology        import ...  # only what you need

    # ── 1. The cond(state) function ─────────────────────────────────
    def cond(state: State) -> bool:
        # pure reader; NEVER mutates state.
        # reads allowed:
        #   • varṇa phonemes and tags
        #   • pratyāhāra memberships (AC, HAL, IK, ...)
        #   • state.samjna_registry
        #   • state.paribhasha_gates
        #   • state.adhikara_stack via engine.gates.adhikara_in_effect
        #   • state.atidesha_map
        #   • state.nipatana_flag
        #   • Term.meta['upadesha_slp1'], Term.meta['gana']
        # reads FORBIDDEN:
        #   • Term.meta['vibhakti'], meta['vacana'], meta['lakara'], etc.
        #   • surface Devanāgarī strings
        #   • any file under the gold-corpus firewall (see CONSTITUTION Art. 6)
        return ...

    # ── 2. The act(state) function ──────────────────────────────────
    def act(state: State) -> State:
        # state is already a clone (the dispatcher cloned it).
        # mutate and return.
        ...
        return state

    # ── 3. The SutraRecord ──────────────────────────────────────────
    SUTRA = SutraRecord(
        sutra_id       = "X.Y.Z",
        sutra_type     = SutraType.<TYPE>,
        text_slp1      = "<full sūtra, anuvṛtti baked in>",
        text_dev       = "<full Devanāgarī, anuvṛtti baked in>",
        padaccheda_dev = "<word-split Devanāgarī>",
        why_dev        = "<one-line Devanāgarī justification>",
        anuvritti_from = ("A.B.C", ...),   # metadata only
        cond           = cond,
        act            = act,
        # type-specific fields as applicable:
        #   adhikara_scope    = ("start_id", "end_id")
        #   blocks_sutra_ids  = ("X.Y.Z", ...)
        #   vibhasha_default  = True
        #   atidesha_target   = "..." / atidesha_source = "..." / atidesha_dest = "..."
        #   nipatana_form_slp1 = "..."
    )

    register_sutra(SUTRA)


Naming rules:
  • filename: `sutra_<a>_<b>_<c>.py` (no leading zeros).
  • if a sūtra has a well-known transliteration (e.g. `yasyeti_ca`),
    append it: `sutra_6_4_148_yasyeti_ca.py` — optional.

Hard constraints (enforced by tests/constitutional):
  • exactly ONE SutraRecord per file.
  • exactly ONE register_sutra() call.
  • cond() NEVER reads Term.meta['vibhakti'], meta['vacana'], etc.
  • no imports of engine.dispatcher (a sūtra must never recurse into
    apply_rule — that's the recipe's job).
"""
