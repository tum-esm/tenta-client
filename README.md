# 🐙 Tenta Python Client

This is a Python client library for [Tenta](https//github.com/iterize/tenta), a sensor network management tool. This library uses [Paho MQTT](https://github.com/eclipse/paho.mqtt.python) to communicate with a Tenta server connected to the same broker. The library provides type-safe interfaces to create an MQTT client, send out messages (logs, measurements, and acknowledgements) to the server and receive parameters (configuration messages) from the server.

Please contact [Moritz Makowski](moritz.makowski@tum.de) if you have any questions or feedback that goes beyong the scope of a GitHub issue.

## Usage

Install it with Pip or [Poetry](https://github.com/python-poetry/poetry):

```bash
pip install tenta
# or
poetry add tenta
```

Start using it:

```python
tenta_client = tenta.TentaClient(
    # MQTT broker connection parameters
    mqtt_host="test.mosquitto.org",
    mqtt_port=1884,
    mqtt_identifier="rw",
    mqtt_password="readwrite",

    # the sensor identifier (from the Tenta Dashboard)
    sensor_identifier="81b...",

    # subscribe to configuration messages (created in the Tenta Dashboard)
    receive_configs=True,
)

# Publish log or measurement messages
tenta_client.publish(
    tenta.LogMessage(severity="info", message="Hello, to you!")
)
tenta_client.publish(
    tenta.MeasurementMessage(
        value={
            "temperature": 20.0, "humidity": 50.0,
            "pressure": 1013.25, "voltage": 3.3,
        },
    )
)

# Wait for the client to publish all messages
tenta_client.wait_for_publish()

# check if a new configuration message has arrived
config_message: typing.Optional[
    tenta.ConfigurationMessage
] = tenta_client.get_latest_received_config_message()

# disconnect from the MQTT broker
tenta_client.teardown()
```

## About

**Why does this client exist?** The Tenta specification of how sensor should publish their data is very concise. Still in order to actually use Tenta in a project, one needs to write code that sends out these messages via an Python MQTT library, like Paho. This is not that much code, but need to be implemented, documented and tested in every single Project that wants to use Tenta. Hence, this client library is fully tested, documented and makes onboarding to Tenta significantly easier.

**Compatibility:** Client library version `0.X.*` will be compatible with the Tenta specification `0.X.*`. Client library versions `Y.*.*` will be compatible with Tenta specification `Y.*.*`.

**Adhering to semantic versioning:** The same function calls will produce the same MQTT messages within non-breaking releases, i.e. the function call `tenta_client.function(args)` will produce the same MQTT messages in library versions `0.1.0` and `0.1.3` even if the Tenta specification provides a new feature in `0.1.3`. New non-breaking features in Tenta will alway be opt-in, i.e. `tenta_client.function(args, enable_new_feature=True)´ will opt-into that new feature. This way, the behaviour of sensors does not change with the same code even if they upgrade to non-breaking client library releases (automatically).

**Open-Source:** Issues and Pull Requests are welcome! Every PR undergoes a review process to ensure quality and semantic versioning.

**Testing:** The library is statically typed and is strictly checked using [Mypy](https://github.com/python/mypy). The tests cover publishing all message types, receiving configuration messages and connecting to the MQTT broker with and without TLS encryption with valid and invalid connection details.
