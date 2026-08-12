# ROV Datalogger Master Context

On Linux, the documented clone location is `~/ROV - Datalogger`, beside the other ROV repositories. On macOS, use a user-selected workspace beneath the home directory, for example `~/Projects/ROV/ROV - Datalogger`. This is a default convention, not a hard-coded path; scripts must derive paths from their own location.

The enforceable documentation policy is `docs/documentation-policy.md`, with contributor guidance in `CONTRIBUTING.md`, current status in `docs/status.md`, and checks in `tests/test_documentation.py` and `tests/documentation_change_policy.py` using `tests/documentation_change_policy.json`.

The Datalogger repository captures raw NATS Core telemetry to SQLite and provides a foundation for CSV export and later reporting. It does not control the ROV or provide a web UI.

Windows support is provided through `scripts/1_install_dependencies.bat` and `scripts/2_start_app.bat`. These follow the TiaB workflow: they detect UNC paths, install portable WinPython locally without administrator rights, use `requirements.txt` when present, and do not use `uv` on Windows.

The service is started with `PYTHONPATH=src python -m rov_datalogger.main`. Configuration is supplied through `NATS_URL`, `NATS_SUBJECT`, and `DATALOGGER_DATABASE`. Raw payload bytes are retained; valid JSON is stored in a normalized companion column for analysis. The Datalogger uses NATS Core only, not JetStream.

When the schema, NATS subject selection, retention policy, or export behaviour changes, update this file and the relevant documentation in the same change. Every change must include a consistency check of this file; if it is not a true reflection of current behaviour, correct it in the same change. Documentation must remain current, use formal British English, and be written for readers with an engineering degree or equivalent technical experience.

Where SI units are used, place a space between the numerical value and the unit symbol, for example `5 m`, `12 V`, and `20 °C`. Use the degree symbol `°` by preference for angles.

The verbose portable scripting standard applies equally to Windows batch/PowerShell scripts and POSIX shell scripts on macOS, Linux, and Raspberry Pi.
