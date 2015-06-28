import random

def HangmanBoard(length):

    if length == 0:
	print '   -----'
    	print '   |   |'
    	print '       |'
    	print '       |'
    	print '       |'
    	print '   ____|___'
    elif length == 1:
	print '   -----'
    	print '   |   |'
    	print '   O   |'
    	print '       |'
    	print '       |'
    	print '   ____|___'
    elif length == 2: 
	print '   -----'
    	print '   |   |'
    	print '   O   |'
    	print '   |   |'
    	print '       |'
    	print '   ____|___'
    elif length == 3: 
	print '   -----'
    	print '   |   |'
    	print '   O   |'
    	print '   |   |'
    	print '    \  |'
    	print '   ____|___'

    elif length == 4: 
	print '   -----'
    	print '   |   |'
    	print '   O   |'
    	print '   |   |'
    	print '  / \  |'
    	print '   ____|___'

    elif length == 5: 
	print '   -----'
    	print '   |   |'
    	print '   O   |'
    	print '   |\  |'
    	print '  / \  |'
    	print '   ____|___'

    elif length == 6: 
	print '   -----'
    	print '   |   |'
    	print '   O   |'
    	print '  /|\  |'
    	print '  / \  |'
    	print '   ____|___'


def WordBank():

    words = [ "words","are","badger","badger","walrus",
	      "potter","turkeybadger","water",
	      "feces","sausage","chili","turkeytime" ] 

    r = random.randint(0,len(words)-1) 
    return words[r]

def MakeYourOwnWordBank():
    moreWords = True
    customWordBank = []
    
    while moreWords:
        entry = raw_input("Enter your words one by one; hit enter after each. Type 0 when you are done : ")
	customWordBank.append(entry)
	if entry == "0":
	    moreWords = False
	    customWordBank.pop()
	    break
    
    if len(customWordBank) >0:
        r = random.randint(0,len(customWordBank)-1) 
	return customWordBank[r]

    else: 
	return -1

	
	
