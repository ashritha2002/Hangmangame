#Step 1 
import random
word_list = ["aardvark", "baboon", "camel","ape", "cat", "dog", "baboon", "elephant", "giraffe", "apple", "coconut", "monkey", "rubik", "mice", "mouse", "pineapple", "android", "apple", "house", "fence", "python", "grail", "zerg"]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list) 
# print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Python program showing
# a use of input()


# print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# print(chosen_word.find(guess))# returns index of letter
won = False
ans= ""
# print(len(chosen_word))
for i in range(0,len(chosen_word)):
  ans+="-"
print(ans)  
i = 0
while won == False:
  guess = input("guess a letter in word: ")
  if chosen_word.find(guess) != -1:
    for letter in chosen_word:
      if letter == guess:
        index = chosen_word.find(letter)
        ans = ans[:index] + guess + ans[index + 1:]
        chosen_word = chosen_word[:index] + '-' + chosen_word[index + 1:]
  else:
    i+=1    
  print(ans)
  print(HANGMANPICS[i])
  # print(i)
  if(i==6):
    print("game over you lose")
  if(ans.find('-') == -1):
    won = True
    print("you won congrats")
 
