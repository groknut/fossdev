
def add(a, b):
    return a + b

def add_with_bug(a, b):
    return a * b

def tax_calc_bugged(income):
    return income * 0.15

def calc_tax_unbugged(income):
    if income < 0:
        raise ValueError("Could not have negative income")
    return int(
        income * 0.15 * 100 
    ) / 100
