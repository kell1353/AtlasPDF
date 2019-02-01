import numpy as np
import math
import sys

# Reference Page for distributions: 
# https://support.minitab.com/en-us/minitab/18/help-and-how-to/probability-distributions-and-random-data/how-to/probability-distributions/methods-and-formulas/methods-and-formulas/

def C(n1,n2):
  return math.factorial(n1)/(math.factorial(n2)*math.factorial(n1-n2))

print("\nDiscrete Uniform Distribution - 1")
print("Binomial Distribution - 2")
print("Negative Binomial Distribution - 3")
print("Geometric Distribution - 4")
print("Hypergeometric Distribution - 5")
print("Poisson Distribution - 6")
print("Continuous Uniform Distribution - 7")
print("Exponential Distribution - 8")

Distribution = input("\nWhat distribution do you want to use?: ")
  
################################################################################################################
################################################################################################################
  
"""Discrete Distributions"""

################################################################################################################
################################################################################################################

if Distribution == '1':

    "Uniform Distribution"""

    def uniform_discrete(a,b):
      return 1/(b-a)                            # b > a

    """Inputs for variables"""
    a1 = input("What is the smallest endpoint value?: ")
    b1 = input("What is the largest endpoint value?: ")            

    mean = (a1+b1)/2
    variance = ((b1-a1)**2)/12

    print("\nThe probability is: " + str(uniform_discrete(a1,b1)))
    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))
    

##################################################################################################
if Distribution == '2':

    """Binomial Distribution"""

    def binomial(n, p, x):
        return C(n,x)*(p**(x))*((1-p)**(n-x))

    """Inputs for variables"""
    n1 = int(input("How many independent trials?: "))
    p1 = float(input("What is the probability of event?: "))
    e = input("Is P(X = x) (type: e), Is P(a ≤ X ≤ b) (type: r)?: ")

    if e == 'e':
        x1 = int(input("How many events (x) in the " + str(n1) + " independent trials?: "))           #(x = 0,1,2,...,n)
        print("\nThe probability is: " + str(binomial(n1, p1, x1)))

    # the CDF (Cumulative Distribution Function) solution
    if e == 'r':            
        probability_list = []
        lower_endpoint = int(input("Least number of events?: "))
        upper_endpoint = int(input("Most number of events?: "))
      
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = binomial(n1,p1,i)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))
      
    mean = n1*p1
    variance = (n1*p1)*(1-p1)
    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))
    

##################################################################################################
if Distribution == '3':

    """Negative Binomial Distribution"""

    def negative_binomial1(r, x, p):
        return C(x-1,r-1)*((p**r)*((1-p)**(x-r)))

    def negative_binomial2(r, y, p):
        return (C(y+r-1,r-1))*(p**r)*((1-p)**(y))
      
    """Inputs for variables"""
    p1 = float(input("What is the probability of event?: "))
    r1 = int(input("Number of successess you want to produce (r)?: "))    
    e = input("Is P(X = x) (type: e), or P(a ≤ X ≤ b) (type: r), or P(X ≥ x) (type: g)?: ")
    Q = input("\nIf question is: Number of trials to produce r events? (x), or \nNumber of non-events that occur before you observe the first r events? (y): ")


############## Negative Binomial  problem Type 1 ##############
    

    if e == 'e' and Q == 'x':
        x1 = int(input("Number of trials to produce r successes?: "))                                                             #(x = r,r+1,r+2,...)
        print("\nThe probability is: " + str(negative_binomial1(r1, x1, p1)))
        mean = r1/p1
        variance = (r1*(1-p1))/p1**2

    probability_list = []
    # the CDF (Cumulative Distribution Function) solution 1
    if (e == 'r') and Q == 'x':
        lower_endpoint = int(input("Least number of trials to acheive r successes? (x ≥ r): "))                             
        upper_endpoint = int(input("Most number of trials to acheive r successes?: "))
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = negative_binomial1(r1, i, p1)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))
        mean = r1/p1
        variance = (r1*(1-p1))/p1**2
        
    if (e == 'g') and Q == 'x':
        lower_endpoint = r1                           
        upper_endpoint = int(input("Least number of trials to acheive r successes?: "))
        for i in range(lower_endpoint,upper_endpoint):
            p_x = negative_binomial1(r1, i, p1)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(1 - sum(probability_list)))
        mean = r1/p1
        variance = (r1*(1-p1))/p1**2


