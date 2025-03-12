myName = input("Hello, what is your name? ")
print("Hello " + myName + "!")


print()
if myName == "Connor":
  Day = input("what day is it?")
  if Day == "Monday":
    print("Its the going to be a good week!", myName)
  if Day == "Tuesday":
    print("I hope you have a great tuesday", myName)
  if Day == "Wednesday":
    print("Its going to be a wonderful wednesday")
  if Day == "Thursday":
    print("you have two days until the weekend")
  if Day == "Friday":
    print("it's the end of the week, woohoo")
elif myName == "David" or myName== "david":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", myName)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("You look great in that color", myName)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("You look chipper today", myName)
 if DOW == "thursday" or DOW == "Thursday":
   print(myName,"you are doing a great job!")
 if DOW == "friday" or DOW == "Friday":
   print(myName, "it's FRIDAY!")
else:
  print("I don't know who you are, but I hope you are having a great day!")

# "Common Error With If Statements"
name = input("Name: ")
if name == "Dave" or name == "dave":
  print("Hi Dave")
