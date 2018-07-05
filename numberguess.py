from random import randint

## generate hint
def generate_hint(inp, num):
    if num > inp:
        return 'Your Guess is too low!'
    else:
        return 'Your Guess is too high!'

## Welcome and run the logic
print('Welcome to the Number Guessing Game!')
num = randint(1,10)

# print(num)

## get user input
inp = int(input('Please guess a number.'))

## print as long as number is wrong
while num != inp: 
    print(generate_hint(inp, num))
    inp = int(input('Please guess a number.'))

