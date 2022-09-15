# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:11:00 2022

@author: user
"""

import random
import time

print("Welcome Hangman Game")
name=input("Please enter your game: ")
print("heyy", name ,"lets Play")
time.sleep(2)
limit=4

def main():
    global count
    global display
    global word
    words_to_guess=["apple","pencil","flower","bag","ocean","patient","funny","cheerful","morning"]
    word=random.choice(words_to_guess)
    lenght_of_word=len(word)
    display="_" * lenght_of_word
    count=0
    
def loop():
    print("Do you wanna play again?")    
    answer=input("Answer:")
    if answer=="yes":
        print("Lets Play")
        main()
        hangman()
    else:
        print("Thanks to play \n exit" )
        
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    import string
    alphabet=string.ascii_lowercase
    list(alphabet)
    limit=4
    length=len(word)
    print("lenght of word:"+ str(len(word))+ " letters" )
    while count<limit:
     guess = input("This is the Hangman Word: " + display + " Enter your guess: \n") 
     if guess in alphabet:
      if guess == word:
        print("congrulations you find this word")
        loop()
        break
      if guess in word:
        while guess in word:
           index = word.find(guess)  
           word = word[:index] + "_" + word[index + 1:]
           display = display[:index] + guess + display[index + 1:]
        print(display)
        if word == '_' * length:
          print("congrulations you find this word")
          loop()    
      else:
        count= count+1
        if count==1:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
            print("Wrong guess "+ str(limit-count)+ " gueses remaining")            
        elif count==2:
            print("   _____ \n"
                  "  |    | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            
            print("Wrong guess "+ str(limit-count)+ " gueses remaining")    
        elif count==3:
            print("   _____   \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |        \n"
                  "  |        \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__      \n")
            
            print("Wrong guess " + str(limit-count)+ " gueses remaining")                   
        else:
            print("   _____  \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |    O  \n"
                  "  |   /|\ \n"
                  "  |   / \ \n"
                  "  |       \n"
                  "__|__     \n")
            
            print("Wrong guess "+ str(limit-count)+ "gueses remaining")        
            loop()
            
     else:
         print("Please enter a letter")
        
main()
hangman()              
            
            
            