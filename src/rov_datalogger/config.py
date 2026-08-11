from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    mqtt_host: str = os.getenv("MQTT_HOST", "127.0.0.1")
    mqtt_port: int = int(os.getenv("MQTT_PORT", "1883"))
    mqtt_topic: str = os.getenv("MQTT_TOPIC", "#")
    database_path: Path = Path(os.getenv("DATALOGGER_DATABASE", "data/telemetry.sqlite3"))

    @classmethod
    def from_environment(cls) -> "Settings":
        return cls()
