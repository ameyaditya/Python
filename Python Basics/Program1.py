#Variables and data types
greeting = "Hello"
print(greeting)
#variables can begin with underscores and texts
#but vairables cannot begin with numbers, but can have numbers in the middle and end

#getting text from user
greeting2 = input("Write a Greeting: ")#the input function is used to take input from the user at runtime
print(greeting2)

#the above example covered the use of strings,
#in this sectioon we will see the use of numbers
a = 2
b = 3
#we cannot just write a+b to print the sum of two numbers, we have to use the following command
print(a+b)
print(type(a))#the type command gives use the type of variables (int, float, string)
print("2"+"3")# will output 23 and not 5 as the two inputs are considered as strings.

#A small program using everything we learnt
age = input("Enter your age: ")
new_age = int(age) + 50
print("Your age after 50 years is ",(new_age))
#the input command always assigns the variable as a strings
#so in line two we have to cob=nvert the variable age to an integer type before adding it with 50
#in the print command, we can concatenate text and variables with a coma
