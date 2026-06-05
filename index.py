
#Python Lists :-
#List is a collection which is ordered and changeable. Allows duplicate members.

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#list length
print("Length : ",len(mylist))

#Get items
print("All values : ",mylist)
print("Single Item : ",mylist[1])
print("Negetive indexing : ",mylist[-1])
print("Range of values : ",mylist[2:5])
print("Range from beginning : ",mylist[:4])
print("Range to end : ",mylist[2:])
print("Negative range : ",mylist[-4:-1])

# change items
mylist[1] = "blackcurrant"
mylist[2:4] = ["jack fruit", "watermelon"]
print("After change : ",mylist)

#add items
mylist.append("blueberry")
mylist.insert(4, "pineapple")
print("After add : ",mylist)

#Remove items
mylist.remove("mango")
print("After remove : ",mylist)

#check item
print("Checking an item in list:")
if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")

#Loop list
print("Print items using loop:")
for x in mylist:
  print(x)
                