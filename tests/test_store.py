from pathlib import Path

from rov_datalogger.store import TelemetryStore


def test_record_preserves_raw_and_json_payload(tmp_path: Path):
    store = TelemetryStore(tmp_path / "telemetry.sqlite3")
    store.record("sensor/depth", b'{"value": 12.5}')
    row = store.connection.execute(
        "SELECT topic, payload, payload_text, payload_json FROM mqtt_messages"
    ).fetchone()
    store.close()
    assert row[0] == "sensor/depth"
    assert row[1] == b'{"value": 12.5}'
    assert row[2] == '{"value": 12.5}'
    assert row[3] == '{"value":12.5}'
