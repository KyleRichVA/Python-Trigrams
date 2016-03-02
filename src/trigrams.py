# -*- coding; utf-8 -*-

import io
import random
import re


def get_file_txt(inputFile):
    f = io.open(inputFile)
    file_txt = f.read()
    f.close()
    return file_txt


def txt_to_list(text):
    str_list = text.split(" ")
    print str_list  # TESTING
    for ind, word in enumerate(str_list):
        str_list[ind] = re.sub("[^\w]", "", word)
        str_list = [x for x in str_list if x]
    print str_list  # TESTING
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
    print trigam  # TESTING
    return trigam
