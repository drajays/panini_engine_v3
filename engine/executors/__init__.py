"""
engine.executors — one executor per SutraType.

An executor is a pure function:
    exec_<type>(rec: SutraRecord, state: State, step: dict) -> (State, bool)

The bool is `fired` — True iff the cond(state) returned True AND the
act(state) was run.  The dispatcher uses `fired` to decide whether to
log APPLIED or SKIPPED in the trace.
"""
