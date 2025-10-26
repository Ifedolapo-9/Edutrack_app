import sys
import os
import pytest
from fastapi.testclient import TestClient

# 👇 Add the project root (one level up) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client
