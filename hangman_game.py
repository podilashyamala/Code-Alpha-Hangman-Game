# -*- coding: utf-8 -*-
"""hangman game

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11C834QTOBibRb5W5RilTQP3Z7znA-nCN
"""

import random
import hangman_stages
import word_file
word_list=["apple","beautiful","potato"]
lives=6
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
display=[]
for _ in range(word_length):
    display+="_"
print(display)
game_over=False
while not game_over:
    guess=input("Guess a letter:").lower()
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        game_over = True
        print("You lose.")
    if "_" not in display:
        game_over = True
        print("You win.")
    print(hangman_stages.stages[lives])

"""# New Section"""

