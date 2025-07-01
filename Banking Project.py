import sqlite3
import time
first=sqlite3.connect("ECLIPSEBANK.db")
second=first.cursor()

second.execute("CREATE TABLE IF NOT EXISTS USERS(FirstName TEXT,LastName TEXT, PhoneNumber TEXT , Email TEXT, Password TEXT , Username TEXT, BVN TEXT, AccountNumber TEXT, BALANCE INTEGER, Credit INTEGER, Debit INTEGER, CreditHistory INTEGER, DebitHistory INTEGER)")
print("Table successfully created")


import re
import random
import datetime
import time

class BankAccount:
    
    def __init__(self, first_name, last_name, age, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.email = email
        self.phone_number = phone_number
        self.balance = 0
        self.bvn = self.bvn_creation()
        self.account_number = self.accnumber_creation()
        
    
    def bvn_creation(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(11)])
    
    def accnumber_creation(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Main code


print("WELCOME TO THE ECLIPSE BANK...")  


while(True):
    while True:
        try:
            creation = int(input('''Would you like to create an account with us or login your account:
                1. Yes
                2. No 
                3. Login
                '''))
            if creation in [1, 2, 3]:
                break
            else:
                print("Invalid input. Enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    if creation == 1:
        while(True):
            first_name = input("What is your first name: ").upper()
            if not first_name.isalpha():
                print("Invalid first name. It should only contain alphabets.")
                continue
            else:
                break
        
        while(True):
            last_name = input("What is your last name: ").upper()
            if not last_name.isalpha():
                print("Invalid last name. It should only contain alphabets.")
                continue
            else:
                break


        while(True):
            while(True):
                try:
                    age = eval(input("What is your age: "))
                    break
                except:
                    print("Invalid Input")
                    continue
            if age < 18:
                    print("You are not old enough to create an account.")
                    continue
            else:
                break

        while(True):    
            email = input("What is your email: ")
            if not re.match(r"^[a-zA-Z0-9_+.-]+@[a-zA-Z-]+\.[a-zA-Z]{2,}$",email):
                print("Invalid Email Format")
                continue
            else:
            
                break

        
        while(True):
            
            phone_number = input("What is your phone number (e.g., +234xxxxxxxxxx or 0xxxxxxxxxx): ")
               
            if not re.match(r"(^\+)(234){1}+[0-9]{10}$|^(0)(7|8|9)(0|1){1}[0-9]{8}$",phone_number):
                print("Invalid phone number format ")
                continue
            else:
                 break
        

        
        account = BankAccount(first_name, last_name, age, email, phone_number)
        
    
        if account.age >= 18 and re.match(r"^[a-zA-Z0-9_+.-]+@[a-zA-Z-]+\.[a-zA-Z]{2,}$", account.email) and re.match(r"^\+234\d{10}$|^0\d{10}$", account.phone_number):
            print(f"Here are your details: \n Name: {account.first_name} {account.last_name}")
            print(f"Your email: {account.email} \nYour phone number: {account.phone_number}")
            print(f"Your BVN is: {account.bvn} (PLEASE DO NOT SHARE WITH ANYNONE)")
            print(f"Your Account Number is: {account.account_number}")
            username=input("Please create a username: ").strip()
            password= input("Please create a password for your account(Must not be more than 15 characters): ").strip()
            while(True):
                if not (password=="") or (len(password)>15):
                    break
                else:
                     print("invallid password")
                     continue
            second.execute(F"INSERT INTO USERS(FirstName,LastName,PhoneNumber,Email,Password,Username,BVN,AccountNumber,Balance) VALUES('{first_name}','{last_name}',{phone_number},'{email}','{password}','{username}',{account.bvn},{account.account_number},{account.balance})")
            second.execute("UPDATE USERS SET Balance= '0' WHERE Balance IS NULL AND Username= ?", (username,))
           
            first.commit()
            print("ACCOUNT CREATION SUCCESSFUL")
            continue
    else:
        if creation==2:
            print("THANK YOU FOR VISITING!!!")
        break
      
  



if creation==3:
        while(True):
            login1=input("Please enter your username: ")
            login2=input("Please enter your password: ")
            second.execute("SELECT PASSWORD FROM USERS WHERE USERNAME=?", (login1,))
            fetch = second.fetchone()

            if fetch is None:
                print("Incorrect username or password. Try again.")
                continue

            correct_password = fetch[0]
            if login2 == correct_password:
                print("Login successful.")
                break
            else:
                print("Incorrect username or password. Try again.")
        if login2==correct_password:
            while(True):
                print(f"WELCOME {login1}")
                print("""
                    1.DEPOSIT
                    2.WITHDRAW
                    3.CHECK BALANCE
                    4.Transfer
                    5.Logout  
                    """)
                while(True):

                    userinput=input("Please pick an option: ")
                    if not userinput.isdigit():
                        print("Invalid input,try again")
                        continue
                    else:
                        break
            
                if userinput=="1":
                    while(True):
                            while(True):
                                try:
                                    acc_num=int(input("What is your account number: "))
                                    break
                                except:
                                    print("Invalid Input")
                                    continue
                            
                            while(True):
                                try:
                                    second.execute("SELECT BALANCE FROM USERS WHERE AccountNumber=?",(acc_num,))
                                    result=second.fetchone()
                                    current_balance=result[0]
                                    depos=int(input("How much would you like to deposit: "))
                                    new_money= depos+current_balance
                                    credit=depos
                                    credit_history=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    break
                                except:
                                    print("Invalid Input")
                                    continue

                            try:
                                print(f"You deposited {depos} 'at' {credit_history}")
                                second.execute("UPDATE USERS SET CREDIT = '0' WHERE CREDIT IS NULL AND AccountNumber=?", (acc_num,))
                                second.execute("UPDATE USERS SET CreditHistory= '' WHERE CreditHistory IS NULL AND AccountNumber= ?", (acc_num,))
                                second.execute("UPDATE USERS SET CREDIT= CREDIT || ',+' || ? WHERE AccountNumber=?",(credit,acc_num,))
                                second.execute("UPDATE USERS SET CreditHistory= CreditHistory || ', ' || ? WHERE AccountNumber=?",(credit_history,acc_num,))
                                second.execute("UPDATE USERS SET BALANCE=? WHERE AccountNumber=?",(new_money,acc_num,))
                                first.commit()
                                break
                            except:
                                print("Invalid Input")
                            continue
                elif  userinput=="2":
                    

                        while(True):
                                while(True):
                                        try:
                                            acc_num=int(input("What is your account number: "))
                                            break
                                        except:
                                            print("Invalid Input")
                                            continue
                                
                                while(True):
                                    try:
                                        Withdraw=float(input("How much would you like to withdraw: "))
                                    except:
                                        print("Invalid Input")
                                    second.execute("SELECT BALANCE FROM USERS WHERE AccountNumber=?",(acc_num,))
                                    result=second.fetchone()
                                    current_balance=result[0]
                                    if Withdraw < current_balance:
                                        new_bal=current_balance - Withdraw
                                        debit= -Withdraw
                                        debit_history=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        break
                                    else:
                                        print("Insufficient Funds")
                                        continue
                                        
                                        
                                try:
                                    print(f"Your withdrew {Withdraw} 'at' {debit_history}")
                                    second.execute("UPDATE USERS SET DEBIT= '0' WHERE DEBIT IS NULL AND AccountNumber=?", (acc_num,))
                                    second.execute("UPDATE USERS SET DebitHistory= '' WHERE DebitHIstory IS NULL AND AccountNumber=?", (acc_num,))
                                    second.execute("UPDATE USERS SET DEBIT= DEBIT || ', ' || ? WHERE AccountNumber=?",(debit,acc_num,))
                                    second.execute("UPDATE USERS SET DebitHistory= DebitHistory || ', ' || ? WHERE AccountNumber=?",(debit_history,acc_num,))
                                    second.execute("UPDATE USERS SET BALANCE=? WHERE AccountNumber=?",(new_bal,acc_num))
                                    first.commit()
                                    break
                                except:
                                    print("Invalid Input")
                                continue
            
                elif userinput=="3":
                
                
                    
                            while(True):
                                try:

                                    acc_num=int(input("What is your account number: "))
                            
                                    second.execute("SELECT BALANCE FROM USERS WHERE AccountNumber=?",(acc_num,))
                                    result=second.fetchone()
                                    print("Your account balance is:" + str(result[0]))
                                    first.commit()
                                    break
                                except:
                                    print("Account Not Found")
                                    continue
            
                
                elif userinput=="4":
                    while(True):
                        try:
                            acc_num=int(input("What is your account number: "))
                            break
                        
                        except:
                            print("invlaid input")
                            continue
                    while(True):
                        try:
                            Transfer=float(input("How much would you like to transfer: "))
                            second.execute("SELECT BALANCE FROM USERS WHERE AccountNumber=?",(acc_num,))
                            result=second.fetchone()
                            current_balance=result[0]
                            break
                        except:
                            print('Invalid Input')
                            continue
                        
                    while(True):
                        if not Transfer>current_balance:
                            break
                        else:
                            print("Insufficient Funds")
                            continue
                    while(True):
                        try: 
                            recipient_number=input("Enter the recipient account number: ")
                            second.execute("SELECT BALANCE FROM USERS WHERE AccountNumber=?",(recipient_number,))
                            results=second.fetchone()
                            recipient_balance=results[0]
                            second.execute("SELECT AccountNumber FROM USERS WHERE Password=?",(login2,))
                            check=second.fetchone()
                            checks=check[0]
                            if recipient_number==checks:
                                    print("Same account number as user")
                            else:      
                              break
                        except:
                            print("Invalid Account Number")
                            continue
                    new_recipient=Transfer+recipient_balance
                    transfer_debit= -Transfer
                    debit_history=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    credit_history=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    second.execute("UPDATE USERS SET DEBIT= '0' WHERE DEBIT IS NULL AND AccountNumber=?", (acc_num,))
                    second.execute("UPDATE USERS SET DebitHistory= '' WHERE DebitHIstory IS NULL AND AccountNumber=?", (acc_num,))
                    second.execute("UPDATE USERS SET DEBIT= DEBIT || ', ' || ? WHERE AccountNumber=?",(transfer_debit,acc_num,))
                    second.execute("UPDATE USERS SET BALANCE=? WHERE AccountNumber=?",(new_recipient,recipient_number))
                    second.execute("UPDATE USERS SET CREDIT = '0' WHERE CREDIT IS NULL AND AccountNumber=?", (recipient_number,))
                    second.execute("UPDATE USERS SET CreditHistory= '' WHERE CreditHistory IS NULL AND AccountNumber= ?", (recipient_number,))
                    second.execute("UPDATE USERS SET CREDIT= CREDIT || ',+' || ? WHERE AccountNumber=?",(Transfer,recipient_number,))
                    second.execute("UPDATE USERS SET CreditHistory= CreditHistory || ', ' || ? WHERE AccountNumber=?",(credit_history,recipient_number,))
                    print(f"Transfer of {Transfer} was successful")
                    first.commit()
        
                    
                
                elif userinput=="5":
                    print(f"THANK YOU FOR USING ECLIPSE BANK {login1}")
                    time.sleep(5)
                    print("Logout Successful")
                    break
                else:
                    continue
            

            
first.close()