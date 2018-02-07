#python can give current date and time with microsecond accuracy
#date and time are special objects in python

import datetime as dt
def part1():
    print(dt.datetime.now())
    #year, month, day, hour, minute,seconds, microsecond
    other_day = dt.datetime(2018,2,4,10,0,0,0)#manually passing a specific date.
    print(other_day)
    difference_in_time = dt.datetime.now()-other_day
    print(difference_in_time)
    print(difference_in_time.days)
    print(difference_in_time.total_seconds())

#practical application
#naming files with the current date
def create_file():
    filename = dt.datetime.now()
    with open(str(filename),"w") as file:
        file.write("")
        #if we run the following code we will get an error as datetime as special characters which are not allowed in filename
def create_file2():
    filename = dt.datetime.now().strftime("%Y %m %d")
    #this is the string format function to get desired strings out of datetime object
    with open(filename,"w") as file:
        file.write("")
def adding_certain_period_to_date():
    after_two_days = dt.datetime.now()+dt.timedelta(days = 2)
    print(after_two_days)

#now lets look into another module called time
import time
#used to perform delay operations in python
def adding_delay():
    lst = []
    for i in range(5):
        lst.append(dt.datetime.now().strftime("%H %M %S"))
        time.sleep(1)
    for i in lst:
        print(i)
"""
1. Please download the three text files attached in this lecture and put them in a folder. The first text file contains the text Content1 . The second contains Content2 and the third Content3 .

2. You should create a Python script that generates a new text file which should contain the content of all three text files. So the generated file should have this content:

Content1
Content2
Content3

In other words, your Python script should merge the three text files.

3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt

You have some tips in the next lecture and the solution in the lecture after that.
"""
import glob2
def exercise_problem():
    filenames = glob2.glob("Datetime_Practice/*.txt")
    #above code to access filenames in the datetime_practice folder
    with open(dt.datetime.now().strftime("%Y %m %d %H %M %S")+".txt","w") as file:
        for filename in filenames:
            with open(filename,"r") as ft:
                file.write(ft.read()+"\n")

exercise_problem()
