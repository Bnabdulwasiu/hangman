import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo)
# print(f"Psst this is the chosen word: {chosen_word}")

display = []
for letter in range(word_length):
    display += '_'

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
      print(f"You've already guessed: '{guess}'")   
    
    for position in range(word_length):
        letter = chosen_word[position]                  
        if letter == guess:                                
            display[position] = letter
      
    if guess not in chosen_word:
      lives -= 1
      print(f"You guessed '{guess}' that's not in the word, You lose a life\nYou have {lives} lives left.")
      print(stages[lives])
      if lives == 0:
        end_of_game = True
        print(f"You lose\nThe word is {chosen_word}")
        
    print(display)
    
    if "_" not in display:
      end_of_game = True
      print("You win")