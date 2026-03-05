
def calc_tax(income):
    if income < 0:
        raise ValueError("Could not have negative income")
    return int(income * 0.13 * 100) / 100
