 # 1. Create a list
# n = int(input("Enter number of elements: "))
# li = []

# for i in range(n):
#     x = input("Enter element: ")
#     li.append(x)

# print(li)

#2. Add an item
# li = ["Apple", "Mango", "Orange"]
# x = input("Enter item: ")
# li.append(x)
# print(li)

3#. Insert a color
# colors = ["Red", "Blue", "Green", "Yellow", "Black"]
# pos = int(input("Enter position: "))
# color = input("Enter color: ")
# colors.insert(pos, color)
# print(colors)

#4. Combine two lists
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

#5.Remove a fruit if it exists
# fruits = ["Apple", "Mango", "Orange", "Banana"]
# fruit = input("Enter fruit: ")
# if fruit in fruits:
#     fruits.remove(fruit)
#     print(fruits)
# else:
#     print("Item Not Found")

#6. Remove the last element
# numbers = [10, 20, 30, 40, 50]
# removed = numbers.pop()
# print("Removed:", removed)
# print("Updated list:", numbers)

#7. Search for a student name
# students = ["Abhinav", "vinayak", "Adarsh", "naveen"]
# name = input("Enter student name: ")
# if name in students:
#     print("Student Found")
# else:
#     print("Student Not Found")

#8. Count duplicate values
# li = [1, 2, 3, 2, 4, 2, 5]
# element = int(input("Enter element: "))
# print("Count:", li.count(element))

#9. Replace a subject
# subjects = ["Maths", "Physics", "Chemistry"]
# old = input("Enter old subject: ")
# new = input("Enter new subject: ")
# if old in subjects:
#     i = subjects.index(old)
#     subjects[i] = new
# print(subjects)

# 10. Reverse list
# li = [1, 2, 3, 4, 5]
# li.reverse()
# print(li)

# 11. Largest number
# i = [10, 25, 5, 40]
# print(max(li))

# 12. Smallest number
# li = [10, 25, 5, 40]
# print(min(li))

# 13. Sum of elements
# li = [10, 20, 30, 40]
# print(sum(li))

# 14. Average
# li = [10, 20, 30, 40]
# average = sum(li) / len(li)
# print(average)

# 15. Count even and odd
# li = [1, 2, 3, 4, 5, 6]
# even = 0
# odd = 0
# for x in li:
#     if x % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even:", even)
# print("Odd:", odd)

# 16. Positive and negative
# li = [-5, 10, -3, 8]
# positive = []
# negative = []
# for x in li:
#     if x >= 0:
#         positive.append(x)
#     else:
#         negative.append(x)
# print("Positive:", positive)
# print("Negative:", negative)

# 17. Ascending and descending
# li = [5, 2, 8, 1, 9]
# li.sort()
# print("Ascending:", li)
# li.sort(reverse=True)
# print("Descending:", li)

# 18. Remove duplicates
# li = [1, 2, 2, 3, 4, 4, 5]
# unique = []
# for x in li:
#     if x not in unique:
#         unique.append(x)
# print(unique)

# 19. Menu-driven program
# li = ["Apple", "Mango", "Orange"]
# while True:
#     print("1. Add")
#     print("2. Delete")
#     print("3. Update")
#     print("4. Search")
#     print("5. Display")
#     print("6. Exit")
#     choice = int(input("Enter choice: "))
#     if choice == 1:
#         x = input("Enter item: ")
#         li.append(x)
#     elif choice == 2:
#         x = input("Enter item: ")
#         li.remove(x)
#     elif choice == 3:
#         old = input("Enter old item: ")
#         new = input("Enter new item: ")
#         i = li.index(old)
#         li[i] = new
#     elif choice == 4:
#         x = input("Enter item: ")
#         if x in li:
#             print("Found")
#         else:
#             print("Not Found")
#     elif choice == 5:
#         print(li)
#     elif choice == 6:
#         break
#     else:
#         print("Invalid choice")

# # 20. Second largest
# li = [10, 25, 5, 40, 15]
# li.sort()
# print("Second largest:", li[-2])
