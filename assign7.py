# 1. Even or Odd
a = int(input("Enter number: "))
print("Even" if a % 2 == 0 else "Odd")


# 2. Larger Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a if a > b else b)


# 3. Pass or Fail
marks = int(input("Enter marks: "))
print("Passed" if marks >= 40 else "Failed")


# 4. Positive or Negative
a = int(input("Enter number: "))
print("Positive" if a >= 0 else "Negative")


# 5. Discount
amount = int(input("Enter amount: "))
print("Eligible" if amount >= 5000 else "Not Eligible")


# 6. Day using match-case
day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")


# 7. Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator: ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")


# 8. Grade
grade = input("Enter grade: ")

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")


# 9. Traffic Signal
signal = input("Enter signal: ")

match signal:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid signal")
