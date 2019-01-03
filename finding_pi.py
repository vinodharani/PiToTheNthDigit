import math

def calculate_pi(num):
    return round(math.pi, num)

try:
    num = int(input("Enter the N-th digit of Pi you want to know: "))
    print(calculate_pi(num))
except ValueError:
    print("Invalid input")
