# -*- coding; utf-8 -*-

import io
import random


def get_file_txt(inputFile):
    f = io.open(inputFile)
    file_txt = f.read()
    f.close()
    return file_txt

