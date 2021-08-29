# Author name: Shweta Das
# Date: 22 August 2021
# Quick Description: Number Guessing Game Program


import random

guessnumber = int(input("I have a number in my mind, can you guess the number?:"))

selection = random.randint(1,5)

if selection == guessnumber:
                print("Yes, you got it right!!")

else:
                print("No, it is not right,keep guessing:)")

                

    



