#Dictionaries
l = [1,2,3]
#here l is a list
#in dictionaries, instead of python giving the indexing we can give our own indexing
d = {"name":"john","surname":"andrews"}
#here naem and surname are known as keys and john and andrews is known as values
#so it is a collection is keys and values
print(d["name"])
#in dictionaries the order of the keys and values are not always same.
#prinitng d["name"] is same as accessing d[0] by indexing
#lists and tuples can be values of a dictionaries
x = {"list1":l,"tuple":("one","two","three")}
print(x["tuple"])
print(x["tuple"][1])
#the output will give use the second element in that particular tuple
