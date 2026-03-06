import random
name =input("Your name?")
number =int(input("Gues the number 1-10:"))

secret = random.randint(1,10)

if number == secret:
    print(f"Well done, {name}!, The number is {secret}!")
else: 
    print(f" You lost, {name}, The correct number was {secret}.")


