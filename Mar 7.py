print ("SECURE LOGING")
userName = input ( "Username > ")
password = input ("Password > ")
if userName == "mark" and password == "password":
  print ("Welcome, Mark!")
elif userName == "connor" and password == "Password":
  print("Hey there Connor!")
else: 
  print ("go away!")

## Common Errors ##
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
  ## The problem was that the else statement was after the esle statement. ##

## Fixing Code ##
season = input("what is your favorite season?")
if season == "spring"
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn"
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")
  ## The code didn't have proper indentation, quotations, and the "==" ##

## Day 6 Challenge ##
print("SECURE LOGIN")
print( )
username = input("Username:  ")
password = input("Password:  ")
if username == "connor" and password == "password":
  print( )
  print("\033[32mCORRECT\033[0m")
  print("Welcome Connor!")
elif username == "mark" and password == "Replit":
  print( )
  print("\033[32mCORRECT\033[0m")
  print("Welcome mark!")
else: 
  print( )
  print("\033[31mINCORRECT\033[0m")
