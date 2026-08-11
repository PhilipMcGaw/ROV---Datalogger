# ROV data logger

This folder is reserved for the standalone telemetry logging service.

## Planned responsibility

Subscribe to selected MQTT telemetry topics and persist timestamped readings to SQLite. Provide CSV export for analysis and backup workflows.

## Design constraints

- Run independently from `Control/` and `Cockpit/`.
- Never block or alter motor-control messages.
- Store the original MQTT topic, value, timestamp, and quality/status where available.
- Use SQLite as the primary store and CSV as an export format.
- Add retention, batching, recovery, and backup behaviour before production deployment.

Implementation is intentionally not included yet; this directory marks the service boundary and planned ownership.
# ROV Datalogger

The Datalogger subscribes to the ROV MQTT broker and stores raw messages in SQLite. It preserves the original topic, timestamp, bytes, text representation, and JSON representation where the payload is valid JSON. This keeps capture lossless while making later CSV analysis practical.

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

Set `MQTT_HOST`, `MQTT_PORT`, `MQTT_TOPIC`, and `DATALOGGER_DATABASE` using the example in `configs/datalogger.env.example`. The default database is `data/telemetry.sqlite3` and the default subscription is `#`; narrow the topic before production use if only selected telemetry is required.

## Design boundary

This service records data but does not control the ROV, alter MQTT messages, or provide a web UI. Cockpit and Control remain separate services.

## CSV export

CSV export is available through the `TelemetryStore.export_csv()` API. A command-line export tool will be added when the query/reporting requirements are settled.
