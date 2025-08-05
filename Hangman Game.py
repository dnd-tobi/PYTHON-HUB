import random
import time
from colorama import init, Fore, Style
init(autoreset=True)
words = (
"python", "hangman", "computer", "keyboard", "monitor", "laptop", "mouse", "internet",
"network", "software", "hardware", "programming", "variable", "function", "loop",
"condition", "syntax", "compile", "debug", "execute", "database", "server", "client",
"packet", "router", "switch", "encryption", "password", "username", "algorithm",
"array", "string", "integer", "boolean", "float", "dictionary", "tuple", "list",
"stack", "queue", "binary", "hexadecimal", "decimal", "operator", "expression",
"statement", "module", "library", "import", "export", "cloud", "storage", "backup",
"restore", "upload", "download", "process", "thread", "kernel", "shell", "command",
"prompt", "script", "virtual", "machine", "bytecode", "framework", "template", "class",
"object", "method", "inheritance", "polymorphism", "elucidate", "constructor",
"destructor", "override", "overload", "exception", "try", "catch", "finally",
"return", "break", "continue", "pass", "global", "local", "scope", "comment", "print",
"input", "output", "file", "open", "close", "percipient", "write", "append", "amalgamate"
)

hangman_art = {
    0: (
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    1: (
        "  +---+",
        "  |   |",
        "  o   |",
        "      |",
        "      |",
        "      |",
        "========="
    ),
    2: (
        "  +---+",
        "  |   |",
        "  o   |",
        "  |   |",
        "      |",
        "      |",
        "========="
    ),
    3: (
        "  +---+",
        "  |   |",
        "  o   |",
        " /|   |",
        "      |",
        "      |",
        "========="
    ),
    4: (
        "  +---+",
        "  |   |",
        "  o   |",
        " /|\\  |",
        "      |",
        "      |",
        "========="
    ),
    5: (
        "  +---+",
        "  |   |",
        "  o   |",
        " /|\\  |",
        " /    |",
        "      |",
        "========="
    ),
    6: (
        "  +---+",
        "  |   |",
        "  o   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "========="
    )
}

def display_man(wrong_guesses):
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print(Fore.RED + Style.BRIGHT + "🎯 Welcome to Hangman 🎯".center(40))
    print(Fore.CYAN + "="*40)
    time.sleep(1)  # Pause for 1 second
# A little loading animation
    for i in range(3):
        print(Fore.YELLOW + "Loading" + "."*(i+1))
        time.sleep(0.3)
    for i in hangman_art[wrong_guesses]:
            print(i)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
         for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess
        else:
            print(Fore.RED + Style.BRIGHT + "WRONG")
            wrong_guesses +=1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(Fore.GREEN + Style.BRIGHT + "YOU WIN")
            break
        elif wrong_guesses >= len(hangman_art) - 1:
            print(Fore.RED + Style.NORMAL + "YOU HAVE USED ALL YOUR GUESSES")
            display_man(wrong_guesses)
            display_answer(answer)
            break

main()