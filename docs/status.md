# ROV Datalogger current status

## Implemented

The Python service captures raw NATS Core telemetry to SQLite. It does not control the ROV or provide a web UI.

## Automated-test verification

The repository contains `tests/test_store.py` and the documentation audit `tests/test_documentation.py`.

## Bench-tested and Production-validated

Physical ROV and production deployment validation are not recorded here and must not be inferred from source-code presence.

## Planned or unverified

CSV export, reporting, retention policy, and production backup procedures require explicit implementation and evidence.

## References

- `MASTER_CONTEXT.md`
- `docs/documentation-policy.md`
- `src/rov_datalogger/main.py`
- `src/rov_datalogger/store.py`
- `tests/test_store.py`
