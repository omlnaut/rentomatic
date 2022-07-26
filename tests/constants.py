import uuid

import pytest


@pytest.fixture
def code():
    return uuid.uuid4()


@pytest.fixture
def init_dict(code):
    return {
        "code": code,
        "size": 200,
        "price": 10,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }


@pytest.fixture
def serialized_dict(init_dict):
    init_dict["code"] = str(code)
    return init_dict
