#Make a dictionary and save it to the file without using json
# content are saved in python formate mean the saved data type is in "string"

def dict_file():
    my_dict={}
    for i in range(5):
        name = input("Enter the name: ")
        age = int(input("Enter his/her age: "))
        my_dict.update({name : age})
    return my_dict

with open ("dictionary.txt", "w") as f:
    content = dict_file()
    f.write(str(content))


    