import time
tries = 0
while(True):
    user_input = input("Enter your password: ")
    if user_input == "admin123":
        print("login successful")
        break
    else:
      tries +=1
      if tries == 3:
         print("Incorrect password you have been locked out for 30 seconds")
         time.sleep(30)
         continue
   