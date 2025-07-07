import random
low = 1
high = 100
number = random.randint(low, high)
guesses= 0
Sign= "Welcome to the number guessing game!" 
print(f"{Sign:^}")

print(f"Guess a number between {low} and {high}")

while True:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess < low or guess > high:
            print("Number is out of bounds!")
            print(f"Guess a number between {low} and {high}")
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"CORRECT answer is {number} ")
            break
    else:
        print("Not a number")
        print(f"Guess a number between {low} and {high}")
    