1. Student Marks
def calculate_average(a, b, c, d, e):
    return (a + b + c + d + e) / 5
avg = calculate_average(50, 60, 70, 80, 90)
print("Average:", avg)
if avg >= 40:
    print("Pass")
else:
    print("Fail")

2. Even or Odd
def check_number(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_number(10))
print(check_number(7))
print(check_number(24))
print(check_number(15))
print(check_number(8))

3. Shopping Bill
def calculate_bill(price, quantity):
    total = price * quantity
    if total > 5000:
        total = total - (total * 10 / 100)
    return total
print(calculate_bill(2000, 3))

4.Find Largest Number
def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print(find_largest(10, 25, 15))
