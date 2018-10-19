"""
The FizzBuzz Game v1.0
by: Jonathan Chapman
date: September 20, 2018
"""

print("\nWELCOME TO THE FizzBuzz GAME!!!\n")
print("In this game, you enter a number, and I, the computer,\n"\
      "will list off the sequence of numbers up till the number\n"\
      "you listed. As I list off the numbers, for every number\n"\
      "that is divisible by 3, I will say Fizz, but for every\n"\
      "number that is divisible by 5, I will say Buzz. If the\n"
      "number is both divisible by 3 and 5, I will say FizzBuzz.\n"
      "I hope you have fun!\n")

while True:
    try:
        userInput = int(input("Enter a number: "))
        break
    except:
        print("Sorry. This is not a number. You must enter a number (without decimals).")
        pass

userInput = userInput + 1
userInput = range(userInput)

print("")

for number in userInput:
    if number == 0:
        print(number)
    elif number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print ("Fizz")
    else:
        print(number)