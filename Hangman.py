import random
import hangman_ascii
import wordlist
print(hangman_ascii.logo)
end_of_game = False
word_list = wordlist.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(guess)
    if guess in display:
      print(f"You have already guessed: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"'{guess}' is not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(hangman_ascii.lose)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(hangman_ascii.win)
    print(hangman_ascii.stages[lives])