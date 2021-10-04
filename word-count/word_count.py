import string
import re


def count_words(sentence):
    """Counts all the words in a string and returns a dictionary
        in the format {word: count, word: count}"""
    # Split on spaces, _, \n, \t and anything in string.punction
    words = re.split(r"[ _\n\t" + string.punctuation +  "]+", sentence.lower())
    countDict = {}
    
    for word in set(words):
        if (word not in string.punctuation):
            countDict[word] = words.count(word)
    return countDict
