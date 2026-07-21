1.# Find the length of a string
s = input("Enter a string: ")
print("Length:", len(s))

2. #Print each character of a string on a new line

s = input("Enter a string: ")
for ch in s:
    print(ch)

# 3. Concatenate two strings without using the + operator
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("".join([s1, s2]))

# 4. Reverse a string
s = input("Enter a string: ")
print(s[::-1])

#5. Convert a string to uppercase
s = input("Enter a string: ")
print(s.upper())# 

# # 6. Convert a string to lowercase
# s = input("Enter a string: ")
# print(s.lower())

# 7. Check if a string contains only digits
s = input("Enter a string: ")
if s.isdigit():
    print("Only digits")
# else:
    print("Not only digits")

    # 8. Count the number of spaces in a string
s = input("Enter a string: ")
print("Spaces:", s.count(" "))

# 9. Remove all spaces from a string
s = input("Enter a string: ")
print(s.replace(" ", ""))

# 10. Replace all occurrences of a character
s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print(s.replace(old, new))

# 11. Count the number of vowels
s = input("Enter a string: ")
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

# 12. Count uppercase and lowercase letters
s = input("Enter a string: ")
upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

# 12. Count uppercase and lowercase letters
s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

# 13. Find the first occurrence of a character
s = input("Enter a string: ")
ch = input("Enter character: ")
print(s.find(ch))

14. #Find the last occurrence of a character
a = "messi"
b = "s"
c = a.rfind(b)
print("Last occurrence:", c)
      
# 15. Check if a string starts with a vowel
s = input("Enter a string: ")
if s[0].lower() in "aeiou":
    print("Starts with a vowel")
else:
    print("Does not start with a vowel")

    # 16. Check if a string is a palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    # 17. Count the number of words in a string
s = input("Enter a string: ")
print("Words:", len(s.split()))

# 18. Remove duplicate characters
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)

# 19. Count the total number of digits and characters
s = input("Enter an alphanumeric string: ")
digits = 0
letters = 0
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
print("Digits:", digits)
print("Characters:", letters)

