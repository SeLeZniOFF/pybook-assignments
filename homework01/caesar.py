import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> decrypt_caesar("python")
    'sbwkrq'
    >>> decrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> decrypt_caesar("")
    ''
    """
    j = 0

    ciphertext = ""

    for i in plaintext:

        j += 1

        if ord("A") <= ord(i) <= ord("Z"):

            k = ord(i) + (shift % 26)

            if k > ord("Z"):

                k = ord("A") + k % 91

                ciphertext += chr(k)

            else:


                ciphertext += chr(k)

        elif ord("a") <= ord(i) <= ord("z"):

            k = ord(i) + (shift % 26)

            if k > ord("z"):

                k = ord("a") + k % 123

                ciphertext += chr(k)

            else:


                ciphertext += chr(k)
        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for i in ciphertext:

        if ord("A") <= ord(i) <= ord("Z"):

            k = ord(i) - (shift % 26)

            if k < ord("A"):

                k = ord("Z") + (k - 64)

                plaintext += chr(k)

            else:

                plaintext += chr(k)

        elif ord("a") <= ord(i) <= ord("z"):

            k = ord(i) - (shift % 26)

            if k < ord("a"):

                k = ord("z") + (k - 96)

                plaintext += chr(k)

            else:


                plaintext += chr(k)
        
        else:


            plaintext += i

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0

    # PUT YOUR CODE HERE
    
    return best_shift
