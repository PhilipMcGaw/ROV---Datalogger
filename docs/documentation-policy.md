# Documentation currency policy

Documentation must be updated in the same change whenever logging behaviour, NATS subjects or payloads, configuration, storage schema, export formats, deployment, tests, workflows, dependencies, or supported platforms change. Status must distinguish implemented, automated-test verified, bench-tested, production-validated, and planned or unverified behaviour. `tests/test_documentation.py` and the pull-request classifier run in CI; exemptions are recorded in `tests/documentation_change_policy.json`.
