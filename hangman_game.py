import random

# List of predefined words
words = ["python", "computer", "programming", "developer", "software"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
max_attempts = 6
wrong_attempts = 0

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time.")
print("You have 6 wrong attempts.")

# Main game loop
while wrong_attempts < max_attempts:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts:", wrong_attempts, "/", max_attempts)

    # Check if player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_attempts += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")