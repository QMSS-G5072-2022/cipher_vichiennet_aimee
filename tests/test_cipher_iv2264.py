from cipher_iv2264 import cipher_iv2264
import pytest

def test_cipher():
    example = "test"
    shift = 2
    expected = "vguv"
    result = cipher_iv2264.cipher(example, shift)
    assert expected == result

def test_negative_cipher():
    example = "test"
    shift = -2
    expected = "rcqr"
    result = cipher_iv2264.cipher(example, shift)
    assert expected == result

def test_symbols_cipher():
    example = "t#st"
    shift = 2
    expected = "v#uv"
    result = cipher_iv2264.cipher(example, shift)
    assert expected == result
