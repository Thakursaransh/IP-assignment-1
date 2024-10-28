def poly_function(x):
    return x*3 - 10.5*x*2 + 34.5*x - 35
def poly_derivative(x):
    return 3*x**2 -21*x + 34.5
def _test():
    assert poly_function(0)==-35
    assert poly_derivative(0)==34.5
_test()
check=0
x0=int(input("enter first guess: "))
for i in range(100):
    if abs(poly_function(x0))<0.2:
        print("root is: ",x0)
        check=1
        break
    if poly_derivative(x0)==0:
        print("no solution found")
        check=1
        break
    x0=x0-poly_function(x0)/poly_derivative(x0)
if check==0:
    print("no root found")