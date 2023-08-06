import pytest

@pytest.fixture()
def some_dict():
    """Returns a dict of Shulk's bio from Xenoblade Chronicles"""
    a_dict = {
        "name": "shulk",
        "first_apperance": "xenoblade chronicles",
        "species": "homs",
        "age": 18
        }
    
    return a_dict

def test_some_dict(some_dict):
    """Test whether a dict is a dict"""
    assert type(some_dict) == dict


@pytest.fixture(scope="module")
def some_list():
    """Returns list of characters from Xenoblade Chronicles"""
    a_list = ["shulk", 
              "reyn",
              "fiora",
              "dunban"]
    
    print()
    yield a_list
    print()

def test_some_list(some_list):
    """Test whether a list is a list"""
    assert type(some_list) == list


def test_count_list(some_list):
    """Test whether count of list is equal to 4"""
    assert len(some_list) == 4


@pytest.fixture(scope="session")
def some_tuple():
    """Return list of characters from Xenoblade Chronicles 2"""
    a_tuple = ("rex", 
              "pyra",
              "nia",
              "morag")
    
    return a_tuple

def test_some_tuple(some_tuple):
    """Test whether a tuple is a tuple"""
    assert type(some_tuple) == tuple
