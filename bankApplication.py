import math

name = None
pin = None
currentCash = 0
rate = 0

def signUp():
    global name
    global pin

    name = str(input("please enter your username: "))
    pin = str(input("please enter your 6 digits pin number: "))

    if len(pin) == 6:
        pin = pin
    else:
        print(" ")
        print("Invalid PIN credential. Try again")
        newpin = str(input("please enter your 6 digits pin number: "))
        if len(newpin) != 6:
            print(" ")
            print("Invalid PIN length digit. Redo again")
            signUp()
            print(" ")
        else: 
            pin = newpin
    print(" ")
    print("Thanks for create your bank account ")

def forgottenPin():
    global pin
    getUserName = str(input("Please enter your username: "))
    if name == getUserName:
        recoverPin = str(input("Please enter your NEW 6 digits pin number: "))
        if len(recoverPin) != 6:
            print(" ")
            print("Invalid PIN. Redo again")
            forgottenPin()
            print(" ")
        else:
            print(" ")
            print("The new pin has been stored, Please sign-in")
            print(" ")
            pin = recoverPin
            signIn()
    else:
        print("Invalid username ")

def calculateCompoundInterest(principal, interstRate, time):
# A = Pe^(rt) which is the formula for calculating the compound interest
    principal = float(principal)
    interstRate = float(interstRate)
    time = float(time)
    rateTime =  interstRate * time
    e = math.exp(rateTime)

    amount = principal * e #Future value of your investment
    return amount


def deposit(value):
    global currentCash

    if currentCash == 0:
        currentCash = value
    else:
        currentCash += value

    print(f"Your current balance is {currentCash}")
    print(" ")


def withdraw():
    global currentCash

    amountValue = int(input("Enter the amount to withdraw: "))

    if amountValue > currentCash:
        while True:
            print(" ")
            print("Insufficient Funds")
            print("1. re-Try again")
            print("2. No, don't want to withdraw ")
            print("3. EXIT")
            newOptionN_Y = str(input("Enter 1-2-3 <> "))
            if "1" == newOptionN_Y:
                print(" ")
                withdraw()
                print(" ")
                break
            elif "2" == newOptionN_Y:
                print(" ")
                print(f"Your current balance is still {currentCash}")
                print(" ")
                break
            elif "3" == newOptionN_Y:
                print(" ")
                break
    else:
        currentCash -= amountValue
        print(f"Your current balance is {currentCash} after withdraw")
        print(" ")
        


def Transfer():
    dest = str(input("Please enter the account number of your destination in 8 digits: "))
    if len(dest) == 8:
        amountValue = int(input("Please enter the amount of money that you want to transfer: "))
        global currentCash

        if amountValue > currentCash:
            while True: 
                print(" ")
                print("You have an Insufficient Funds: ")
                print("1. Re-Try again ")
                print("2. Want to Deposit: ")
                print("3. EXIT")
                newOptionN_Y = str(input("Enter 1-2-3 <> "))
                if "1" == newOptionN_Y:
                    print(" ")
                    Transfer()
                    break
                elif "2" == newOptionN_Y:
                    print(" ")
                    depositValue = int(input("Enter the amount of your deposit: "))
                    deposit(depositValue)
                elif "3" == newOptionN_Y:
                    print(" ")
                    break
        else:
            currentCash -= amountValue
            print(" ")
            print(f"The transaction of {amountValue}, has been transfered to {dest}, current amount is {currentCash} ")
            print(" ")
    else:
        print(" ")
        print("The transaction has been rejected since the destination account number is invalid")
        print(" ")




def checkBalance():
    global currentCash
    return currentCash
    #print(f"Your current balance is {currentCash}")


def displayDepositInterestRate(value):
    global rate
    if int(value) >= 100000:
        rate = 10
    elif int(value) >= 50000:
        rate = 5
    elif int(value) >= 25000:
        rate = 2.5
    elif int(value) >= 10000:
        rate = 1.5
    else:
        rate = 0.05
    return rate
    #print(f"Your current deposit interest rate is {rate}%")


def signIn():
    userInputName = str(input("please enter your username: "))
    userInputPin = str(input("please enter your 6 digits pin number: "))
    
    # Check if the name and pin matched
    if userInputName == name and userInputPin == pin:
        while True:
            print(" ")
            print(f"Welcome {name}, Please choose the menu down here: ")
            print("1. Deposit ")
            print("2. Withdraw ")
            print("3. Transfer ")
            print("4. Check Balance ")
            print("5. Deposit interest rate ")
            print("6. Calculate compound interest")
            print("7. EXIT")
            print(" ")
            userInput = str(input("Enter an Option. "))

            match userInput:
                case "1":
                    print(" ")
                    amountValue = int(input("Enter the amount of your deposit: "))
                    deposit(amountValue)
                case "2":
                    print(" ")
                    withdraw()
                case "3":
                    print(" ")
                    Transfer()
                case "4":
                    print(" ")
                    print(f"Your current balance is {checkBalance()}")
                case "5":
                    print(" ")
                    print(f"Your current deposit interest rate is { displayDepositInterestRate(checkBalance())} %")
                case "6":
                    print(" ")
                    print("1. Calculate compound interest based on your desire value")
                    print("2. Calculate compound interest based on your current balance")
                    print("")                    
                    userOptions = str(input("Enter 1 OR 2 <> "))
                    print(" ")
                    if "1" == userOptions:
                        print(" ")
                        userDesireValue = int(input("Enter the desire balance account "))
                        calculateDisplayDepositInterestRate = displayDepositInterestRate(userDesireValue) / 100
                        time = int(input("Enter : how many year's to invest "))
                        result = calculateCompoundInterest(currentCash,calculateDisplayDepositInterestRate, time )
                        print(f"Your desire balance {userDesireValue}, {time} years will be: { result} ")
                    else: 
                        print(" ")
                        calculateDisplayDepositInterestRate = displayDepositInterestRate(checkBalance()) / 100
                        time = int(input("Enter : how many year's to invest "))
                        result = calculateCompoundInterest(currentCash,calculateDisplayDepositInterestRate, time )
                        print(f"Your current balance {currentCash}, {time} years will be: { result} ")
                case "7":
                    print(" ")
                    break

    else: 
        while True:
            print(" ")
            print("Invalid Credentials.")
            print("1. to try login again ")
            print("2. CREATE ACCOUNT ")
            print("3. forgotten my pin number ")
            print(" ")
            userInput = str(input("Enter 1 OR 2 <> "))
            match userInput:
                case "1":
                    print(" ")
                    signIn()
                    break
                case "2":
                    print(" ")
                    signUp()
                    break
                case "3":
                    print(" ")
                    forgottenPin()
                    break
                case "4":
                    print(" ")
                    print(" Thank you for using the application ")
                    break


#deposit(500)

#withdraw()

#Transfer()

#signUp()
#signIn()