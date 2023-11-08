a = int(input("Enter a number: "))

factors = []

for i in range(1,a+1):
    if a%i == 0:
        factors.append(i)

print("Factors of ", a, "are ", factors)