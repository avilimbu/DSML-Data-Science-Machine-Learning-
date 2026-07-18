# Make a dictionary and save it to the file using json
# This saves the content in json formate i.e type is in dictionary.
# so that any language can understand it. 

import json

def dict_file():
    my_dict = {}

    for i in range(5):
        name = input("Enter the name: ")
        age = int(input("Enter his/her age: "))

        my_dict[name] = age

    return my_dict

# creating and writing in the file 
with open("dictionary_json.txt", "w") as f:
    content = dict_file()

    #Telling save the content in f(file) in json format
    json.dump(content, f)