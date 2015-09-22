#hw10pr3.py
#Philip Geurin and Cassie Gamm
#Nov 14 2010
# aka (today= Date( 11, 14, 2010)

import random
import math
    
def wordCount( filename = None ):
    """ creates and prints the input list of words
    """
    
    text = ''
    if filename == None:
        print "Enter lots o' text. End with a plain '42' line."
        while True:
            nextline = raw_input()
            if nextline == '42': break
            text += nextline + ' '
            
    else:
        f = file( filename, 'r' )  # open a file for 'r'eading
        text = f.read()

    # text is a bunch of space-separated words

    list_of_words = text.split()  # split splits a string
    print "The list of words is", list_of_words
    num_words = len( list_of_words )
    print "There are", num_words, "words."




    

def vocabCount( filename = None ):
    """ creates and returns a dictionary of distinct words """
    
    text = ''
    if filename == None:
        print "Enter lots o' text. End with a plain '42' line."
        while True:
            nextline = raw_input()
            if nextline == '42': break
            text += nextline + ' '
            
    else:
        f = file( filename, 'r' )  # open a file for 'r'eading
        text = f.read()

    # text is a bunch of space-separated words

    list_of_words = text.split()  # split splits a string
    #print "The list of words is", list_of_words
    num_words = len( list_of_words )
    print "There are", num_words, "words."

    D = {}  # an empty dictionary

    for w in list_of_words:
        
        #"""
        for punc in ".,`'\"~!@#$%^&*();:<>|\\/?}{][_+=":
            w = w.replace( punc, '' )
            w = w.lower() # lower-case
        #"""
        
        if D.has_key( w ) == False:  # w was not there!
            D[w] = 1
            
        else: # d.has_key( w ) == True,  so w IS already there!
            D[w] += 1

    num_distinct_words = len( D )
    print "There are", num_distinct_words, "distinct words."

    RevItems = [ x[::-1] for x in D.items() ]
    RevItems.sort()
    RevItems = RevItems[::-1]
    counter = 40
    for item in RevItems:
        if counter < 1: break
        counter -= 1
        print item[1], "\t\t-->", item[0], "times"

    if len(D) < 20:
        return D
    else:
        return  # avoids returning too large a dictionary

def createDictionary( filename=None ):
    """ creates and returns a dictionary of distinct words """
    
    text = ''
    if filename == None:
        print "Enter lots o' text. End with a plain '42' line."
        while True:
            nextline = raw_input()
            if nextline == '42': break
            text += nextline + ' '
            
    else:
        f = file( filename, 'r' )  # open a file for 'r'eading
        text = f.read()

    # text is a bunch of space-separated words

    list_of_words = text.split()  # split splits a string
    num_words = len( list_of_words )
    D = {}  # an empty dictionary
    """
    for w in range(len(list_of_words)):
        
        for punc in ".,`'\"~!@#$%^&*();:<>|\\/?}{][_+=":
            list_of_words[w] = list_of_words[w].replace( punc, '' )
            list_of_words[w] = list_of_words[w].lower() # lower-case
    """
    D['$']=[list_of_words[0]]
    for w in range(len(list_of_words)-1):
        if (punk(list_of_words[w]) in D) == False:  # w was not there!
            D[punk(list_of_words[w])] = [list_of_words[w+1]]
            
        else: # d.has_key( w ) == True,  so w IS already there!
            D[punk(list_of_words[w])] += [list_of_words[w+1]]

                #THIS IS WHEN YOU FIND THE END OF SENTENCES---ANYTHING WITH A punctuation in the word

    num_distinct_words = len( D )

    RevItems = [ x[::-1] for x in D.items() ]
    RevItems.sort()
    RevItems = RevItems[::-1]
    counter = 40
    return D

    """
    for item in RevItems:
        if counter < 1: break
        counter -= 1
        print item[1], "\t\t-->", item[0], "times"
    """
    """
    if len(D) < 20:
        return D
    else:
        return  # avoids returning too large a dictionary
    """

def punk(mystring):
    """takes a string input, then outputs '$' if there is a '?','.', or
'!' in the string and outputs the origional string if not. """
    if ('!') in mystring:
        return '$'
    elif ('.') in mystring:
        return '$'
    elif ('?') in mystring:
        return '$'
    else:
        return mystring

def generateText( D, n ):
    """take in a dictionary or word transitions d (generated in your
createDictionary function, above) and a positive integer, n. Then,
generateText should print a string of n words"""
    choice=random.choice(D['$'])
    string=choice
    for count in range(n):
        choice=random.choice(D[punk(choice)])
        string=string+' '+choice
    return string


d = createDictionary( 'shakespeare.txt' )
print generateText( d, 20)
