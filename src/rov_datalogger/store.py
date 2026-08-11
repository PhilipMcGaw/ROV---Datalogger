import csv
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


class TelemetryStore:
    def __init__(self, database_path: Path):
        self.database_path = database_path
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.database_path)
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS mqtt_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                received_at TEXT NOT NULL,
                topic TEXT NOT NULL,
                payload BLOB NOT NULL,
                payload_text TEXT,
                payload_json TEXT
            )
        """)
        self.connection.execute("CREATE INDEX IF NOT EXISTS idx_mqtt_messages_received_at ON mqtt_messages(received_at)")
        self.connection.execute("CREATE INDEX IF NOT EXISTS idx_mqtt_messages_topic ON mqtt_messages(topic)")
        self.connection.commit()

    def record(self, topic: str, payload: bytes, received_at: str | None = None) -> None:
        timestamp = received_at or datetime.now(timezone.utc).isoformat()
        text = payload.decode("utf-8", errors="replace")
        try:
            structured = json.dumps(json.loads(text), separators=(",", ":"))
        except (json.JSONDecodeError, TypeError):
            structured = None
        self.connection.execute(
            "INSERT INTO mqtt_messages(received_at, topic, payload, payload_text, payload_json) VALUES (?, ?, ?, ?, ?)",
            (timestamp, topic, payload, text, structured),
        )
        self.connection.commit()

    def export_csv(self, destination: Path, rows: Iterable[tuple] | None = None) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        query = rows if rows is not None else self.connection.execute(
            "SELECT id, received_at, topic, payload_text, payload_json FROM mqtt_messages ORDER BY id"
        )
        with destination.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(("id", "received_at", "topic", "payload_text", "payload_json"))
            writer.writerows(query)

    def close(self) -> None:
        self.connection.close()
