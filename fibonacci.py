n = 10

a = 0
print(a, end=" ")

b = 1
print(b, end=" ")

for i in range(1, n+1):
    nextNumber = a + b
    print(nextNumber, end=" ")
    a = b
    b = nextNumber
