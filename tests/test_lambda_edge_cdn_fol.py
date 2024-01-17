from importlib import reload

import pytest
import json

from lambdas import lambda_edge


def test_lambda_edge_dev():
    with open("tests/fixtures/origin-event-fol-dev.json", encoding="utf-8") as json_file:
        lambda_response = lambda_edge.lambda_handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == "/fol"
        assert lambda_response["uri"] == "/index.html"


def test_lambda_edge_stage():
    with open(
        "tests/fixtures/origin-event-fol-stage.json", encoding="utf-8"
    ) as json_file:
        lambda_response = lambda_edge.lambda_handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == "/fol"
        assert lambda_response["uri"] == "/index.html"


def test_lambda_edge_prod_1():
    with open(
        "tests/fixtures/origin-event-fol-prod-1.json", encoding="utf-8"
    ) as json_file:
        lambda_response = lambda_edge.lambda_handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == "/fol"
        assert lambda_response["uri"] == "/index.html"


def test_lambda_edge_prod_2():
    with open(
        "tests/fixtures/origin-event-fol-prod-2.json", encoding="utf-8"
    ) as json_file:
        lambda_response = lambda_edge.lambda_handler(json.load(json_file), "context")
        assert lambda_response["origin"]["s3"]["path"] == "/fol"
        assert lambda_response["uri"] == "/index.html"
