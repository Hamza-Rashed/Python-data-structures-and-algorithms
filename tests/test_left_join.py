
from data_structures_and_algorithms.challenges.left_join.left_join import left_join
import pytest

@pytest.fixture
def my_dict():
    first = {
        'fond':'enamored',
        'wrath':'anger',
        'diligent':'employed',
        'outfit':'garb',
        'guide':'usher'
        }

    return first

def test_given_example(my_dict):

    first = my_dict
    second = {
        'fond':'averse',
        'wrath':'delight',
        'diligent':'idle',
        'guide':'follow',
        'flow':'jam'
        }

    assert left_join(first,second) == {
                                "fond": ["enamored","averse"],
                                "wrath": ["anger","delight"],
                                "diligent": ["employed","idle"],
                                "outfit": ["garb",None],
                                "guide": ["usher","follow"]
                                }

