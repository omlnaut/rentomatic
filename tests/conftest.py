import pytest

from application.app import create_app
from manage import read_json_configuration


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture(scope="session")
def app_configuration():
    return read_json_configuration("testing")
