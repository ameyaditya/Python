"""
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
"""

def max_activity_selection(s,f):
    print("following activities can be performed:")
    i = 0
    print (i, end=" ")
    for j in range(len(s)):
        if s[j] >= f[i]:
            print (j,end =" ")
            i = j

s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]

max_activity_selection(s,f)
