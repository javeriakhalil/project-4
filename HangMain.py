import random
from words import words  # type: ignore # This should be a list of words in a separate file called words.py
import string
 
def get_valid_word(words):
     word = random.choice(words)
     while '-' in word or ' ' in word:
         word = random.choice(words)
     return word.upper()
 
def hangman():
     word = get_valid_word(words)
     word_letters = set(word)  # letters in the word
     alphabet = set(string.ascii_uppercase)
     used_letters = set()  # what the user has guessed
     lives = 6
 
     # getting user input
     while len(word_letters) > 0 and lives > 0:
         print('You have', lives, 'lives left. You have used these letters: ', ' '.join(used_letters))
 
         # what the current word is (e.g. W - R - D)
         word_list = [letter if letter in used_letters else '-' for letter in word]
         print("Current word: ", ' '.join(word_list))
 
         user_letter = input("Guess a letter: ").upper()
 
         if user_letter in alphabet - used_letters:
             used_letters.add(user_letter)
             if user_letter in word_letters:
                 word_letters.remove(user_letter)
                 print("Correct guess!")
             else:
                 lives -= 1
                 print("Letter is not in the word.")
         elif user_letter in used_letters:
             print("You have already used that letter. Try again.")
         else:
             print("Invalid character. Please try again.")
 
     if lives == 0:
         print('You died. Sorry! The word was:', word)
     else:
         print('Congratulations! You guessed the word:', word)
 
 # Run the game
hangman()