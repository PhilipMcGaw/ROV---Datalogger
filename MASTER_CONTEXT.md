# ROV Datalogger Master Context

The Datalogger repository captures raw MQTT telemetry to SQLite and provides a foundation for CSV export and later reporting. It does not control the ROV or provide a web UI.

Windows support is provided through `scripts/1_install_dependencies.bat` and `scripts/2_start_app.bat`. These follow the TiaB workflow: they detect UNC paths, install portable WinPython locally without administrator rights, use `requirements.txt` when present, and do not use `uv` on Windows.

The service is started with `PYTHONPATH=src python -m rov_datalogger.main`. Configuration is supplied through `MQTT_HOST`, `MQTT_PORT`, `MQTT_TOPIC`, and `DATALOGGER_DATABASE`. Raw payload bytes are retained; valid JSON is stored in a normalized companion column for analysis.

When the schema, topic selection, retention policy, or export behaviour changes, update this file and the relevant documentation in the same change.
