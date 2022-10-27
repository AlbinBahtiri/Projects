"""
import random
taken=0
print('HELLO! What is your name? ')
myName=input()
number=random.randint(1,20)
print('Nice,' + myName + 'I am thinking a number between 1 and 20')
while taken < 6:
    print('Take a guess')
    guess=input()
    guess=int(guess)

    taken=+1

    if guess < number:
        print('Your guess is to low')

    if guess > number:
        print("Your guess is to high")

    if guess == number:
        break

if guess == number:
    taken=str(taken)
    print("You guessed correctly. " + myName +  ' You guessed my number in  ' + taken +  ' guesses!')
    
if guess != number:
    number=str(number)

    print('Nope. The number I was thinking of was ' + number)

"""


import random
guess=int(input("Enter a number between 0 and 100: "))
number=random.randint(0,100)
while guess != number:
        if guess < number:
            print("You guess is to low")
            guess=int(input("\nEnter a number between 0 and 100: "))
        else:
            print("You need to guess lower. Try again ")
            guess=int(input("Enter a number between 0 and 100: "))
            
print("You guessed the number correctly")
user_input='.'
while user_input != 'exit':
    user_input = input('Type exit to quit the program! ')
    
