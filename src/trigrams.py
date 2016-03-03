"""Trigrams.py.

Generates a random piece of text based of user entered text file
-*- coding; utf-8 -*-
Created by Kyle Richardson and AJ Wohlfert
"""
import io
import random
import re
from sys import argv


def get_file_txt(inputfile):
    """Take a text file(inputfile) and returns it's text."""
    f = io.open(inputfile)
    file_txt = f.read()
    f.close()
    return file_txt


def txt_to_list(text):
    """Take a single string(text), and returns a list of its words.

    ingores or replaces non alphabetical or numeric characters.
    """
    # replaces newlines and '-' with a single space
    spaced_text = re.sub(r"[\r\n]|[+-]", ' ', text)
    str_list = spaced_text.split(" ")
    for ind, word in enumerate(str_list):
        # removes any non alphabetical or numeric characters
        str_list[ind] = re.sub(r"[^\w]", "", word)
    # clears out any empty string values left behind.
    str_list = [x for x in str_list if x]
    return str_list


def list_to_tri(inputlist):
    """Return a trigram dict based off inputlist."""
    trigram = {}
    while len(inputlist) >= 3:
        key1 = inputlist[-3]
        key2 = inputlist[-2]
        value = inputlist.pop(-1)
        # Attempt to append value to key if it is in the trigram dict.
        trigram.setdefault((key1, key2), []).append(value)
    return trigram


def get_rand_trikey(trigram):
    """Return a random key from a trigram dict."""
    return random.choice(list(trigram.keys()))


def generate_text(trigram, num_words):
    """Generate (num_words) ammount of words in a single string.

    Based off the (trigram) dict.
    """
    # set the first two words as a random key in trigram
    word_list = list(get_rand_trikey(trigram))
    while len(word_list) < num_words:
        # if key exists add one trigram value to generated text
        if (word_list[-2], word_list[-1]) in trigram:
            potential_words = trigram[(word_list[-2], word_list[-1])]
            word_list.append(potential_words[
                random.randint(0, len(potential_words) - 1)])
        # if a trigram cannot be found select a random key and add the words
        else:
            rand_key = get_rand_trikey(trigram)
            word_list.append(rand_key[0])
            word_list.append(rand_key[1])
    # clear out any extra words that may have been made
    word_list = word_list[:num_words]
    return ' '.join(word_list)

if __name__ == "__main__":
    script, fileName, num_words = argv
    fileTxt = get_file_txt(fileName)
    strList = txt_to_list(fileTxt)
    trigram = list_to_tri(strList)
    print(generate_text(trigram, int(num_words)))
