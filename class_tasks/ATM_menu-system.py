print("Welcome to ABC branch ATM\n")
balance = 1000
while True:
    print("ATM menu")
    print("____________")
    print("Enter 1, to check balance")
    print("Enter 2, to load balance")
    print("Enter 3, to exit")
    n = int(input("Plese enter (1/2/3) according to your preference:  "))
    
    if n == 1:
        print(f"Your current balance is Rs. {balance}")
    elif n == 2:
        add = int(input("Enter the balance you want to deposite: Rs. "))
        balance+= add
        print(f"Your current balance is Rs. {balance}")
    elif n ==3:
        print("Thank you wonderful customer")
        break
    else:
        print("Invalid input!\nPlease choose between (1/2/3) according to your preference: ")
        continue
