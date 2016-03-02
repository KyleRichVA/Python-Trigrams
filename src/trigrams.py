# -*- coding; utf-8 -*-

import io
import random
import re


def get_file_txt(inputFile):
    f = io.open(inputFile)
    file_txt = f.read()
    f.close()
    return file_txt


def txt_to_tri(text):
    str_list = text.split(" ")
    print str_list
    for ind, word in enumerate(str_list):
        str_list[ind] = re.sub("[^\w]", "", word)
        str_list = [x for x in str_list if x]
    print str_list
    return str_list