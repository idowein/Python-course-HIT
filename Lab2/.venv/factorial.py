# Factorial - n!

# n! = 1 * 2 * 3 * ... * n

# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 3! = 1 * 2 * 3 = 6

n = int(input("Enter a positive integer: "))  # Example input: 5
result = 1

for i in range(1, n+1):  # 1, 2, 3, ..., n
    result *= i  # result = result * i

print(f"The factorial of {n} is {result}")