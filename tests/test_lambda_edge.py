from importlib import reload

import pytest
import json

from lambdas import lambda_edge


def test_lambda_edge():
    with open("tests/fixtures/s3-origin-request.json", encoding="utf-8") as json_file:
        assert lambda_edge.lambda_handler(json.load(json_file), "context")
