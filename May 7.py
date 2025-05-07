adding = 4 + 3
print(adding)
subtraction = 8 - 9
print(subtraction)
multiplication = 4 * 32
print(multiplication)
division = 50 / 5
print(division)
# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)
# remainder of a division
modulo = 15 % 4
print(modulo)
# whole number division
divisor = 15 // 2
print(divisor)

## fix my code ##
# multiplication
muliplication = 3.4 * 6.8
print (muliplication)
# division
division = 2467 / 4673
print (division)
#raise 10 to the power of 2
power = 10 ** 2
print (power)
# print the remainder when 343 is divided by 4
remainder = 343 // 100
print (remainder)

## spliting the bill ##
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)

## day 10 challenge ## 
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What tip do you want to leave: 15, 18, or 20%? "))
billWithTip = tip / 100 * myBill + myBill
billPerPerson = billWithTip / numberOfPeople
final_amount = round(billPerPerson, 2)
print("You all owe", final_amount)

