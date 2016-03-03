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
    '''returns a trigam dict based off InputList where (0,1) refer to List[2],
    (1,2) refer to List[3] and so forth'''
    trigam = {}
    # goes through the list 3 at a time.
    while len(InputList) >= 3:
        key1 = InputList.pop(0)
        key2 = InputList[0]
        value = InputList[1]
        # if a key already exists modify it's value
        if (key1, key2) in trigam.keys():
            trigam[(key1, key2)].append(value)
        # otherwise make a new key value relation
        else:
            trigam[(key1, key2)] = [value]
    return trigam


def get_rand_triKey(trigam):
    '''returns a random key from a trigam dict'''
    return trigam.items()[random.randint(0, len(trigam)-1)][0]


def generate_text(trigam, numWords):
    '''generates (numWords) ammount of words in a single string
    based off the (trigam) dict'''
    # set the first two words as a random key in trigram
    wordList = list(get_rand_triKey(trigam))
    while len(wordList) < numWords:
        # if key exists add one trigram value to generated text
        if (wordList[-2], wordList[-1]) in trigam.keys():
            potentialWords = trigam[(wordList[-2], wordList[-1])]
            wordList.append(potentialWords[
                random.randint(0, len(potentialWords)-1)])
        # if a trigram cannot be found select a random key and add the words
        else:
            randKey = get_rand_triKey(trigam)
            wordList.append(randKey[0])
            wordList.append(randKey[1])
    # clear out any extra words that may have been made
    wordList = wordList[:numWords]

    return ' '.join(wordList)

if __name__ == "__main__":
    script, fileName, numWords = argv
    fileTxt = get_file_txt(fileName)
    strList = txt_to_list(fileTxt)
    trigam = list_to_tri(strList)
    print(generate_text(trigam, int(numWords)))
