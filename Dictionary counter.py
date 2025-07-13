word = input("Enter a word: ")

# Create an empty dictionary to store letter counts
letter_counts = {}

# Loop through each letter in the word
for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1  # Increment if already exists
    else:
        letter_counts[letter] = 1   # Start count at 1 if not seen before

# Print the result
print("Letter frequencies:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
