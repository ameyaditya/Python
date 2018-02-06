#try and except can be used to handles errors in python
#check this example program
def divide(a,b):
    try:
        return(a/b)
    except ZeroDivisionError:
        return"you are trying to divide by zero"

print(divide(1,2))
print(divide(2,0))
#in the above example if we pass 1,0 or n,0 as the arguments in function call we would encounter an error
#Zerodivisionerror
#without the try and catch inside the definition

#further more  we can make out except fucntion more specific by mentioning the error we want to except
#so if we encounter any other type of error it wont except that
