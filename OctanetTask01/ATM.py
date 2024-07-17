import time

def print_separator():
    print("\n" + "-"*40 + "\n")

print("\t\t!! Welcome to Alisha's ATM machine !!")
print("\t\tPlease insert your valuable card down here!!")
print("\t\tPlease wait while the card is being read...")

time.sleep(5)

security_check = 2896
try:
    pin_no = int(input("\nEnter your ATM_PIN NO: "))
except ValueError:
    print("\tInvalid input. Please restart the program and enter a numeric PIN.")
    exit()

name = "Ankita Mishra" #Random user name
age = 20
phone_no = "XXXXXX2268"
gender = "Female"
current_balance = 1000

if pin_no == security_check:
    withdraw_amt = 0
    deposit_cash = 0

    while True:
        print_separator()
        print("""
        |------------------ Menu ------------------|
        | 1. Account Inquiry                       |
        | 2. Withdraw Cash                         |
        | 3. Deposit Cash                          |
        | 4. Change PIN                            |
        | 5. Transaction History                   |
        | 6. Exit                                  |
        |------------------------------------------|
        """)
        
        try:
            choice = int(input("\tPlease enter your choice (1-6): "))
        except ValueError:
            print("\tInvalid input. Please enter a valid number (1-6)....")
            continue

        print_separator()

        if choice == 1:
            print("\tYour Bank Details:")
            print(f"\n\tName: {name}")
            print(f"\tAge: {age}")
            print(f"\tContact no: {phone_no}")
            print(f"\tGender: {gender}")
            print(f"\tCurrent Balance: ${current_balance}")

        elif choice == 2:
            try:
                withdraw_amt = int(input("\tEnter the amount to withdraw: $"))
            except ValueError:
                print("\n\tInvalid input. Please enter a numeric amount.")
                continue
            if withdraw_amt <= current_balance:
                current_balance -= withdraw_amt
                print(f"\t${withdraw_amt} has been withdrawn from your account.")
                print(f"\n\tYour current balance is: ${current_balance}")
            else:
                print("\tInsufficient balance!")

        elif choice == 3:
            try:
                deposit_cash = int(input("\tEnter the amount to deposit: $"))
            except ValueError:
                print("\tInvalid input. Please enter a numeric amount.")
                continue
            current_balance += deposit_cash
            print(f"\t${deposit_cash} has been deposited into your account. Congratulations!")
            print(f"\n\tYour current balance is: ${current_balance}")

        elif choice == 4:
            try:
                change_pin = int(input("\tEnter a new PIN: "))
            except ValueError:
                print("\n\tInvalid input. Please enter a numeric PIN.")
                continue
            security_check = change_pin
            print(f"\tYour updated PIN is: {change_pin}")

        elif choice == 5:
            print("\tTransaction History:")
            print(f"\t- Last Withdrawal: ${withdraw_amt}")
            print(f"\t- Last Deposit: ${deposit_cash}")

        elif choice == 6:
            print("\tThank you for using Alisha's ATM machine. Have a nice day!")
            break
        
        else:
            print("\tInvalid choice. Please select a number from the menu (1-6).")

        print_separator()

else:
    print("\tOops!! You entered the wrong PIN.\n\t--Please restart the program and enter a numeric PIN.--")
