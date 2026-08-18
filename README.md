# ROV data logger

This folder is reserved for the standalone telemetry logging service.

## Planned responsibility

The intended service subscribes to selected NATS Core subjects and persists timestamped readings to SQLite, with CSV export for analysis and backup workflows.

Implementation status: the service boundary and target NATS interface are documented, but the checked-in implementation still requires migration and testing before it can be described as production-ready.

## Design constraints

- Run independently from `Control/` and `Cockpit/`.
- Never block or alter motor-control messages.
- Store the original NATS subject, value, timestamp, and quality/status where available after migration.
- Use SQLite as the primary store and CSV as an export format.
- Add retention, batching, recovery, and backup behaviour before production deployment.

Implementation is intentionally not included yet; this directory marks the service boundary and planned ownership.
# ROV Datalogger

The target Datalogger interface is NATS Core. The current storage layer preserves raw message bytes, text, and JSON representations in SQLite, but the checked-in runtime subscriber still uses MQTT/Paho and must be migrated before deployment.

## Quick start

Windows:

```text
scripts\1_install_dependencies.bat
scripts\2_start_app.bat
```

Linux/Raspberry Pi:

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
./run.sh
```

The target configuration is `NATS_URL`, `NATS_SUBJECT`, and `DATALOGGER_DATABASE`. The current implementation still uses MQTT-specific settings, so these are design targets rather than a verified deployment recipe. The default database is `data/telemetry.sqlite3`; narrow the subject before production use if only selected telemetry is required.

## Design boundary

This service records data but does not control the ROV, alter NATS messages, or provide a web UI. Cockpit and Control remain separate services.

## CSV export

CSV export is available through the `TelemetryStore.export_csv()` API. A command-line export tool will be added when the query/reporting requirements are settled.
