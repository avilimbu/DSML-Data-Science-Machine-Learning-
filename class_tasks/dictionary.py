
#class task

#creating the dictionary to store student name, age, and faculty.

student ={ 
    "name" : "shyam",
    "age" : 21,
    "faculty" : "DSML"
}

#creating a new key called phone in an existing directory
student["phone"] =98777455

#updating the value of age in a directory
student["age"] = 25

#Remove key named city from a dictionary using del
student["city"] = "kathmandu"

print(f"values in student = {student}")

del student["city"]
print(f"After key city deletion values in student = {student}")

#checking whether the key email exists in a dictionary
is_find = "email" in student
if is_find==True:
    print("Yes, the email key is in the student dictionary")

else:
    print("No, the email key is not in the student dictionary")