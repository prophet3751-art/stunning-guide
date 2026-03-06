import random 
while True:
    secret = random.randint(1,10)
    attempts = 0

    print("\n New Game: Guess the number from 1 to 10")

    while attempts < 5:
        guess = int(input(f"Guess the number from 1 to 10"))
        attempts +=1
        print(f"Attempt:{attempts}")

        if guess == secret:
            print(f"Well done, bro!")
            break
        elif guess < secret:
            print(f"Too low")
        elif guess > secret:
            print(f"Too high")

    if attempts == 5 and guess != secret:
                print(f"You loose, bro, the numbre was {secret}")
    again = input("Play Again? y/n:")
    if again != "y":
        print("Have a nice day, bro")
        break