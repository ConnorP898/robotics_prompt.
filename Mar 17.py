myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
  
##fix my code
score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")

## day 9 challenge
print("Generation Identifier")
print()
year = int(input("Which year were you born? "))
if year >= 1947 and year <= 1964:
  print("Baby Boomer!")
elif year >= 1965 and year <= 1981:
  print("Generation X!")
elif year >= 1982 and year <= 1995:
  print("Millenials!")
elif year >= 1996 and year <= 2012:
  print("Generation Z!")
else:
  print("Generation Alpha!")
