balance=2000
password='1234'
chance=3
while chance >0:
    code=input("Enter the password")
    if code ==password:
        print("Press 1 for checking balance ")
        print("Press 2 for withdrawal")
        print("Press 3 for diposit")
        print("Press 4 to cancel")
        option=input("Enter option ")
        if option == '1':
            print("Balance is ",balance)
        elif option == '2':
            withdraw=int(input("Enter amount to withdraw "))
            if balance < withdraw:
                print("Insufficient balance")
                break
            balance-=withdraw
            print("Amount is withdran is ",withdraw)
            print("balance amount is ",balance)
        elif option == '3':
            diposit=int(input("Enter amount to diposit"))
            balance+=diposit
            print("Amount diposited is ",diposit)
            print("balance amount is ",balance)
        elif option =='4':
            break
    else:
        chance=chance-1

if chance ==0 :
    print("Account is locked")
else: print("Transaction completed")