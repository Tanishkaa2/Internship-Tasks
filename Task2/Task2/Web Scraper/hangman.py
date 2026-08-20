import random


# ------------------------------------------------------------
# TASK 2.2: HANGMAN GAME
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. WORD SELECTION
# ------------------------------------------------------------

words = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "algorithm": "A step-by-step solution to a problem",
    "developer": "A person who creates software",
    "database": "A collection of organized data",
    "internet": "A global network of computers",
    "programming": "Writing instructions for computers",
    "software": "Programs used by computers"
}


# ------------------------------------------------------------
# 2. HANGMAN VISUAL PROGRESS
# ------------------------------------------------------------

hangman_stages = [

    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


# ------------------------------------------------------------
# 3. DISPLAY WORD
# ------------------------------------------------------------

def display_word(word, guessed_letters):

    result = ""

    for letter in word:

        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


# ------------------------------------------------------------
# 4. PLAY ONE GAME
# ------------------------------------------------------------

def play_game():

    # Random word selection
    word = random.choice(list(words.keys()))

    # Game setup
    guessed_letters = set()

    incorrect_guesses = 0
    max_attempts = 6

    hint = words[word]

    print("\n====================================")
    print("           HANGMAN GAME")
    print("====================================")

    print("\nHint:", hint)

    # --------------------------------------------------------
    # GAME LOOP
    # --------------------------------------------------------

    while incorrect_guesses < max_attempts:

        print(
            hangman_stages[incorrect_guesses]
        )

        print(
            "Word:",
            display_word(
                word,
                guessed_letters
            )
        )

        print(
            "Incorrect guesses:",
            incorrect_guesses,
            "/",
            max_attempts
        )

        if guessed_letters:
            print(
                "Guessed letters:",
                " ".join(sorted(guessed_letters))
            )

        # ----------------------------------------------------
        # USER INPUT
        # ----------------------------------------------------

        guess = input(
            "\nGuess a letter: "
        ).lower().strip()

        # Input validation
        if len(guess) != 1:

            print(
                "Please enter exactly one letter."
            )

            continue

        if not guess.isalpha():

            print(
                "Please enter a valid alphabet letter."
            )

            continue

        if guess in guessed_letters:

            print(
                "You already guessed that letter."
            )

            continue

        # Add letter to guessed letters
        guessed_letters.add(guess)

        # ----------------------------------------------------
        # CHECK GUESS
        # ----------------------------------------------------

        if guess in word:

            print(
                "Correct! The letter is in the word."
            )

        else:

            incorrect_guesses += 1

            print(
                "Wrong guess!"
            )

        # ----------------------------------------------------
        # WIN CONDITION
        # ----------------------------------------------------

        if all(
            letter in guessed_letters
            for letter in word
        ):

            print(
                "\n===================================="
            )

            print(
                "Congratulations!"
            )

            print(
                "You guessed the word:",
                word
            )

            print(
                "===================================="
            )

            return True

    # --------------------------------------------------------
    # LOSS CONDITION
    # --------------------------------------------------------

    print(
        hangman_stages[max_attempts]
    )

    print(
        "\nGame Over!"
    )

    print(
        "The correct word was:",
        word
    )

    return False


# ------------------------------------------------------------
# 5. PLAY AGAIN
# ------------------------------------------------------------

def main():

    while True:

        play_game()

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower().strip()

        if play_again not in ["yes", "y"]:

            print(
                "\nThanks for playing Hangman!"
            )

            break

        print(
            "\nStarting a new game..."
        )


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------

if __name__ == "__main__":
    main()