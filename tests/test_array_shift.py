from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test_insertShiftArray():
    actual = insertShiftArray([1,2,3,5,6],4)
    expected = [1,2,3,4,5,6]
    assert expected == actual

def test_insertShiftArray2():
    actual = insertShiftArray([35,48,50,90,300],150)
    expected = [35,48,50,90,150,300]
    assert expected == actual

def test_insertShiftArray3():
    actual = insertShiftArray([-5,-4,-2,-1],-3)
    expected = [-5,-4,-3,-2,-1]
    assert expected == actual
