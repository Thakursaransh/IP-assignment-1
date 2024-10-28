def differential_equation(x, y):
    return x + y

def calculate_y(target_x):
    y_value = 1  
    step_size = 0.1  
    current_x = 0  

    while current_x < target_x:
        y_value += step_size * differential_equation(current_x, y_value)  
        current_x += step_size  

    return y_value
def _test():
    assert calculate_y(3) == 30.898804537772822
    assert differential_equation(1,5) ==6
_test()
user_input = float(input("Enter the value of x: "))
result_y = calculate_y(user_input)
print("The value of y at x =", user_input, "is:", result_y)
