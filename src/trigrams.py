# -*- coding; utf-8 -*-

import io
import random
import re
from sys import argv


def get_file_txt(inputFile):
    f = io.open(inputFile)
    file_txt = f.read()
    f.close()
    return file_txt


def txt_to_list(text):
    str_list = text.split(" ")
    for ind, word in enumerate(str_list):
        str_list[ind] = re.sub("[^\w]", "", word)
        str_list = [x for x in str_list if x]
    return str_list


def list_to_tri(InputList):
    trigam = {}
    while len(InputList) >= 3:
        key1 = InputList.pop(0)
        key2 = InputList[0]
        value = InputList[1]
        if (key1, key2) in trigam.keys():
            trigam[(key1, key2)].append(value)
        else:
            trigam[(key1, key2)] = [value]
    return trigam


def get_rand_triKey(trigam):
    return trigam.items()[random.randint(0, len(trigam)-1)][0]


def generate_text(trigam, numWords):
    wordList = list(get_rand_triKey(trigam))
    while len(wordList) < numWords:
        if (wordList[-2], wordList[-1]) in trigam.keys():
            potentialWords = trigam[(wordList[-2], wordList[-1])]
            wordList.append(potentialWords[
                random.randint(0, len(potentialWords)-1)])
        else:
            randKey = get_rand_triKey(trigam)
            wordList.append(randKey[0])
            wordList.append(randKey[1])
    return ' '.join(wordList)

if __name__ == "__main__":
    script, fileName, numWords = argv
    fileTxt = get_file_txt(fileName)
    strList = txt_to_list(fileTxt)
    trigam = list_to_tri(strList)
    print(generate_text(trigam, numWords))
