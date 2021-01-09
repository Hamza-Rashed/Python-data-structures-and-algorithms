from data_structures_and_algorithms.data_structures.hash_table.hash_table import Hashmap
import pytest

def test_add(prep):
    prep.add('name', 'hamza')
    assert prep.contains('name') == True   

def test_hash(prep):
    assert prep.get_hash('could') == 903

@pytest.fixture
def prep():
    finall = Hashmap(1024)
    return finall