############## Negative Binomial  problem Type 2 ##############


    if e == 'e' and Q == 'y':
        y1 = int(input("Number of non-events that occur before you observe r successes?: "))        #(y = 0,1,2,...)
        print("\nThe probability is: " + str(negative_binomial2(r1, x1, p1)))
        mean = (r1*(1-p1))/p1
        variance = (r1*(1-p1))/p1**2      
      
    # the CDF (Cumulative Distribution Function) solution 2
    if (e == 'r') and Q == 'y':
        lower_endpoint = int(input("Least number of non-events that occur before you observe r successes?: "))
        upper_endpoint = int(input("Most number of non-events that occur before you observe r successes?: "))
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = negative_binomial2(r1, i, p1)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))
        mean = (r1*(1-p1))/p1
        variance = (r1*(1-p1))/p1**2
        
    if (e == 'g') and Q == 'y':
        lower_endpoint = r1                           
        upper_endpoint = int(input("Least number of non-events that occur before you observe r successes? : "))
        for i in range(lower_endpoint,upper_endpoint):
            p_x = negative_binomial2(r1, i, p1)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(1 - sum(probability_list)))
        mean = (r1*(1-p1))/p1
        variance = (r1*(1-p1))/p1**2 

    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))
    

##################################################################################################
if Distribution == '4':

    """Geometric Distribution"""

    def geometric1(x, p):
      return p*((1-p)**(x-1))

    def geometric2(y, p):
      return p*((1-p)**(y))

    """Inputs for variables"""
    p = float(input("What is the probability of event?: "))
    e = input("Is P(X = x) (type: e), Is P(a ≤ X ≤ b) (type: r), Is P(X ≥ x) (type: g)?: ")
    Q = input("\nIf question is: Number of trials to produce one successful event? (x), or is: \nNumber of non-events that occur before you observe the first event? (y): ")


############## Geometric problem Type 1 ##############


    if e == 'e' and Q == 'x':
        x = int(input("Number of trials to produce one successful event (x > 0)?: "))                                                    #(x = 1,2,3,...)
        print("\nThe probability is: " + str(geometric1(x,p)))
        mean = 1/p
        variance = (1-p)/p**2
      
    probability_list = []  
    # the CDF (Cumulative Distribution Function) solution  1
    if e == 'r' and Q == 'x':
        lower_endpoint = int(input("Least number of trials to produce one successful event (x > 0)?: "))                             
        upper_endpoint = int(input("Most number of trials to produce one successful event?: "))
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = geometric1(i,p)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))
        mean = 1/p
        variance = (1-p)/p**2
        
    if e == 'g' and Q == 'x':
        lower_endpoint = 1                        
        upper_endpoint = int(input("Least possible number of trials to produce one successful event?: "))
        for i in range(lower_endpoint,upper_endpoint):
            p_x = geometric1(i,p)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(1 - sum(probability_list)))
        mean = 1/p
        variance = (1-p)/p**2


############## Geometric problem Type 2 ##############

  
    if e == 'e' and Q == 'y':
        y = int(input("Number of non-events that occur before you observe the first successful event?: "))      #(y = 0,1,2,...)
        print("\nThe probability is: " + str(geometric2(y,p)))
        mean = (1-p)/p
        varaiance = (1-p)/p**2
      
    probability_list = []  
    # the CDF (Cumulative Distribution Function) solution  2
    if e == 'r' and Q == 'y':
        lower_endpoint = int(input("Least number of non-events that occur before you observe the first successful event?: "))                             
        upper_endpoint = int(input("Most number of non-events that occur before you observe the first successful event?: "))
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = geometric2(i,p)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))
        mean = (1-p)/p
        variance = (1-p)/p**2
        
    if e == 'g' and Q == 'y':
        lower_endpoint = 0                       
        upper_endpoint = int(input("Least possible number of non-events that occur before you observe the first successful event?: "))
        for i in range(lower_endpoint,upper_endpoint):
            p_x = geometric2(i,p)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(1 - sum(probability_list)))
        mean = (1-p)/p
        variance = (1-p)/p**2

    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))
    
  
################################################################################################## 
if Distribution == '5':

    """Hypergeometric Distribution"""

    def hypergeometric(N1, N2, n, x):
        return (C(N1, x)*C(N2, n-x))/C(N,n)

    """Inputs for variables"""
    N = int(input("Population size?: "))                                      # Population size
    N1 = int(input("Number of possible successes within the population size?: "))
    n = int(input("Sample size selected from population?: "))
    N2 = N-N1                                                             # Number of non-events in a population 
    e = input("Is P(X = x) (type: e), Is P(a ≤ X ≤ b) (type: r)?: ")

    if e == 'e':
        x = int(input("Number of successesful events within the sample size?: "))              # (max(0,n-(N+N1)) <= x <= min(n,N1)
        print("\nThe probability is: " + str(hypergeometric(N1, N2, n, x)))

    # the CDF (Cumulative Distribution Function) solution
    if e == 'r':
        probability_list = []
        lower_endpoint = int(input("Least number of events within the sample size?: "))
        upper_endpoint = int(input("Most number of events within the sample size?: "))
        if upper_endpoint > N1:
            print("\nERROR: Upper endpoint to large for sample size, please restart from beginning.")
            sys.exit()
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = hypergeometric(N1, N2, n, i)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))

    mean = n*(N1/N)
    variance = n*((N-n)/(N-1))*(N1/N)*(N2/N)
    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))
    

