import random
name =("Your name?")
secret = random.randint

attempts = 0

while attempts < 5:
    number =int(input("Guess the number:"))
    attempts += 1
    print(f"Attempts # {attempts}")
    