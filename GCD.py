#Compute GCD with naive aproach recursion

'''def hcfnaive(a,b):
    if b==0:
        return a
    else:
        return hcfnaive(b, a % b)
    
a = int(input("Enter a : "))
b = int(input("Enter b : "))

#print("GCD of:" +a "and" +b "is: " )

print(hcfnaive(a,b))'''

#Compute GCD with loops

'''def computeGCD(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range (1, small+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

a = int(input("Enter a : "))
b = int(input("Enter b : "))

#print("GCD of:" +a "and" +b "is: " )

print(computeGCD(a,b))'''


#Euclidean algorithm to find GCD
def computeGCD(a, b):
    while(b):
        a, b = b, a % b
    return a

a = int(input("Enter a : "))
b = int(input("Enter b : "))

print("GCD of:",a, "and",b, "is: " )

print(computeGCD(a,b))