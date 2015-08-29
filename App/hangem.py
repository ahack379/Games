#! usr/bin/python 

# Project 0
# 6/5/15
# Hangman
# Ariana Hackenburg

# Things to implement:
# 0) Hangman display using pygame interface
# 1) Allow for spaces, apostropes, etc
# 2) Better exception handling
# 3) Other things I can't think of riight now 

from Base.Board import * #HangmanBoard, WordBank
import os, re

word = WordBank()
#word = MakeYourOwnWordBank()
word = list(word) 

#More desirable to write as a string with '_'*len(word), but strings are goddamn
#immutable in python, so can't assign later on  
temp = [ '_' for i in word ]

incorrect = 0 
keepGoing = True
wrongBank =[]
os.system('clear')



while keepGoing:
    
    HangmanBoard(incorrect) 
    print 'Wrong letter bank: ', [ ','.join(wrongBank) ]
    print "\n", ' '.join(temp)
    guess = str(raw_input('\nEnter a letter: '))
    os.system('clear')
    if not re.match("^[a-z]*$", guess):
        print "Only letters a-z allowed, dingus. Try again."
	continue
    if len(guess)!=1:
	print "1 letter at a time you heathen"
	continue
    
    if guess in word: 
	for i in xrange(len(word)): 
	    if guess == word[i]:
		temp[i] = guess 
    else: 
	print "That letter sucks" 
	if guess in wrongBank: 
	    print "...and you already guessed it. you dingus."
	    continue
	wrongBank.append(guess)
	incorrect += 1
	if incorrect == 6:
	    HangmanBoard(incorrect) 
	    print "You lose! Word was ", ' '.join(word)
	    keepGoing = False
    
    if temp == word:
	HangmanBoard(incorrect) 
	print "\n", ' '.join(temp)
        print "You win!" 
	keepGoing = False 




