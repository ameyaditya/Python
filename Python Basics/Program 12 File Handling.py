#file handing

def file_handling1():
    #to read the content we need to open and read using read method
    file = open("File_Handling_example.txt",'r')
    content = file.read()
    print(content)
    #we can use seek function to reset file pointer
    file.seek(0)
    #to store all the data into a list, we use the following function
    content2 = file.readlines()
    #applying list comprehension
    content2 = [i.rstrip("\n") for i in content2]
    print(content2)
    file.close()

def file_handling_read_practice():
    file = open("fruits.txt",'r')
    content = file.readlines()
    content = [j.rstrip("\n") for j in content]
    for i in content:
        print(i)
    file.close()
    #or
    file = open("fruits.txt",'r')
    content = file.read()
    print(content)
    file.close()

def file_handling_read_practice2():
    file = open("fruits.txt",'r')
    content = file.readlines()
    content = [i.rstrip("\n") for i in content]
    content = [len(i) for i in content]
    for i in content:
        print(i)
    file.close()

def file_handling2():
    #writing content into a text file
    file = open("Write_example.txt",'w')
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.close()
    #the write method creates a file if it doesnt exist or overwrites on an existing file.
    #the 'w' mode is not an append function.

def file_handling_writing_lists():
    #writing content into a text file
    file = open("Write_example_lists.txt",'w')
    l = ["file 1","file 2","file 3"]
    for i in l:
        file.write(i+"\n")
    file.close()
    #the write method creates a file if it doesnt exist or overwrites on an existing file.
    #the 'w' mode is not an append function.

def file_handling_appending_to_textfiles():
    file = open("Write_example.txt",'a')
    #here the 'a' stands for appending to a string
    file.write("This text is appended")
    file.close()

def file_handling_other_methods():
    #r+ opens in both reading and writing mode
    # w+ opens in writing and reading
    #w+ overwrites the existing files
    #a+ works in both appending and reading mode
    print("nothing")
def file_handling_with_statement():
    with open("Write_example.txt",'a+') as file:
        file.seek(0)
        content = file.read()
        file.write("\nAdded using with statement")

file_handling_with_statement()
