
from main import sum, div, subs

"""
Tests for sum() function
"""
def test_sum():
    a, b = 1, 2
    res = 3
    assert sum(a, b) == res

def test_sum_str():
    a, b = "10", 5
    res = 15
    assert sum(a, b) == res

"""
Tests for div() function
"""
def test_div():
    a, b = 15, 3
    res = 5
    assert div(a, b) == res

def test_div_str():
    a, b = "1", 5
    try:
        div(a, b)
    except:
        print("Test failed: wrong type")

def test_div_zero():
    a, b = 5, 0
    try:
        div(a, b)
    except:
        print("Test failed: Zero")

def test_subs():
    a = 5
    b = 3
    result = 2
    assert subs(a, b) == result

if __name__ == "__main__":
    test_sum()
    test_div()
    test_div_str()
    test_div_zero()
    test_subs()
