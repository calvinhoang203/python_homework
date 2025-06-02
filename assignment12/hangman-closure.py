# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join([l if l in guesses else '_' for l in secret_word])
        print(display)
        return all(l in guesses for l in secret_word)
    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    game = make_hangman(secret_word)
    while True:
        guess = input("Guess a letter: ").lower()
        if game(guess):
            print(f"You've guessed the word: {secret_word}")
            break
