def f(x):                                                                     
    fact=1
    for i in range(1,x+1):
        fact*=i    
    return fact    

def sin(x):                                                                   
    sum=0    
    for i in range(75):
        sum=sum+((-1)**i)*x**(2*i+1)/f(2*i+1)        
    return sum

def cos(x):                                                                     
    sum=0    
    for i in range(75):
        sum=sum+((-1)**i)*x**(2*i)/f(2*i)        
    return sum

def tan(x):                                                                     
    return sin(x)/cos(x)
pi=3.14

def _test():
    assert (sin(0)) == 0.0
    assert (cos(0)) == 1.0
    assert (tan(0)) == 0.0
_test()
angle=float(input("Enter angle in degrees: "))
distance=float(input("Enter distance from pole: "))

print((tan(pi/180*angle)*distance ),"metres")         