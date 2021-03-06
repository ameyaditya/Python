#We are using a json data, which is a collection of all the words and meanings as a python dictionary.
#program to make an interactive dictionary

#importing the json library
import json
#using the get_close_matches function from difflib library to get the closest match of the wrong word entered by the user.
from difflib import get_close_matches as gcm

#used the json module to import the data from data.json
data = json.load(open("data.json",'r'))

#function to return the definitions for the word entered by the user.
def return_definition(word):
    #converting all words to lowercase to avoid problems
    word = word.lower()
    #setting the cutoff value for get_close_matches()
    error_tolerance = 0.7
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(gcm(word,data.keys(),cutoff = error_tolerance))!=0:
        #Asking the user if he had made a typo and finding the closest match to it.
        #print("Did u mean {0}?Enter Y(yes) or N(no).".format(gcm(word,data.keys(),cutoff = 0.8)[0]))
        reply = input("Did u mean {0}?Enter Y(yes) or N(no).".format(gcm(word,data.keys(),cutoff = error_tolerance)[0]))
        if reply == 'Y':
            return data[gcm(word,data.keys(),cutoff = error_tolerance)[0]]
        elif reply == 'N':
            return "The word doesn't exist. PLease check again."
        else:
            return "Didn't understand your entry."
    else:
        return ["The word doesn't exist. Please check again."]

#taking user's input
word = input("Enter a Word to search in the Dictionary: ")

definitions = return_definition(word)

if type(definitions) == list:
    for item in definitions:
        print(item)
else:
    print(definitions)
