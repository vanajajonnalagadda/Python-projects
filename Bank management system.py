print(" ")
customer_names=["Alex Smith","Kelvin Pal","John Doe","Jack Smith","Joseph Roy"]
customer_pins=["6776","8967","3422","9574","4523"]
customer_balances=[4000, 5000, 8000, 3000, 2000]
deposition=0
withdrawal=0
balance=0
counter_1=1
counter_2=5
i=0

while True:
    print(31*"*")
    print(5*"=","Welcome to YES bank",5*"=")
    print(31*"*")
    print(5*" ","1. Open a new account")
    print(5*" ","2. Deposit money")
    print(5*" ","3. Withdraw money")
    print(5*" ","4. Balance enquery")
    print(5*" ","5. Exit")
    print(31*"*")
    print(" ")
    option=int(input("Enter the option:"))




    if option==1:
        noc=int(input("Number of customers:"))
        i = i + noc
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - noc
        else:
            while counter_1 <= i:
                name=input("Enter your full name:")
                customer_names.append(name)
                pin=input("Enter your 4-digit pin as of your choice:")
                customer_pins.append(pin)
                balance=0
                deposition=int(input("Please input a value to deposit to start an account: "))
                balance = balance + deposition
                customer_balances.append(balance)
                print("\nName=", end=" ")
                print(customer_names[counter_2])
                print("Pin=", end=" ")
                print(customer_pins[counter_2])
                print("Balance=", end=" ")
                print(customer_balances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is added to  customers system.")
                print("Your pin is added to customers system.")
                print("Your balance is added to customers system.")
                print(" ")
                print("----New account created successfully !----")
                print(" ")
                print("Your name is avalilable on the YES bank customers list now : ")
                print(customer_names)
                print(" ")
                print("Note! Please remember the Name and Pin.")
                print("\n")
            OPTION = input("Please press 'enter key' to go back to main menu to perform another function or exit ...") 


    
        
    elif option == 2:
        name = input("Enter your name: ")
        pin = input("Enter your pin: ")
        
        found = False
        for k in range(len(customer_names)):
            if name == customer_names[k] and pin == customer_pins[k]:
                found = True
                print("Your current balance:", end=" ")
                print(customer_balances[k], end=" ")
                print("-/Rs")
                print(" ")
                deposition = int(input("Enter the amount you want to deposit: "))
                customer_balances[k] += deposition
                print(" ")
                print("\n----Deposited Successfully!----")
                print("Your New Balance: ", customer_balances[k], end=" ")
                print("-/Rs\n")
                break

        if not found:
            print("Your name and pin did not match! Please try again.")
            print(" ")
        OPTION = input("Please press enter key to go back to main menu to perform another function or exit ...")



    elif option == 3:
        name = input("Enter your name: ")
        pin = input("Enter your pin: ")

        found = False
        for j in range(len(customer_names)):
            if name == customer_names[j] and pin == customer_pins[j]:
                found = True
                print("Your current balance:", end=" ")
                print(customer_balances[j], end=" ")
                print("-/Rs\n")
                print("")
                withdrawal = int(input("Enter the amount you want to withdraw: "))
                if withdrawal > customer_balances[j]:
                    print("Your balance mentioned above is not enough in your account.")
                else:
                    customer_balances[j] -= withdrawal
                    print("\n----Withdraw Successful!----")
                    print("Your New Balance: ", customer_balances[j], end=" ")
                    print("-/Rs\n")
                break

        if not found:
            print("Your name and pin did not match! Please try again.")
            print(" ")
        OPTION= input("Please press enter key to go back to main menu to perform another function or exit ...")




    elif option == 4:
        name = input("Enter your name: ")
        pin = input("Enter your pin: ")

        found = False
        for k in range(len(customer_names)):
            if name == customer_names[k] and pin == customer_pins[k]:
                found = True
                print("Your current balance:", end=" ")
                print(customer_balances[k], end=" ")
                print("-/Rs\n")
                break
        
        if not found:
            print("Your name and pin did not match! Please try again.")   
            print(" ")
        OPTION= input("Please press enter key to go back to main menu to perform another function or exit ...")

    


    elif option == 5:
        print("Thank you for using 'YES bank' services!")
        break
    
    else:
        print("Invalid option! Please try again.")