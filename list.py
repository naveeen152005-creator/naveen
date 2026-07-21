# index()
li = [1, 2, 3, 2, 4, 2, 5]
print(li.index(3))


# reverse()
li = [1, 2, 3, 2, 4, 2, 5]
li.reverse()
print(li)


# sort (descending)
li = [10, 2, 3, 2, 4, 2, 5, 0]
li.sort(reverse=True)
print(li)


# accessing
li = [9, 4, 3, 5, 6, 2]
print(li[3])      # Element at index 3
print(li[-2])     # Second last element
print(li[0:3])    # Elements from index 0 to 2
print(li[:])      # Entire list
print(li[3:])     # Elements from index 3 to end
print(li[:3])     # Elements from start to index 2
print(li[::-1])   # Reverse list using slicing

#create a list of 3 items
items=["orange","banana","apple"]
print(items)
print("choices\n1.add\n2.delete\n3.update\n4.exit")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Add elements:")
    additems=input("Enter item to add:")
    items.append(additems)
    print(items)
elif choice==2:
     print("Delete elements:")
     delitems=input("Enter item to delete:")
     items.remove(delitems)
     print(items)
elif choice==3:
     print("Update elements:")
     olditems=input("Enter item to be updated:")
     newitems=input("Enter new item:")
     b=items.index(olditems)
     items[b]=newitems
     print(items)
elif choice==4:
     print("exit")
else:
     print("invalid choice")
















