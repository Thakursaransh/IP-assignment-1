from math import e

def D(a, b, p):
    return e**(a - b * p)

def S(c, d, p):
    return e**(c + d * p)

def find_equilibrium_price(a, b, c, d):
    price = 1
    while D(a, b, price) > S(c, d, price):
        price *= 1.05
    else:
        if D(a, b, price) > S(c, d, price) + 50:
            return None 
        else:
            return price, D(a, b, price), S(c, d, price)

def _test():
    a, b, c, d = 10, 1.05, 1, 1.06
    result = find_equilibrium_price(a, b, c, d)
    if result is None:
        assert result is None 
    else:
        price, demand, supply = result
        assert demand <= supply + 50 
        print("Equilibrium price:", price)
        print("Demand:", demand)
        print("Supply:", supply)

_test()
