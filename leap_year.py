year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")
    
elif year % 100 == 0:
    print(year, "is not a Leap Year")
    
elif year % 4 == 0:
    print(year, "is a Leap Year")
    
else:
    print(year, "is not a Leap Year")

'''
Input: Enter a year: 2024
Output: 2024 is a Leap Year
'''
