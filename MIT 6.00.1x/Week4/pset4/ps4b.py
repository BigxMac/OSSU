from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxSoFar = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWordSoFar = ''
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            worth = getWordScore(word, HAND_SIZE)
            # If the score for that word is higher than your best score
            if worth > maxSoFar:
                # Update your best score, and best word accordingly
                bestWordSoFar = word
                maxSoFar = worth
    # return the best word you found.
    return bestWordSoFar

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    #1
    handCopy = hand.copy()
    overallScore = 0
    while True:
        #2
        print handCopy
        while True:
            chosenWord = compChooseWord(handCopy, wordList, HAND_SIZE)
            if chosenWord is '':
                print 'No word found'
                print 'Total score was', overallScore
                break
            #3
            print 'chose ' + chosenWord
            overallScore += getWordScore(chosenWord, HAND_SIZE)
            print 'Got', getWordScore(chosenWord, HAND_SIZE), 'points'
            handCopy = updateHand(handCopy, chosenWord)
            print handCopy
            chosenWord = ''
        break
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    while True:
        userInput = raw_input('Choose n, r, or e: ')
        if userInput == 'n':
             counter = HAND_SIZE
             hand = {}
             # GENERATE HAND
             while counter > 0:
                 # generate number add to dict
                char = random.choice(string.ascii_lowercase)
                #add to dict
                if hand.get(char, -800) == -800:
                    hand[char] = 1
                else:
                    hand[char] += 1
                counter -= 1
             while True:
                 newInput = raw_input('Enter a u or a c: ').strip()
                 if newInput == 'c':
                     compPlayHand(hand, wordList, HAND_SIZE)
                     break
                 elif newInput == 'u':
                     playHand(hand, wordList, HAND_SIZE)
                     break
                 else:
                     print 'not valid. Come on man'
        elif userInput == 'r':
            if hand == {}:
                print 'there is no previous hand'
            else:
                while True:
                    newInput = raw_input('Enter a u or a c: ').strip()
                    if newInput == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    elif newInput == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print 'not valid. Come on man'
        elif userInput =='e':
            break
        else:
            print 'How hard is it to do that?!'

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


