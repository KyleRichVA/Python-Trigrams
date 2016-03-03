# -*- coding; utf-8 -*-
# created by Kyle Richardson and AJ Wohlfert
# Trigrams.py generates a random piece of text based of user entered text file.

import io
import random
import re
from sys import argv


def get_file_txt(inputFile):
    '''Takes a text file(inputFile) and returns it's text'''
    f = io.open(inputFile)
    file_txt = f.read()
    f.close()
    return file_txt


def txt_to_list(text):
    '''Takes a single string(text), and returns a list of its words ingoring or
    replacing non alphabetical or numeric characters'''
    # replaces newlines and '-' with a single space
    spaced_text = re.sub(r"[\r\n]|[+-]", ' ', text)
    str_list = spaced_text.split(" ")
    for ind, word in enumerate(str_list):
        # removes any non alphabetical or numeric characters
        str_list[ind] = re.sub(r"[^\w]", "", word)
    # clears out any empty string values left behind.
    str_list = [x for x in str_list if x]
    return str_list


def list_to_tri(InputList):
    '''return a trigram dict based off InputList'''
    trigram = {}
    while len(InputList) >= 3:
        key1 = InputList[-3]
        key2 = InputList[-2]
        value = InputList.pop(-1)
        # Attempt to append value to key if it is in the trigram dict.
        try:
            trigram[(key1, key2)].append(value)
        # If a Key Error is thrown, make a new list for that key
        except KeyError:
            trigram[(key1, key2)] = [value]
    return trigram


def get_rand_triKey(trigram):
    '''return a random key from a trigram dict'''
    return random.choice(list(trigram.keys()))


def generate_text(trigram, numWords):
    '''generate (numWords) ammount of words in a single string
    based off the (trigram) dict'''
    # set the first two words as a random key in trigram
    wordList = list(get_rand_triKey(trigram))
    while len(wordList) < numWords:
        # if key exists add one trigram value to generated text
        if (wordList[-2], wordList[-1]) in trigram.keys():
            potentialWords = trigram[(wordList[-2], wordList[-1])]
            wordList.append(potentialWords[
                random.randint(0, len(potentialWords)-1)])
        # if a trigram cannot be found select a random key and add the words
        else:
            randKey = get_rand_triKey(trigram)
            wordList.append(randKey[0])
            wordList.append(randKey[1])
    # clear out any extra words that may have been made
    wordList = wordList[:numWords]
    return ' '.join(wordList)

if __name__ == "__main__":
    script, fileName, numWords = argv
    fileTxt = get_file_txt(fileName)
    strList = txt_to_list(fileTxt)
    trigram = list_to_tri(strList)
    print(generate_text(trigram, int(numWords)))
