def cipher(text, shift, encrypt=True):
    """
    Encrypt and decrypt a Ceasar cipher.

    Parameters
    ----------
    text : string
      Enter a string to encrypt or decrypt.
    shift : integer != 0
      Input a positive or negative integer to indicate the positional shift of the alphabets.
    encrypt : bool, default=True
      Indicate a Boolean value of True to encrypt or False to decrypt the text.


    Returns
    -------
    string
      The encrypted or decrypted text.

    Examples
    --------
    >>> cipher_iv2264.cipher('Hello',2, encrypt=True)
    'Jgnnq'

    >>> cipher_iv2264.cipher('Jgnnq',-2, encrypt=False)
    'Hello'
    """
    
    assert isinstance(shift, int)
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
