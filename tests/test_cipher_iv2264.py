from cipher_vichiennet_aimee.cipher_iv2264.src.cipher_iv2264.cipher_iv2264 import cipher

import pytest

# a) Write a test function that checks whether the cipher function works using a single word as an example.
def test_cipher():
    example = "test"
    shift = 2
    expected = "vguv"
    result = cipher(example, shift)
    assert expected == result

# b) Write a test function that checks a negative shift works (shift < 0).
def test_negative_cipher():
    example = "test"
    shift = -2
    expected = "rcqr"
    result = cipher(example, shift)
    assert expected == result

# c) Write a test for the case when the text contains symbols which are not in the alphabet.
def test_symbols_cipher():
    example = "t#st"
    shift = 2
    expected = "v#uv"
    result = cipher(example, shift)
    assert expected == result
