import random
def random_walk(n, m):
    x, y = 0, 0
    steps = 0   
    while x < n and y < m:
        direction = random.choice(['x', 'y'])
        distance = random.randint(1, 5)
        if direction == 'x':
            x += distance
            if x > n: 
                x = n
        else:
            y += distance
            if y > m: 
                y = m    
        steps += 1    
    return steps

def average_steps(n, m):
    averages = []   
    while True:
        num_walks = 100
        total_steps = sum(random_walk(n, m) for _ in range(num_walks))
        current_average = total_steps / num_walks
        averages.append(current_average)       
        if len(averages) > 1:
            change = abs(averages[-1] - averages[-2]) / averages[-2]
            if change < 0.1:
                break
    return averages[-1]

while True:
    try:
        n = int(input(" x-coordinate : "))
        m = int(input(" y-coordinate  : "))
        if n < 0 or m < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter valid non-negative integers.")

avg_steps = average_steps(n, m)
print(f"Average steps to reach ({n}, {m}): {avg_steps}:")
