# نظام إدارة الحسابات البنكية 
names        =["Boda","Ahmed","Ali"]
balances     =[7000,3000,5000]
transactions = [0,0,0]
menu = "yes"

while True :
    print("-----BANK MANAGMENT SYSTEM-----")
    print("\n1. Show All Accounts")
    print("2. Creadte New Account")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Account Statistics")
    print("8. Transaction History")
    print("9.Exit")
    
    choice = int(input("Enter choice :"))
# عرض حساب 
    if choice == 1 :
            if names :
                for number,name in enumerate(names,1) :
                    print(f"Account :{number}.{name} - Balance :{balances[number-1]}")
# اضافة اكون جديد
    elif choice == 2 :
        name = input("Enter name account :")
        if name in names :
            print("name account exsit !")
        else :
            balance = int(input("Enter balance :"))
            if balance >= 0 :
                transaction = 0
                names.append(name)
                balances.append(balance)
                transactions.append(transaction)
                print("Account added !")
            else :
                print("The balance must be zero or higher !")
# عرض معلومات عن حساب 
    elif choice == 3 :
        name = input("Enter name account :")
        if name in names :
            index =names.index(name)
            print(f"Account :{name}\nBalance :{balances[index]}\ntransaction :{transactions[index]}")
        else :
            print("Not Account Found !")
# اضافه رصيد الي حساب
    elif choice == 4 :
        name = input("Enter name account :")
        if name in names :
            balance = int(input("Enter add balance :"))
            if balance > 0 :
                index = names.index(name)
                balances[index] += balance
                transactions[index] += 1
                print("Successful !")
            else :
                print("The balance must be zero or higher !")
        else :
            print("Not found account !")
# سحب الاموال
    elif choice == 5 :
        name = input ("Enter name account :")
        if name in names :
            index = names.index(name)
            withdraw = int(input("Enter the withdrawal amount : "))
            if 0 < withdraw <= balances[index] :
                balances[index] -= withdraw 
                transactions[index] += 1 
                print(f"Successful\nAccount :{name}\nWithdraw :{withdraw}\nBalance :{balances[index]}\ntransaction :{transactions[index]}")
            elif balances[index] < withdraw :
                print("Not enough money !")
            elif withdraw == 0 :
                print("Greater then zero !")
        else :
            print("NOt founde !")
# تحويل اموال من حساب الي حساب
    elif choice == 6 :
        name = input("Enter the sender's account :")
        if name in names :
            index = names.index(name)
            name2 = input("Enter the recipient's account :")
            if name2 in names :
                index1 = names.index(name2)
                if index == index1 :
                    print("Coannot transfer to the same account !")
                else :
                    transfer = int(input("Enter the transfer amount :"))
                    if 0 >= transfer :
                        print("Transfer amount must be greater than zero !")
                    elif transfer > balances[index] :
                        print("NOt enough money !")
                    else :
                        balances[index1] += transfer
                        balances[index] -= transfer
                        transactions[index] += 1
                        transactions[index1] += 1
                        print(f"successful\nSender account :{name}\nTransfur amount :{transfer}\nbalance :{balance[index]}\nrecipient's account :{name2}\nTransfur amount :{transfer}\nbalance :{balance[index1]}")
            else :
                print(f"Not found {name2}")
        else :
            print("NOt found",name)
# عرض كل شئ يخص الاموال في الحسابات
    elif choice == 7 :
        if len(balances) == 0 :
            print('Not found accound !')
        else :
            average = sum(balances)/len(balances)
            print(f"Number of account :{len(names)}.")
            print(f"Total customer balances:{sum(balances)}. ")
            print(f"Average balance: {average:.0f}")
            print("Highest balance:",max(balances))
            print("Low balance :",min(balances))
# 
    elif choice == 8 :
        for number,name in enumerate(names) :
            print(f"{number +1}.{name}-successful Operations :{transactions[number]}")
        print(f"Number of operations :{sum(transactions)}")

    elif choice == 9 :
        print("Thank you ")
        break

