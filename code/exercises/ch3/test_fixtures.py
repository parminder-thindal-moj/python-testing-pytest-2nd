import pytest

@pytest.fixture()
def some_dict():
    a_dict = {
        "name": "shulk",
        "first_apperance": "xenoblade chronicles",
        "species": "homs",
        "age": 18
        }
    
    return a_dict

def test_some_dict(some_dict):
    assert type(some_dict) == dict
