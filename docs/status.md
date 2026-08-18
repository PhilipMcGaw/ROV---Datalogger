# ROV Datalogger current status

## Implemented

The storage layer captures raw messages to SQLite and provides CSV export primitives. The checked-in runtime subscriber is still MQTT/Paho and is not compatible with the current NATS Core service contract. It does not control the ROV or provide a web UI.

## Automated-test verification

The repository contains `tests/test_store.py` and the documentation audit `tests/test_documentation.py`.

## Bench-tested and Production-validated

Physical ROV and production deployment validation are not recorded here and must not be inferred from source-code presence.

## Planned or unverified

- Migrate the runtime subscriber and configuration from MQTT/Paho to NATS Core.
- Rename MQTT-specific schema identifiers and configuration names, with an explicit existing-database migration decision.

CSV export, reporting, retention policy, and production backup procedures require explicit implementation and evidence.

## References

- `MASTER_CONTEXT.md`
- `docs/documentation-policy.md`
- `src/rov_datalogger/main.py`
- `src/rov_datalogger/store.py`
- `tests/test_store.py`
