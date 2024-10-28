def sum(x):                                                                    
    sum=0
    for i in x:
        sum+=i
    return sum

def growth_rate(x,y):                                                                 
    return 2.5-0.4*x-0.1*y

population = [50, 1450, 1400, 1700, 1500, 600, 1200]                                   
population_nextyear=0                                                                 
current_population=0
max_population=0                                                                       
n=0

def _test():
    assert sum(population)== 7900
_test()

year=int(input("Enter nth year: "))

while n<year:
    for i in range(7):
        population[i]=population[i]*(1+growth_rate(i,n)/100)

    n+=1
else:
    print("Nth Year Population:",(sum(population)),"million")

population = [50, 1450, 1400, 1700, 1500, 600, 1200]

n=0
while current_population<=population_nextyear:
    current_population=sum(population)
    for i in range(7):
        population[i]=population[i]*(1+growth_rate(i,n)/100)

    n+=1
    population_nextyear=sum(population)
    
    if current_population<population_nextyear:    
        max_year=n
        max_population=population_nextyear

else:
    print("Maximum population:", max_population ,"million","\nPopulation will reach it's maximum after "+str(max_year)+" years") 
