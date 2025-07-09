import random

# Dice art split into lists of strings (one per line)
dice_art = {
    1: ["┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"],

    2: ["┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"],

    3: ["┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"],

    4: ["┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"],

    5: ["┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"],

    6: ["┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"]
}

dice = []
total = 0
num_of_dice = int(input("How many dice do you want to roll?: "))

# Generate random rolls
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

# Print total
total = sum(dice)
print(f"\nYou rolled: {total}")
