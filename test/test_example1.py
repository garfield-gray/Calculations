import pytest
from example import add, subtract

# Fixture: prepares some data for your tests
@pytest.fixture
def sample_data():
    return 3, 4  # This is the data your tests will use

# Test using the fixture
def test_add(sample_data):
    a, b = sample_data  # Get the data from the fixture
    assert add(a, b) == 7  # Check if add(3, 4) equals 7

def test_subtract(sample_data):
    a, b = sample_data  # Get the data from the fixture
    assert subtract(a, b) == -1  # Check if subtract(3, 4) equals -1

