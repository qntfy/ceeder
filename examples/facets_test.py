import json

import pytest

from falcon import testing, HTTP_200

from ceeder import cdr, validate, FacetAnnotator


def create_facet():
    fx = lambda x: ([{"value": "hello", "confidence": 0.99}], HTTP_200)
    anno = FacetAnnotator(
        fx,
        label="facet analytic",
    )
    return anno.create()


@pytest.fixture()
def client():
    return testing.TestClient(create_facet())


def test_get_message(client):
    sample_cdr = cdr(extracted_text="Hello world!!!")

    # perform a POST request, as one would in curl
    result = client.simulate_post("/api/v1/annotate/cdr", json=sample_cdr)
    output = result.json
    assert output["label"] == "facet analytic"
    assert output["type"] == "facets"
    sample_cdr["annotators"] = output
    validate(sample_cdr)


def test_health_check(client):
    chk = client.simulate_get("/api/v1/health")
    assert "status" in chk.json
    assert chk.json["status"] == "ok"
