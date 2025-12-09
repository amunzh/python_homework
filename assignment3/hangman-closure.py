#TASK 4
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(gues_let):
        guesses.append(gues_let)
        final_hangman =''
        for letter in secret_word:
            if letter in guesses:
                final_hangman += letter
            else:
                final_hangman += '_'   
        print(final_hangman)
        if secret_word == final_hangman:
            return True
        else:
            return False
    return hangman_closure


secret_wrd = input("Enter secret word:")

x=make_hangman(secret_wrd)
correct = False
while not correct:
    guess = input("Enter your guess:")
    correct = x(guess)
if correct:
    print("Correct!")
