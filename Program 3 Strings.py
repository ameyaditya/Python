#strings
#everything that goes inside a quote is known as a string
print("Hello")
name = "amey"
# strings can be stored in a variable
print(name)
#strings have a few methods associated with them
# to use the methods on strings we use the dot operator
name = name.replace("a", "A")
#the above code will replace all the instances of the letter 'a' with an uppercase letter 'A' in the variable name
print(name)
# to view all the methods or function that can be used on a particular variable or object, we can view them by the
#following command 'dir(name)' / 'dir("")' (which is an empty string) Note: this has to be done is the cmd interactive session
print(name.upper())#this will convert all the letter is a string to uppercase

#again if we want to know what a particular function can do we can use the following command in the interactive session
# help("".replace)

#strings also support operators
#indexing the strings
#every character in the string starts indexing from zero
#an individual character can be access from a string using name[]
#example name[2]
#we can use name[-1] to access from the end of the string and name[-2] to extract the second last character from the strings
#more than one character can be extracted using name[0:2] which means from index 0 to index (2-1) that is 1
#in general it is from 0 to n-1 as splitting is upperbound
#we can also pass name[:] to get all the characters
#name[:3]everything from first till third index
# also name[3:] and also negative indexing can be used