##################################################################################################
if Distribution == '6':

    """Poisson Distribution"""

    def poisson(lambda1, x):
      return ((math.exp(-lambda1))*(lambda1**x))/math.factorial(x)

    """Inputs for variables"""
    lambda1 = int(input("What is the constant rate of occurence?: "))                 # lambda > 0
    e = input("Is P(X = x) (type: e), Is P(a ≤ X ≤ b) (type: r), Is P(X ≥ x) (type: g)?: ")

    if e == 'e':
      x1 = int(input("Number of events (x) in that constant rate of occurence?: "))        #(x = 0,1,2,...)
      print("\nThe probability is: " + str(poisson(lambda1, x1)))

    # the CDF (Cumulative Distribution Function) solution        
    probability_list = []
    if e == 'g':
        lower_endpoint = 0
        upper_endpoint = int(input("Least possible number of events?: "))
        if upper_endpoint - 1 == 0:
            print("\nThe probability is: " + str(1 - poisson(lambda1, lower_endpoint)))     
        else:
            for i in range(lower_endpoint,upper_endpoint):
                p_x = poisson(lambda1, i)
                probability_list.append(p_x)
            print("\nThe probability is: " + str(1 - sum(probability_list)))
            
    if e == 'r':
        lower_endpoint = int(input("Least number of events?: "))
        upper_endpoint = int(input("Most number of events?: "))
        for i in range(lower_endpoint,upper_endpoint+1):
            p_x = poisson(lambda1, i)
            probability_list.append(p_x)
        print("\nThe probability is: " + str(sum(probability_list)))

    mean = lambda1
    variance = lambda1
    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))
    

################################################################################################################
################################################################################################################

"""Continuous Distributions"""

################################################################################################################
################################################################################################################

if Distribution == '7':

    """Uniform Distribution"""

    def uniform_cont(x, a, b):
        return (x - a)/(b - a)

    """Inputs for variables"""
    e = input("Is (X ≤ x) (type: l), or P(a ≤ X ≤ b) (type: r), or P(X ≥ x) (type: g)?: ")
    lower_endpoint_a = float(input("Lower endpoint of uniform range (a)?: "))
    upper_endpoint_b = float(input("Upper endpoint of uniform range (b)?: "))

    # the CDF (Cumulative Distribution Function) solution
    if e == 'r':
        lower_endpoint_x = float(input("Lower endpoint of x time range?: "))
        upper_endpoint_x = float(input("Upper endpoint of x time range?: "))
        p_x = uniform_cont(upper_endpoint_x, lower_endpoint_a, upper_endpoint_b) - uniform_cont(lower_endpoint_x, lower_endpoint_a, upper_endpoint_b)
        print("\nThe probability is: " + str(p_x))
      
    if e == 'g':
        x1 = float(input("What is the least amount of time we need to wait before a given event occurs?: "))        # (x > 0)
        if x1 <  lower_endpoint_a or x1 > upper_endpoint_b:
            print("\nThe probability is: 0")
        else:
            print("\nThe probability is: " + str(1 - uniform_cont(x1, lower_endpoint_a, upper_endpoint_b)))
      
    if e == 'l':  
        x1 = float(input("What is the greatest amount of time we need to wait before a given event occurs?: "))        # (x > 0)
        print("\nThe probability is: " + str(uniform_cont(x1, lower_endpoint, upper_endpoint)))
      
    mean = (lower_endpoint_a + upper_endpoint_b)/2
    variance = ((upper_endpoint_b - lower_endpoint_a)**2)/12
    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance))   
  

##################################################################################################
if Distribution == '8':

    """Exponential Distribution"""

    def exponential(lambda1, x):
        return (1 - np.exp((-lambda1)*x))

    """Inputs for variables"""
    lambda1 = float(input("What is the constant rate of occurence (lambda)?: "))                 # lambda > 0
    e = input("Is P(X = x) (type: e), or P(a ≤ X ≤ b) (type: r), or P(X ≥ x) (type: g)?: ")

    if e == 'e':
        x1 = float(input("What is the time we need to wait before a given event occurs?: "))        # (x > 0)
        print("\nThe probability is: " + str(exponential(lambda1, x1)))

    # the CDF (Cumulative Distribution Function) solution     
    if e == 'g':
        lower_endpoint = 0
        upper_endpoint = float(input("Least amount of time?: "))
        p_x = exponential(lambda1, upper_endpoint) - exponential(lambda1, lower_endpoint)
        print("\nThe probability is: " + str(1 - p_x))
        
    if e == 'r':
        lower_endpoint_a = float(input("Least amount of time (a)?: "))
        upper_endpoint_b = float(input("Most amount of time (b)?: "))
        p_x = exponential(lambda1, upper_endpoint_b) - exponential(lambda1, lower_endpoint_a)
        print("\nThe probability is: " + str(p_x))

    mean = 1/lambda1
    variance = 1/lambda1**2
    print("The mean is: " + str(mean))
    print("The variance is: " + str(variance)) 


##################################################################################################

"""Normal Distribution"""

##################################################################################################

"""Gamma Distribution"""
