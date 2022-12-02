import random
import Day_7_Hangman_Art 
import Day_7_Hangman_Words 
print(Day_7_Hangman_Art.logo)
print("\n")
chosen_word = random.choice(Day_7_Hangman_Words.word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
  display.append("_") 
  
end_of_the_game = False
life = 6
while end_of_the_game == False:
  print("\n")
  guess = input("Guess a letter: ").lower()
  print("\n")
  if guess in chosen_word:
    for i in range(0,len(chosen_word)):
      if chosen_word[i] == guess:
          display[i] = guess
    print(",".join(display))
  else:
    life = life -1
    print(f"You guessed '{guess}', that's not in the word. You lose a life.\nYou have {life} lifes")
    print(Day_7_Hangman_Art.stages[life])
    
  if "_" not in display:
    end_of_the_game = True
    print("\n")
    print("You Win!")
  elif life == 0:
    end_of_the_game = True
    print("\n")
    print("You lose")