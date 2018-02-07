#loops
#for loop
#lets create a list first

def for_loop1():
    emails = ["me@email.com","he@was.com","she@coldmail.com"]
    for email in emails:
        print(email)
        #this is the most simple example of for loop and shows the simple syntax of for loop

#lets make a function which prints emails which have only gmail in them
def for_loop2():
    emails = ["me@gmail.com","he@was.com","she@coldmail.com","they@gmail.com"]
    for email in emails:
        if 'gmail' in email:
            print(email)


#while loops

#program to loop until user enter correct password
def while_loop1():
    password = ''
    while password != 'python123':
        password = input("Enter password: ")
        if password == "python123":
            print("You logged in")
        else:
            print("sorry try again.")
#loop with multiple lists

def multiple_list_loop():
    names = ["james","john","jack"]
    email = ["gmail","hotmail","yahoo"]
    for i,j in zip(names,email):
        print(i,j)
multiple_list_loop()
