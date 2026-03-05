
from tax.income import calc_tax

def test_income_tax():
    assert calc_tax(100) == 13
    print("Test INCOME TAX PASSED")

if __name__ == "__main__":
    test_income_tax()
