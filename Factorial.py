number = int(input("Enter number to find Factorial "))
factorial = 1

for i in range(1, number+1):
    factorial *= i

print("Factorial is:", factorial)
