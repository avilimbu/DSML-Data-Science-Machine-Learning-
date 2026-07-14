#checking if num is positive or even
num = int(input("enter the number: "))
if num >=0 and (num%2==0):
  print("positive and even")
elif num >=0 and (num%2!=0):
  print("positive and odd")
else:
  print("you entered negative number.")

#if a user is not logged in
logged_in = False
if not logged_in:
  print("please login")
else:
  print("welcome")

#check if age is between 18 and 60 using and
age = int(input("enter your age: "))
if age >=18 and age <=60:
  print("you are in the criteria")
else:
  print("you are not in criteria")

#check if a day is saturday or sunday using or
day = input("enter the day in a week: ").strip().capitalize()
if day == "Saturday" or day == "Sunday":
  print("It is a weekend")
else:
  print("It is not a weekend")