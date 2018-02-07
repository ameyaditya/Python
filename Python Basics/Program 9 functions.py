#functions
#defining a function starts with def keyword followed by the function name and
#parameters and colon
def minutes_to_hours(minutes):
    hours = minutes/60
    return hours

def seconds_to_hours(seconds):
    hours = seconds/3600
    return hours

def mins_to_hours(minutes,seconds):
    hours = minutes/60 + seconds/3600
    return hours
#after definiting the function, we can use it later
print(minutes_to_hours(140))
print(seconds_to_hours(4300))
print(mins_to_hours(120,4000))
#we get the output in hours

#a function can have more than one parameter.
#exaple function which takes seconds and minutes as parameters
#default arguments work the same way as it does in c++
#function need not always return a value\
