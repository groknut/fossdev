
from main import sum, div

"""
Tests for sum() function
"""
def test_sum():
    a, b = 1, 3
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

if __name__ == "__main__":
    test_sum()
    test_div()
