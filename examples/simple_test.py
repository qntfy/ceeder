import json

import pytest
from falcon import testing

from seeder import cdr, validate
from simple import create_tag


@pytest.fixture()
def client():
    # Take  function `create` from `simple.py` in this folder.
    return testing.TestClient(create_tag())


def test_get_message(client):
    sample_cdr = cdr(extracted_text="Hello world!!!")

    # perform a POST request, as one would in CURL
    result = client.simulate_post("/api/v1/annotate/cdr", json=sample_cdr)
    output = result.json
    assert output["label"] == "simple analytic"
    assert output["type"] == "tags"
    sample_cdr["annotators"] = output
    validate(sample_cdr)


def test_health_check(client):
    chk = client.simulate_get("/api/v1/health")
    assert "status" in chk.json
    assert chk.json["status"] == "ok"
