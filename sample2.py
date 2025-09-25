"""
sample2.py
Author: Jacob Catayoc
Date:   September 11, 2025
"""
dividend = int(input("Enter dividend number: "))
divisor = int(input("Enter divisor number: "))
answer = divmod(dividend, divisor)

print("""There are 3 methods in displaying the answer using divmod.

1. Using + operator
2. Using , in print()
3. Using string interpolation""")
# Method 1
print("Quotient: " + str(answer[0]))
print("Remainder: " + str(answer[1]))

# Method 2
print("Quotient:", answer[0])
print("Remainder:", answer[1])

# Method 3
print(f"Quotient: {answer[0]}")
print(f"Remainder: {answer[1]}")