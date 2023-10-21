import bankApplication

if __name__ == '__main__':
    while True:
        print(" ")
        print("Welcome to the online banking appliction")
        print("1. Sign-In ")
        print("2. Sign-Up ")
        print("3. Close Appliction ")
        print(" ")
        userInput = str(input("Enter 1 OR 2 <> "))
        if "1" == userInput:
            bankApplication.signIn()
        elif "2" == userInput:
            bankApplication.signUp()
        elif "3" == userInput:
            print(" ")
            print(" Thank you for using this application ")
            break
