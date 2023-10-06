import random

guessesTaken = 0

print("Hello! What is your name? ")
myname = input()

number = random .randint(1, 10)
print('Well ,' + myname + ' , I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    
    if guess < number :
        print('Your guess is too low.')
        
    if guess > number :
        print('Your guess is too high.')
        
    if guess == number:
        break
    
if guess == number :
    guessesTakenn= str(guessesTaken + 1)
    print('Good Job, ' + myname + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')

if guess != number :
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
    
    