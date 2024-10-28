import math
def f(t):
    return 2000 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t

def calculate_distance(a, b):
    distance = 0
    while a < b:
        distance += 0.25 * (f(a) + f(a + 0.25)) / 2
        a += 0.25
    return distance

def _test():
    assert(2,6) == 339.57234631722434
    assert(10,25) == 6679.409082226381 

a = int(input("Enter start time: "))
b = int(input("Enter end time: "))

distance = calculate_distance(a, b)

print("Distance travelled:", (distance), "metres")
