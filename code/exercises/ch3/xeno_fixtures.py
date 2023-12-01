import pytest

@pytest.fixture()
def xeno_dict():
    
    """A dictionary of Xenoblade characters """
    
    characters_dict = {
        "Shulk": {
            "name": "shulk",
            "age": 18,
            "species": "homs",
            "weapon": "monado"
        },
        "Reyn": {
            "name": "reyn",
            "age": 18,
            "species": "homs",
            "weapon": "gunlance"
        },
        "Fiora": {
            "name": "fiora",
            "age": 18,
            "species": "homs",
            "weapon": "double blades"
        },
        "Dunban": {
            "name": "dunban",
            "age": 30,
            "species": "homs",
            "weapon": "sword"
        }
    }
    
    yield characters_dict
    
    
@pytest.fixture(scope="module")
def xeno_list():
    """ A list of Xenoblade Characters"""
    x_list = ["shulk",
              "fiora",
              "reyn",
              "dunban"]
    
    print("before yield")
    yield x_list
    print("after yield")


@pytest.fixture()
def xeno_tuple():
    """ """
    x_tuple = ("shulk",
               "reyn",
               "fiora",
               "dunban")
    
    yield x_tuple

def test_fixture_dict(xeno_dict):
    """ Testing whether the dict is a dictionary"""
    assert type(xeno_dict) == dict

def test_fixture_list(xeno_list):
    """Testing the fixture is a list """
    assert type(xeno_list) == list
    
def test_fixture_tuple(xeno_tuple):
    assert type(xeno_tuple) == tuple
    
def test_count_list(xeno_list):
    count = len(xeno_list)
    assert count == 4
    
