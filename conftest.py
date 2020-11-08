import pytest
from facade import Facade


@pytest.fixture(scope="session")
def facade():
    return Facade()
