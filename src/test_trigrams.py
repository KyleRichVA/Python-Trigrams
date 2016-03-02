# -*- coding; utf-8 -*-

import pytest


def test_get_file_txt():
    from trigrams import get_file_txt
    assert len(get_file_txt('./sherlock_small.txt')) > 0

testStr = "hello, my name Is Kyle Richardson! 45 %%%%"
expectedList = ['hello', 'my', 'name', 'Is', 'Kyle', 'Richardson', '45']


@pytest.mark.parametrize('text, expected', [(testStr, expectedList)])
def test_txt_to_list(text, expected):
    from trigrams import txt_to_list
    assert txt_to_list(text) == expected

textList = ['hello', 'there', 'my', 'hello', 'there', 'kyle']
expectedDict = {('hello', 'there'): ['my', 'kyle'],
                ('there', 'my'): ['hello'],
                ('my', 'hello'): ['there']}


@pytest.mark.parametrize('InputList, expected', [(textList, expectedDict)])
def test_list_to_tri(InputList, expected):
    from trigrams import list_to_tri
    assert list_to_tri(InputList) == expected
