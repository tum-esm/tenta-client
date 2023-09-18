# Tenta Python Client

[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/tum-esm/tenta-client/test.yml?label=tests%20on%20main%20branch)](https://github.com/tum-esm/tenta-client/actions/workflows/test.yml)
[![GitHub](https://img.shields.io/github/license/tum-esm/tenta-client?color=f1f5f9)](https://github.com/tum-esm/tenta-client/blob/main/LICENSE.md)
[![PyPI - Version](https://img.shields.io/github/v/tag/tum-esm/tenta-client?label=version&color=f1f5f9)](https://pypi.org/project/tenta)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tenta?label=supported%20Python%20versions&color=f1f5f9)](https://pypi.org/project/tenta)

This is a Python client library for [Tenta](https://github.com/iterize/tenta), a sensor network management tool. This library uses [Paho MQTT](https://github.com/eclipse/paho.mqtt.python) to communicate with a Tenta server connected to the same broker. The library provides type-safe interfaces to create an MQTT client, send messages (logs, measurements, and acknowledgments) to the server, and receive parameters (configuration messages) from the server.

Please contact [Moritz Makowski](mailto:moritz.makowski@tum.de) if you have any questions or feedback that goes beyond the scope of a GitHub issue. The documentation for this client library is hosted at [tenta-python-client.onrender.com](https://tenta-python-client.onrender.com).

<br/>

## Usage

Install it with Pip or [Poetry](https://github.com/python-poetry/poetry):

```bash
pip install tenta
# or
poetry add tenta
```

Import and use it in your project:

```python
import tenta

# connect to the MQTT broker

tenta_client = tenta.TentaClient(
    mqtt_host="test.mosquitto.org",
    mqtt_port=1884,
    mqtt_identifier="rw",
    mqtt_password="readwrite",
    sensor_identifier="81b...",
)

# publish log or measurement messages

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

# wait for the client to publish all messages

tenta_client.wait_for_publish()

# check if a new configuration message has arrived

config_message: typing.Optional[
    tenta.ConfigurationMessage
] = tenta_client.get_latest_received_config_message()

# disconnect from the MQTT broker

tenta_client.teardown()
```

<br/>

## About

**Why does this client exist?** The Tenta specification of how a sensor should publish its data is simple, but to actually use Tenta in a project, one needs to write code that sends out these messages via a Python MQTT library, like Paho. This implementation code is relatively simple but needs to be written, documented, and tested in every single project that wants to use Tenta. This client library is thoroughly tested and documented. Hence, it makes onboarding to Tenta significantly easier.

**Compatibility:** Client library version `0.X.*` will be compatible with the Tenta specification `0.X.*`. Client library versions `Y.*.*` will be compatible with Tenta specification `Y.*.*`.

**Adhering to semantic versioning:** The same function calls will produce the same MQTT messages within non-breaking releases, i.e., the function call `tenta_client.function(args)` will produce the same MQTT messages in library versions `0.1.0` and `0.1.3` even if the Tenta specification provides a new feature in `0.1.3`. New non-breaking features in Tenta will always be opt-in, i.e., `tenta_client.function(args, enable_new_feature=True)` will opt into that new feature. This way, the behavior of sensors does not change with the same code even if they upgrade to non-breaking client library releases (automatically).

**Open-Source:** Issues and Pull Requests are welcome! Every PR undergoes a review process to ensure quality and semantic versioning.

**Testing:** The library is statically typed and is strictly checked using [Mypy](https://github.com/python/mypy). The tests cover publishing all message types, receiving configuration messages, and connecting to the MQTT broker with and without TLS encryption with valid and invalid connection details. The tests run for all supported Python versions (3.8, 3.9, 3.10, 3.11).

**Documentation:** The documentation is built using [Nextra](https://nextra.site/) and [Pydoc-Markdown](https://github.com/NiklasRosenstein/pydoc-markdown).
