import random   
name =input("your name")
secret = random.randint(1, 15)

guess =  None

while guess != secret:
    guess = int(input("Guess the number from 1 o 15"))

    if guess < secret:
        print("too low!")
    elif guess > secret:
        print("Too high")
    else:
        print(f"well done, {name}! The number is {secret}")