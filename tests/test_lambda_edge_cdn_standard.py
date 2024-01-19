from importlib import reload

import pytest
import json

from lambdas import lambda_edge


def test_lambda_edge_dev():
    with open("tests/fixtures/origin-event-cdn-dev.json", encoding="utf-8") as json_file:
        lambda_response = lambda_edge.handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == ""
        assert lambda_response["uri"] == "/index.html"


def test_lambda_edge_stage():
    with open(
        "tests/fixtures/origin-event-cdn-stage.json", encoding="utf-8"
    ) as json_file:
        lambda_response = lambda_edge.handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == ""
        assert lambda_response["uri"] == "/index.html"


def test_lambda_edge_prod_1():
    with open(
        "tests/fixtures/origin-event-cdn-prod-1.json", encoding="utf-8"
    ) as json_file:
        lambda_response = lambda_edge.handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == ""
        assert lambda_response["uri"] == "/index.html"


def test_lambda_edge_prod_2():
    with open(
        "tests/fixtures/origin-event-cdn-prod-2.json", encoding="utf-8"
    ) as json_file:
        lambda_response = lambda_edge.handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == ""
        assert lambda_response["uri"] == "/index.html"
