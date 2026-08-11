import logging
import signal
from pathlib import Path

import paho.mqtt.client as mqtt

from .config import Settings
from .store import TelemetryStore

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
LOGGER = logging.getLogger(__name__)


def run(settings: Settings | None = None) -> None:
    settings = settings or Settings.from_environment()
    store = TelemetryStore(settings.database_path)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="rov-datalogger")
    stopping = False

    def on_message(_client, _userdata, message):
        store.record(message.topic, message.payload)

    def stop(_signum, _frame):
        nonlocal stopping
        stopping = True
        client.disconnect()

    client.on_message = on_message
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    LOGGER.info("Connecting to MQTT at %s:%s and subscribing to %s", settings.mqtt_host, settings.mqtt_port, settings.mqtt_topic)
    client.connect(settings.mqtt_host, settings.mqtt_port)
    client.subscribe(settings.mqtt_topic)
    try:
        client.loop_forever()
    finally:
        store.close()
        if not stopping:
            client.disconnect()


if __name__ == "__main__":
    run()
