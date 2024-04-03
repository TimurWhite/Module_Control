import pytest

@pytest.fixture
def example_text():
    return "This is a test sentence. With a comma, and more words!"

@pytest.fixture
def empty_text():
    return ""

@pytest.fixture
def special_characters_text():
    return "!@#$%^&*()"
