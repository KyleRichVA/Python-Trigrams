# -*- coding; utf-8 -*-

import pytest


@pytest.mark.parametrize('inputFile', './sherlock_small.txt')
def test_get_file_txt(inputFile):
    from trigrams import get_file_txt
    assert len(get_file_txt(inputFile)) > 0

testStr = "hello, my name Is Kyle Richardson! 45 %%%%"
expectedList = ['hello', 'my', 'name', 'Is', 'Kyle', 'Richardson', '45']


@pytest.mark.parametrize('testStr, expectedList', [testStr, expectedList])
def test_txt_to_tri(text, expected):
    from trigrams import txt_to_tri
    assert txt_to_tri(text) == expected
