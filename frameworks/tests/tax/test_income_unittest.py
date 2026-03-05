

from tax.income import calc_tax
import unittest


class TaxCalc(unittest.TestCase):

    def test_income(self):
        self.assertEqual(calc_tax(100), 13.0)

    def test_cents_income(self):
        self.assertEqual(
            calc_tax(10.5), 1.36
        )

if __name__ == "__main__":
    unittest.main()
