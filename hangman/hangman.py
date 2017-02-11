# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if(secretWord==lettersGuessed):
        return True
    else:
        return False
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      return example: '_ p p _ _'
    '''
    # fILL IN YOUR CODE HERE...
    lettersGuessed =list(lettersGuessed)
    secretWord =list(secretWord)
    len1=len(secretWord)
    copy7=secretWord
    print(" ")
    for k in range(0,len1):
        if secretWord[k] not in lettersGuessed:
               copy7[k]="_"
               
             
    copy7="".join(copy7)
    return copy7
                
                
            
        
        

''' getavailableLetters is made by me .....just for hint '''



'''def getAvailableLetters(secretwords,lettersGuessed):
  
    
    # FILL IN YOUR CODE HERE...
    lettersGuessed =list(lettersGuessed)
    secretWord1 =list(secretWord)
    len1=len(secretWord1)
    copy4=list(" ")
    for k in range(0,len1):
        if secretWord1[k]  not in lettersGuessed:
            j=secretWord1[k]
            copy4.append(j)
    copy4=" ".join(copy4)        
    return copy4   '''
    
def getAvailableLetters_All(lettersGuessed):
    
    keys="abcdefghijklmnopqrstuvwxyz"
    lettersGuessed =list(lettersGuessed)
    secretWord1 =list(keys)
    len1=len(secretWord1)
    copy4=list(" ")
    for k in range(0,len1):
        if secretWord1[k]  not in lettersGuessed:
            j=secretWord1[k]
            copy4.append(j)
    copy4=" ".join(copy4)        
    return copy4 
    
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.
      

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    # FILL IN YOUR CODE HERE...\
    COUNT=1
    length= len(secretWord)
    print(" ")
    print(" ")
    print("      ...........WELCOME.............")
    print(" ")
    print("         SECRET WORD IS OF LENGTH          ",length)
    print(" ")
    lettersGuessed=input("       PLEASE ENTER ONE LETTER           ")
    k=isWordGuessed(secretWord, lettersGuessed) 
    
    
    while k!=True: 
         print("----------------------------------------------------------")
         #print("         SECRET WORD IS OF LENGTH............",length)
         x=input("     PLEASE ENTER ONE MORE LETTER        ")
         lettersGuessed += x         
         print("")
         print("* GUESSED LETTERS ARE...............",lettersGuessed)
         copy2=getGuessedWord(secretWord, lettersGuessed)
         print("")
         print("* PARTIALLY GUESSED WORD SO FAR                  ",copy2)
         if copy2==secretWord:
             k=True
         print("")
         print("* The guess matches ?   ",k) 
         '''copy5=getAvailableLetters(secretWord,lettersGuessed)
         print("")
         
           print("* letters that the user has not yet guessed       ",copy5)'''
         copy6=getAvailableLetters_All(lettersGuessed)
         print("")
         
         print("* letters that the user has not yet guessed       ",copy6)
         
         COUNT+=1
         k=isWordGuessed(secretWord, lettersGuessed)
         if copy2==secretWord:
             k=True
    print("")
    print("")
    print("----------------------------------------------------------")
    print("              DONE        ")
    print(" YOU Guess The Word in  " ,COUNT, "Chance" )
    print("----------------------------------------------------------")
         
         
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
