#lists
# lists are sequences of items
c = ["hi",  2, "Hello"]
#list is a collection of items may or may not belong to different datatypes
#they can be considered to be kind of as arrays is c++
print(c)
#other onjects can also be stored in a lists and many more,
#even lists have indexing and is same as indexing strings
print(c[1])
#and all the rules of indexing of the strings apply to lists too
#in the python interactive shell we can see the attributes/methods of the list by dir(list)
#and help can be used to understand each item in a list
#the append method can be used to add items into an alreaady existing lists
c.append(3)
print(c)

#we can remove items from a list
c.remove("hi")
print(c)
