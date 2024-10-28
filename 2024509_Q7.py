import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_visible_points(N):
    visible_count = 0
    for i in range(N):
        for j in range(N):
            if gcd(i, j) == 1:
                visible_count += 1
    return visible_count

def find_N_within_density(percentage):
    target_density = 6 / math.pi**2
    N = 1
    while True:
        visible_points = count_visible_points(N)
        density = visible_points / (N * N)
        if abs(density - target_density) / target_density <= percentage / 100:
            return N
        N += 1

def _test():
    assert gcd(54,24) == 6
    assert gcd(0,5) ==5

N_result = find_N_within_density(20)
print("The value of N for which the density comes within 20% of 6/pi^2 is:", N_result)
