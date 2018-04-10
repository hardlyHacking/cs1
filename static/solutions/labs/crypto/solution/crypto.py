# crypto.py
# Solution to CS 1 Lab Assignment 2 by THC.
# Encrypts and decrypts files using a hybrid cryptosystem.
# Files are encrypted using block cipher with a one-time pad.
# The one-time pad is encrypted using RSA.
# The format of an encrypted file is
#    The one-time pad, encrypted by RSA, given as the ASCII representation
#        of the encrypted pad;
#    Followed by a newline character ("\n");
#    Followed by the ciphertext of the original file, encrypted using a
#        block cipher with the one-time pad.

from mod_exp import modular_exponentiation
from random import randint

BYTE_SIZE = 8                   # bits per byte

# Takes a string and converts it to a long int.
# Character 0 of the string should be in byte 0 of the 
# long when we are done.  (Recall that byte 0 is the rightmost byte.)
def string_to_long(s):
    converted = 0   # holds the converted int
    shift = 0       # how many bits to shift
    for c in s:     # process each character in s
        # Add in c, but into the next byte of the long int.
        converted += ord(c) << shift
        
        # Adjust the shift for the next byte.
        shift += BYTE_SIZE
        
    # Make sure it's a long int (rather than just an int) before returning.
    return long(converted)

# Takes a long l, and assuming that it is a representation of a string
# with num_bytes characters, returns that string.
def long_to_string(l, num_bytes):
    mask = ~((~0) << BYTE_SIZE)     # mask to isolate rightmost byte
    string = ""
    for i in range(num_bytes):
        # Concatenate onto the string the least significant byte, converted to a char.
        string += chr(l & mask)
        
        # Shift l to the right by one byte.
        l >>= BYTE_SIZE
        
    return string

# Generate a random pad for a given number of bytes.  Return the pad,
# represented as a string of bytes.
def generate_pad(block_size):
    pad = ""
    MAX_BYTE_VALUE = 2**BYTE_SIZE - 1
    for i in range(block_size):
        # Randomly generate the next byte and concatenate it onto the pad.
        pad += chr(randint(0, MAX_BYTE_VALUE))
    return pad

# XOR a block of text, byte by byte, with a key, which is a string of bytes.
# The key must be at least as long as the block.
# Return the XORed block of text.
def xor_block(key, block):
    assert len(key) >= len(block)

    xored_block = ""

    # XOR each byte in the block with a byte from the key, and concatenate it to the result.
    for i in range(len(block)):
        xored_block += chr(ord(block[i]) ^ ord(key[i]))
        
    return xored_block

# Encrypt a plaintext file into a ciphertext file, using the hybrid cryptosystem.
# Parameters are the name of the plaintext file, the name of the ciphertext file,
# the exponent and modulus used for RSA encryption of the one-time pad, and the
# number of bytes in the one-time pad.
def encrypt(plaintext_file_name, ciphertext_file_name, exp, n, block_size):
    cipher_file = open(ciphertext_file_name, "w")
    
    # Generate a random one-time pad.
    pad = generate_pad(block_size)
    
    # Convert the one-time pad to a long so that it can be encrypted with RSA.
    pad_as_long = string_to_long(pad)
    
    # Encrypt the one-time pad using RSA.
    encrypted_pad = modular_exponentiation(pad_as_long, exp, n)
    
    # Write the encrypted one-time pad to the ciphertext file, followed by a newline.
    cipher_file.write(str(encrypted_pad) + "\n")
    
    plaintext_file = open(plaintext_file_name, "rb")
    while True:
        # Read the next block of the plaintext file.
        plaintext_block = plaintext_file.read(block_size)
        if len(plaintext_block) == 0:
            break   # done if no characters left to read
        else:
            cipher_file.write(xor_block(pad, plaintext_block))

    cipher_file.close()
    plaintext_file.close()
    
# Decrypt a ciphertext file into a decrypted plaintext file, using the hybrid cryptosystem.
# Parameters are the name of the ciphertext file, the name of the decrypted plaintext file,
# the exponent and modulus used for RSA decryption of the one-time pad, and the
# number of bytes in the one-time pad.
def decrypt(ciphertext_file_name, decrypted_file_name, exp, n, block_size):
    cipher_file = open(ciphertext_file_name, "rb")
    
    # Read the encrypted one-time pad a character at a time, until hitting the newline.
    encrypted_pad_text = ""
    while True:
        digit = cipher_file.read(1)
        if digit == "\n":
            break
        else:
            encrypted_pad_text += digit
            
    # Convert the encrypted one-time pad to a long int so that it can be decrypted with RSA.
    encrypted_pad = long(encrypted_pad_text)
    
    # Decrypt the one-time pad with RSA.
    pad_as_long = modular_exponentiation(encrypted_pad, exp, n)
    
    # Convert the one-time pad to a string of bytes.
    pad = long_to_string(pad_as_long, block_size)

    decrypted_file = open(decrypted_file_name, "w")
    while True:
        # Process the next block of the ciphertext.
        ciphertext_block = cipher_file.read(block_size)
        if len(ciphertext_block) == 0:
            break       # done when no ciphertext characters remain 
        else:
            decrypted_file.write(xor_block(pad, ciphertext_block))
                            
    cipher_file.close()
    decrypted_file.close()
