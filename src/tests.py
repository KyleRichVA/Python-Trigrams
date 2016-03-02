# -*- coding; utf-8 -*-

import pytest


@pytest.mark.parametrize('inputFile', './sherlock_small.txt')
def test_get_file_txt(inputFile):
    from trigrams import get_file_txt
    assert len(get_file_txt(inputFile)) > 0
